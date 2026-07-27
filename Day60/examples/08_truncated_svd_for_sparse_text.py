"""Day 60 — Dimensionality reduction
Concept 8: Truncated SVD for sparse text

Run:  python 08_truncated_svd_for_sparse_text.py
"""

import numpy as np

X = np.random.default_rng(0).normal(size=(100, 5))
U, S, Vt = np.linalg.svd(X, full_matrices=False)
print('singular values', np.round(S, 2))

energy = np.cumsum(S ** 2) / np.sum(S ** 2)
print('variance kept by first 2 dims:', round(float(energy[1]), 3))

# ---------------------------------------------------------------------
# Remember: Singular values sorted descending tell you how many dimensions actually carry information.
# Common mistake: Running PCA/SVD on unscaled features so the largest-unit column dominates every component.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
