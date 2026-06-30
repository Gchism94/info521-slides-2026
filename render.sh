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
# 3. PDF. revealjs does NOT emit a PDF itself — `?print-pdf` is a browser print
#    mode. We drive headless Chrome's --print-to-pdf over each rendered deck's
#    `index.html?print-pdf` URL; the deck's @media print rules force the light
#    theme on white. Output (index.pdf) sits beside the HTML under docs/.
#
#    Notes:
#    * --headless=new + --run-all-compositor-stages-before-draw is what makes
#      reveal finish paginating before capture; plain --headless yields blanks.
#    * Pagination occasionally races and yields a 1-page/near-empty PDF — we
#      retry up to 3x and keep the largest result.
#    * Fallback if Chrome misbehaves: decktape (npx decktape reveal IN OUT).
# ---------------------------------------------------------------------------
if [ "$MODE" = "all" ] || [ "$MODE" = "pdf" ]; then
  CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
  if [ ! -x "$CHROME" ]; then
    echo "[render] Chrome not found at \$CHROME; skipping PDF. Set CHROME=... or use decktape." >&2
  else
    echo "[render] PDF (headless Chrome print-to-pdf) ..."
    while IFS= read -r html; do
      pdf="${html%.html}.pdf"
      best=0
      for attempt in 1 2 3; do
        "$CHROME" --headless=new --disable-gpu --no-pdf-header-footer \
          --run-all-compositor-stages-before-draw --virtual-time-budget=20000 \
          --window-size=1600,1200 \
          --print-to-pdf="$pdf.try" "file://$ROOT/$html?print-pdf" >/dev/null 2>&1 || true
        sz=$( [ -f "$pdf.try" ] && wc -c < "$pdf.try" || echo 0 )
        if [ "$sz" -gt "$best" ]; then best=$sz; mv -f "$pdf.try" "$pdf"; else rm -f "$pdf.try"; fi
        # ~50KB+ means real multi-slide pagination landed; good enough to stop.
        [ "$best" -gt 50000 ] && break
      done
      echo "  - $pdf  (${best} bytes)"
    done < <(cd "$ROOT" && find docs -name index.html)
  fi
fi

echo "[render] done. Review docs/ — publishing is a manual step (not done here)."
