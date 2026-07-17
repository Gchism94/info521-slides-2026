---
deck: "PCA"
subtitle: "INFO 521 · Module 7 — Principal Component Analysis & Course Synthesis"
source_qmd: modules/m7-pca/m7a-pca.qmd
dest: scripts/m7-pca/m7a-pca.script.md
scenes: 13
est_spoken_words: 1605
est_runtime_min: 12.3   # at ~130 wpm
---

## Title slide — PCA

Welcome to Module 7 — Principal Component Analysis, and the synthesis of the whole course. This is the last one. In Lecture B of Module 6 we asked which groups the patients fall into; today we ask the other unsupervised question — which directions among the features actually matter? That's PCA. And because it's the finale, we'll end by stepping back and watching all seven modules resolve into a single arc, around a single matrix that's been following you the entire term. These materials are adapted with permission from lecture materials by Clayton Morrison at the University of Arizona.

## Learning outcomes

Four outcomes. First, compute PCA from scratch — center, covariance, eigendecomposition. Second, state both of its views — maximum variance and minimum reconstruction error — and see that they're the same thing. Third, read variance explained and choose the number of components with a scree plot. And fourth, interpret the components on our NHANES features — and state PCA's limits honestly, because it has real ones.

## The question: which directions matter?

Here's the motivating question. Each patient has six features — but are those six independent pieces of information? We already know they're not. BMI and waist circumference track each other at a correlation around zero-point-nine — that's very nearly one measurement wearing two names, and you saw that redundancy directly in last lecture's clustering plane. So PCA asks: can we find new axes — the principal components — that are uncorrelated with each other, and ordered by how much of the data's variance each one carries? Rotate to those axes, keep just the first few, and you've got a shorter description of every patient that throws away as little as possible.

## Center first, then covariance

Three setup steps, and each one is a callback. First, center every feature by subtracting its mean — because PCA is about spread around the mean, and if you skip this the first component just points at where the mean sits. Second, standardize, since our units are all over the place — years, kilograms per meter squared, centimeters, milligrams per deciliter, percent — and PCA maximizes variance, which is unit-squared; that's Module 6's scaling lesson, verbatim. Third, form the sample covariance matrix — and here it is one final time, the centered X-transpose-X, the object m3b promised would come back. Then find its eigenvectors and eigenvalues. The eigenvectors are the new axes; the eigenvalues are the variance each axis carries, sorted from most to least. That eigendecomposition is the entire algorithm.

## Two views, one solution

Now the beautiful part — PCA solves two problems that look completely different and turn out to be the same. View one, maximum variance: find the unit direction along which the projected data spreads the most. The answer is the top eigenvector. View two, minimum reconstruction: project each patient onto K directions, rebuild them from just those coordinates, and choose the directions that make the squared rebuilding error smallest. The answer is the same top-K eigenvectors. Why are they identical? Because variance kept, plus reconstruction error, equals the total variance — which is fixed — so maximizing the one is exactly minimizing the other. And notice what that reconstruction picture is: projecting onto a subspace and measuring squared error. That's least squares — m1b's projection geometry, the hat matrix, now pointed at feature space. In the accent color: least squares closes the course exactly as it opened it.

## PC1 on the adiposity plane

Let's warm up in two dimensions, where we can actually see it — just BMI and waist, that correlated pair. The cloud is a long, thin cigar lying along its shared diagonal. The vermillion arrow is the leading direction PCA finds, running right down the length of the cigar, and the short green arrow is the leftover direction across it. Nearly all the spread — around ninety-five percent of it in this plane — lives along that one vermillion direction. So one number, a patient's position along that arrow, recaptures almost everything these two features were telling us. That's the redundancy PCA is built to find and collapse. Now let's do it with all six features at once.

## All six features: the scree plot

Here's PCA on all six features, as a scree plot — the bars are how much variance each component carries, and the line is the running cumulative total. The first component captures about thirty-seven percent, the first two together fifty-nine, the first three seventy-six. And look at the last one, component six: a tiny one-point-three percent. That near-zero component is the algebra's way of announcing that one of our six numbers is almost redundant — and we already know which pair is responsible. Notice, though, there's no dramatic cliff after the first component. That's honest, and worth saying: clinical features really are multi-dimensional; the strong finding here isn't one dominant axis, it's the floor at the very end.

## What do the components mean?

