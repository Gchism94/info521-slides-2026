# D2L lecture-note pages

One self-contained HTML page per lecture, the D2L-ready version of the Markdown
in `notes/`. Each carries the course dark theme (matching the `d2l/` activity
stubs in the activities repo) and renders its equations with MathJax.

**Usage:** in D2L, **upload the matching `*.html` file** as a content topic.
Do *not* paste the source into the D2L HTML/WYSIWYG editor â it strips the
MathJax `<script>`, so the math would show as raw LaTeX. Uploaded HTML topics
run the script and render correctly.

**Dependency:** the only external dependency is the MathJax CDN
(`cdn.jsdelivr.net/npm/mathjax@3`). If your D2L instance blocks external
scripts, a MathML-prerendered variant that needs no script can be produced.

## PDFs (`pdf/`)

`pdf/` carries the same lecture material as printable, D2L-attachable PDFs, two
families with matching stems so everything sorts together:

- `slides-<deck>.pdf` — one landscape page per slide, forced light, copied from
  the rendered decks in `../docs/`. Regenerate the decks first (`./render.sh`),
  then re-copy.
- `notes-<deck>.pdf` — the student notes from `../notes/`, US Letter, UA styled.
  Regenerate with `python build-notes-pdfs.py` from the repo root (needs quarto
  and pdftotext).

Upload either as content-topic attachments beside the matching HTML page; the
PDFs need no external scripts, so they also work where D2L blocks the MathJax
CDN the HTML pages rely on.

## Pages

| File | Lecture |
|---|---|
| `m1a-setup-and-model.html` | Module 1 · Lecture A â Setup, Data & the Linear Model |
| `m1b-normal-equations.html` | Module 1 · Lecture B â Normal Equations & Geometry |
| `m2a-evaluation-cv.html` | Module 2 · Lecture A â Evaluation & Cross-Validation |
| `m2b-bias-variance-ridge.html` | Module 2 · Lecture B â Bias–Variance & Regularization |
| `m3a-likelihood-mle.html` | Module 3 · Lecture A â Likelihood & Maximum Likelihood |
| `m3b-mle-uncertainty.html` | Module 3 · Lecture B â Properties of the MLE: Uncertainty in Parameters |
| `m4a-bayes-beta-binomial.html` | Module 4 · Lecture A â Priors, Posteriors & the Beta–Binomial |
| `m4b-gaussian-posterior.html` | Module 4 · Lecture B â The Conjugate Gaussian Posterior |
| `m5a-logistic-newton.html` | Module 5 · Lecture A â Breaking Conjugacy: Logistic Regression & Newton's Method |
| `m5b-laplace-sampling.html` | Module 5 · Lecture B â Laplace Approximation & a Taste of Sampling |
| `m6a-svm.html` | Module 6 · Lecture A â Maximum-Margin Classification |
| `m6b-kmeans-clustering.html` | Module 6 · Lecture B â k-means & the Unsupervised Turn |
| `m7a-pca.html` | Module 7 â Principal Component Analysis & Course Synthesis |
