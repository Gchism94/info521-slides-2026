---
deck: "Module 7: Principal Component Analysis, and the Course in One Arc"
subtitle: "INFO 521 · Module 7 · Overview and Course Wrap-Up"
source_qmd: modules/m7-pca/m7-overview.qmd
dest: scripts/m7-pca/m7-overview.script.md
generated_from: overviews/module_spec.py + overviews/narration.py
scenes: 10
est_spoken_words: 690
est_runtime_min: 5.3   # at ~130 wpm
---

## Title slide — Module 7: Principal Component Analysis, and the Course in One Arc

Module 7. The last method of the course, and then we step back and look at the whole thing, because by now you have all of it and can actually see the shape.

## The question

The question is which directions in the data matter. You have six features and they are not six independent stories. Principal component analysis finds the directions along which the cohort genuinely varies, and it turns out those are the same directions that reconstruct the data best. Two different questions, one eigendecomposition.

## What the lectures do

One lecture this week. Centre the data, form the covariance matrix, take its eigendecomposition, and read the eigenvalues as variance explained. You will see the first component on the adiposity plane, a scree plot across all six features, and an honest discussion of when a component means something and when it does not.

## Where this sits

This closes the unsupervised turn that Module 6 opened. It is also where the arc of the course gets named out loud.

## Week 7 at a glance

Milestones 2.3 and 2.4 are due this week, which is Gate B. No homework unit and no checkpoint quiz. The discussion is about the course arc, and it is a good place to work out what your final report should say.

## Watch out for

PCA never looked at your outcome. It maximises variance, and variance is not relevance, so the top component can be the least useful predictor you have. And a component is a direction, not a concept. Loadings sometimes read cleanly and sometimes do not, and interpreting one is a claim that needs evidence like any other.

## The course, in one arc

Here is the whole course on one slide. Modules 1 and 2: write down a loss, solve it exactly, then find out whether the answer generalises. Module 3: stop assuming the loss and derive it from a noise model, which hands you parameter uncertainty for free. Module 4: replace the estimate with a distribution and update it in closed form. Module 5: conjugacy breaks, so approximate or sample. Module 6: drop probability for the margin, then drop the labels. Module 7: ask what structure the features have on their own. Read down that list and it is one idea getting steadily less convenient and more honest. Every step was taken because the previous tool could not answer the next question. That is worth remembering when you meet a method this course did not cover. The question to ask is not whether it is new. It is what the previous tool could not do.

## What you can do now

Stated as a capability rather than a syllabus: you can write down a model and a loss, derive the estimator, say how uncertain it is, update it as evidence arrives, approximate it when the algebra runs out, and check whether any of it generalises. That is what the five course outcomes were asking for, and the project is where you demonstrate it. Worth saying plainly: the point was never the seven methods. Any of them is one line from a library. The point was being able to say what a method assumes, what it gives you, and where it stops being trustworthy, which is the part the library call cannot do for you.

## What is left

What is left. Week 7.5 is the course close, and it carries Milestone 2.5 and the Part 2 report. On homework, your best five core units count and Unit 0 is required, so one core unit can be dropped; if you are carrying a Not-Yet you want to convert, this is the week to do it. Revision tokens expire with the term, so spend them. The discussion this week is on the course arc, and it is a useful place to work out what your final report should argue before you write it.

## Where next

One last thing. Neural networks are the obvious next step and they are deliberately not in this course. There are optional readings on the schedule, and INFO 557 picks the thread up properly. Nothing there replaces what you built here. A network is still a model with a loss, fitted by an optimiser, and evaluated on data it has not seen. You already know how to ask whether it works. Good luck with the final report.
