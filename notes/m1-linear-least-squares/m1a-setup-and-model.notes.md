---
title: "Setup, Data & the Linear Model"
module: "Module 1 · Lecture A"
source_script: scripts/m1-linear-least-squares/m1a-setup-and-model.script.md
reading_time_min: 6
---

# Module 1 · Lecture A — Setup, Data & the Linear Model

This lecture lays the ground floor for the whole course: it frames the regression problem, introduces the one dataset used all term, and assembles the two ingredients least squares is built from — a **model** and a **loss**. Solving for the best fit is deferred to Lecture B.

## The course spine

The term studies a single clinical outcome — **systolic blood pressure (SBP)** — through four lenses: least squares (Module 1), maximum likelihood (Module 3), the Bayesian posterior (Module 4), and unsupervised discovery (Modules 6–7). Because the data never changes, differences you see across modules are differences in *method*, not in problem. You build intuition on one clinical question.

## Regression, notation, and the data

Machine learning splits into supervised (learning from labelled pairs), unsupervised (structure with no labels), and reinforcement (learning from reward). **Regression is supervised learning with a continuous target**: given pairs $(\mathbf{x}_n, y_n)$, learn $f$ so that $\hat y = f(\mathbf{x}) \approx y$ on unseen patients.

One patient is a feature vector $\mathbf{x}_n$; stacking all patients as rows gives the **design matrix** $\mathbf{X}$ (with $N$ rows and $D$ columns), and their targets stack into the vector $\mathbf{y}$. Note the convention: targets are written $y$ (where Bishop's textbook uses $t$).

The data is **NHANES 2021–22**: about 5,102 U.S. adults, target SBP in mmHg, with six leakage-safe features — `age` (the Project-1 primary predictor), `bmi`, `waist`, `chol`, `hdl`, and `hba1c`. Diastolic blood pressure is deliberately excluded.

## The leakage rule

Diastolic BP is held out because of the **leakage rule**: exclude any predictor that is itself a blood-pressure measurement, or that would trivially determine the label. This is a modelling choice made *by design, before fitting* — not something the algorithm discovers. The same discipline returns in Module 2 (cross-validation) and in Project 2's cluster-versus-label reveal.

## Model and loss

The linear model predicts the target as a weighted sum of features, $\hat y = \mathbf{w}^{\top}\mathbf{x}$, with the intercept absorbed as a constant-1 feature. Fit is scored by the **mean squared error**,

$$\mathcal{L}(\mathbf{w}) = \tfrac{1}{N}\lVert \mathbf{y} - \mathbf{X}\mathbf{w}\rVert_2^2 .$$

Squared error is chosen because it is smooth (differentiable — which lets Lecture B set a gradient to zero) and because it penalises large misses disproportionately. A quiet foreshadow: a squared loss is exactly what a Gaussian-noise model implies — the tie made explicit in Module 3.

On NHANES, the scalar fit of SBP on standardized age gives an intercept near 121.5 mmHg (predicted BP at average age) and a slope near 6.5 mmHg per standard deviation of age — about 0.38 mmHg per year. Always translate a weight back into clinical units before trusting it.

## The demo

The least-squares explorer lets you drag a fit line (or move intercept/slope sliders) and watch the residuals and the loss respond; **Show least-squares solution** reveals the optimum, and **Add outlier** drops in a young, high-BP patient so you can watch the least-squares line swing toward it — a direct look at squared error's sensitivity to outliers.

## What to remember

- Regression = supervised learning with a continuous target; $\mathbf{X}$ is patients-by-features, $\mathbf{y}$ their targets.
- The linear model $\hat y = \mathbf{w}^{\top}\mathbf{x}$ plus the MSE loss are the two pieces least squares needs.
- Leakage is decided before fitting; the answer must never sneak into the inputs.
- Squared error is smooth and outlier-sensitive, and secretly assumes Gaussian noise (Module 3).

## Through-lines

The matrix $\mathbf{X}^{\top}\mathbf{X}$ that dominates the loss here is the object that recurs all term (Modules 3–7). The single NHANES problem and the leakage discipline both persist throughout.
