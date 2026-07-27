"""Day 54 — Boosting
Concept 4: Learning rate and number of trees

Run:  python 04_learning_rate_and_number_of_trees.py
"""

import numpy as np

rng = np.random.default_rng(0)
X = rng.normal(size=(1000, 3))
true_w = np.array([1.0, -2.0, 0.5])
y = X @ true_w + rng.normal(scale=0.1, size=1000)

w, lr, batch = np.zeros(3), 0.1, 32
for epoch in range(20):
    idx = rng.permutation(len(X))
    for start in range(0, len(X), batch):
        b = idx[start:start + batch]
        grad = 2 * X[b].T @ (X[b] @ w - y[b]) / len(b)
        w -= lr * grad
print('learned', np.round(w, 3), 'target', true_w)

# ---------------------------------------------------------------------
# Remember: Shuffle every epoch, otherwise the model learns the order of your file.
# Common mistake: Leaving the learning rate fixed forever instead of decaying it once the loss plateaus.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
