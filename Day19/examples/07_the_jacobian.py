"""Day 19 — Calculus: derivatives and gradients
Concept 7: The Jacobian

Run:  python 07_the_jacobian.py
"""

import numpy as np

def f(x):
    return x ** 2 + 3 * x

def numeric_grad(fn, x, h=1e-6):
    return (fn(x + h) - fn(x - h)) / (2 * h)

x = 2.0
print('numeric  ', numeric_grad(f, x))
print('analytic ', 2 * x + 3)   # should match to ~1e-6

# ---------------------------------------------------------------------
# Remember: A central difference `(f(x+h)-f(x-h))/2h` is the cheapest way to check a hand-written gradient.
# Common mistake: Trusting a derivation you never gradient-checked; a sign error trains slowly instead of failing loudly.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
