---
deck: "SVM & Clustering"
subtitle: "INFO 521 · Module 6 · Lecture A — Maximum-Margin Classification"
source_qmd: modules/m6-svm-clustering/m6a-svm.qmd
dest: scripts/m6-svm-clustering/m6a-svm.script.md
scenes: 10
est_spoken_words: 1200
est_runtime_min: 9.2   # at ~130 wpm
---

## Title slide — SVM & Clustering

Welcome to Module 6 — SVM and Clustering, Lecture A: maximum-margin classification. This is the third act. We've fit probabilities and we've carried uncertainty; today we try something more direct. If all you actually want is the boundary between two classes, why bother modeling probabilities at all? Just draw the best line. That's the support vector machine, and it introduces a genuinely different way to think about what a classifier optimizes. These materials are adapted with permission from lecture materials by Clayton Morrison at the University of Arizona.

## Learning outcomes

Four outcomes. First, state the maximum-margin idea, and define what a support vector is. Second, compare the hinge loss to the logistic loss from Module 5 — the same family of boundaries, but very different priorities. Third, understand the kernel idea at the concept level — nonlinearity without ever leaving our linear machinery. And fourth, evaluate a classifier honestly, which at thirty-nine percent disease prevalence means looking well past raw accuracy.

## One boundary, three philosophies

Let's frame today against what we've already done. Module 5 modeled the probability of the label and then took its half-contour as the boundary. But notice — that's a lot of machinery if the boundary is all you're really after. So, three philosophies. Logistic: model the probability, and the boundary falls out of it. The Bayesian version: model your belief over the weights, and average the boundaries. And the new one, max-margin: skip the probabilities entirely and choose the boundary directly, by a geometric criterion. In the accent color: it's the same linear score, w-transpose x, we've used since day one — what changes today is what we optimize.

## The maximum-margin idea

Here's the geometric idea, and it's lovely. When two classes are separable, infinitely many lines split them — so which is best? The one that sits farthest from both classes, leaving the widest possible empty corridor down the middle. That corridor width is the margin, and it works out to two over the length of w — so maximizing the margin means minimizing the squared length of w. Stop and notice that: a norm penalty on w, but this time as the whole objective, not a bolted-on regularizer. It's ridge's cousin from Module 2. And here's the striking part — only the points sitting right on the edge of the corridor actually constrain the solution. Those are the support vectors. Every other point could be deleted and the boundary wouldn't move an inch. That's the exact opposite of least squares, where every single point pulls on the fit.

## The margin, drawn

Here it is on illustrative separable data — two clean clouds, one boundary running between them, with the dashed margin edges marking the corridor. The circled points are the support vectors, the two or three points touching those edges. Run the thought experiment with me: grab any uncircled point, delete it, and nothing changes — the boundary doesn't care about it at all. But nudge one of those circled support vectors and the whole boundary tilts to follow. That's the entire idea, right there in the name: the machine is supported by just those few vectors. A handful of critical points hold up the whole decision.

## Real data isn't separable: the hinge loss

Of course, real data is never that tidy. NHANES ages overlap heavily across hypertension status — there's no clean empty corridor to find. So the soft-margin SVM lets points violate the margin, for a price. That price is the hinge loss: a point comfortably on the correct side pays exactly zero, but a point inside the corridor or on the wrong side pays in proportion to how far it's strayed. Add the norm penalty on w, and look at the shape of the objective — it's the ridge template from Module 2 all over again: a loss plus a norm penalty, just with hinge in place of squared error. And the trade-off knob, lambda, balances margin width against violations — tuned by cross-validation, exactly as always. Everything you already know composes; only the loss function is new.

## Hinge vs. logistic: what each loss cares about

And here's that new loss against the old one, plotted against the margin — how correct, and how confidently correct, a prediction is. The black step is the zero-one loss, what we actually care about: wrong or right, full stop. But it's flat and un-optimizable, so both methods use a smooth stand-in. The hinge, in vermillion, drops to exactly zero once a point is confidently correct — past the margin, it completely stops caring. The logistic loss, in blue, decays smoothly but never quite reaches zero — even a confidently-correct point still pays a sliver. That one difference is the whole philosophy. Hinge ignores comfortable points, which buys you sparsity — the support vectors — but no probabilities. Logistic charges every point a little, which gives you no sparsity but calibrated probabilities. Two convex surrogates for the same impossible zero-one goal, with different souls.

## Kernels, at concept level

One more idea, kept deliberately at concept level — kernels. Linear boundaries fail when the truth is curved, and we already have one fix from Module 1: map the inputs to richer features, phi of x, and stay linear in the weights. Here's the beautiful observation: max-margin training only ever touches the inputs through inner products — dot products between pairs of points. So you don't actually need the feature map itself; you only need a function that returns the inner product of two mapped points, and that function is called a kernel. Choose the kernel directly — polynomial, Gaussian, whatever — and you never build the feature space at all, even when it's infinite-dimensional. The boundary becomes a weighted sum of kernels sitting on the support vectors. In the accent color: basis functions from Module 1 walked so that kernels could run — the same move, industrialized.

## Evaluating classifiers at 38.8% prevalence

Now the honesty slide, and it matters directly for your projects. Hypertension prevalence in NHANES is about thirty-nine percent — which means a model that simply declares nobody hypertensive scores sixty-one percent accuracy, while catching precisely zero real cases. Accuracy alone is a rigged scoreboard. So we read the confusion matrix instead. Sensitivity, or recall — of the truly hypertensive patients, how many did we actually catch? That false-negative cell, the missed cases, is the clinically costly one. Precision — of all the patients we flagged, how many were genuinely hypertensive? And here's the clinical part: margin methods output a score, and where you set the cut-off along that score trades sensitivity against precision. That's a decision about which error hurts more for this particular disease — not something the math gets to decide for you.

## Recap & the unsupervised turn

Recapping. Max-margin: pick the widest corridor, held up by support vectors alone. Hinge versus logistic: sparsity and geometry on one side, probabilities and calibration on the other — the same linear score, a different contract. Kernels: because training sees only inner products, you get nonlinear boundaries with linear machinery. And evaluation: at thirty-nine percent prevalence, report sensitivity and precision, never bare accuracy. That closes the supervised arc we opened all the way back in Module 1. In the accent color, Lecture B makes the course's last big pivot: we drop the labels entirely, ask what structure lives in the features alone — and confront what goes wrong when we pretend clusters are diagnoses.
