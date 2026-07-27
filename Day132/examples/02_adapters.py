"""Day 132 — Parameter-efficient fine-tuning
Concept 2: Adapters

Run:  python 02_adapters.py
"""

from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
import numpy as np

X, y = load_breast_cancer(return_X_y=True)
space = {
    'n_estimators': [100, 300, 600],
    'max_depth': [None, 4, 8, 16],
    'min_samples_leaf': [1, 2, 4, 8],
}
search = RandomizedSearchCV(
    RandomForestClassifier(random_state=0, n_jobs=-1),
    space, n_iter=12, cv=5, random_state=0,
).fit(X, y)
print(search.best_params_, round(search.best_score_, 4))

# ---------------------------------------------------------------------
# Remember: Fix the random seed and log every trial, or you cannot reproduce your own best model.
# Common mistake: Tuning 40 hyperparameters on 400 rows — you are now fitting the validation set.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
