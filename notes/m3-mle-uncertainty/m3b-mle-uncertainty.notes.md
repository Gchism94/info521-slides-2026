---
title: "Properties of the MLE: Uncertainty in Parameters"
module: "Module 3 · Lecture B"
source_script: scripts/m3-mle-uncertainty/m3b-mle-uncertainty.script.md
reading_time_min: 7
---

# Module 3 · Lecture B — Properties of the MLE

Lecture A produced $\hat{\mathbf{w}}$. This lecture puts it on trial with three questions: is it unique, is it unbiased, and how uncertain is it?

## Uniqueness

The gradient of the log-likelihood vanishes at the normal equations, and its second derivative — the **Hessian** — comes out constant, $\mathbf{H} = -\tfrac{1}{\sigma^2}\mathbf{X}^{\top}\mathbf{X}$. This is **negative definite**, so the log-likelihood is strictly concave: one hump, no ridges, a single global maximum. It is the Module 1 uniqueness argument again — the same full-column-rank $\mathbf{X}^{\top}\mathbf{X}$, now wearing the name "negative-definite Hessian."

## The generative picture and unbiasedness

Uncertainty is defined by imagining **repeated datasets**: run the generating process again and again, fit each one, and the estimates scatter into a cloud. The spread of that cloud is the covariance of $\hat{\mathbf{w}}$.

Taking the expectation of $\hat{\mathbf{w}}$ over that process — with $\mathbf{X}$ fixed and $\mathbb{E}[\mathbf{y}] = \mathbf{X}\mathbf{w}$ — the inverse cancels its own matrix and leaves $\mathbb{E}[\hat{\mathbf{w}}] = \mathbf{w}$: the estimator is **unbiased**. Be careful what that means. It is a statement about the *center* of the cloud across many size-$N$ samples. It is *not* the claim that more data helps (a separate sample-size effect), *not* the stronger minimum-variance (UMVU) property, and *not* a promise that $\hat{\mathbf{w}}$ is best for your one dataset.

## Covariance and Fisher information

The spread of the cloud has a closed form,

$$\mathrm{Cov}[\hat{\mathbf{w}}] = \sigma^2 (\mathbf{X}^{\top}\mathbf{X})^{-1}.$$

Read it for intuition: low noise (small $\sigma^2$) and abundant, well-spread data (large $\mathbf{X}^{\top}\mathbf{X}$) both sharpen the estimate. The full derivation is in the [covariance appendix](../../modules/m3-mle-uncertainty/appendix-covariance.qmd).

The same quantity has a deeper name. The **Fisher information** is the expected curvature of the log-likelihood, $\mathcal{I} = \tfrac{1}{\sigma^2}\mathbf{X}^{\top}\mathbf{X}$, so $\mathrm{Cov}[\hat{\mathbf{w}}] = \mathcal{I}^{-1}$. Curvature and uncertainty are inverses: a sharply curved peak pins the parameters tightly; a flat one leaves them loose. On NHANES, a covariance ellipse from 40 patients is wide and fuzzy while the full-sample ellipse collapses to a tight blob — the payoff of data, drawn.

## The demo

The parameter-uncertainty explorer lets you **Draw one dataset** (a single $\hat{\mathbf{w}}$ dot), **Draw 100** (the cloud floods the theoretical $2\sigma$ ellipse, centred on the true $\mathbf{w}$ — unbiasedness made visible), and nudge the noise or sample-size sliders to watch the ellipse grow or shrink.

## What to remember

- The MLE is unique (concave $\ell$, negative-definite Hessian), unbiased ($\mathbb{E}[\hat{\mathbf{w}}]=\mathbf{w}$), and quantifiably uncertain.
- $\mathrm{Cov}[\hat{\mathbf{w}}] = \sigma^2(\mathbf{X}^{\top}\mathbf{X})^{-1} = \mathcal{I}^{-1}$ — the inverse Fisher information.
- Unbiasedness is about the center of the estimate-cloud, not any single fit.
- The closed-book checkpoint gates on reproducing the uniqueness and unbiasedness arguments.

## Through-lines

One matrix does three jobs across modules: the negative-definite Hessian (uniqueness) is, in expectation, the Fisher information, whose inverse becomes the **Laplace posterior covariance** in Module 5. Keep your eye on $\mathbf{X}^{\top}\mathbf{X}$.
