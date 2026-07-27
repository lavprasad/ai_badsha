"""Day 61 — Anomaly detection
Concept 4: One-class SVM

Run:  python 04_one_class_svm.py
"""

from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons
from sklearn.model_selection import cross_val_score

X, y = make_moons(n_samples=500, noise=0.2, random_state=0)
linear = make_pipeline(StandardScaler(), SVC(kernel='linear'))
rbf = make_pipeline(StandardScaler(), SVC(kernel='rbf', C=1.0, gamma='scale'))
print('linear', cross_val_score(linear, X, y, cv=5).mean().round(3))
print('rbf   ', cross_val_score(rbf, X, y, cv=5).mean().round(3))

# ---------------------------------------------------------------------
# Remember: SVMs scale roughly quadratically with rows — above ~100k samples reach for boosting instead.
# Common mistake: Skipping feature scaling, which silently wrecks the RBF kernel.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
