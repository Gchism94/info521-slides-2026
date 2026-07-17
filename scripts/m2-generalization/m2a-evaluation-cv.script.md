---
deck: "Generalization"
subtitle: "INFO 521 · Module 2 · Lecture A — Evaluation & Cross-Validation"
source_qmd: modules/m2-generalization/m2a-evaluation-cv.qmd
dest: scripts/m2-generalization/m2a-evaluation-cv.script.md
scenes: 14
est_spoken_words: 1338
est_runtime_min: 10.3   # at ~130 wpm
---

## Title slide — Generalization

Welcome to Module 2 — Generalization, Lecture A: evaluation and cross-validation. Module 1 got us a fit. Module 2 asks the harder question: will that fit hold up on patients we haven't seen? Today is the diagnosis half — how to measure whether a model has actually learned the pattern or just memorized the sample, and how to estimate that honestly with cross-validation. These materials are adapted with permission from lecture materials by Clayton Morrison at the University of Arizona.

## Learning outcomes

Four things by the end. First, tell training error apart from generalization error — the error on new data. Second, diagnose overfitting from the gap between those two. Third, run k-fold cross-validation. And fourth, use it to actually pick a model or a hyperparameter. The whole lecture is really one question — how well will this do on data it hasn't seen? — and how to answer it without fooling ourselves.

## Bridge from Module 1

Let's pick up the thread we left dangling at the end of Module 1. Basis functions let us make a model as flexible as we like — swap the raw input for features of it, crank the degree up. And flexibility buys fit: a high-degree curve can bend through every single training point. But we saw the danger too — that degree-nine wiggle that chased individual points. It isn't learning the pattern; it's memorizing the sample. So here's the question that runs through this whole module: how much flexibility is actually right? Today we make "too flexible" something we can measure.

## Overfitting, made visible

Here's overfitting you can see. One honest caveat first: real blood pressure is basically linear in age, so it wouldn't show this on its own — for the complexity pictures we use a deliberately curved illustrative signal, still evaluated on the real NHANES age grid. Now look at three fits to thirty points. The degree-one line is too stiff — it sails right past the curvature, underfitting. The degree-three curve tracks the real shape nicely. And the degree-nine curve does that nervous wiggle, bending to touch individual points. Same data, three very different stories — and the only thing we changed is how much flexibility we allowed.

## The trap: training error always drops

Now the trap that catches everyone. Make the model more flexible, and training error only ever goes down — never up. In fact a degree-k polynomial can thread exactly through k-plus-one points and hit zero training loss. Zero. And that should make you suspicious, not happy, because low training error is cheap — you can always buy it with more complexity. The trouble is it tells you nothing about the next patient. So here's the line to burn in: training error is not generalization error. A zero on the training set might mean a perfect model, or a perfectly memorized one — and training error alone can't tell you which.

## Hold out a test set

So how do we get an honest number? Score the model on data it never saw while fitting. Split your patients: a training set to fit the weights, and a separate test set used only to score. Because those test patients sat out the fitting, the error there is a fair estimate of how you'll do on genuinely new people. And when we're also tuning a knob — a degree, a penalty — we carve out a third slice, a validation or "dev" set, to do that tuning, so the test set stays sealed. Treat the test set as sacred: you touch it once, at the very end. Tune on it even a little, and it quietly stops being honest.

## Training vs. test vs. complexity

Here's the central picture of the whole module. Complexity along the bottom, error up the side, two curves. Training error, in blue, slides down and down as complexity rises — no surprise now. But test error, in orange, is U-shaped. On the left it's high because the model's too simple to catch the signal. It falls to a sweet spot in the middle. And then it climbs back up on the right, as the model starts fitting noise instead of pattern. That U is the shape everything in this module hangs on — the left wall, the bottom, and the right wall.

## The generalization gap

The distance between those two curves has a name — the generalization gap — and it diagnoses your model. A wide gap on the right, low training error but high test error: that's overfitting, the model memorized. Both curves high on the left, small gap but bad either way: that's underfitting, too rigid to catch the signal at all. And the bottom of the test-error U, where test error is lowest — that's the just-right complexity. The gap widens exactly when complexity starts outrunning the amount of data you actually have.

## Why cross-validation?

One honest split has two problems, and both bite harder when data's tight. First, it wastes data — every patient you hold out for testing is a patient you didn't get to learn from. Second, it's twitchy: draw a different split and you get a different test error, so the number you report is partly luck of the draw. Cross-validation fixes both by letting every patient play both roles — train and validate — just at different times.

## k-fold cross-validation

Here's the mechanic — five-fold, say. Chop the data into five equal folds, then run five rounds. Round one: fold one is the validation set, the other four train the model, and you score on fold one. Round two: fold two validates, the rest train. And so on down the diagonal, each fold taking exactly one turn in the validation seat. Every patient ends up validating exactly once and training in four of the five rounds — nobody's wasted. Your cross-validation error is just the average of those five round scores: one stable number, squeezed out of all your data.

## Cross-validation error curve

Run that across a range of complexities and you get this — cross-validation error against polynomial degree, with a shaded band showing how much the five folds disagree. It's the same U we saw before, but now honestly estimated using all the data, and the band tells you how much to trust it. The vertical marker sits at the minimum — the degree cross-validation picks. That's the payoff: instead of eyeballing one noisy split, you've got a stable curve that points at a choice.

## Model selection by CV

So here's the workflow, and the discipline baked into it. Use cross-validation to pick the complexity that minimizes CV error. Then refit that chosen model on all of your training data, and report its performance on the held-out test set you still haven't touched. Two different jobs: cross-validation is a selection tool — it turns the knob — and the sealed test set is what you report. The one rule: don't let the data that picks the model also be the data that grades it.

## The pitfall: leakage

And here's the pitfall that silently ruins all of this — leakage. Cross-validation only tells the truth if the folds are honestly walled off from each other. So any preprocessing that learns from the data — centering, scaling — has to be fit inside each training fold and only then applied to its validation fold. Standardize using the whole dataset's mean and standard deviation before you split, and you've let every validation fold peek at itself. Same for the test set — every glance leaks a little information and makes your estimate look rosier than reality. And notice: this is the exact same discipline as the Module 1 feature-leakage rule. The answer must never sneak into the inputs — there it was diastolic BP; here it's the fold statistics.

## Recap & bridge

Quick recap. Training error falls with complexity; test and CV error are U-shaped. K-fold cross-validation gives you a stable estimate and picks the knob. And leakage quietly breaks that estimate, so keep your folds honestly separated. What cross-validation gives us is where we sit on the U. What it doesn't explain is why there's a U at all. That's Lecture B — the bias-variance decomposition that produces the U, and ridge regression, the knob that lets us slide along it.
