"""Day 176 — Testing machine learning code
Concept 10: A test suite you actually run

Run:  python 10_a_test_suite_you_actually_run.py
"""

import numpy as np

def predict(x, w):
    return float(x @ w)

def test_metamorphic_scaling():
    """Doubling all inputs must double a linear prediction."""
    w = np.array([2.0, -1.0])
    x = np.array([3.0, 4.0])
    assert abs(predict(2 * x, w) - 2 * predict(x, w)) < 1e-9

def test_deterministic():
    """Same seed, same result — or your test suite will flake forever."""
    a = np.random.default_rng(42).normal(size=5)
    b = np.random.default_rng(42).normal(size=5)
    assert np.allclose(a, b)

test_metamorphic_scaling()
test_deterministic()
print('all tests passed')

# ---------------------------------------------------------------------
# Remember: Every test that touches randomness must pass an explicit seed. Global seeding is not enough under parallelism.
# Common mistake: A test suite so slow that CI skips it and bugs reach production anyway.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
