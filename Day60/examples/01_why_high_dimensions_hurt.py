"""Day 60 — Dimensionality reduction
Concept 1: Why high dimensions hurt

Run:  python 01_why_high_dimensions_hurt.py
"""

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_digits
import numpy as np

X, y = load_digits(return_X_y=True)
Xs = StandardScaler().fit_transform(X)
pca = PCA(n_components=0.95, random_state=0).fit(Xs)   # keep 95% of variance
print(f'{X.shape[1]} dims -> {pca.n_components_} dims, variance kept {pca.explained_variance_ratio_.sum():.3f}')

# ---------------------------------------------------------------------
# Remember: `n_components=0.95` lets PCA pick the count for you by variance target.
# Common mistake: Running PCA before scaling, so one wide-range column becomes component 1 all by itself.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
