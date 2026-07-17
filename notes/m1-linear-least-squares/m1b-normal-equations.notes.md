---
title: "Normal Equations & Geometry"
module: "Module 1 · Lecture B"
source_script: scripts/m1-linear-least-squares/m1b-normal-equations.script.md
reading_time_min: 7
---

# Module 1 · Lecture B — Normal Equations & Geometry

Lecture A left the best weights unfound. This lecture solves for them in closed form, shows the geometry underneath the algebra, and ends on the condition that makes the answer unique.

## From loss to normal equations

The MSE loss is a smooth, convex bowl in $\mathbf{w}$: one bottom, no other dips, so the minimum sits wherever the gradient vanishes. In one dimension, setting the two partial derivatives to zero puts the line through the means and gives the slope as covariance-over-variance — exactly the line fit in Lecture A.

Scaling to all $D$ features, the gradient of the matrix form is

$$\nabla_{\mathbf{w}}\mathcal{L} = -\tfrac{2}{N}\,\mathbf{X}^{\top}(\mathbf{y} - \mathbf{X}\mathbf{w}),$$

and setting it to zero drops the constant and leaves the **normal equations**,

$$\mathbf{X}^{\top}\mathbf{X}\,\hat{\mathbf{w}} = \mathbf{X}^{\top}\mathbf{y}
\qquad\Longrightarrow\qquad
\hat{\mathbf{w}} = (\mathbf{X}^{\top}\mathbf{X})^{-1}\mathbf{X}^{\top}\mathbf{y}.$$

One expression gives the global optimum in a single shot — no iteration. In practice you *solve* the linear system rather than form the inverse (better conditioned, less work). The full vector-calculus behind the gradient is in the [matrix-calculus appendix](../../modules/m1-linear-least-squares/appendix-matrix-calculus.qmd); reproducing the $\nabla\mathcal{L}=0 \Rightarrow \hat{\mathbf{w}}$ step is the Project-1 checkpoint.

On NHANES with all six features, a predicted-vs-actual plot tilts along the identity line but scatters widely — an honest verdict: useful, not the whole story. How good is good enough is Module 2.

## The geometry: least squares is a projection

Picture a space with one axis per patient. The target $\mathbf{y}$ is a point; every possible prediction $\mathbf{X}\mathbf{w}$ lives in the **column space** of $\mathbf{X}$. Least squares drops $\mathbf{y}$ straight onto that subspace: the prediction $\hat{\mathbf{y}}$ is the closest point in it, and the residual is perpendicular to the subspace. In matrix form $\hat{\mathbf{y}} = \mathbf{P}\mathbf{y}$ with the **hat matrix** $\mathbf{P} = \mathbf{X}(\mathbf{X}^{\top}\mathbf{X})^{-1}\mathbf{X}^{\top}$ — symmetric and idempotent.

The algebra and the geometry are one statement: "residual perpendicular to every feature column" is $\mathbf{X}^{\top}\mathbf{r} = \mathbf{0}$, which rearranges straight back into the normal equations.

## Basis functions and uniqueness

Replacing raw inputs with functions of them, $\boldsymbol{\phi}(\mathbf{x})$, keeps the model **linear in the weights** — so the same solution applies with $\mathbf{X}$ swapped for the feature matrix $\boldsymbol{\Phi}$. "Linear model" means linear in $\mathbf{w}$, not in $x$; you can fit curves. But more flexibility means more room to overfit (a degree-9 polynomial chases individual points), which is exactly Module 2's subject.

The solution is **unique** iff $\mathbf{X}^{\top}\mathbf{X}$ is invertible, iff $\mathbf{X}$ has full column rank: no feature is a combination of the others (no collinearity), and there are at least as many patients as features. Otherwise infinitely many weight vectors tie.

## What to remember

- $\hat{\mathbf{w}} = (\mathbf{X}^{\top}\mathbf{X})^{-1}\mathbf{X}^{\top}\mathbf{y}$, from $\nabla\mathcal{L}=0$; solve the system, don't invert.
- Least squares = orthogonal projection of $\mathbf{y}$ onto $\mathrm{col}(\mathbf{X})$; the residual is orthogonal to every feature.
- Basis functions buy curves while staying linear in the weights — at the cost of overfitting risk.
- Uniqueness needs full column rank (invertible $\mathbf{X}^{\top}\mathbf{X}$).

## Through-lines

The uniqueness condition here — $\mathbf{X}^{\top}\mathbf{X}$ invertible — returns in Module 3 as a *negative-definite Hessian*: uniqueness becomes curvature. The overfitting hook opens Module 2.
