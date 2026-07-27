"""Day 64 — Ensembling your own models
Concept 5: Stacking with a meta-learner

Run:  python 05_stacking_with_a_meta_learner.py
"""

import numpy as np

rng = np.random.default_rng(0)
x = rng.integers(0, 100, size=10)
print('data      ', x)

mask = x > 50
print('mask      ', mask)
print('selected  ', x[mask])                 # boolean mask
print('positions ', x[[0, 3, 5]])            # fancy indexing
print('clipped   ', np.where(x > 50, 50, x)) # conditional build

order = np.argsort(-x)
print('top 3     ', x[order[:3]])

# ---------------------------------------------------------------------
# Remember: A boolean mask returns a copy; a basic slice returns a view. Mutating one does not affect the other the same way.
# Common mistake: Chaining `arr[mask][0] = 5` and wondering why the original array never changed — you wrote to a copy.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
