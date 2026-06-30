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
# 3. PDF. revealjs PDF export is per-deck via `-M print-pdf` (needs Chrome;
#    `quarto check` reports Chrome found on this machine). Output sits beside
#    the deck's HTML under docs/.
# ---------------------------------------------------------------------------
if [ "$MODE" = "all" ] || [ "$MODE" = "pdf" ]; then
  echo "[render] PDF (print-pdf) ..."
  while IFS= read -r qmd; do
    echo "  - $qmd"
    quarto render "$qmd" -M print-pdf
  done < <(find modules -name index.qmd)
  # Fallback if print-pdf is unavailable: decktape (npm i -g decktape), e.g.
  #   decktape reveal docs/modules/m1-linear-least-squares/index.html out.pdf
fi

echo "[render] done. Review docs/ — publishing is a manual step (not done here)."
