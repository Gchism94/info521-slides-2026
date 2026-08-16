"""Single source for the seven module overviews.

Each module gets three artifacts, and all three are generated from the entry
below so they cannot drift apart:

    modules/<dir>/m<N>-overview.qmd    a short reveal deck, about 3 minutes
    overviews/out/module-<N>-overview.{html,pdf}   the written overview
    overviews/out/module-<N>-script.{html,pdf}     the recording script

If you want to change what an overview says, change it HERE and re-run the
builders. Editing the generated `m<N>-overview.qmd` by hand will be overwritten,
and worse, will silently desynchronise the script you record from.

Every fact in this file traces to a source in the repos:

* week, readings, activity, discussion, and the assessment column come from
  `info521/schedule.qmd`
* deck names and their section headings come from the decks themselves
* milestone titles come from `info521-projects-2026/project-{1,2}/*.qmd`
* homework unit titles come from `info521/homeworks/unit*.qmd`
* checkpoint numbering and what each gates comes from
  `info521-homeworks-2026/quizzes/quiz_bank.py`
* course outcomes CLO1 to CLO5 and the grade weights come from
  `info521/syllabus.qmd` sections 1.2 and 3.1.3.1

Narration budget: 130 words per minute, the same rate the repo's other
delivery scripts use. The script builder checks each module
against its `minutes` target and fails the build if a script has drifted long
or short, which is the failure mode that actually costs recording time.
"""

# 130 words per minute, matching the `est_runtime_min` field the existing
# lecture delivery scripts in scripts/**/*.script.md are timed at. Keep these
# consistent: two different rates across one repo means two different ideas of
# how long a deck runs.
WPM = 130

# ---------------------------------------------------------------------------
# Course-level material, used by Module 7's wrap-up.
# ---------------------------------------------------------------------------

CLOS = [
    ("CLO1", "Identify and evaluate machine-learning approaches appropriate for "
             "regression, classification, clustering, and dimensionality-reduction problems."),
    ("CLO2", "Implement machine-learning algorithms in Python using industry-standard "
             "tools and workflows."),
    ("CLO3", "Compare and interpret model performance using appropriate evaluation "
             "metrics, validation techniques, and statistical reasoning."),
    ("CLO4", "Apply machine-learning methods to real-world datasets to develop "
             "predictive and descriptive models."),
    ("CLO5", "Communicate machine-learning results, limitations, and recommendations "
             "through written, visual, and technical presentations."),
]

WEIGHTS = [("Project", 55), ("Homework", 25), ("Peer loops and discussions", 10),
           ("Checkpoints", 9), ("Prerequisite quiz", 1)]

