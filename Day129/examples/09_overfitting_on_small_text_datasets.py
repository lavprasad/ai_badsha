"""Day 129 — Fine-tuning encoder models
Concept 9: Overfitting on small text datasets

Run:  python 09_overfitting_on_small_text_datasets.py
"""

import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=800, n_informative=5, random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0)

for depth in (1, 3, 8, None):
    m = DecisionTreeClassifier(max_depth=depth, random_state=0).fit(Xtr, ytr)
    print(f'depth={str(depth):>4}  train={m.score(Xtr, ytr):.3f}  test={m.score(Xte, yte):.3f}')

# ---------------------------------------------------------------------
# Remember: Train 1.00 / test 0.70 is overfitting. Train 0.70 / test 0.69 is underfitting. Fix the right one.
# Common mistake: Adding capacity to fix a gap that was caused by too little data or a leak, not by too little capacity.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
