# SOURCE_MAP.md — Clay Morrison lectures → INFO 521 (2026) module arc

Crosswalk from Clay Morrison's source lecture decks to the redesigned **7-module / 7.5-week** arc. This is an authored scoping document — it contains **no** Clay content and is safe to commit. The source decks themselves live outside any repo at `../_source-lectures-morrison/` (reference only, used with permission, never committed, never published).

**Reconciliation deltas applied to every deck on conversion**
- **Notation → PML/Murphy:** targets $y_n$, design matrix $\mathbf{X}$, weights $\mathbf{w}$, loss $\mathcal{L}$ = MSE. (Clay uses Bishop/FCML targets $t_n$.)
- **Examples → NHANES:** the one clinical dataset carried all term.
- **Chrome → UA + Okabe-Ito theme** (replaces SISTA footer / saguaro title).
- **Figures →** matplotlib `{python}` cells (data) or redrawn SVG (schematic).

**Source inventory:** 28 PDFs across 26 numbered lectures (Lecture 09 and 12 each ship an extra sub-deck).

**Dispositions:** `Keep` · `Keep-compress` · `Keep-trim` · `Async` (→ reading / prereq quiz, not a live lecture) · `Activity` (→ in-class or interactive tool, not a slide module) · `Build-fresh` · `Cut`

---

## M1 · Linear models & least squares — Wk1 · P1-M1 · activity: LS explorer
| Clay | Title | Disposition | Notes |
|---|---|---|---|
| 01 | Introduction | Keep-trim | NHANES + preprocessing entry point |
| 02 | ML Linear Model | Keep | |
| 03 | Scalar Least Squares | Keep | |
| 04 | Higher Dimensions | Keep | design matrix, normal equations |
| 05 | Geometry & Nonlinear Response | Keep-compress | projection geometry + basis functions |

## M2 · Generalization — Wk2 · supports P1 · activity: bias-variance/ridge
| Clay | Title | Disposition | Notes |
|---|---|---|---|
| 06 | Evaluation / CV | Keep | |
| 07 | Model Selection & Regularization | Keep | ridge |
| 14 | Bias-Variance Tradeoff | Keep | |

## M3 · MLE & parameter uncertainty — Wk3 · P1-M2
| Clay | Title | Disposition | Notes |
|---|---|---|---|
| 08 | Probability Review | Async | prereq reading + prereq quiz |
| 09a | Expectation / Discrete Distributions | Async | prereq |
| 09b | Continuous Probability / Gaussian | Keep-compress | keep the Gaussian; rest async |
| 10 | Linear Gaussian Noise & ML | Keep | likelihood; MLE = least squares |
| 11 | Maximum Likelihood | Keep | |
| 12 | Properties of Linear Gaussian Model 01 | Keep-compress | ✓ converted → modules/m3-mle-uncertainty/ (+ appendix-covariance) |
| 13 | Properties of Linear Gaussian Model 02 | Keep-compress | Fisher info + worked example |

## M4 · Bayesian inference — Wk4 · P1-M3 · activity: Beta-Binomial
| Clay | Title | Disposition | Notes |
|---|---|---|---|
| 15 | Intro to Bayes | Keep | |
| 16 | Posterior / Prior Scenarios | Keep | |
| 17 | Using Posterior / Marginal Likelihood / Hyperparams | Keep | lands on conjugate posterior (**keystone**) |

## M5 · Approximate inference + Bayesian classification — Wk5 · P2 Gate A · activity: logistic + Newton
| Clay | Title | Disposition | Notes |
|---|---|---|---|
| 19 | Estimation I — Gradient & Newton-Raphson | Keep | |
| 20 | Estimation II — Laplace Approximation | Keep | Laplace cov = inverse Hessian = inverse Fisher info |
| 21 | Estimation III — Sampling / MH | Keep | |
| 22 | Classification — Bayes | Keep | binarize → break-conjugacy application · ⚠ confirm not a naive-Bayes generative deck |

## M6 · SVM + clustering — Wk6 · P2 Gate A/B · activity: k-means
| Clay | Title | Disposition | Notes |
|---|---|---|---|
| — | SVM | Build-fresh | no Clay source; lecture-only for now (stub activity TBD) |
| 23 | Classification — NN Evaluation | Keep-compress | eval metrics → SVM eval; kNN off-arc (cut / one-slide mention) |
| 24 | Clustering — k-means | Keep | |
| 25 | Clustering — Mixture Models / GMM & EM | Keep-compress | soft-assignment bridge + honest cluster-vs-label (RR framing) |

## M7 · PCA — Wk7 · P2 Gate B · activity: PCA
| Clay | Title | Disposition | Notes |
|---|---|---|---|
| 26 | Projection / PCA | Keep | covariance eigendecomposition; + Gate B synthesis |

## Off-arc (not slide modules)
| Clay | Title | Disposition | Notes |
|---|---|---|---|
| 12a | Numpy default_rng | Activity | RNG-reproducibility note; ties to value-based oracles |
| 18 | Bayesian Olympics | Activity | in-class worked example |

---

## Through-lines to preserve across decks
1. **Uniqueness → uncertainty → approximation.** M1 "unique solution / full column rank" → M3 negative-definite Hessian → M3 Fisher info $\mathcal{I}=\tfrac{1}{\sigma^2}\mathbf{X}^\top\mathbf{X}$ → M5 Laplace covariance = inverse observed Fisher info. Same object, four modules apart.
2. **Conjugacy bridge (keystone).** M4 closes on the closed-form conjugate Gaussian posterior; P2 / M5 opens by binarizing the outcome to break conjugacy, forcing approximate inference.
3. **One dataset.** Every data figure regenerates from NHANES via the `info521` loader — slides, activities, homeworks, and projects all show the same blood-pressure problem.

## Compression budget
Clay's arc is a full ~16-week course (26 lectures); the redesign is 7.5 weeks. Most compression lands on the front half (L01–18, through Bayesian): keep each spine, push derivations/proofs to appendix decks or reading.
