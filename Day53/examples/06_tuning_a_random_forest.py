"""Day 53 — Ensembles: bagging and random forests
Concept 6: Tuning a random forest

Run:  python 06_tuning_a_random_forest.py
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score

X, y = load_breast_cancer(return_X_y=True)
rf = RandomForestClassifier(n_estimators=300, min_samples_leaf=2, n_jobs=-1, random_state=0)
print('cv accuracy', cross_val_score(rf, X, y, cv=5).mean().round(4))

rf.fit(X, y)
top = sorted(zip(load_breast_cancer().feature_names, rf.feature_importances_), key=lambda t: -t[1])[:5]
print('top features', [(n, round(v, 3)) for n, v in top])

# ---------------------------------------------------------------------
# Remember: More trees never overfit — they only cost time. Depth and leaf size are the knobs that control fit.
# Common mistake: Using impurity-based importances for business decisions instead of permutation importance.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
