"""Recording narration for the module overview decks.

One entry per module, keyed by the slide ids the deck builder emits. The script
builder cross-checks these keys against the slides actually generated, so a
slide can never appear without narration and narration can never survive a slide
being removed.

Written to be read aloud at roughly 140 words per minute. `build_scripts.py`
counts the words and fails if a module lands outside its target window, because
a script that quietly grows to double length is discovered in the recording
booth otherwise.

Voice notes for anyone editing: first person, plain sentences, no em dashes, no
"not X, but Y" construction. Say the number and move on.
"""

NARRATION = {
    1: {
        "open": (
            "Welcome to Module 1. This is the module where the course gets its floor, so "
            "almost everything in it comes back later. Three minutes here, then the two "
            "lectures do the real work."
        ),
        "question": (
            "The question is what predicts systolic blood pressure. It sounds like a clinical "
            "question and it is, but answering it forces you through the whole modelling "
            "pipeline: pick a model, write down what makes a fit good or bad, and then solve "
            "for the best one exactly. That sequence is the course. Every module after this "
            "takes the same three steps and makes one of them harder."
        ),
        "lectures": (
            "Lecture A sets up the data and the model. You will meet the NHANES cohort we use "
            "all term, the leakage rule that governs which features are allowed, and mean "
            "squared error as the quantity you minimise. Lecture B derives the closed-form "
            "solution: take the gradient, set it to zero, and read off the normal equations. "
            "There is also an appendix with the two matrix-calculus identities that "
            "derivation leans on, if you want them spelled out."
        ),
        "sits": (
            "Nothing sits behind this module, so we spend the time on things you will use "
            "every week: notation, the dataset, and the habit of writing down a loss before "
            "fitting anything. The cohort is 5,102 adults with six features, and we stay on it "
            "all term precisely so you are never learning a new dataset and a new method in "
            "the same week. Module 2 turns around immediately and asks whether the fit you "
            "just computed means anything at all."
        ),
        "work": (
            "This week you have Homework Units 0 and 1, the prerequisite quiz, and the project "
            "gets assigned. Unit 0 is tooling and it is required. The quiz is "
            "worth one percent and gates nothing; it is there to show you where to put review "
            "time. Read the description document before you take it. The project runs the "
            "whole term in two parts, so read the brief this week even though nothing is due."
        ),
        "watch": (
            "Two things to watch. The leakage rule is not a formality. Six features were "
            "chosen precisely because they do not encode blood pressure, and adding one that "
            "does will make your model look excellent and mean nothing. Second, when you "
            "implement the normal equations, solve the linear system. Do not form the inverse. "
            "Milestone 1.1 is graded on that distinction. The reason is conditioning: inverting "
            "a matrix is numerically worse than solving the system it came from, and on a "
            "design matrix with correlated columns you will see the difference."
        ),
    },
    2: {
        "open": (
            "Module 2. Short version: the number you got last week is not the number you care "
            "about, and this module is about the difference."
        ),
        "question": (
            "Your model fits the data you have. The question is whether it will work on data "
            "you do not have. Training error can be pushed as low as you like just by adding "
            "flexibility, which is exactly why it cannot be trusted as a measure of quality. "
            "So we need a way to measure the thing we actually want, and then a way to buy it "
            "on purpose."
        ),
        "lectures": (
            "Lecture A is measurement. Hold out a test set, look at the gap between training "
            "and test error, and then use k-fold cross-validation so you are not spending your "
            "test set on model selection. Lecture B is explanation and remedy. The "
            "bias-variance decomposition says where the U-shaped curve comes from, and ridge "
            "regression buys you a better place on it by shrinking coefficients. There is an "
            "appendix that derives the decomposition line by line."
        ),
        "sits": (
            "Module 1 ended with a polynomial that fit its training data beautifully and was "
            "obviously wrong. This module explains that picture. It also leaves a debt: "
            "cross-validation tells you which model generalises, but nothing so far says why "
            "squared error was the right loss. Module 3 pays that."
        ),
        "work": (
            "Homework Units 2a and 2b this week, and checkpoint quiz 1.1 on the normal "
            "equations. Passing that quiz opens Milestone 1.1, which is due the following "
            "week, so do not leave it until the last day. That gating pattern holds all "
            "term: the quiz lands the week its module is taught, and the milestone it opens "
            "is due the week after, so the derivation is always behind you before the work "
            "that uses it. If a quiz is blocking you, clear it first. Everything downstream "
            "waits on it."
        ),
        "watch": (
            "The mistake I see most is leakage through preprocessing. If you scale or impute "
            "using the whole dataset and then split, test information is already in your "
            "training data. The fold is the unit, not the dataset. Related: do not choose "
            "lambda on the test set. Cross-validate inside training data. The test set is "
            "spent the first time you look at it."
        ),
    },
    3: {
        "open": (
            "Module 3. This is the hinge of the course. If you only get one module fully "
            "solid, make it this one."
        ),
        "question": (
            "Two questions. Why squared error, which we have been using for two modules "
            "without justifying, and how sure are we about the weights we estimated. Both get "
            "answered by the same move: assume a model for the noise, write down the "
            "probability of the data you actually observed, and maximise it."
        ),
        "lectures": (
            "Lecture A does the derivation. Gaussian noise, the likelihood of the dataset, the "
            "log-likelihood, and then maximum likelihood for the weights turning out to be "
            "exactly the least-squares solution you already have. The loss was never "
            "arbitrary. You also get the noise variance estimated as part of the deal. "
            "Lecture B asks what kind of estimator you now hold: whether it is unique, whether "
            "it is unbiased, and how much it would move if you collected the data again."
        ),
        "sits": (
            "Before this module you minimise a loss because it seems reasonable. After it you "
            "write down a probability model and derive the loss. Everything from here runs on "
            "likelihoods, so it is worth doing this derivation until you can do it without "
            "notes. It is also the shortest path to understanding why so much of machine "
            "learning looks like optimisation. You are usually maximising a likelihood "
            "wearing a different hat."
        ),
        "work": (
            "Homework Unit 3, checkpoint quiz 1.2 on maximum likelihood, and Milestone 1.1 is "
            "due. There is no activity loop this week. The parameter-uncertainty demo is used "
            "live in Lecture B rather than as a peer loop, so the discussion carries the week "
            "on its own."
        ),
        "watch": (
            "Unbiased does not mean close. It means centred on the truth across repeat "
            "experiments you will never run. Your one estimate can still be far off, and the "
            "covariance is what tells you how far. Also, the maximum likelihood estimate of "
            "the noise variance is biased. It divides by N where the unbiased version divides "
            "by N minus the number of parameters. Lecture A shows you the bias rather than "
            "hiding it. The same correction turns up any time you estimate a spread from data "
            "you also used to estimate a centre."
        ),
    },
    4: {
        "open": (
            "Module 4. We go Bayesian, and for two weeks the algebra is unusually kind to us."
        ),
        "question": (
            "The question is what you should believe about a parameter before and after seeing "
            "data. Module 3 gave you a single best estimate with an error bar. Here the point "
            "estimate is replaced by a distribution that you update as evidence arrives."
        ),
        "lectures": (
            "Lecture A works the Beta-Binomial pair on hypertension prevalence. The headline "
            "is conjugacy: when the prior and likelihood are matched, updating the posterior "
            "is addition. You count successes, you count failures, you add. You also see how "
            "fast the prior stops mattering as data accumulates. Lecture B does the same thing "
            "for the regression weights, watches the posterior contract, and shows ridge "
            "regression reappearing as nothing more than a Gaussian prior."
        ),
        "sits": (
            "That ridge result is worth pausing on. In Module 2 it was a penalty you add "
            "because it works. Here it falls out of taking the probability model seriously. "
            "That keeps happening once you commit to the model. Module 5 then breaks the "
            "conjugacy that makes all of this closed form."
        ),
        "work": (
            "Homework Unit 4, checkpoint quiz 1.3 on the conjugate posterior, and Milestone "
            "1.2 is due. The activity loop is the Bayesian-updating explorer, which is the "
            "fastest way to build intuition for how the prior loses its grip. Push the sample "
            "size up and watch a strong prior and a weak one land on the same answer. That "
            "picture is worth more than the algebra for most people."
        ),
        "watch": (
            "The MAP is not the posterior. It is the single highest point of it, and reporting "
            "it alone throws away the spread, which was the reason for going Bayesian. And "
            "remember that conjugacy is a convenience, not a law. It holds for the pairs in "
            "this module and fails the moment the likelihood changes shape, which is exactly "
            "what happens next week. Enjoy the arithmetic while it lasts."
        ),
    },
    5: {
        "open": (
            "Module 5. This is the busiest week of the term, and it is also where the course "
            "stops having exact answers."
        ),
        "question": (
            "The question is what you do when the posterior has no closed form. Binarise the "
            "outcome, put a logistic link on the linear model, and the conjugacy from last "
            "week is gone. There is no formula left to write down. So we need honest ways to "
            "proceed without one."
        ),
        "lectures": (
            "Lecture A builds the logistic model and fits it with Newton-Raphson, which uses "
            "the curvature of the log-likelihood to get there in a handful of steps rather "
            "than crawling downhill. Lecture B gives you two approximations. Laplace fits a "
            "Gaussian at the mode, which is fast and often good enough. Metropolis draws "
            "samples from the posterior without ever computing the normalising constant, "
            "because in a ratio the constant cancels. That cancellation is the whole trick, and "
            "it is worth sitting with, because it is why sampling works at all on posteriors "
            "nobody can normalise."
        ),
        "sits": (
            "This is the week the material starts looking like practice rather than algebra. "
            "It is also where the second half of the project opens, on the binarised outcome "
            "this module introduces."
        ),
        "work": (
            "Look at the week honestly before it starts. Homework Unit 5, checkpoint quiz 2.1 "
            "on the Newton update, Milestones 1.3 and 1.4 due, and the project midpoint: Part "
            "1 due. Part 2 begins immediately. There is no "
            "discussion this week because of the midpoint. Starting this week on the Wednesday "
            "will not work. Look at what Part 1 asks for now, while you still have room to "
            "move things around."
        ),
        "watch": (
            "Laplace only sees the peak. It is a Gaussian fitted at the mode, so skew and "
            "multimodality are invisible to it. That is fine right up until it is not, and "
            "Lecture B shows you a case where it is not. Knowing which of your approximations "
            "is lying to you is most of the skill here."
        ),
    },
    6: {
        "open": (
            "Module 6. Two shifts in one module, and the second one is bigger than it looks."
        ),
        "question": (
            "First question: what if you optimise the decision boundary directly instead of "
            "modelling probabilities at all. Second question: what if there are no labels. "
            "That second one changes what counts as an answer, because with no labels there is "
            "nothing to be right about."
        ),
        "lectures": (
            "Lecture A is maximum-margin classification. You see the same boundary from three "
            "philosophies, meet the hinge loss for data that is not separable, and compare "
            "what hinge and logistic each actually care about. Kernels get covered at concept "
            "level. Lecture B is k-means: the objective, why standardising comes first, why "
            "restarts are mandatory, and how to choose K without fooling yourself. Minimising "
            "the objective over K does not work, because it keeps dropping until every point "
            "is its own cluster, so we read the elbow and stay honest about how soft that "
            "reading is."
        ),
        "sits": (
            "Everything before this was supervised and probabilistic. Lecture A keeps the "
            "labels and drops the probability. Lecture B keeps neither. Module 7 stays in that "
            "unsupervised world and asks about directions rather than groups. If you have spent "
            "six weeks thinking of a model as a thing that predicts a label, this is the week "
            "to widen that."
        ),
        "work": (
            "Checkpoint quiz 2.3 on k-means and PCA, and Milestones 2.1 and 2.2 are due, which "
            "is Gate A. There is no new homework "
            "unit this week, which is deliberate, because the project is heavy right now."
        ),
        "watch": (
            "Three quick ones. Accuracy is a weak claim at 38.8 percent prevalence, because "
            "always predicting the majority class scores 61.2. Distances have units, so "
            "k-means on unstandardised features clusters on whichever variable has the biggest "
            "numbers. And clusters are not diagnoses. A cluster is a region of feature space, "
            "and naming it after a condition is a claim you have not earned. Milestone 2.3 asks "
            "you to make that distinction explicitly, so practise it here."
        ),
    },
    7: {
        "open": (
            "Module 7. The last method of the course, and then we step back and look at the "
            "whole thing, because by now you have all of it and can actually see the shape."
        ),
        "question": (
            "The question is which directions in the data matter. You have six features and "
            "they are not six independent stories. Principal component analysis finds the "
            "directions along which the cohort genuinely varies, and it turns out those are "
            "the same directions that reconstruct the data best. Two different questions, one "
            "eigendecomposition."
        ),
        "lectures": (
            "One lecture this week. Centre the data, form the covariance matrix, take its "
            "eigendecomposition, and read the eigenvalues as variance explained. You will see "
            "the first component on the adiposity plane, a scree plot across all six features, "
            "and an honest discussion of when a component means something and when it does not."
        ),
        "sits": (
            "This closes the unsupervised turn that Module 6 opened. It is also where the arc "
            "of the course gets named out loud."
        ),
        "work": (
            "Milestones 2.3 and 2.4 are due this week, which is Gate B. No homework unit "
            "and no checkpoint quiz. The discussion is about the course "
            "arc, and it is a good place to work out what your final report should say."
        ),
        "watch": (
            "PCA never looked at your outcome. It maximises variance, and variance is not "
            "relevance, so the top component can be the least useful predictor you have. And a "
            "component is a direction, not a concept. Loadings sometimes read cleanly and "
            "sometimes do not, and interpreting one is a claim that needs evidence like any "
            "other."
        ),
        # ── wrap-up ──
        "arc": (
            "Here is the whole course on one slide. Modules 1 and 2: write down a loss, solve "
            "it exactly, then find out whether the answer generalises. Module 3: stop assuming "
            "the loss and derive it from a noise model, which hands you parameter uncertainty "
            "for free. Module 4: replace the estimate with a distribution and update it in "
            "closed form. Module 5: conjugacy breaks, so approximate or sample. Module 6: drop "
            "probability for the margin, then drop the labels. Module 7: ask what structure the "
            "features have on their own. Read down that list and it is one idea getting "
            "steadily less convenient and more honest. Every step was taken because the "
            "previous tool could not answer the next question. That is worth remembering when "
            "you meet a method this course did not cover. The question to ask is not whether "
            "it is new. It is what the previous tool could not do."
        ),
        "learned": (
            "Stated as a capability rather than a syllabus: you can write down a model and a "
            "loss, derive the estimator, say how uncertain it is, update it as evidence "
            "arrives, approximate it when the algebra runs out, and check whether any of it "
            "generalises. That is what the five course outcomes were asking for, and the "
            "project is where you demonstrate it. Worth saying plainly: the point was never the "
            "seven methods. Any of them is one line from a library. The point was being able "
            "to say what a method assumes, what it gives you, and where it stops being "
            "trustworthy, which is the part the library call cannot do for you."
        ),
        "left": (
            "What is left. Week 7.5 is the course close, and it carries Milestone 2.5 and "
            "the Part 2 report. On homework, your best five core units count and Unit 0 is required, "
            "so one core unit can be dropped; if you are carrying a Not-Yet you want to "
            "convert, this is the week to do it. Revision tokens expire with the term, so "
            "spend them. The discussion this week is on the course arc, and it is a useful "
            "place to work out what your final report should argue before you write it."
        ),
        "next": (
            "One last thing. Neural networks are the obvious next step and they are "
            "deliberately not in this course. There are optional readings on the schedule, and "
            "INFO 557 picks the thread up properly. Nothing there replaces what you built "
            "here. A network is still a model with a loss, fitted by an optimiser, and "
            "evaluated on data it has not seen. You already know how to ask whether it works. "
            "Good luck with the final report."
        ),
    },
}
