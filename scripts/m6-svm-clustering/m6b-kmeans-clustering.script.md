---
deck: "SVM & Clustering"
subtitle: "INFO 521 · Module 6 · Lecture B — k-means & the Unsupervised Turn"
source_qmd: modules/m6-svm-clustering/m6b-kmeans-clustering.qmd
dest: scripts/m6-svm-clustering/m6b-kmeans-clustering.script.md
scenes: 13
est_spoken_words: 1580
est_runtime_min: 12.2   # at ~130 wpm
---

## Title slide — SVM & Clustering

Welcome back to Module 6 — Lecture B, k-means and the unsupervised turn. This is the pivot the whole course has quietly been building toward. For five and a half modules, the label y has been the star — everything we did was in service of predicting it. Today we delete the y column and ask a genuinely different question: with only the features in hand, do the patients fall into groups at all? That's clustering, and k-means is where we start. These materials are adapted with permission from lecture materials by Clayton Morrison at the University of Arizona.

## Learning outcomes

Four outcomes. First, pose the clustering problem — structure in the features, with no labels. Second, run k-means — the assign and update steps — and state its distortion objective. Third, diagnose its failure modes: local optima, choosing the number of clusters, and scaling. And fourth — the one with real teeth — refuse the free lunch: clusters are not labels, and I want you able to say why, with data.

## The unsupervised turn

Here's the turn, precisely. Every method so far ate pairs — an input and its label. Now we delete the labels and keep just the feature vectors. No y, and crucially, no right answer to check against. Two flavors of this. Clustering: do the patients form groups? — that's today. And dimensionality reduction: do the features hide a simpler description? — that's Module 7. In the accent color, here's the hard part: without labels there's no test set and no ground truth. Evaluation becomes internal — how well does the structure fit the data — plus judgment — is it actually meaningful? Losing the answer key is the whole philosophical weight of this module, and it comes back hard by the end of the hour.

## k-means: the objective

k-means, concretely. You pick a number of clusters, K, and you're looking for two things: K centroids — cluster centers — and an assignment of every patient to one of them. What you minimize is the distortion: the total squared distance from each patient to its assigned centroid. It's a loss again — the same squared error we've had all term. And the trick is it splits into two sub-problems, each trivial once you fix the other. Assign: with the centroids fixed, send every patient to its nearest one. Update: with the assignments fixed, move each centroid to the mean of its members — which, of course, is the point that minimizes squared error, straight out of Module 1. Alternate those two until nothing moves. Each step can only lower the distortion, so it's guaranteed to converge — though, and hold this thought, not necessarily to the best answer.

## k-means on NHANES: the adiposity plane

Let's run it on real patients, in the plane of two features — standardized BMI and waist circumference — with K equals three. And here's the honest read of what you're seeing. BMI and waist are almost the same measurement; they're correlated around zero-point-nine, so this cloud is really one long diagonal continuum. k-means slices it into three bands — lower, middle, and upper adiposity — with the centroids marked by the purple X's. But look carefully at what just happened: those three groups exist because we asked for three, not because nature drew three. The algorithm will always hand you exactly K clusters, whether or not K clusters are really there. Keep that skepticism close.

## Standardize first — distances have units

A quick but non-negotiable point: because k-means runs on Euclidean distance, the feature scales literally are the model. Leave the features in raw units and waist, which varies by about seventeen centimeters, would utterly drown out HbA1c, which varies by about one percent — your clustering would be "waist circumference, with faint commentary." Standardizing every feature to mean zero and standard deviation one gives them an equal vote. It's the same standardizing move as Module 1's standardized age, except here it's load-bearing — it changes the answer. No distance-based method is scale-free: choosing your units is choosing your clusters. And the Module 2 leakage discipline still applies — in a train-test setting, you'd compute those standardizing statistics on the training data alone.

## Local optima: restarts are not optional

Remember I said converge, but not necessarily to the best? Here's that made real. Same NHANES data, K equals four, and the only thing that changes across these twenty runs is the random starting position of the centroids. Look at the final distortions — they settle on several visibly different levels. Same algorithm, same data, different answers, purely because of where each run started. That's the local-optima problem: k-means always rolls downhill to a valley, but not always the deepest valley. The fix is refreshingly dumb — just run it many times from different random starts, and keep the one with the lowest distortion. Smarter seeding, like k-means-plus-plus, helps too. But the one-line lesson: a single run of k-means is not to be trusted.

