"""Day 59 — Unsupervised learning: clustering
Concept 10: Customer segmentation walkthrough

Run:  python 10_customer_segmentation_walkthrough.py
"""

import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score

X, _ = make_blobs(n_samples=500, centers=4, random_state=0)
for k in range(2, 7):
    km = KMeans(n_clusters=k, n_init=10, random_state=0).fit(X)
    print(f'k={k}  inertia={km.inertia_:8.1f}  silhouette={silhouette_score(X, km.labels_):.3f}')

# ---------------------------------------------------------------------
# Remember: Silhouette near 1 means tight, well-separated clusters; near 0 means the boundaries are arbitrary.
# Common mistake: Reading cluster IDs as meaningful labels — they are arbitrary and change between runs.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
