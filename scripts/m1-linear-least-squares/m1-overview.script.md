---
deck: "Module 1: Foundations and Linear Regression"
subtitle: "INFO 521 · Module 1 · Overview"
source_qmd: modules/m1-linear-least-squares/m1-overview.qmd
dest: scripts/m1-linear-least-squares/m1-overview.script.md
generated_from: overviews/module_spec.py + overviews/narration.py
scenes: 6
est_spoken_words: 419
est_runtime_min: 3.2   # at ~130 wpm
---

## Title slide — Module 1: Foundations and Linear Regression

Welcome to Module 1. This is the module where the course gets its floor, so almost everything in it comes back later. Three minutes here, then the two lectures do the real work.

## The question

The question is what predicts systolic blood pressure. It sounds like a clinical question and it is, but answering it forces you through the whole modelling pipeline: pick a model, write down what makes a fit good or bad, and then solve for the best one exactly. That sequence is the course. Every module after this takes the same three steps and makes one of them harder.

## What the lectures do

Lecture A sets up the data and the model. You will meet the NHANES cohort we use all term, the leakage rule that governs which features are allowed, and mean squared error as the quantity you minimise. Lecture B derives the closed-form solution: take the gradient, set it to zero, and read off the normal equations. There is also an appendix with the two matrix-calculus identities that derivation leans on, if you want them spelled out.

## Where this sits

Nothing sits behind this module, so we spend the time on things you will use every week: notation, the dataset, and the habit of writing down a loss before fitting anything. The cohort is 5,102 adults with six features, and we stay on it all term precisely so you are never learning a new dataset and a new method in the same week. Module 2 turns around immediately and asks whether the fit you just computed means anything at all.

## Week 1 at a glance

This week you have Homework Units 0 and 1, the prerequisite quiz, and the project gets assigned. Unit 0 is tooling and it is required. The quiz is worth one percent and gates nothing; it is there to show you where to put review time. Read the description document before you take it. The project runs the whole term in two parts, so read the brief this week even though nothing is due.

## Watch out for

Two things to watch. The leakage rule is not a formality. Six features were chosen precisely because they do not encode blood pressure, and adding one that does will make your model look excellent and mean nothing. Second, when you implement the normal equations, solve the linear system. Do not form the inverse. Milestone 1.1 is graded on that distinction. The reason is conditioning: inverting a matrix is numerically worse than solving the system it came from, and on a design matrix with correlated columns you will see the difference.
