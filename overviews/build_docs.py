#!/usr/bin/env python3
"""Build the written module overviews and the recording scripts.

Two documents per module, each in HTML and PDF, all four generated from
`module_spec.py` and `narration.py` so the deck, the written overview, and the
words you say over the deck cannot drift apart.

    overviews/out/module-<N>-overview.{html,pdf}   student-facing prose
    overviews/out/module-<N>-script.{html,pdf}     what you read while recording

    python overviews/build_docs.py            # all seven modules
    python overviews/build_docs.py 3 7        # just these

The script builder counts narration words at 140 wpm and fails the build when a
module drifts outside its target window. A script that has quietly doubled in
length is otherwise discovered in the recording booth.

Requires: quarto (bundles Typst), pdftotext (Poppler).
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from module_spec import MODULES, CLOS, WPM, by_number
from narration import NARRATION
from build_decks import slides

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "out"

# how far a script may land from its target before the build fails
TOLERANCE = 0.35

TYPST_HEADER = """    include-in-header:
      - text: |
          #show heading.where(level: 1): set text(fill: rgb("#1B4F72"))
          #show heading.where(level: 2): set text(fill: rgb("#1B4F72"))
          #show heading.where(level: 3): set text(fill: rgb("#205a80"))
          #show link: set text(fill: rgb("#AB0520"))
"""


def frontmatter(title, subtitle):
    return f"""---
title: "{title}"
subtitle: "{subtitle}"
format:
  typst:
    papersize: us-letter
    margin:
      x: 1.1in
      y: 1in
    fontsize: 10.5pt
    section-numbering: ""
    mainfont: Arial
{TYPST_HEADER}  html:
    embed-resources: true
    html-math-method: mathml
    toc: false
    theme: cosmo
