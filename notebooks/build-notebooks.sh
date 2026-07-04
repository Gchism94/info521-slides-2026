#!/usr/bin/env bash
# Build the worked notebooks: .qmd (editable source) → executed .ipynb (D2L artifact).
# Runs inside the repo venv (info521 loader installed editable). LOCAL ONLY.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"
ROOT="$(cd .. && pwd)"
# shellcheck disable=SC1091
. "$ROOT/.venv/bin/activate"

for q in w*.qmd; do
  n="${q%.qmd}"
  echo "[notebooks] $n"
  quarto convert "$q" --output "$n.ipynb" --quiet
  jupyter nbconvert --to notebook --execute --inplace "$n.ipynb" \
    --ExecutePreprocessor.timeout=300 >/dev/null
done
echo "[notebooks] done — executed .ipynb files ready for D2L."
