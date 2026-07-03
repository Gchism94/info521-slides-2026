#!/usr/bin/env bash
# Render every INFO 521 slide deck locally to self-contained HTML (and PDF).
# LOCAL ONLY: this never pushes, publishes, or touches GitHub Pages — staging
# docs/ is the end of the line; publishing is Greg's manual step.
#
# Usage:
#   ./render.sh           # one-time env bootstrap (if needed) + render HTML + PDF
#   ./render.sh html      # HTML only
#   ./render.sh pdf       # PDF only (per-deck print-pdf)
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

MODE="${1:-all}"

# ---------------------------------------------------------------------------
# 1. Python env. Quarto's {python} engine needs Python 3.11–3.13 (numpy 2.1.x
#    ships no cp314 wheel). Build .venv once with uv against Python 3.11.
# ---------------------------------------------------------------------------
if [ ! -d "$ROOT/.venv" ]; then
  echo "[render] creating .venv (Python 3.11) ..."
  uv venv --python 3.11 "$ROOT/.venv"
  # shellcheck disable=SC1091
  . "$ROOT/.venv/bin/activate"
  uv pip install -r requirements.txt
else
  # shellcheck disable=SC1091
  . "$ROOT/.venv/bin/activate"
fi

# Quarto should use this interpreter for {python} cells.
export QUARTO_PYTHON="$ROOT/.venv/bin/python"

# ---------------------------------------------------------------------------
# 2. Render. HTML is the primary artifact (embed-resources self-contained).
# ---------------------------------------------------------------------------
if [ "$MODE" = "all" ] || [ "$MODE" = "html" ]; then
  echo "[render] HTML -> docs/ ..."
  quarto render
fi

# ---------------------------------------------------------------------------
# 3. PDF. revealjs does NOT emit a PDF itself. We use decktape, which drives the
#    deck slide-by-slide and is deterministic — unlike Chrome's `?print-pdf`
#    --print-to-pdf, which races on this machine (orientation flips
#    portrait/landscape and pagination yields 1 vs N pages run-to-run).
#
#    decktape captures SCREEN media, so @media print does NOT apply. To still
#    ship a forced-light PDF, we decktape a temp copy of each deck with the light
#    theme forced (data-theme=light) on a pure-white background. Output
#    (<deck>.pdf) sits beside the HTML under docs/. One landscape page per slide.
#
#    Notes:
#    * decktape's bundled Chromium download is unreliable here, so we point it at
#      the system Chrome via --chrome-path. First `npx decktape` run fetches the
#      decktape package (cached afterward).
#    * Fallback if decktape/npx are unavailable: open <deck>.html?print-pdf in
#      Chrome and "Save as PDF" (landscape) — the @media print rules force light.
# ---------------------------------------------------------------------------
if [ "$MODE" = "all" ] || [ "$MODE" = "pdf" ]; then
  CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
  if [ ! -x "$CHROME" ]; then
    echo "[render] Chrome not found at \$CHROME; skipping PDF. Set CHROME=... ." >&2
  elif ! command -v npx >/dev/null 2>&1; then
    echo "[render] npx not found; skipping PDF (decktape needs it). See header for the manual fallback." >&2
  else
    echo "[render] PDF (decktape, forced-light) ..."
    while IFS= read -r html; do
      pdf="${html%.html}.pdf"
      tmp="${html%.html}.pdf-light.html"
      # Forced-light temp copy: light tokens + pure-white bg, toggle hidden.
      python - "$ROOT/$html" "$ROOT/$tmp" <<'PY'
import sys
src, dst = sys.argv[1], sys.argv[2]
h = open(src, encoding="utf-8").read()
inject = (
    '<style id="pdf-force-light">'
    'html,body,.reveal-viewport,.reveal,.reveal .slides section'
    '{background:#fff !important;background-color:#fff !important;}'
    '#info521-theme-toggle{display:none !important;}'
    '</style>'
    '<script>document.documentElement.setAttribute("data-theme","light");</script>'
)
i = h.rfind("</body>")
open(dst, "w", encoding="utf-8").write(h[:i] + inject + h[i:])
PY
      npx -y decktape@3 reveal --chrome-path "$CHROME" \
        "file://$ROOT/$tmp" "$ROOT/$pdf" 2>&1 | grep -E "Printed [0-9]+ slides" || true
      rm -f "$ROOT/$tmp"
      sz=$( [ -f "$ROOT/$pdf" ] && wc -c < "$ROOT/$pdf" || echo 0 )
      echo "  - $pdf  (${sz} bytes)"
    done < <(cd "$ROOT" && find docs -name '*.html' ! -name 'index.html')   # every deck; index.html = thin landings, not decks
  fi
fi

echo "[render] done. Review docs/ — publishing is a manual step (not done here)."
