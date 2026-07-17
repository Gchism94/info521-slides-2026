---
title: "Bias–Variance & Regularization"
module: "Module 2 · Lecture B"
source_script: scripts/m2-generalization/m2b-bias-variance-ridge.script.md
reading_time_min: 7
---

# Module 2 · Lecture B — Bias–Variance & Regularization

Lecture A found the U-curve empirically. This lecture explains why it exists (the bias–variance decomposition) and gives a knob to move along it (ridge regression).

## Bias and variance

Imagine refitting on many datasets drawn the same way. **Bias** is the systematic miss: a too-simple model is wrong in the same direction on average. **Variance** is the sensitivity: a too-flexible model swings wildly from dataset to dataset, chasing each one's noise. In the repeated-fits picture, a degree-1 model has fits that huddle tightly but miss the truth (high bias, low variance), while a degree-9 model tracks the truth on average but its individual fits fan out wildly (low bias, high variance).

For a fixed input, expected test error splits into three pieces,

$$\mathbb{E}\bigl[(y - \hat f(\mathbf{x}))^2\bigr] = \text{bias}^2 + \text{variance} + \sigma^2,$$

where $\sigma^2$ is irreducible noise no model can beat. As complexity rises, bias$^2$ falls and variance rises; their sum is the U-curve, resting on the $\sigma^2$ floor. The best model balances the two — it is not the most flexible one. The full derivation is in the [bias–variance appendix](../../modules/m2-generalization/appendix-bias-variance.qmd).

## Ridge regression

Ridge adds a penalty on weight size to the loss,

$$\mathcal{L}_{\text{ridge}}(\mathbf{w}) = \lVert \mathbf{y} - \mathbf{X}\mathbf{w}\rVert^2 + \lambda\lVert\mathbf{w}\rVert^2,$$

which discourages the large coefficients that drive wiggly overfit curves. It has a closed form that just adds $\lambda\mathbf{I}$ inside the normal equations:

$$\hat{\mathbf{w}}_{\text{ridge}} = (\mathbf{X}^{\top}\mathbf{X} + \lambda\mathbf{I})^{-1}\mathbf{X}^{\top}\mathbf{y}.$$

That added term lifts every eigenvalue by $\lambda>0$, making the matrix positive definite and **always invertible** — even with more features than patients, or collinear columns. Ridge hands you, for free, the unique solution Module 1 had to assume.

As $\lambda$ grows, every coefficient shrinks smoothly toward zero (the coefficient path). The two limits are degenerate: $\lambda\to 0$ recovers ordinary least squares (the overfit right end of the U), and $\lambda\to\infty$ crushes the weights to a constant fit (the underfit left end). The useful $\lambda$ lives in between and is **tuned by cross-validation**, exactly as in Lecture A but with $\lambda$ as the knob.

## The demo

The bias–variance / ridge explorer lets you raise the polynomial degree and watch train and test MSE diverge, toggle **Show 20 fits** to see the variance fan widen at high degree, and slide $\lambda$ up to pull the fan back in as variance drops and a little bias creeps in.

## What to remember

- Test error $=$ bias$^2$ $+$ variance $+ \sigma^2$; the U is the sum of the first two.
- Ridge trades a little bias for less variance and is always invertible — uniqueness for free.
- $\lambda\to 0$ is OLS; $\lambda\to\infty$ is a constant; CV picks the middle.

## Through-lines

Ridge's $\mathbf{X}^{\top}\mathbf{X}+\lambda\mathbf{I}$ is the Module 1 uniqueness condition, guaranteed. And the ridge penalty is secretly a **Gaussian prior** on the weights — ridge is MAP estimation, a fact Module 4 makes exact ($\lambda = \sigma^2/\tau^2$).
