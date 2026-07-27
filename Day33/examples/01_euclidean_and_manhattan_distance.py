"""Day 33 — Distance, similarity and geometry
Concept 1: Euclidean and Manhattan distance

Run:  python 01_euclidean_and_manhattan_distance.py
"""

import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([4.0, 0.0, 3.0])
print('euclidean', round(float(np.linalg.norm(a - b)), 3))
print('manhattan', round(float(np.abs(a - b).sum()), 3))

s1, s2 = {'ml', 'ai', 'data'}, {'ai', 'data', 'stats'}
print('jaccard  ', round(len(s1 & s2) / len(s1 | s2), 3))

rng = np.random.default_rng(0)
for d in (2, 10, 100, 1000):
    pts = rng.normal(size=(200, d))
    dists = np.linalg.norm(pts[:100] - pts[100:], axis=1)
    print(f'dim {d:>4}: spread/mean = {dists.std() / dists.mean():.3f}')

# ---------------------------------------------------------------------
# Remember: As dimensions grow, the ratio of distance spread to mean shrinks — nearest neighbour stops meaning much.
# Common mistake: Using Euclidean distance on features with wildly different units and calling the result similarity.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
