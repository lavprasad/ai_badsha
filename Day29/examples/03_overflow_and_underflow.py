"""Day 29 — Numerical computing pitfalls
Concept 3: Overflow and underflow

Run:  python 03_overflow_and_underflow.py
"""

import numpy as np

print(0.1 + 0.2 == 0.3, 0.1 + 0.2)          # False — welcome to floats

def logsumexp(x):
    m = np.max(x)
    return m + np.log(np.sum(np.exp(x - m)))   # never exp() a big number directly

big = np.array([1000.0, 1001.0, 1002.0])
print('naive :', np.log(np.sum(np.exp(big))))  # inf
print('stable:', logsumexp(big))

def safe_ratio(a, b, eps=1e-12):
    return a / (b + eps)
print(safe_ratio(1.0, 0.0))

# ---------------------------------------------------------------------
# Remember: Compare floats with a tolerance (`np.isclose`), never with `==`.
# Common mistake: Getting `nan` deep in training and only then discovering an `exp()` overflowed twelve steps earlier.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
