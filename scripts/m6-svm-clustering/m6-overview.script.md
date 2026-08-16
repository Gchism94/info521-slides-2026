---
deck: "Module 6: Support Vector Machines and Clustering"
subtitle: "INFO 521 · Module 6 · Overview"
source_qmd: modules/m6-svm-clustering/m6-overview.qmd
dest: scripts/m6-svm-clustering/m6-overview.script.md
generated_from: overviews/module_spec.py + overviews/narration.py
scenes: 6
est_spoken_words: 323
est_runtime_min: 2.5   # at ~130 wpm
---

## Title slide — Module 6: Support Vector Machines and Clustering

Module 6. Two shifts in one module, and the second one is bigger than it looks.

## The question

First question: what if you optimise the decision boundary directly instead of modelling probabilities at all. Second question: what if there are no labels. That second one changes what counts as an answer, because with no labels there is nothing to be right about.

## What the lectures do

Lecture A is maximum-margin classification. You see the same boundary from three philosophies, meet the hinge loss for data that is not separable, and compare what hinge and logistic each actually care about. Kernels get covered at concept level. Lecture B is k-means: the objective, why standardising comes first, why restarts are mandatory, and how to choose K without fooling yourself. Minimising the objective over K does not work, because it keeps dropping until every point is its own cluster, so we read the elbow and stay honest about how soft that reading is.

## Where this sits

Everything before this was supervised and probabilistic. Lecture A keeps the labels and drops the probability. Lecture B keeps neither. Module 7 stays in that unsupervised world and asks about directions rather than groups. If you have spent six weeks thinking of a model as a thing that predicts a label, this is the week to widen that.

## Week 6 at a glance

Checkpoint quiz 2.3 on k-means and PCA, and Milestones 2.1 and 2.2 are due, which is Gate A. There is no new homework unit this week, which is deliberate, because the project is heavy right now.

## Watch out for

Three quick ones. Accuracy is a weak claim at 38.8 percent prevalence, because always predicting the majority class scores 61.2. Distances have units, so k-means on unstandardised features clusters on whichever variable has the biggest numbers. And clusters are not diagnoses. A cluster is a region of feature space, and naming it after a condition is a claim you have not earned. Milestone 2.3 asks you to make that distinction explicitly, so practise it here.
