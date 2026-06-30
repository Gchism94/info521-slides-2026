# INFO 521 — Slides (2026)

Quarto + reveal.js lecture decks for INFO 521. The slides counterpart to
[`info521-activities-2026`](../info521-activities-2026); it mirrors that repo's
conventions (Okabe-Ito data palette with redundant non-color cues, KaTeX 0.16.9,
full dark mode, accessibility, no ES modules) so notation and styling stay
consistent across the course.

## Layout

```
_quarto.yml              shared revealjs format (theme, embed-resources, katex, svg)
theme/info521.scss       UA + Okabe-Ito reveal theme; dark default + light toggle; print=light
shared/slide_helpers.py  matplotlib Okabe-Ito defaults + NHANES loader shim
modules/<m>/index.qmd     one deck per module (topic-named, not lecture numbers)
docs/                    rendered, self-contained HTML decks (tracked; Pages output)
render.sh                local render to HTML (+ PDF); never publishes
requirements.txt         numpy 2.1.x + matplotlib + jupyter + editable info521 loader
```

## Build

Python **3.11–3.13** is required (numpy 2.1.x has no cp314 wheel). `render.sh`
bootstraps a `.venv` with `uv` against Python 3.11 on first run:

```bash
./render.sh          # env bootstrap (first run) + render all decks to docs/ (HTML + PDF)
./render.sh html     # HTML only
./render.sh pdf      # PDF only
```

Each deck renders to a single self-contained `.html` (figures/CSS/JS inlined)
suitable for upload to D2L. KaTeX 0.16.9 loads from jsdelivr (the one external
dependency, matching the activities repo).

## Conventions

- **PML (Murphy) notation**, identical to the activities repo.
- **Okabe-Ito data palette only**, every hue paired with a redundant non-color
  cue (line style / marker). Accessibility floor, not a preference.
- **Classic scripts only** (no ES modules) so decks open via `file://`.
- **Dark mode default**; an unobtrusive toggle flips to light in-session
  (no `localStorage`). Print forces light on a white background.

## The NHANES loader

Figures pull data through the `info521` package
([`../info521-projects-2026/common/info521`](../info521-projects-2026)),
installed **editable** so its bundled NHANES extract resolves. It is *plumbing
only* — no estimators; least-squares fits are written from scratch in the decks.

## Publishing

Local only. `git init` + local commits. Repo creation, remotes, pushes, Pages,
and Classroom wiring are all manual steps done outside this tooling.
