# Cowork task brief — INFO 521 lecture delivery scripts (M1–M7)

**Destination for this file:** keep at repo root as `scripts/COWORK_BRIEF.md` (reference doc; not a deck).

---

## Goal

Write **lecture delivery scripts** for the INFO 521 reveal.js decks — the words Greg says
while presenting (or self-recording a voiceover for) each deck, one block per slide. This is
a live-delivery aid: a script Greg reads and speaks from, slide by slide. It is **not**
avatar/TTS narration and **not** student-facing notes (see Phase 2 for the optional notes
pass).

Run on the **Opus model at HIGH reasoning effort** for Module 1. After M1 is approved (STOP
GATE 1), you may drop to **medium** for M2–M7 — the template will be locked by then.

## Repo, paths, and what to read first

Slides repo root:
`/Users/gregchism/dev/InfoSciCourses/INFO521/info521-slides-2026`

- **Source of truth = the QMD decks in `modules/`** — NOT `docs/modules/` (rendered
  HTML/PDF; never parse it).
- Read first: `CLAUDE.md` and `SOURCE_MAP.md` at the repo root — the 7-module arc,
  PML/Murphy notation, the single NHANES dataset, and three load-bearing through-lines.
  **They are the authority** — do not infer any mapping from slug names.
- **Two approved exemplars already exist** — read both before writing anything and match
  their format and voice exactly:
  - `scripts/m3-mle-uncertainty/m3a-likelihood-mle.script.md`  (static deck)
  - `scripts/m3-mle-uncertainty/m3b-mle-uncertainty.script.md`  (embed deck — shows the
    live-tool calibration described below)

Live activity tools (for embed decks):
`/Users/gregchism/dev/InfoSciCourses/INFO521/info521-activities-2026`
Each tool is a directory with `index.html` plus a JS file (e.g. `demo.js`).

## Scope — the 11 remaining decks

M3 is done (m3a, m3b). Write scripts for these, in M1→M7 order. **●** marks decks that
embed a live activity tool and therefore require the calibration step below.

| Module | Deck | Embed? | Live tool dir (activities repo) |
|---|---|---|---|
| M1 | `m1a-setup-and-model` | ● | `week01-least-squares` |
| M1 | `m1b-normal-equations` | — | — |
| M2 | `m2a-evaluation-cv` | — | — |
| M2 | `m2b-bias-variance-ridge` | ● | `week02-bias-variance` |
| M4 | `m4a-bayes-beta-binomial` | ● | `week03-bayesian-updating` |
| M4 | `m4b-gaussian-posterior` | — | — |
| M5 | `m5a-logistic-newton` | ● | `week04-logistic-regression` |
| M5 | `m5b-laplace-sampling` | — | — |
| M6 | `m6a-svm` | — | — |
| M6 | `m6b-kmeans-clustering` | ● | `week05-kmeans` |
| M7 | `m7a-pca` | ● | `week06-pca` |

Do **not** write scripts for `index.qmd` (thin landing pages) or the `appendix-*.qmd` decks.

## What a script is

- Every reveal.js slide — each `##` heading (and `#` section dividers) — is **one delivery
  block**. Give it the spoken narration for that slide.
- Content under a heading, including every `::: {.fragment}` reveal and each bullet, belongs
  to that block, narrated in the order it appears on screen. Insert a sparse `> [cue: ...]`
  line where a fragment reveals or a delivery beat helps (advance, pause, point). These cues
  are stage directions for Greg.
- `::: {.notes}` blocks are **private director's cues** (emphasis, the `(Clay NN)` source
  credit, what lands well). Use them to decide framing, then write full spoken prose. Never
  read a note verbatim; never speak the `(Clay NN)` credits; never speak CUTTABLE/HTML
  comments.
- The **title slide** (YAML front matter) becomes an opening block: name the module and
  lecture, one sentence of where it's going, and speak the attribution plainly — "These
  materials are adapted with permission from lecture materials by Clayton Morrison at the
  University of Arizona."

## Math in a delivery script

Greg reads off his own slide, so this is looser than TTS narration: **lean toward spoken
math where it aids delivery, but referencing an equation by sight is fine.** Say what the
equation *means* and speak the key line the way a lecturer talks over a derivation — don't
enumerate every symbol in a dense expression, and don't pre-verbalize equations that are
easier to just point at on the slide. Style examples (a guide, not a hard rule):

- `$\hat{\mathbf{w}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}$`
  → "w-hat is X-transpose-X inverse, times X-transpose y."
- `$\mathbf{H} = -\tfrac{1}{\sigma^2}\mathbf{X}^\top\mathbf{X}$`
  → "the Hessian — minus one over sigma-squared, times X-transpose-X."

