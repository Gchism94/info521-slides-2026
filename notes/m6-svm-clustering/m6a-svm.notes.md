---
title: "Maximum-Margin Classification"
module: "Module 6 · Lecture A"
source_script: scripts/m6-svm-clustering/m6a-svm.script.md
reading_time_min: 6
---

# Module 6 · Lecture A — Maximum-Margin Classification

If the boundary between two classes is all you want, why model probabilities at all? The support vector machine chooses the boundary directly, by a geometric criterion — the third way of thinking about a classifier, alongside logistic (model the probability) and Bayesian (model belief over $\mathbf{w}$).

## The maximum margin

When classes are separable, many hyperplanes split them; prefer the one farthest from both, leaving the widest empty corridor. The corridor width is the **margin** $2/\lVert\mathbf{w}\rVert$, so maximizing it minimizes $\lVert\mathbf{w}\rVert^2$ — a norm penalty as the *objective* itself (ridge's cousin). Only the points on the corridor's edge constrain the answer: the **support vectors**. Delete any other point and the boundary does not move; nudge a support vector and it tilts. That sparsity is the opposite of least squares, where every point pulls.

## Hinge loss and kernels

Real data is not separable — NHANES ages overlap across hypertension status. The **soft-margin** SVM lets points violate the margin at a price given by the **hinge loss**: comfortably-correct points pay exactly zero, violators pay linearly. Added to the norm penalty, this is the ridge template (loss + penalty), with $\lambda$ tuned by cross-validation.

Comparing losses against the classification margin: the **hinge** drops to exactly zero past the margin (giving sparsity, but no probabilities), while the **logistic** loss decays smoothly and never reaches zero (giving calibrated probabilities, but no sparsity). Both are convex surrogates for the un-optimizable 0–1 loss.

**Kernels** handle curved boundaries. Max-margin training touches inputs only through inner products, so you supply a kernel $k(\mathbf{x},\mathbf{x}') = \boldsymbol{\phi}(\mathbf{x})^{\top}\boldsymbol{\phi}(\mathbf{x}')$ directly and never build the (possibly infinite-dimensional) feature map — Module 1's basis functions, industrialized.

## Honest evaluation

At ≈ 39% prevalence, a model that predicts "nobody hypertensive" scores 61% accuracy while catching zero cases — **accuracy is a rigged scoreboard**. Read the confusion matrix instead: **sensitivity/recall** (of the hypertensive, how many were caught — the costly false-negative cell) and **precision** (of the alarms, how many were real). Margin methods output a score, and where you cut it trades sensitivity against precision — a *clinical* decision about which error is worse, not a mathematical one.

## What to remember

- Max-margin picks the widest corridor, held up only by support vectors (sparse).
- Hinge vs logistic: geometry/sparsity vs probabilities/calibration; both surrogate the 0–1 loss.
- Kernels give nonlinear boundaries using only inner products.
- At skewed prevalence, report sensitivity and precision, not accuracy.

## Through-lines

The $\lVert\mathbf{w}\rVert^2$ objective echoes ridge (Module 2); the leakage-safe hypertension label is the same one from Module 1. Lecture B makes the course's last pivot: drop the labels and ask what structure the features hold on their own.
