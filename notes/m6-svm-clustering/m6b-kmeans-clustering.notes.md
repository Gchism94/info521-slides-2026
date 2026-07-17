---
title: "k-means & the Unsupervised Turn"
module: "Module 6 · Lecture B"
source_script: scripts/m6-svm-clustering/m6b-kmeans-clustering.script.md
reading_time_min: 7
---

# Module 6 · Lecture B — k-means & the Unsupervised Turn

For five and a half modules the label $y$ was the star. Here we delete it and ask a different question: with only the features, do the patients form groups? Without labels there is no test-set truth — evaluation becomes internal fit plus judgment about meaning.

## k-means

Pick $K$ **centroids** and an assignment of each patient to one, minimizing the **distortion** (a squared-error loss again),

$$\mathcal{L} = \sum_{n} \lVert \mathbf{x}_n - \boldsymbol{\mu}_{z_n}\rVert^2 .$$

It splits into two steps, each trivial given the other: **assign** each patient to its nearest centroid, then **update** each centroid to the mean of its members (the squared-error-minimizing point — Module 1 again). Alternating lowers $\mathcal{L}$ every step, so it **converges** — though not necessarily to the best answer.

On the standardized (BMI, waist) plane — two features correlated at $r\approx 0.90$, essentially one continuum — $K=3$ slices the cloud into adiposity bands. The clusters exist because three were requested, not because nature drew three. k-means always returns $K$ clusters whether or not they are real.

## Three failure modes

**Scaling.** k-means runs on Euclidean distance, so feature scales *are* the model; raw units let waist drown out HbA1c. Standardize first (Module 1's move, now load-bearing); the Module 2 leakage discipline applies too.

**Local optima.** With $K=4$ and only the initialization varying, 20 runs land on visibly different distortions. The fix is dumb but essential: many random restarts, keep the lowest distortion (smarter seeding like k-means++ also helps).

**Choosing $K$.** Distortion always falls with $K$ (zero at $K=N$) — the Module 2 training-error trap in new clothes. Look for the **elbow**, and accept that real data often gives a soft one; $K$ is a modelling choice you own and defend.

The **Gaussian mixture model** is the soft upgrade, fit by **EM** — the same assign/update dance, where responsibilities (posteriors, Module 4) replace hard assignments and the M-step is weighted MLE (Module 3). k-means is the shrunk-covariance limit of a GMM.

## Clusters are not diagnoses

Colouring the three adiposity clusters (which never saw blood pressure) by the held-back hypertension label, the rate climbs ≈ 30% → 40% → 48% against 39% overall. Two things hold at once: the **enrichment is real** (and the clusters obeyed the leakage rule), yet **no cluster is remotely pure**. Pretending clusters are labels manufactures diagnoses the data never made — Project 2's honesty requirement in one figure. Descriptive tools describe; they do not diagnose.

The k-means explorer (BMI vs fasting glucose, no labels) lets you set $k$, drag the centroids to seed them, **Step** through assign/update or **Run to convergence**, and use **New centroids** to escape a bad local optimum.

## What to remember

- Distortion = squared error; assign/update converges to *a* local optimum — restart and keep the best.
- Standardize (distances have units); $K$ is a defended choice, not a data verdict.
- GMM/EM is the soft version; responsibilities are posteriors, the M-step is weighted MLE.
- Clusters enrich risk without being pure — never treat them as labels.

## Through-lines

Squared error, standardization, the training-error trap, Bayes' rule, and MLE all reappear inside the unsupervised loop. Module 7 asks the other unsupervised question — which *directions* matter — and closes the course.
