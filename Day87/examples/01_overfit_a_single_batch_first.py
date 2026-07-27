"""Day 87 — Debugging neural networks
Concept 1: Overfit a single batch first

Run:  python 01_overfit_a_single_batch_first.py
"""

import numpy as np

def sanity_report(X, y, n_classes):
    print('shapes        ', X.shape, y.shape)
    print('nan in X      ', bool(np.isnan(X).any()))
    const = [i for i in range(X.shape[1]) if np.std(X[:, i]) == 0]
    print('constant cols ', const)
    counts = np.bincount(y, minlength=n_classes)
    print('class counts  ', counts)
    print('expected loss at init ~', round(float(np.log(n_classes)), 4))

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 5)); X[:, 2] = 1.0     # planted constant column
sanity_report(X, rng.integers(0, 3, 200), 3)

# ---------------------------------------------------------------------
# Remember: Expected cross-entropy at initialisation is ln(n_classes). A different value means a wiring bug.
# Common mistake: Tuning hyperparameters for two days on a pipeline whose labels were misaligned by one row.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
