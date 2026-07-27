"""Day 32 — Logistic regression, mathematically
Concept 3: Odds and log-odds interpretation

Run:  python 03_odds_and_log_odds_interpretation.py
"""

import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-np.clip(z, -500, 500)))

rng = np.random.default_rng(0)
X = rng.normal(size=(400, 2))
y = (X[:, 0] + X[:, 1] > 0).astype(float)

w, b, lr = np.zeros(2), 0.0, 0.5
for _ in range(500):
    p = sigmoid(X @ w + b)
    w -= lr * (X.T @ (p - y)) / len(y)
    b -= lr * float((p - y).mean())
print('weights', np.round(w, 2), 'acc', ((sigmoid(X @ w + b) > 0.5) == y).mean())

# ---------------------------------------------------------------------
# Remember: Clip the sigmoid input — `exp` of a large negative number overflows and returns NaN.
# Common mistake: Reading the raw output as a calibrated probability without ever checking a calibration curve.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
