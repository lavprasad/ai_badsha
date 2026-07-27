"""Day 65 — Recommender systems
Concept 7: Popularity bias and feedback loops

Run:  python 07_popularity_bias_and_feedback_loops.py
"""

import numpy as np

R = np.array([
    [5, 3, 0, 1],
    [4, 0, 0, 1],
    [1, 1, 0, 5],
    [0, 0, 5, 4],
], dtype=float)
mask = R > 0

rng = np.random.default_rng(0)
U, V = rng.normal(size=(4, 2)) * 0.1, rng.normal(size=(4, 2)) * 0.1
for _ in range(3000):
    err = (U @ V.T - R) * mask
    U -= 0.02 * (err @ V + 0.05 * U)
    V -= 0.02 * (err.T @ U + 0.05 * V)
print((U @ V.T).round(2))

# ---------------------------------------------------------------------
# Remember: Evaluate recommenders with ranking metrics (precision@k, NDCG), not RMSE on ratings.
# Common mistake: Building a feedback loop that only ever recommends what it already recommended.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
