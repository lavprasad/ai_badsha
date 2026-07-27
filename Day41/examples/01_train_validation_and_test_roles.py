"""Day 41 — Data splitting done right
Concept 1: Train, validation and test roles

Run:  python 01_train_validation_and_test_roles.py
"""

import numpy as np
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit, GroupShuffleSplit

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 3))
y = (rng.random(200) < 0.1).astype(int)      # 10% positive
groups = rng.integers(0, 40, size=200)       # 40 customers

_, _, ytr, yte = train_test_split(X, y, test_size=0.3, stratify=y, random_state=0)
print('stratified positive rate  train %.3f  test %.3f' % (ytr.mean(), yte.mean()))

tr, te = next(GroupShuffleSplit(test_size=0.3, random_state=0).split(X, y, groups))
print('group overlap (must be 0):', len(set(groups[tr]) & set(groups[te])))

# ---------------------------------------------------------------------
# Remember: One entity must live on exactly one side of the split. Check the overlap; do not assume it.
# Common mistake: A random split on data with repeated customers, so the model recognises the customer, not the pattern.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
