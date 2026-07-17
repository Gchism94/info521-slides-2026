---
title: "The Conjugate Gaussian Posterior"
module: "Module 4 · Lecture B"
source_script: scripts/m4-bayesian-inference/m4b-gaussian-posterior.script.md
reading_time_min: 7
---

# Module 4 · Lecture B — The Conjugate Gaussian Posterior

This is the keystone of the course. Lecture A put a distribution on a proportion; here the same conjugate move scales up to the **regression weights**, and the whole Project 1 pipeline comes to rest.

## The posterior

Place a Gaussian prior on the weights, $p(\mathbf{w}) = \mathcal{N}(\mathbf{m}_0, \mathbf{S}_0)$, and pair it with the Module 3 linear-Gaussian likelihood (treating $\sigma^2$ as known). A Gaussian prior times a Gaussian likelihood gives a **Gaussian posterior** in closed form:

$$\mathbf{S}_N^{-1} = \mathbf{S}_0^{-1} + \tfrac{1}{\sigma^2}\mathbf{X}^{\top}\mathbf{X},
\qquad
\mathbf{m}_N = \mathbf{S}_N\!\left(\mathbf{S}_0^{-1}\mathbf{m}_0 + \tfrac{1}{\sigma^2}\mathbf{X}^{\top}\mathbf{y}\right).$$

Every ingredient is a callback: $\mathbf{X}^{\top}\mathbf{X}$ (Module 1), $\tfrac{1}{\sigma^2}$ (Module 3), the prior (Lecture A). **Project 1 ends exactly here.**

Read in **precisions** (inverse covariances), the update is addition again — posterior precision = prior precision + data precision — and the data's term $\tfrac{1}{\sigma^2}\mathbf{X}^{\top}\mathbf{X}$ is the **Fisher information** from Module 3 (its fourth appearance). The mean is a precision-weighted blend of prior and data. As $N$ grows the data drowns the prior: $\mathbf{m}_N \to \hat{\mathbf{w}}_{\text{MLE}}$ and $\mathbf{S}_N \to \sigma^2(\mathbf{X}^{\top}\mathbf{X})^{-1}$ — the Module 3 covariance. On NHANES the posterior ellipse contracts from a wide prior to a tight blob on the MLE; it is the Module 3 ellipse *reborn*, but now it is belief given one real dataset rather than spread over imagined ones — same math, opposite epistemics.

## Ridge as MAP, and prediction

Take a zero-mean isotropic prior, $\mathbf{S}_0 = \tau^2\mathbf{I}$, and the posterior mean becomes

$$\mathbf{m}_N = \bigl(\mathbf{X}^{\top}\mathbf{X} + \tfrac{\sigma^2}{\tau^2}\mathbf{I}\bigr)^{-1}\mathbf{X}^{\top}\mathbf{y} = \hat{\mathbf{w}}_{\text{ridge}},
\qquad \lambda = \tfrac{\sigma^2}{\tau^2}.$$

This cashes Module 2's hook: **the ridge penalty is a Gaussian prior**, and $\lambda$ becomes a statement (noisy data or a tight prior both shrink harder). The **MAP** estimate is the posterior's peak (= mean for a Gaussian); it keeps the location but discards the spread $\mathbf{S}_N$. In this Gaussian world MAP and the full posterior look interchangeable — Module 5 breaks that illusion.

Predicting a new patient integrates over the posterior, giving a variance with two parts: $\sigma^2$ (irreducible patient-level noise) plus $\mathbf{x}_*^{\top}\mathbf{S}_N\mathbf{x}_*$ (our ignorance about $\mathbf{w}$, which shrinks with data and grows away from the data's center). Plug-in prediction uses only the first term and is over-confident — most visibly at extreme ages, where the predictive band flares.

## What to remember

- Conjugate Gaussian posterior: precisions add; $\mathbf{S}_N^{-1} = \mathbf{S}_0^{-1} + \tfrac{1}{\sigma^2}\mathbf{X}^{\top}\mathbf{X}$.
- Ridge = MAP under a zero-mean Gaussian prior, $\lambda = \sigma^2/\tau^2$.
- Predictive variance = noise $\sigma^2$ + parameter uncertainty $\mathbf{x}_*^{\top}\mathbf{S}_N\mathbf{x}_*$.
- The marginal likelihood (evidence) scores whole models and is a built-in Occam's razor.

## Through-lines

$\mathbf{X}^{\top}\mathbf{X}$ is now the posterior precision. Every formula here exists because everything is Gaussian — Module 5 binarizes the outcome, conjugacy breaks, and approximation begins.
