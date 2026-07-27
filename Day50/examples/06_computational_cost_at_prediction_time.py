"""Day 50 — k-nearest neighbours
Concept 6: Computational cost at prediction time

Run:  python 06_computational_cost_at_prediction_time.py
"""

import numpy as np

def knn_predict(X_train, y_train, x, k=3):
    d = np.linalg.norm(X_train - x, axis=1)
    idx = np.argsort(d)[:k]
    vals, counts = np.unique(y_train[idx], return_counts=True)
    return vals[np.argmax(counts)]

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 2))
y = (X[:, 0] > 0).astype(int)
print('predicted', knn_predict(X, y, np.array([1.5, 0.0])), 'expected 1')

# ---------------------------------------------------------------------
# Remember: Scale your features first — kNN is pure distance, so units decide the answer.
# Common mistake: Using kNN on high-dimensional data where every point is roughly equidistant from every other.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
