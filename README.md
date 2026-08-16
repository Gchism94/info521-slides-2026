# INFO 521 Slides (2026)

Quarto + reveal.js lecture decks for INFO 521, plus everything recorded or posted
alongside them: per-module overview decks, recording scripts, student note pages for
D2L, and rendered PDFs. Styling matches `info521-activities-2026` (Okabe-Ito palette
with redundant non-color cues, KaTeX 0.16.9, dark default with light toggle,
keyboard accessibility).

Seven modules, two lecture decks each (one for module 7), plus a module overview deck per
module and the instructor intro deck. All rendered output is committed under
`docs/`, which is what GitHub Pages serves.

## What is in this repo

```
_quarto.yml            shared revealjs format; renders into docs/
_variables.yml         cross-repo URL (activities site)
theme/info521.scss     UA + Okabe-Ito reveal theme; dark default, light toggle, print=light
shared/slide_helpers.py  matplotlib defaults + NHANES loader shim used by deck code cells
modules/<m>/           deck sources, one directory per module (m1 … m7)
  m<N><a|b>-*.qmd        the lecture decks
  m<N>-overview.qmd      the ~3-minute module overview deck (GENERATED; see below)
  index.qmd              the module landing page
intro/gc-intro.qmd     instructor introduction deck
scripts/<m>/*.script.md  recording scripts, one per deck: YAML header (scene count,
                         word count, runtime at 130 wpm), then one prose block per slide
notes/<m>/*.notes.md   student note pages (source for the D2L pages and PDFs)
d2l/                   D2L-ready HTML note pages + notes PDFs (d2l/pdf/)
overviews/             the overview-deck generator: module_spec.py + narration.py are
                       the single source; build_decks.py and build_docs.py emit the
                       overview decks, written overviews, and scripts
docs/                  rendered site (committed; served by GitHub Pages)
notes/, SOURCE_MAP.md  SOURCE_MAP.md maps every deck to its content authority
render.sh              renders every deck locally (HTML, and PDF via print pass)
build-notes-pdfs.py    renders notes/ to the PDFs in d2l/pdf/
check-overflow.py      headless check that no slide content overflows its frame
requirements.txt       Python deps for deck code cells (numpy 2.1.x: needs Python <= 3.13)
```

## Editing rules

- The `m<N>-overview.qmd` decks are **generated**. Edit
  `overviews/module_spec.py` / `overviews/narration.py` and re-run
  `python overviews/build_decks.py && python overviews/build_docs.py`. Hand edits
  are overwritten and silently desynchronize the recording scripts.
- Everything else is edited in place; re-render with `./render.sh` (or
  `quarto render modules/<m>/<deck>.qmd` for one deck) so `docs/` stays current.
- The course has one project in two parts (Part 1 and Part 2). The builders
  regression-check the overview decks for retired framing ("Project 1/2",
  capstone-scope language); keep new prose consistent with that.

## Publishing

GitHub Pages serves `docs/` via `.github/workflows/publish.yml`
(Settings → Pages → Source: GitHub Actions). Rendered output is committed, so the
site never depends on CI having a working Python toolchain.

## Environment

`render.sh` bootstraps a uv-managed Python 3.11 venv. numpy is pinned at 2.1.x,
which has no Python 3.14 wheels; keep Python at or below 3.13.
