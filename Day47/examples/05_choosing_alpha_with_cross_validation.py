"""Day 47 — Regularised linear models
Concept 5: Choosing alpha with cross-validation

Run:  python 05_choosing_alpha_with_cross_validation.py
"""

from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, StratifiedKFold

X, y = load_wine(return_X_y=True)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
scores = cross_val_score(RandomForestClassifier(random_state=0), X, y, cv=cv)
print('folds', scores.round(3))
print(f'mean {scores.mean():.3f} +/- {scores.std():.3f}')

# ---------------------------------------------------------------------
# Remember: Report the spread across folds, not just the mean — high variance means you cannot trust the mean.
# Common mistake: Random K-fold on time-series or on grouped data (same patient in train and test) — both leak.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
