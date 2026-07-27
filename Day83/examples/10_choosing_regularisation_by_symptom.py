"""Day 83 — Regularisation in deep nets
Concept 10: Choosing regularisation by symptom

Run:  python 10_choosing_regularisation_by_symptom.py
"""

import numpy as np
from sklearn.linear_model import Ridge, Lasso
from sklearn.datasets import make_regression

X, y = make_regression(n_samples=200, n_features=20, n_informative=5, noise=10, random_state=0)

ridge = Ridge(alpha=1.0).fit(X, y)
lasso = Lasso(alpha=1.0).fit(X, y)
print('ridge non-zero coefs', int(np.sum(np.abs(ridge.coef_) > 1e-6)))
print('lasso non-zero coefs', int(np.sum(np.abs(lasso.coef_) > 1e-6)))

# ---------------------------------------------------------------------
# Remember: Scale features before regularising, or the penalty punishes whichever column happens to use small units.
# Common mistake: Tuning `alpha` on the test set — pick it with cross-validation on train only.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