And unlike a lot of PCA, ours is interpretable — here are the loadings, how each feature contributes to the first two components. The first component loads strongly and positively on BMI and waist, moderately on HbA1c, our blood-sugar marker, with HDL cholesterol pushing the opposite way. Read clinically, that's an adiposity-and-metabolic-risk axis — bigger body size, higher blood sugar, lower good cholesterol, all moving together. The second component is a different story: it's dominated by age and the cholesterol measures, largely separate from adiposity — call it an age-and-cholesterol axis. So the machine found two clinically sensible dimensions of patient variation, on its own, with no labels. That interpretability is a genuine gift — and one we'll caveat in just a moment.

## Choosing K, and what "explained" buys

How many components should you keep? Three legitimate answers. One: the scree elbow — the same judgment call as choosing K in clustering; here the gains flatten after about the third component, so two or three describe these patients reasonably. Two: a variance threshold — "keep ninety percent," which here lands you at five components. Three, and the most principled if the components feed a downstream model: choose K by cross-validation on that model — and there Module 2 closes the loop, unsupervised output handed back to supervised discipline. But one warning, in the accent color, that sets up the next slide: compression is a tool, not a truth. Every bit of "variance explained" was measured on the features alone. No label ever got a vote.

## Limitations — said plainly

So let me be blunt about what PCA can't do. It's linear — the components are straight axes, so if your real structure is curved, a spiral or a ring, PCA is blind to it. It's scale-dependent — standardize, or your units silently choose your components. Interpretability is a gift, not a guarantee — ours happened to read cleanly, but rotated blends of features often mean nothing at all. And the big one, the one to carry straight into Project 2: variance is not the same as usefulness. PCA never saw the label, so the direction that actually predicts hypertension could be hiding in a low-variance component you were about to throw away. A PCA that proudly explains ninety percent of the variance can still discard the diagnostic ten. It's the cluster-versus-label caution from last lecture, transposed from groups to axes.

## Live demo: the PCA explorer

Let's feel the two-views equivalence with our own hands. This tool plots a correlated pair — systolic against diastolic blood pressure, centered at the mean — and hands you one control: a slider that rotates a candidate axis around, the angle theta. As you rotate it, watch two readouts move in lockstep, in opposite directions: "variance captured" climbs while "reconstruction error" falls, and they hit their best values at exactly the same angle. That's view one and view two turning out to be the same solution, live, right in front of you. Rotate to find that sweet spot by eye, then hit "Snap to PC1" to jump precisely to it and confirm you were close. "Show both components" draws in the second axis, perpendicular to the first, so you can see the full rotated frame. "Reset" starts over. Play with it until the trade-off feels obvious — capture the most spread, and you've automatically lost the least in reconstruction.

> [cue: interact directly on the full-bleed slide — drag the Axis angle θ slider (variance captured up, reconstruction error down, together) → Snap to PC1 → Show both components → Reset; the adiposity-plane snapshot on the next slide is the PDF fallback if the embed can't load]

## Explorer — static fallback

For print or PDF, or if the embed doesn't load, this snapshot stands in — the leading principal direction drawn on the adiposity plane. Live in class, we drive the rotating-axis tool itself on the slide before; there's nothing new to learn here.

> [cue: optional — skip aloud if the live embed worked; this slide exists only for print and PDF]

## The course, in one arc

And that brings us to the end — so let's step all the way back and see the whole course at once. One dataset, five ways of seeing it, and each module's answer became the next module's question. We started with loss, in Modules 1 and 2: minimize squared error, control the flexibility, and out came w-hat equals X-transpose-X inverse, X-transpose y. Then likelihood, Module 3: model the noise, maximize the log-likelihood — and the same w-hat fell out, now with a noise estimate and a covariance. Then posterior, Module 4: don't just estimate, believe and update — the conjugate Gaussian, Project 1's endpoint. Then approximation, Module 5: when conjugacy broke, we stopped solving exactly and started approximating — Laplace, and Metropolis. And finally discovery, Modules 6 and 7: we dropped the labels and asked what structure the features hold on their own — clusters, and principal axes; described, never diagnosed. And in the accent color, the thing I most want you to carry out the door: one object followed you the entire way. X-transpose-X. It was the loss bowl in Module 1, the likelihood curvature and Fisher information in Module 3, the posterior precision in Module 4, and the covariance whose eigenvectors we just read in Module 7. Same matrix, the whole course through. That — that's the course. Thank you.
