"""Day 56 — Model selection and validation strategy
Concept 6: The one-standard-error rule

Run:  python 06_the_one_standard_error_rule.py
"""

import numpy as np
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
cv = StratifiedKFold(5, shuffle=True, random_state=0)   # identical folds for both

for name, model in [
    ('logreg', make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000))),
    ('forest', RandomForestClassifier(n_estimators=300, random_state=0)),
]:
    s = cross_val_score(model, X, y, cv=cv)
    print(f'{name}: {s.mean():.4f} +/- {s.std():.4f}   folds {s.round(3)}')

# ---------------------------------------------------------------------
# Remember: Use the same `cv` object for every candidate, or you are comparing luck.
# Common mistake: Declaring a winner from a difference smaller than the standard error across folds.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