MODULES = [
    # ─────────────────────────────── Module 1 ───────────────────────────────
    {
        "n": 1,
        "dir": "m1-linear-least-squares",
        "title": "Foundations and Linear Regression",
        "week": "Week 1",
        "minutes": 3,
        "question": "What predicts systolic blood pressure?",
        "question_gloss": (
            "One clinical question opens the whole course. Answering it means choosing a "
            "model, writing down what makes a fit good or bad, and solving for the best fit "
            "exactly. Every module after this one takes that same machinery and asks harder "
            "questions of it."
        ),
        "lectures": [
            ("Lecture A: Setup, Data, and the Linear Model",
             "NHANES 2021-2022, the leakage rule, the linear model, and mean squared error "
             "as the thing you minimise."),
            ("Lecture B: Normal Equations and Geometry",
             "The gradient of the loss, the normal equations, least squares as an orthogonal "
             "projection, and basis functions when a straight line will not do."),
            ("Appendix: Matrix Calculus",
             "The two identities the Lecture B derivation leans on, worked out."),
        ],
        "sits": (
            "This is the floor. There is nothing behind it to build on, so the module spends "
            "its time on things you will use every week after: the notation, the dataset, and "
            "the habit of writing down a loss before you fit anything. Module 2 immediately "
            "asks whether the fit you just computed means anything."
        ),
        "work": [
            "Homework Units 0 and 1. Unit 0 is tooling and reproducibility and is required; "
            "Unit 1 is linear models and model selection.",
            "The prerequisite quiz, worth 1% and gating nothing. It is a readiness check.",
            "The project is assigned this week. It runs the whole term in two parts, with "
            "Part 1 due at the Week 5 midpoint.",
            "Activity loop: the week01 least-squares explorer, embedded live in Lecture A.",
            "Discussion: introductions.",
            "Reading: PML Chapter 1 sections 1.1 to 1.3 and section 1.5; MML Chapters 2 and 9.",
        ],
        "watch": [
            ("The leakage rule is not a formality.",
             "Six features were chosen for this dataset specifically because they do not "
             "encode the outcome. If you add a feature that does, your model will look "
             "excellent and mean nothing."),
            ("Solve the system, do not form the inverse.",
             "The normal equations are written with an inverse because that is how the algebra "
             "reads. In code you solve the linear system. Milestone 1.1 is graded on this."),
        ],
    },
    # ─────────────────────────────── Module 2 ───────────────────────────────
    {
        "n": 2,
        "dir": "m2-generalization",
        "title": "Generalization",
        "week": "Week 2",
        "minutes": 3,
        "question": "Your model fits the data you have. Will it work on data you do not?",
        "question_gloss": (
            "Module 1 gave you a fit and a number that says how good it is on the points you "
            "trained on. That number can be made as good as you like, which is exactly why it "
            "cannot be trusted. This module is about measuring the thing you actually care "
            "about, and then about buying it deliberately."
        ),
        "lectures": [
            ("Lecture A: Evaluation and Cross-Validation",
             "Training error always drops. Holding out a test set, the generalization gap, "
             "k-fold cross-validation, and selecting a model with it."),
            ("Lecture B: Bias-Variance and Regularization",
             "Where the U-shape comes from, the decomposition behind it, ridge regression and "
             "its closed form, the coefficient path, and choosing lambda by cross-validation."),
            ("Appendix: The Bias-Variance Decomposition",
             "The add-and-subtract trick, and why the cross terms vanish."),
        ],
        "sits": (
            "Module 1 ended with a polynomial that fit the training data beautifully and was "
            "obviously wrong. This module explains that picture and gives you the tools to "
            "avoid it. It also sets up a debt: cross-validation tells you which model "
            "generalises, but not why squared error was the right loss to begin with. "
            "Module 3 pays that debt."
        ),
        "work": [
            "Homework Units 2a and 2b, probability and estimation foundations.",
            "Checkpoint quiz 1.1 on the normal equations. Passing it opens Milestone 1.1, "
            "which is due next week.",
            "Activity loop: the week02 bias-variance explorer.",
            "Discussion: the tradeoff in your own words.",
            "Reading: PML section 4.7 and section 11.3; MML Chapter 5 as review.",
        ],
        "watch": [
            ("Leakage hides in preprocessing.",
             "Scaling or imputing on the full dataset before you split leaks test information "
             "into training. The fold is the unit, not the dataset."),
            ("Do not choose lambda on the test set.",
             "Cross-validate within training data. The test set is spent the first time you "
             "look at it."),
        ],
    },
    # ─────────────────────────────── Module 3 ───────────────────────────────
    {
        "n": 3,
        "dir": "m3-mle-uncertainty",
        "title": "Maximum Likelihood and Parameter Uncertainty",
        "week": "Week 3",
        "minutes": 3,
        "question": "Why squared error, and how sure are we about the numbers we got?",
        "question_gloss": (
            "Squared error has been the loss for two modules without a reason. This module "
            "gives one: assume a noise model, write down the probability of the data, and "
            "maximise it. Least squares falls out. Then the same machinery answers a question "
            "least squares never could, which is how much your estimated weights would move "
            "if you collected the data again."
        ),
        "lectures": [
            ("Lecture A: From Loss to Likelihood",
             "The Gaussian noise model, the likelihood and log-likelihood of a dataset, the "
             "MLE for the weights turning out to be the least-squares solution, and the noise "
             "variance getting estimated too."),
            ("Lecture B: Properties of the MLE",
             "Uniqueness, unbiasedness and what it does not promise, the covariance of the "
             "estimator, and Fisher information as the curvature that sets it."),
            ("Appendix: The Full Covariance Derivation",
             "The second moment, term by term."),
        ],
        "sits": (
            "This is the hinge of the course. Before it, you minimise a loss because it seems "
            "reasonable. After it, you write down a probability model and derive the loss. "
            "Every module that follows is built on likelihoods, so the derivation here is worth "
            "doing until it is automatic."
        ),
        "work": [
            "Homework Unit 3, Monte Carlo and estimators.",
            "Checkpoint quiz 1.2 on maximum likelihood. Passing it opens Milestone 1.2.",
            "Milestone 1.1, least squares, is due this week.",
            "No activity loop this week. The parameter-uncertainty demo is used in lecture "
            "rather than as a peer loop, so the discussion carries the week on its own.",
            "Discussion: what likelihood buys us.",
            "Reading: PML Chapters 2 and 3, sections 4.1 to 4.2 and 4.7; MML Chapter 6 as review.",
        ],
        "watch": [
            ("Unbiased does not mean close.",
             "An unbiased estimator is centred on the truth across imaginary repeat "
             "experiments. Your one estimate can still be far off. The covariance is what "
             "tells you how far."),
            ("The variance MLE is biased, and knowably so.",
             "It divides by N where the unbiased estimator divides by N minus the number of "
             "parameters. Lecture A shows the bias rather than hiding it."),
        ],
    },
    # ─────────────────────────────── Module 4 ───────────────────────────────
    {
        "n": 4,
        "dir": "m4-bayesian-inference",
        "title": "Bayesian Inference",
        "week": "Week 4",
        "minutes": 3,
        "question": "What should we believe about a parameter, before and after seeing data?",
        "question_gloss": (
            "Module 3 gave you a single best estimate and an error bar around it. This module "
            "replaces the point estimate with a distribution you can update. When the prior "
            "and the likelihood are a conjugate pair, that update is closed form: no "
            "optimisation, no simulation, just arithmetic on the parameters."
        ),
        "lectures": [
            ("Lecture A: Priors, Posteriors, and the Beta-Binomial",
             "Bayes' rule term by term, hypertension prevalence as the running question, the "
             "Beta prior, conjugacy as addition, and how quickly the prior stops mattering."),
            ("Lecture B: The Conjugate Gaussian Posterior",
             "The same idea for the regression weights, the posterior contracting as data "
             "arrives, ridge reappearing as a particular prior, and the predictive band for a "
             "new patient."),
        ],
        "sits": (
            "Ridge regression showed up in Module 2 as a penalty you add because it works. "
            "Here it reappears as the consequence of a Gaussian prior, which is the sort of "
            "thing that happens repeatedly once you take the probability model seriously. "
            "Module 5 then breaks the conjugacy that makes all of this easy."
        ),
        "work": [
            "Homework Unit 4, exact and conjugate Bayesian inference.",
            "Checkpoint quiz 1.3 on the conjugate posterior. Passing it opens Milestone 1.3.",
            "Milestone 1.2, maximum likelihood, is due this week.",
            "Activity loop: the week03 Bayesian-updating explorer.",
            "Discussion: how the posterior contracts.",
            "Reading: PML sections 4.6 and 11.7; Think Bayes Chapters 2 and 4.",
        ],
        "watch": [
            ("The MAP is not the posterior.",
             "It is the single highest point of it. Reporting the MAP alone throws away the "
             "spread, which was the reason for going Bayesian in the first place."),
            ("Conjugacy is a convenience, not a law.",
             "It holds for the pairs in this module and fails as soon as the likelihood "
             "changes shape. Module 5 is what happens next."),
        ],
    },
    # ─────────────────────────────── Module 5 ───────────────────────────────
    {
        "n": 5,
        "dir": "m5-approximate-inference",
        "title": "Approximate Inference and Bayesian Classification",
        "week": "Week 5",
        "minutes": 3,
        "question": "What do you do when the posterior has no closed form?",
        "question_gloss": (
            "Binarise the outcome, put a logistic link on the linear model, and the conjugacy "
            "from Module 4 is gone. There is no formula for the posterior any more. This "
            "module gives you two honest ways to proceed: approximate the shape, or draw "
            "samples from it."
        ),
        "lectures": [
            ("Lecture A: Logistic Regression and Newton's Method",
             "Squashing the line, the log-likelihood that results, and Newton-Raphson using "
             "curvature to reach the answer in a handful of steps."),
            ("Lecture B: Laplace Approximation and a Taste of Sampling",
             "Fitting a Gaussian at the mode, when the peak is not the story, and the "
             "Metropolis trick that lets you sample without ever computing the normaliser."),
        ],
        "sits": (
            "This is the week the course stops having exact answers, which is also the week it "
            "starts looking like practice. It is the busiest week on the calendar: the project "
            "midpoint lands here, and the second half of the project opens on the binarised "
            "outcome this module introduces."
        ),
        "work": [
            "Homework Unit 5, approximate Bayesian inference.",
            "Checkpoint quiz 2.1 on the Newton-Raphson update. Passing it opens Milestone 2.1 "
            "and Gate A.",
            "Milestones 1.3 and 1.4 are due this week.",
            "The project midpoint: Part 1 is due. Part 2 begins immediately after.",
            "Activity loop: the week04 logistic-regression explorer. No discussion this week; "
            "it is the midpoint.",
            "Reading: PML sections 10.1 to 10.2 and 4.6.8; Think Bayes Chapter 19.",
        ],
        "watch": [
            ("Laplace only sees the peak.",
             "It is a Gaussian fitted at the mode. Skew and multimodality are invisible to it, "
             "which is fine until it is not. Lecture B shows a case where it is not."),
            ("Plan for the midpoint before it arrives.",
             "Week 5 carries two milestones, a checkpoint, a homework unit, and the Part 1 "
             "deadline. Starting it on the Wednesday will not work."),
        ],
    },
    # ─────────────────────────────── Module 6 ───────────────────────────────
    {
        "n": 6,
        "dir": "m6-svm-clustering",
        "title": "Support Vector Machines and Clustering",
        "week": "Week 6",
        "minutes": 3,
        "question": "What if you optimise the boundary directly, and what if there are no labels at all?",
        "question_gloss": (
            "Two shifts in one module. First, a classifier that ignores probability entirely "
            "and maximises the margin instead, which puts three philosophies of the same "
            "boundary side by side. Then the labels come off altogether and the question "
            "becomes what structure the data has on its own."
        ),
        "lectures": [
            ("Lecture A: Maximum-Margin Classification",
             "The margin idea, the hinge loss for data that is not separable, what hinge and "
             "logistic each care about, kernels at concept level, and evaluating a classifier "
             "when the positive class is 38.8% of the cohort."),
            ("Lecture B: k-means and the Unsupervised Turn",
             "The k-means objective, why standardising comes first, why restarts are not "
             "optional, choosing K honestly, and the bridge from hard assignments to mixtures."),
        ],
        "sits": (
            "Everything up to here has been supervised and probabilistic. Lecture A keeps the "
            "labels and drops the probability; Lecture B keeps neither. Module 7 stays "
            "unsupervised and asks about directions rather than groups."
        ),
        "work": [
            "Checkpoint quiz 2.3 on the k-means objective and PCA. Passing it opens "
            "Milestone 2.3 and Gate B.",
            "Milestones 2.1 and 2.2 are due this week, which is Gate A.",
            "No new homework unit this week.",
            "Activity loop: the week05 k-means explorer.",
            "Discussion: when clusters match labels.",
            "Reading: PML sections 21.3 to 21.4; MML Chapter 11 for the SVM material.",
        ],
        "watch": [
            ("Accuracy is a weak claim at 38.8% prevalence.",
             "Always predicting the majority class gets you 61.2%. Lecture A covers what to "
             "report instead."),
            ("Distances have units.",
             "k-means on unstandardised features clusters on whichever variable happens to "
             "have the largest numbers. Standardise first, every time."),
            ("Clusters are not diagnoses.",
             "A cluster is a region of feature space. Naming it after a condition is a claim "
             "you have not earned."),
        ],
    },
    # ─────────────────────────────── Module 7 ───────────────────────────────
    {
        "n": 7,
        "dir": "m7-pca",
        "title": "Principal Component Analysis, and the Course in One Arc",
        "week": "Week 7",
        "minutes": 6,
        "question": "Which directions in the data actually matter?",
        "question_gloss": (
            "Six features, and not six independent stories. PCA finds the directions along "
            "which the cohort actually varies, which turns out to be the same as finding the "
            "directions that reconstruct it best. Two questions, one eigendecomposition."
        ),
        "lectures": [
            ("Lecture: PCA and Course Synthesis",
             "Centring, the covariance matrix, the two equivalent views, the scree plot across "
             "all six features, what a component means and when it means nothing, and how to "
             "choose how many to keep."),
        ],
        "sits": (
            "The last method of the course, and the one that closes the unsupervised turn "
            "Module 6 started. It is also where the arc gets named out loud, because by this "
            "point you have the whole thing and can see it."
        ),
        "work": [
            "Milestones 2.3 and 2.4 are due this week, which is Gate B.",
            "No new homework unit and no checkpoint quiz this week.",
            "Activity loop: the week06 PCA explorer.",
            "Discussion: the course arc.",
            "Reading: MML section 4.2 and Chapter 10; PML section 20.1 as secondary.",
        ],
        "watch": [
            ("PCA never looked at your outcome.",
             "It maximises variance, and variance is not relevance. The top component can be "
             "the least useful predictor in the set."),
            ("A component is a direction, not a concept.",
             "Loadings sometimes read cleanly and sometimes do not. Interpreting one is a "
             "claim about your data, and it needs the same evidence as any other claim."),
        ],
        # Module 7 alone carries the wrap-up.
        "wrapup": {
            "arc": [
                ("Modules 1 and 2", "Write down a loss, solve it exactly, and then find out "
                                    "whether the answer generalises."),
                ("Module 3", "Stop assuming the loss. Derive it from a noise model, and get "
                             "parameter uncertainty for free."),
                ("Module 4", "Replace the estimate with a distribution, and update it in "
                             "closed form while conjugacy holds."),
                ("Module 5", "Conjugacy breaks. Approximate the posterior at its mode, or "
                             "sample from it."),
                ("Module 6", "Drop probability for the margin, then drop the labels entirely."),
                ("Module 7", "Ask what structure the features have on their own."),
            ],
            "arc_close": (
                "Read down that list and it is one idea getting progressively less "
                "convenient and more honest. Every step was taken because the previous "
                "tool could not answer the next question."
            ),
            "learned": (
                "You can write down a model and a loss, derive the estimator, say how "
                "uncertain it is, update it as evidence arrives, approximate it when the "
                "algebra runs out, and check whether any of it generalises. That is the "
                "whole of the course stated as a capability, and it is what the outcomes "
                "below were asking for."
            ),
            "left": [
                "Week 7.5 is the course close: Milestone 2.5 and the Part 2 report are due.",
                "Homework: your best five core units count, and Unit 0 is required, so one core "
                "unit can be dropped. If you are carrying a Not-Yet you want to convert, this is "
                "the week.",
                "Any revision tokens you have left expire with the term. Spend them.",
                "The discussion this week is the course arc, which is a good place to work out "
                "what you want the final report to say.",
            ],
            "next": (
                "Neural networks are the obvious next thing and they are deliberately not in "
                "this course. There are optional readings on the schedule from Understanding "
                "Deep Learning, and INFO 557 picks the thread up properly. Nothing there "
                "replaces what you built here: a network is still a model with a loss, "
                "fitted by an optimiser, and evaluated on data it has not seen."
            ),
        },
    },
]


def by_number(n):
    for m in MODULES:
        if m["n"] == n:
            return m
    raise KeyError(f"no module {n}")
