"""Day 49 — Regression metrics and residuals
Concept 9: Prediction intervals

Run:  python 09_prediction_intervals.py
"""

import numpy as np

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 1))
y = 3.0 * X[:, 0] + 2.0 + rng.normal(scale=0.5, size=200)

Xb = np.c_[np.ones(len(X)), X]                 # add bias column
w = np.linalg.lstsq(Xb, y, rcond=None)[0]      # solves the normal equations safely
print(f'intercept {w[0]:.3f}  slope {w[1]:.3f}')

resid = y - Xb @ w
print('residual mean (should be ~0):', round(float(resid.mean()), 6))

# ---------------------------------------------------------------------
# Remember: Plot residuals against predictions — any visible pattern means the linear form is wrong.
# Common mistake: Reporting R² on training data and calling it model performance.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
