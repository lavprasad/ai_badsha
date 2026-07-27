"""Day 27 — Linear algebra in practice
Concept 2: Feature scaling as a linear map

Run:  python 02_feature_scaling_as_a_linear_map.py
"""

import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
pipe = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
print('cv accuracy', cross_val_score(pipe, X, y, cv=5).mean().round(4))

# ---------------------------------------------------------------------
# Remember: Put the scaler INSIDE a Pipeline so cross-validation refits it per fold and cannot leak.
# Common mistake: Calling `fit_transform` on the full dataset before splitting — classic, silent, score-inflating leak.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
