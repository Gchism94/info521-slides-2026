---
title: "Breaking Conjugacy: Logistic Regression & Newton's Method"
module: "Module 5 · Lecture A"
source_script: scripts/m5-approximate-inference/m5a-logistic-newton.script.md
reading_time_min: 7
---

# Module 5 · Lecture A — Breaking Conjugacy

Module 4 ended with everything Gaussian and every formula closed-form. Asking the clinical question — *is this patient hypertensive?* — binarizes the outcome and breaks that machinery. This is the second act of the course, and where Project 2 opens.

## The conjugacy break

The target is now a **Bernoulli** outcome, not a Gaussian one. A Gaussian prior on $\mathbf{w}$ meeting a Bernoulli likelihood has **no conjugate pair** — the closed-form posterior of Module 4 is gone. Same data (≈ 39% prevalence), new target type, and the algebra that made Bayes easy is structurally unavailable.

## Logistic regression

Keep the linear score and squash it into a probability with the **sigmoid**,

$$p(y=1\mid\mathbf{x},\mathbf{w}) = \sigma(\mathbf{w}^{\top}\mathbf{x}),
\qquad \sigma(a) = \tfrac{1}{1+e^{-a}}.$$

It is still linear in $\mathbf{w}$ (basis functions still apply) and **discriminative** (it models $p(y\mid\mathbf{x})$ directly); the decision boundary $\mathbf{w}^{\top}\mathbf{x}=0$ is still a line. The log-likelihood is the cross-entropy, and setting its gradient to zero gives $\mathbf{X}^{\top}(\mathbf{y}-\boldsymbol{\mu})=\mathbf{0}$ — which *looks* like the normal equations, but $\boldsymbol{\mu}$ hides $\mathbf{w}$ inside the sigmoid. There is **no closed form**: the equation is transcendental, not merely harder. So we iterate.

## Newton–Raphson

Newton repeatedly jumps to the peak of the local quadratic, using both the gradient (which way is up) and the **Hessian** (how the slope curves): $\mathbf{H} = -\mathbf{X}^{\top}\mathbf{R}\mathbf{X}$ with $\mathbf{R} = \mathrm{diag}(\mu_n(1-\mu_n))$. It is negative definite, so the log-likelihood is concave and the peak Newton finds is *the* peak — Module 3's uniqueness argument, with $\mathbf{X}^{\top}\mathbf{X}$ reweighted into $\mathbf{X}^{\top}\mathbf{R}\mathbf{X}$. The fence-sitters near $\mu=\tfrac12$ carry the most weight — they locate the boundary. On all of NHANES it converges in about five steps to $\hat{\mathbf{w}}\approx(-0.49,\,0.52)$: each SD of age multiplies the odds of hypertension by $e^{0.52}\approx 1.7$, and the fitted probability crosses $\tfrac12$ near age 66.

The logistic explorer (framed as tumor size, benign vs malignant — the same model) lets you set the bias and steepness by eye and watch the log loss and accuracy respond, then **Show MLE fit** snaps to the maximum-likelihood solution and **Generative comparison** shows a per-class Gaussian model reaching essentially the same boundary.

## What survived, and what did not

The frequentist story is intact: $\hat{\mathbf{w}}$ by Newton, uniqueness from concavity, even Module-3-style uncertainty from the curvature at the peak. The Bayesian story took the hit: the posterior is known only up to its normalizer (the evidence integral has no closed form), so exact credible intervals and honest predictive probabilities are out of reach. **Optimization survived binarization; integration did not.**

## What to remember

- Binarizing gives a Bernoulli likelihood; with a Gaussian prior there is no conjugate posterior.
- Logistic regression: $p(y=1\mid\mathbf{x})=\sigma(\mathbf{w}^{\top}\mathbf{x})$, concave $\ell$, gradient $\mathbf{X}^{\top}(\mathbf{y}-\boldsymbol{\mu})$.
- Newton uses curvature ($\mathbf{H}=-\mathbf{X}^{\top}\mathbf{R}\mathbf{X}$) and converges in ~5 steps.
- Finding the peak is easy; knowing the mass around it is the hard part (Lecture B).

## Through-lines

$\mathbf{X}^{\top}\mathbf{X}$ becomes $\mathbf{X}^{\top}\mathbf{R}\mathbf{X}$, and the Hessian at the peak is about to become the covariance of a Gaussian approximation to the posterior — Lecture B reuses it directly.
