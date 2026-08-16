---
deck: "Module 2: Generalization"
subtitle: "INFO 521 · Module 2 · Overview"
source_qmd: modules/m2-generalization/m2-overview.qmd
dest: scripts/m2-generalization/m2-overview.script.md
generated_from: overviews/module_spec.py + overviews/narration.py
scenes: 6
est_spoken_words: 364
est_runtime_min: 2.8   # at ~130 wpm
---

## Title slide — Module 2: Generalization

Module 2. Short version: the number you got last week is not the number you care about, and this module is about the difference.

## The question

Your model fits the data you have. The question is whether it will work on data you do not have. Training error can be pushed as low as you like just by adding flexibility, which is exactly why it cannot be trusted as a measure of quality. So we need a way to measure the thing we actually want, and then a way to buy it on purpose.

## What the lectures do

Lecture A is measurement. Hold out a test set, look at the gap between training and test error, and then use k-fold cross-validation so you are not spending your test set on model selection. Lecture B is explanation and remedy. The bias-variance decomposition says where the U-shaped curve comes from, and ridge regression buys you a better place on it by shrinking coefficients. There is an appendix that derives the decomposition line by line.

## Where this sits

Module 1 ended with a polynomial that fit its training data beautifully and was obviously wrong. This module explains that picture. It also leaves a debt: cross-validation tells you which model generalises, but nothing so far says why squared error was the right loss. Module 3 pays that.

## Week 2 at a glance

Homework Units 2a and 2b this week, and checkpoint quiz 1.1 on the normal equations. Passing that quiz opens Milestone 1.1, which is due the following week, so do not leave it until the last day. That gating pattern holds all term: the quiz lands the week its module is taught, and the milestone it opens is due the week after, so the derivation is always behind you before the work that uses it. If a quiz is blocking you, clear it first. Everything downstream waits on it.

## Watch out for

The mistake I see most is leakage through preprocessing. If you scale or impute using the whole dataset and then split, test information is already in your training data. The fold is the unit, not the dataset. Related: do not choose lambda on the test set. Cross-validate inside training data. The test set is spent the first time you look at it.
