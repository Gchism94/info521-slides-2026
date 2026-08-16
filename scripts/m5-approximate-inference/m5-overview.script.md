---
deck: "Module 5: Approximate Inference and Bayesian Classification"
subtitle: "INFO 521 · Module 5 · Overview"
source_qmd: modules/m5-approximate-inference/m5-overview.qmd
dest: scripts/m5-approximate-inference/m5-overview.script.md
generated_from: overviews/module_spec.py + overviews/narration.py
scenes: 6
est_spoken_words: 321
est_runtime_min: 2.5   # at ~130 wpm
---

## Title slide — Module 5: Approximate Inference and Bayesian Classification

Module 5. This is the busiest week of the term, and it is also where the course stops having exact answers.

## The question

The question is what you do when the posterior has no closed form. Binarise the outcome, put a logistic link on the linear model, and the conjugacy from last week is gone. There is no formula left to write down. So we need honest ways to proceed without one.

## What the lectures do

Lecture A builds the logistic model and fits it with Newton-Raphson, which uses the curvature of the log-likelihood to get there in a handful of steps rather than crawling downhill. Lecture B gives you two approximations. Laplace fits a Gaussian at the mode, which is fast and often good enough. Metropolis draws samples from the posterior without ever computing the normalising constant, because in a ratio the constant cancels. That cancellation is the whole trick, and it is worth sitting with, because it is why sampling works at all on posteriors nobody can normalise.

## Where this sits

This is the week the material starts looking like practice rather than algebra. It is also where the second half of the project opens, on the binarised outcome this module introduces.

## Week 5 at a glance

Look at the week honestly before it starts. Homework Unit 5, checkpoint quiz 2.1 on the Newton update, Milestones 1.3 and 1.4 due, and the project midpoint: Part 1 due. Part 2 begins immediately. There is no discussion this week because of the midpoint. Starting this week on the Wednesday will not work. Look at what Part 1 asks for now, while you still have room to move things around.

## Watch out for

Laplace only sees the peak. It is a Gaussian fitted at the mode, so skew and multimodality are invisible to it. That is fine right up until it is not, and Lecture B shows you a case where it is not. Knowing which of your approximations is lying to you is most of the skill here.
