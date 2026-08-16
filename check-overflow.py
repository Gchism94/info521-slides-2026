#!/usr/bin/env python3
"""Report slides whose content runs past the deck's edges.

Long display math is the usual culprit: KaTeX will happily typeset a formula
wider than the slide, reveal clips it, and the overflow is invisible in the
source. It shows up only when someone opens the deck or the PDF, which is how
m4b shipped with two formulas running off the right edge.

    python check-overflow.py docs/modules/m4-bayesian-inference/m4b-gaussian-posterior.html
    python check-overflow.py docs/modules/*/*.html          # everything

Exit status is 1 when any slide overflows, so this works in a pre-commit hook.

Two things that will otherwise waste your afternoon:

* reveal scales each slide with a CSS transform, so `getBoundingClientRect`
  reports post-transform pixels and every overflow measures as zero. Everything
  here is measured with `offsetWidth` / `scrollWidth`, which are untransformed.
* The decks pin KaTeX to a CDN. In a sandbox without network access the math
  never renders, every deck measures clean, and the check is worthless. If a
  local KaTeX dist is present the requests are served from it; otherwise the
  script warns when a deck renders zero math nodes but contains `$`.

Requires: playwright with chromium.
"""
import mimetypes
import os
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

CDN = "https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/"
# Optional offline KaTeX. Set KATEX_DIST, or leave unset to fetch from the CDN.
KATEX = Path(os.environ.get("KATEX_DIST", "")) if os.environ.get("KATEX_DIST") else None
CHROMIUM = os.environ.get("PLAYWRIGHT_CHROMIUM")  # optional explicit binary

# Elements are allowed to reach the content edge exactly; only real overhang counts.
SLOP = 4

MEASURE = """() => {
  const sec = document.querySelector('.reveal .slides section.present');
  if (!sec) return null;
  const limit = sec.clientWidth;
  let worst = 0, what = '';
  const note = (label, w) => {
    if (w - limit > worst) { worst = w - limit; what = label; }
  };
  for (const el of sec.querySelectorAll('.katex-display')) {
    const k = el.querySelector('.katex');
    if (k) note('display math', k.offsetWidth);
    note('display math', el.scrollWidth);
  }
  for (const el of sec.querySelectorAll('p, li, td, pre, img'))
    note(el.tagName.toLowerCase(), el.scrollWidth);
  return {
    title: (sec.querySelector('h1, h2') || {}).innerText || '',
    worst: Math.round(worst),
    what,
    vOver: Math.max(0, sec.scrollHeight - sec.clientHeight),
  };
}"""


def serve_katex(route, request):
    rel = request.url.split(CDN, 1)[1].split("?")[0]
    f = KATEX / rel
    if not f.is_file():
        route.abort()
        return
    ctype = mimetypes.guess_type(str(f))[0] or "application/octet-stream"
    if f.suffix == ".js":
        ctype = "application/javascript"
    route.fulfill(status=200, body=f.read_bytes(), content_type=ctype,
                  headers={"Access-Control-Allow-Origin": "*"})


def main(decks):
    problems = 0
    with sync_playwright() as pw:
        launch = {"args": ["--no-sandbox", "--disable-dev-shm-usage"]}
        if CHROMIUM:
            launch["executable_path"] = CHROMIUM
        b = pw.chromium.launch(**launch)
        pg = b.new_page(viewport={"width": 1050, "height": 700})
        if KATEX and KATEX.is_dir():
            pg.route(CDN + "**", serve_katex)

        for d in decks:
            path = Path(d).resolve()
            pg.goto(path.as_uri(), wait_until="load", timeout=120000)
            pg.wait_for_timeout(2500)
            n_math = pg.evaluate("document.querySelectorAll('.katex').length")
            n_slides = pg.evaluate("window.Reveal.getTotalSlides()")
            bad = []
            for i in range(n_slides):
                pg.evaluate("j => window.Reveal.slide(j, 0)", i)
                pg.wait_for_timeout(200)
                r = pg.evaluate(MEASURE)
                if r and (r["worst"] > SLOP or r["vOver"] > SLOP):
                    bad.append((i + 1, r))

            print(f"{path.name}: {len(bad)} of {n_slides} slides overflow "
                  f"({n_math} math nodes)")
            if n_math == 0 and "\\(" in path.read_text(encoding="utf-8", errors="ignore"):
                print("   WARNING: no math rendered. If this deck has formulas, KaTeX "
                      "did not load and the result is meaningless. Set KATEX_DIST.")
            for i, r in bad:
                bits = []
                if r["worst"] > SLOP:
                    bits.append(f"right +{r['worst']}px [{r['what']}]")
                if r["vOver"] > SLOP:
                    bits.append(f"bottom +{r['vOver']}px")
                print(f"   slide {i:2d}  {r['title'][:44]:44s} {'  '.join(bits)}")
            problems += len(bad)
        b.close()
    return problems


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.exit(1 if main(sys.argv[1:]) else 0)
