---
title: "Principal Component Analysis & Course Synthesis"
module: "Module 7"
source_script: scripts/m7-pca/m7a-pca.script.md
reading_time_min: 7
---

# Module 7 — PCA & Course Synthesis

The last module asks the other unsupervised question: not which *groups* the patients form, but which *directions* among the features actually matter. It ends by resolving all seven modules into one arc.

## PCA from scratch

Six NHANES features are not six independent pieces of information — BMI and waist track each other at $r\approx 0.90$. PCA finds new axes (**principal components**) that are uncorrelated and ordered by how much variance each carries. The recipe: **center** each feature (else the first component points at the mean), **standardize** (variance is unit-squared — Module 6's scaling lesson again), form the sample covariance $\mathbf{C} = \tfrac{1}{N-1}\mathbf{X}^{\top}\mathbf{X}$, and take its **eigendecomposition**. Eigenvectors are the new axes; eigenvalues are the variance each carries.

## Two views, one solution

PCA solves two problems that turn out identical. **Maximum variance**: the unit direction with the most projected spread is the top eigenvector. **Minimum reconstruction error**: projecting onto $K$ directions and rebuilding with least squared error picks the same top-$K$ eigenvectors. They coincide because variance kept + reconstruction error = total variance (fixed), so maximizing one minimizes the other. And that reconstruction picture is least squares — Module 1's projection geometry, now in feature space. **Least squares closes the course as it opened it.**

On the (BMI, waist) plane, one direction carries ≈ 95% of the spread. On all six features the scree plot reads 37.3 / 21.8 / 17.2 / 12.5 / 9.7 / **1.3%** — no cliff after PC1 (clinical features are genuinely multi-dimensional), but a near-zero floor at PC6 announcing the known redundancy. The loadings are interpretable: **PC1** is an adiposity/metabolic axis (BMI + waist + HbA1c, HDL opposing), **PC2** an age–cholesterol axis.

## Choosing K and honest limits

Choose the number of components by the **scree elbow**, a **variance threshold** ("keep 90%" → $K=5$ here), or — if the scores feed a supervised model — by **cross-validation** on that model (Module 2 closing the loop). But: PCA is **linear** (blind to curved structure); **scale-dependent** (standardize or units choose the components); interpretability is a gift, not a guarantee; and most importantly, **variance is not usefulness** — PCA never saw the label, so the direction that predicts hypertension may hide in a low-variance component you were about to discard. It is Module 6's cluster-versus-label caution, transposed to axes.

The PCA explorer (systolic vs diastolic BP) lets you rotate a candidate axis and watch variance-captured rise while reconstruction-error falls, both hitting their best at the same angle — the two views as one solution — with **Snap to PC1** to confirm.

## The course in one arc

One dataset, five ways of seeing, each module's answer becoming the next one's question:

| Move | Object |
|---|---|
| **Loss** (M1–M2) | $\hat{\mathbf{w}} = (\mathbf{X}^{\top}\mathbf{X})^{-1}\mathbf{X}^{\top}\mathbf{y}$; flexibility controlled |
| **Likelihood** (M3) | same $\hat{\mathbf{w}}$ + $\hat\sigma^2$ + $\mathrm{Cov}[\hat{\mathbf{w}}]$ |
| **Posterior** (M4) | $\mathcal{N}(\mathbf{m}_N,\mathbf{S}_N)$ — Project 1's endpoint |
| **Approximation** (M5) | Laplace $\mathbf{A}^{-1}$; Metropolis draws |
| **Discovery** (M6–M7) | clusters; principal axes — described, not diagnosed |

And one object followed the whole way: $\mathbf{X}^{\top}\mathbf{X}$ — the loss bowl (M1), the likelihood curvature and Fisher information (M3), the posterior precision (M4), and the covariance whose eigenvectors PCA reads (M7). Same matrix, the whole course through.

## What to remember

- PCA = eigendecomposition of the (standardized) covariance; eigenvalues are variance explained.
- Maximum variance and minimum reconstruction error are the same solution (least squares in feature space).
- Choose $K$ by elbow, threshold, or downstream CV — and remember variance ≠ usefulness.
- The whole course is one dataset seen five ways, around the recurring matrix $\mathbf{X}^{\top}\mathbf{X}$.