## Choosing K: the elbow, honestly

And how many clusters should there be? Here's distortion against K. Notice it only ever falls as K grows — and at K equals N, every patient is its own cluster and distortion hits zero. That's the Module 2 training-error trap in a new costume: more complexity always fits better, so lowest distortion can't be the criterion. Instead we hunt for the elbow — the K where the marginal improvement suddenly flattens. And on this real data, the honest truth is the elbow is soft, gentle, not a clean corner at all. Which is itself the finding: the underlying structure is a continuum, so there's no magic K to discover. The number of clusters is a modeling choice you own and defend — the elbow suggests, but you decide.

## Hard assignments → soft: the GMM bridge

One bridge worth naming, because every single piece of it is a callback. k-means makes hard assignments — every patient belongs fully to one cluster, even the ones sitting right on a boundary. The probabilistic upgrade is the Gaussian mixture model: model the data as a blend of Gaussians, one per cluster, fit by an algorithm called EM. And EM is just our assign-and-update dance, made soft. The E-step replaces hard assignments with responsibilities — the posterior probability that a patient belongs to each cluster, which is Bayes' rule from Module 4, running inside the loop. The M-step updates each Gaussian's parameters by weighted maximum likelihood — that's Module 3, inside the loop. And the punchline: k-means is exactly the limiting case where you shrink every cluster's covariance down to a tiny sphere. Hard assignment is just soft assignment with the uncertainty squeezed out.

## Clusters are not diagnoses

And now the payoff slide — the one I most want you to walk out with. Let's take those three adiposity clusters, which never saw a single blood-pressure measurement, and color them by the hypertension label we held back. Here's the hypertension rate inside each cluster: about thirty percent in the low-adiposity group, forty in the middle, forty-eight in the high — against an overall prevalence of thirty-nine, the dashed line. Two things are true at once, and you must hold both. The enrichment is real: risk genuinely climbs across the clusters, and the clusters never cheated — they obeyed the leakage rule from Module 1, never touching blood pressure. But no cluster is anywhere near pure — not one is close to zero or a hundred percent. In the accent color: pretending these clusters are diagnoses would manufacture labels the data never actually made. That's Project 2's honesty requirement, in a single figure. Descriptive tools describe; they do not diagnose.

## Live demo: the k-means explorer

Let's drive k-means by hand. The tool plots patients with no labels — BMI across the bottom, fasting glucose up the side — and asks you to find subtypes. Set the number of clusters, k, in the box. Then you can literally grab the centroids and drag them to seed their starting positions — and this is where you can make trouble on purpose: bunch them all in one corner. Now step it. The "Step" button alternates between the two phases — first "assign," snapping every patient to its nearest centroid, then it flips to "update," moving each centroid to the mean of its members — and you can watch the distortion readout drop with each step, and the "converged" flag flip once nothing moves. Or hit "Run to convergence" to fast-forward. Here's the demonstration I want: seed them badly, run to convergence, and note the distortion — you've trapped it in a bad local optimum. Then hit "New centroids" to reseed randomly and run again — a different, lower distortion. That's the restart lesson, live. "Reset" starts over.

> [cue: interact directly on the full-bleed slide — set k → drag centroids to a bad start → Step (assign ⇄ update) or Run to convergence (watch distortion) → New centroids to escape the local optimum → Reset; the adiposity-plane snapshot on the next slide is the PDF fallback if the embed can't load]

## Explorer — static fallback

For print or PDF, or if the embed doesn't load, this snapshot stands in — the three-cluster k-means result on the NHANES adiposity plane, centroids marked. Live in class, we drive the explorer itself on the slide before; there's nothing new to learn here.

> [cue: optional — skip aloud if the live embed worked; this slide exists only for print and PDF]

## Recap & bridge

Recapping k-means. Assign and update on the distortion loss; it converges, but only to a local optimum — so restart and keep the best. K and the feature scaling are both choices you make and defend; the elbow suggests, you decide. The Gaussian mixture is the soft, probabilistic upgrade, and k-means is its shrunk-covariance limit. And the one to tattoo on your arm: clusters are not labels — real enrichment, from thirty up to forty-eight percent, but no purity anywhere. In the accent color, Module 7 asks the other unsupervised question. Not "which groups do the patients form?" but "which directions among the features actually matter?" That's PCA — and it's where the whole course comes together.