Greek by name, hats as "-hat", numbers and units natural ("about 16 millimeters of
mercury").

## Figures and code cells

`{python}` cells render figures; students see the plot, never the code. **Never narrate
code.** Use each cell's `fig-cap` and `fig-alt` to say, in spoken words, what the figure
shows and the one thing to take from it.

## Embed decks — live-tool calibration (the ● decks)

Before writing the demo/"live" block of a ● deck, **read that deck's live tool** —
`index.html` plus its JS — in the activities dir named in the scope table. Then narrate the
tool's **actual controls in the order Greg would drive them**: name the real buttons and
sliders, describe what each does on screen, and note any reset behavior. Flag the static
figure on the preceding slide as the fallback if the embed can't load.

Worked example (already in `m3b`): the m3 explorer has **Draw one dataset / Draw 100 / Reset
cloud** buttons and **sample-size N** and **noise σ** sliders; changing σ or N *resets the
cloud*. The demo block drives Draw one → Draw 100 (cloud floods the 2σ theory ellipse,
centered on the true-w marker = unbiasedness visible), points at the empirical-SD-vs-theory
readout converging, then nudges a slider (cloud clears) and redraws wider. Match that
control-accuracy for every ● deck.

## Cuttable slides

Slides marked `<!-- CUTTABLE -->` open their block with
`> [cue: optional — cut if running long; nothing downstream depends on it]`, and their
narration must not set up a hard dependency for the next slide.

## Voice and length

- Greg lecturing to graduate students: warm, direct, precise, a little wry. NHANES clinical
  framing throughout. Confident but honest about model limits — the decks make a point of
  "useful, not true"; keep that.
- ~60–120 spoken words per content slide, scaled to slide density; title and section/recap
  slides shorter. Natural spoken rhythm, contractions, short sentences.

## Through-lines to keep audible (from SOURCE_MAP)

1. **The XᵀX object** — the same X-transpose-X runs from the M1 loss bowl → M3
   negative-definite Hessian / Fisher information → M5 Laplace posterior covariance.
2. **The conjugacy keystone** — M4 closes on the closed-form conjugate Gaussian posterior;
   M5 opens by binarizing the outcome to break conjugacy.
3. **One dataset** — every data figure is the same NHANES blood-pressure problem.

## Output format and location

Create a `scripts/` file per deck, mirroring `modules/`:
`scripts/m1-linear-least-squares/m1a-setup-and-model.script.md` (etc.)

Each file:
- A front-matter block: `deck`, `subtitle`, `source_qmd`, `dest`, `scenes`,
  `est_spoken_words`, `est_runtime_min` (with `# at ~130 wpm — rough class-time pacing`).
  Runtime is a **pacing check** — a flag for decks that clearly overrun the slot — not a
  hard target.
- Then one section per slide, using the **exact slide title** as an `##` header, followed by
  the spoken narration as plain prose, with sparse `> [cue: ...]` lines.

## Write path and git (Cowork mechanics)

- Write each script directly to its `scripts/…` path with the Filesystem tools.
- **Known instability:** the Filesystem *write* path can hang (~4-minute timeout). If a write
  hangs, do **not** retry more than once — produce the file for manual placement, hand it
  off, and note in the manifest that the deck needs placement. Reads are reliable; only
  writes are affected.
- **Git is Greg's, entirely.** Cowork never runs `git` and never does any remote operation.
  Greg places (if on the fallback) and commits.

## Run rhythm, resumability, manifest

- Work **module by module**, M1→M7. Read each deck's full QMD before writing; for ● decks,
  read the live tool first.
- Maintain a running **manifest** (deck · scenes · words · est. runtime · written?/placed?)
  checked against the 11-deck queue, so the run is **resumable** — if the MCP stalls and the
  app restarts, resume at the first unwritten deck with nothing lost.
- **If writes land directly on disk:** deliver each module and continue; Greg commits at his
  own pace. **If on the manual-placement fallback:** pause after each module so files are
  placed before the next.

## STOP gates

- **STOP GATE 1 — after Module 1.** Deliver m1a + m1b, then stop and report the two scripts,
  the manifest rows, and confirmation the template held against a fresh (non-M3) exemplar.
  Wait for Greg to approve before continuing M2–M7 (and to confirm the model drop to medium).
- **FINAL STOP — after all 11 decks.** Report a summary manifest table (deck, scene count,
  word count, est. runtime, total). Then ask whether to also script the three appendix decks
  (`appendix-matrix-calculus`, `appendix-bias-variance`, `appendix-covariance`).

## Phase 2 (optional, deferred) — student notes

Do **not** start this during the script run. After the delivery scripts are approved, notes
can be *derived from the approved scripts* (a better source than the QMDs, since the script
already holds the connective narration). If greenlit, scope them deliberately:

- **Register shift:** first-person spoken → second/third-person written; reference equations
  by sight; describe demo slides as "the explorer lets you…", not "let me…".
- **Narrative spine, not derivations:** capture intuition, key results, and the order the
  argument moves in. **Defer full derivations to the existing appendices** (matrix-calculus,
  covariance, bias-variance) — link out, don't duplicate. Keep the three through-lines
  visible.
- Separate output tree (e.g. `notes/`), one file per deck, its own STOP gate after M1.

## Launch toggles (Greg's calls)

- **Model/effort:** default Opus / high for M1, drop to medium after STOP GATE 1.
- **Appendices:** default = held for a separate pass after the 11 core decks.
- **Phase 2 notes:** default = deferred; decide after the scripts land.
