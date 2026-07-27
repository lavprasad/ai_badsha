"""Day 64 — Ensembling your own models
Concept 4: Weighted blending

Run:  python 04_weighted_blending.py
"""

import numpy as np
from sklearn.model_selection import cross_val_predict, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
cv = StratifiedKFold(5, shuffle=True, random_state=0)

base = [RandomForestClassifier(n_estimators=200, random_state=0),
        LogisticRegression(max_iter=5000)]
oof = np.column_stack([
    cross_val_predict(m, X, y, cv=cv, method='predict_proba')[:, 1] for m in base
])
print('correlation between members:', round(float(np.corrcoef(oof.T)[0, 1]), 3))
meta = LogisticRegression().fit(oof, y)
print('meta weights:', meta.coef_.round(3))

# ---------------------------------------------------------------------
# Remember: Stack on out-of-fold predictions only. In-fold predictions are a leak wearing a disguise.
# Common mistake: Shipping a five-model ensemble for a 0.2% gain and quintupling inference cost and failure modes.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