format-links: false
---
"""


def words(s):
    return len(s.split())


# ────────────────────────── the written overview ──────────────────────────
def overview_md(m):
    parts = [f"## {m['question']}\n\n{m['question_gloss']}\n",
             "## What the lectures do\n"]
    for name, desc in m["lectures"]:
        parts.append(f"**{name}.** {desc}\n")
    parts.append(f"## Where this sits in the course\n\n{m['sits']}\n")
    parts.append(f"## {m['week']} at a glance\n")
    for w in m["work"]:
        parts.append(f"- {w}")
    parts.append("\n## Watch out for\n")
    for head, text in m["watch"]:
        parts.append(f"**{head}** {text}\n")

    if "wrapup" in m:
        w = m["wrapup"]
        parts.append("\n# Course wrap-up\n")
        parts.append("## The course, in one arc\n")
        parts.append("| Where | What changed |\n|---|---|")
        for where, what in w["arc"]:
            parts.append(f"| {where} | {what} |")
        parts.append(f"\n{w['arc_close']}\n")
        parts.append(f"## What you can do now\n\n{w['learned']}\n")
        parts.append("The five course outcomes, for reference:\n")
        for k, v in CLOS:
            parts.append(f"- **{k}.** {v}")
        parts.append("\n## What is left to do\n")
        for item in w["left"]:
            parts.append(f"- {item}")
        parts.append(f"\n## Where next\n\n{w['next']}\n")

    return "\n".join(parts)


# ────────────────────────────── the script ──────────────────────────────
def script_md(m):
    narr = NARRATION[m["n"]]
    deck = slides(m)
    ids = ["open"] + [sid for sid, _, _ in deck]
    missing = [i for i in ids if i not in narr]
    extra = [k for k in narr if k not in ids]
    if missing or extra:
        raise SystemExit(f"Module {m['n']} narration mismatch: "
                         f"missing {missing}, unused {extra}")

    total = sum(words(narr[i]) for i in ids)
    mins = total / WPM
    parts = [
        f"**Target:** {m['minutes']} minutes. **Draft:** {total} words, about "
        f"{mins:.1f} minutes at {WPM} words per minute.\n",
        "Slide headings below match the deck exactly. Advance on the heading.\n",
        "---\n",
        f"### Title slide\n\n*Module {m['n']}: {m['title']}*\n\n{narr['open']}\n",
    ]
    for sid, heading, _ in deck:
        w = words(narr[sid])
        parts.append(f"### Slide: {heading}\n\n*({w} words, about "
                     f"{w / WPM * 60:.0f} seconds)*\n\n{narr[sid]}\n")
    return "\n".join(parts), total, mins


# ─────────────────────────────── rendering ───────────────────────────────
def render(stem, title, subtitle, body):
    made = []
    for fmt, ext in (("typst", "pdf"), ("html", "html")):
        qmd = ROOT / f"_{stem}.qmd"
        qmd.write_text(frontmatter(title, subtitle) + "\n" + body, encoding="utf-8")
        r = subprocess.run(["quarto", "render", str(qmd), "--to", fmt],
                           capture_output=True, text=True, cwd=ROOT)
        produced = ROOT / f"_{stem}.{ext}"
        qmd.unlink(missing_ok=True)
        if r.returncode != 0 or not produced.exists():
            print(f"  FAIL {stem}.{ext}\n{r.stdout[-900:]}{r.stderr[-900:]}")
            continue
        if ext == "html":
            h = produced.read_text(encoding="utf-8")
            h = re.sub(r'\s*<script src="https://cdnjs\.cloudflare\.com/polyfill[^"]*"></script>',
                       "", h)
            produced.write_text(h, encoding="utf-8")
        dest = OUT / f"{stem}.{ext}"
        shutil.move(str(produced), str(dest))
        made.append(dest)
    shutil.rmtree(ROOT / f"_{stem}_files", ignore_errors=True)
    return made


def house_script_md(m):
    """The recording script in the repo's own lecture-script format.

    Every other deck has one at `scripts/<module-dir>/<deck-stem>.script.md`:
    YAML front matter, then one `## <slide title>` block of spoken prose per
    slide. The overview decks are decks, so their scripts belong in the same
    place and the same shape. The rendered HTML and PDF in overviews/out are the
    reading copies; this is the source of record.
    """
    narr = NARRATION[m["n"]]
    deck = slides(m)
    ids = ["open"] + [sid for sid, _, _ in deck]
    total = sum(words(narr[i]) for i in ids)
    sub = f"INFO 521 · Module {m['n']} · Overview"
    if m["n"] == 7:
        sub += " and Course Wrap-Up"
    head = (
        "---\n"
        f'deck: "Module {m["n"]}: {m["title"]}"\n'
        f'subtitle: "{sub}"\n'
        f"source_qmd: modules/{m['dir']}/m{m['n']}-overview.qmd\n"
        f"dest: scripts/{m['dir']}/m{m['n']}-overview.script.md\n"
        f"generated_from: overviews/module_spec.py + overviews/narration.py\n"
        f"scenes: {len(ids)}\n"
        f"est_spoken_words: {total}\n"
        f"est_runtime_min: {total / WPM:.1f}   # at ~{WPM} wpm\n"
        "---\n"
    )
    body = [f"\n## Title slide — Module {m['n']}: {m['title']}\n\n{narr['open']}\n"]
    for sid, heading, _ in deck:
        body.append(f"\n## {heading}\n\n{narr[sid]}\n")
    return head + "".join(body)


def text_of(p):
    if p.suffix == ".pdf":
        return subprocess.run(["pdftotext", str(p), "-"],
                              capture_output=True, text=True).stdout
    raw = p.read_text(encoding="utf-8")
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", raw, flags=re.S)
    return re.sub(r"<[^>]+>", " ", t)


def main():
    OUT.mkdir(exist_ok=True)
    wanted = [int(a) for a in sys.argv[1:]] or [m["n"] for m in MODULES]
    built, timing = [], []

    print("Building module overviews and scripts:")
    for n in wanted:
        m = by_number(n)
        sub = f"INFO 521 · Machine Learning Foundations · {m['week']}"
        built += render(f"module-{n}-overview",
                        f"Module {n}: {m['title']}",
                        sub + " · module overview", overview_md(m))
        body, total, mins = script_md(m)
        timing.append((n, total, mins, m["minutes"]))
        house = ROOT.parent / "scripts" / m["dir"] / f"m{n}-overview.script.md"
        house.parent.mkdir(parents=True, exist_ok=True)
        house.write_text(house_script_md(m), encoding="utf-8")
        print(f"  {house.relative_to(ROOT.parent)}")
        built += render(f"module-{n}-script",
                        f"Module {n} overview: recording script",
                        sub + " · instructor script", body)
        for p in built[-4:]:
            print(f"  {p.relative_to(ROOT)}")

    print("\nHouse-format scripts:")
    for n in wanted:
        m = by_number(n)
        h = ROOT.parent / "scripts" / m["dir"] / f"m{n}-overview.script.md"
        t = h.read_text(encoding="utf-8")
        ok = (h.exists() and t.startswith("---") and "est_runtime_min" in t
              and t.count("\n## ") == len(slides(m)) + 1)
        print(f"  {'clean' if ok else 'FAIL '} {h.relative_to(ROOT.parent)}")
        if not ok:
            sys.exit(f"malformed house script for module {n}")

    print("\nTiming:")
    bad = 0
    for n, total, mins, target in timing:
        lo, hi = target * (1 - TOLERANCE), target * (1 + TOLERANCE)
        ok = lo <= mins <= hi
        print(f"  Module {n}: {total:4d} words, {mins:4.1f} min "
              f"(target {target}, window {lo:.1f} to {hi:.1f})"
              f"{'' if ok else '   OUT OF RANGE'}")
        bad += (not ok)

    print("\nChecks:")
    for p in built:
        txt = re.sub(r"\s+", " ", text_of(p))
        problems = []
        n = int(re.search(r"module-(\d)-", p.name).group(1))
        m = by_number(n)
        if m["week"] not in txt:
            problems.append("week band missing")
        if "script" in p.name:
            if "words per minute" not in txt:
                problems.append("timing header missing")
            if "Slide:" not in txt:
                problems.append("slide cues missing")
        else:
            if "Watch out for" not in txt:
                problems.append("pitfalls section missing")
            if n == 7 and "Course wrap-up" not in txt:
                problems.append("wrap-up section missing")
        for term in ("Project 1 and Project 2", "closed-book homework", "decktape"):
            if term in txt:
                problems.append(f"stale {term!r}")
        # the self-guided capstone is no longer an option; the project is one path
        for term in ("capstone", "both scopes", "structured scope", "project scope"):
            if term in txt.lower():
                problems.append(f"retired scope language {term!r}")
        if "—" in txt or "–" in txt:
            problems.append("dash character in text")
        if p.suffix == ".html":
            raw = p.read_text(encoding="utf-8")
            if re.search(r'(?:src|href)="https?://[^"]*\.(?:js|css|woff2?)"', raw):
                problems.append("external resource")
            if re.search(r"https?://cdn[^\"']*\.js", raw):
                problems.append("cdn script url")
        if problems:
            print(f"  FAIL  {p.name}: {'; '.join(problems)}")
            bad += 1
        else:
            print(f"  clean {p.name}")
    if bad:
        sys.exit(1)
    print(f"\nAll {len(built)} documents built and checked into {OUT}.")


if __name__ == "__main__":
    main()
