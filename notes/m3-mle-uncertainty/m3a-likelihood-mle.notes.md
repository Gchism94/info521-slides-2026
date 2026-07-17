---
title: "Likelihood & Maximum Likelihood"
module: "Module 3 · Lecture A"
source_script: scripts/m3-mle-uncertainty/m3a-likelihood-mle.script.md
reading_time_min: 7
---

# Module 3 · Lecture A — Likelihood & Maximum Likelihood

Module 1 chose squared error because it felt reasonable. This lecture earns it: building a probability model for the data recovers the same fit, now with a real foundation — and that foundation pays back twice, with a noise estimate here and parameter uncertainty in Lecture B.

## The noise model and the likelihood

The **linear-Gaussian noise model** says each observation is the linear signal plus independent Gaussian noise, $y_n = \mathbf{w}^{\top}\mathbf{x}_n + \varepsilon_n$ with $\varepsilon_n \sim \mathcal{N}(0,\sigma^2)$. Read generatively, each $y_n$ is a draw from a Gaussian centred on the line — fix $\mathbf{w}$ and $\sigma^2$ and the model can produce datasets.

Because patients are independent, the probability of the whole dataset is the product of per-patient Gaussians. Viewed as a function of the parameters (with the data fixed), this is the **likelihood** — a *score* on parameter settings, not a distribution over them. Taking logs turns the product into the **log-likelihood** $\ell(\mathbf{w})$; its only $\mathbf{w}$-dependent term is $-\tfrac{1}{2\sigma^2}$ times the sum of squared errors. So **maximizing the log-likelihood over $\mathbf{w}$ is exactly minimizing squared error** — visible before taking a single derivative.

## Least squares, re-earned

Setting the gradient to zero, $\sigma^2$ cancels and the normal equations reappear:

$$\hat{\mathbf{w}}_{\text{MLE}} = (\mathbf{X}^{\top}\mathbf{X})^{-1}\mathbf{X}^{\top}\mathbf{y}.$$

This is the Module 1 answer, letter for letter. What is new is the interpretation: **least squares is maximum likelihood under Gaussian noise** — the fit comes from a model now, not a preference. On NHANES the likelihood surface is a single concave arch peaking at the same slope (≈ 6.5 mmHg per SD of age) that least squares found.

## Two dividends

**Noise gets estimated.** Maximizing over $\sigma$ gives $\hat\sigma^2$ as the average squared residual — about 16 mmHg on standardized age. That is the model's honest give-or-take for a single patient: age explains the population trend, not the individual.

Checking the assumption, the NHANES residuals are roughly Gaussian through the bulk but have a **heavy right tail** — the hypertensive patients. The model is *useful, not true*; binarizing that tail (normal vs high) is exactly what Module 5 and Project 2 do.

**But $\hat\sigma^2$ is biased.** Averaged over datasets it equals $\tfrac{N-D}{N}\sigma^2$ — a little too small, because the fit chases the sample and each fitted parameter eats one degree of freedom. The classic repair divides by $N-D$. The lesson: maximum likelihood does not hand you unbiasedness for free; properties are checked, estimator by estimator. A subsampling experiment on real NHANES data shows $\hat\sigma^2$ climbing toward the truth along the theoretical $\tfrac{N-D}{N}\sigma^2$ curve.

## What to remember

- Likelihood is a score on parameters; maximizing the log-likelihood under Gaussian noise = minimizing MSE.
- $\hat{\mathbf{w}}_{\text{MLE}}$ is the Module 1 least-squares fit, now with a model behind it.
- $\hat\sigma^2$ = mean squared residual, biased low by $\tfrac{N-D}{N}$ (correct with $N-D$).
- "Useful, not true": the Gaussian assumption is checked, and its heavy tail sets up Module 5.

## Through-lines

The curvature of the log-likelihood at its peak — the Hessian, which is $\mathbf{X}^{\top}\mathbf{X}$ again — is Lecture B's whole subject: it becomes the **Fisher information**, and later the Laplace posterior covariance in Module 5.
