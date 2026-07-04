# Worked notebooks

The per-module worked notebooks promised in the Course Map's Learning Materials — executed
`.ipynb` files for **D2L upload**, with `.qmd` as the editable source of truth.

| Week | Notebook | Companion lecture(s) |
|---|---|---|
| 1 | `w1-first-look-least-squares` | m1a / m1b |
| 2 | `w2-cv-ridge` | m2a / m2b |
| 3 | `w3-likelihood-mle` | m3a / m3b |
| 4 | `w4-sequential-posterior` | m4a / m4b |
| 5 | `w5-newton-metropolis` | m5a / m5b |
| 6 | `w6-kmeans-restarts` | m6b |
| 7 | `w7-pca-biomarkers` | m7a |

Conventions (mirroring the decks): NHANES via the `info521` loader, from-scratch numpy,
seed `default_rng(521)`, Okabe-Ito palette, one "Try it yourself" prompt per notebook.
They are worked *examples* aligned to already-public lecture figure code — not homework
solutions.

**Edit the `.qmd`, then rebuild:** `./build-notebooks.sh` (converts and executes in the
repo venv, which has the editable `info521` package). Students running them need the
course environment from Unit 0's GitHub Classroom setup; on D2L they read fine as
executed notebooks.

These are lecture-support materials, not rendered into the Pages site (`_quarto.yml`'s
render list covers only `index.qmd` and `modules/**`).
