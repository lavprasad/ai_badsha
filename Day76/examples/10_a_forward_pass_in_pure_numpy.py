"""Day 76 — The artificial neuron
Concept 10: A forward pass in pure NumPy

Run:  python 10_a_forward_pass_in_pure_numpy.py
"""

import numpy as np

def relu(z):
    return np.maximum(0, z)

rng = np.random.default_rng(0)
x = rng.normal(size=(1, 4))
W1, b1 = rng.normal(size=(4, 8)) * 0.5, np.zeros(8)
W2, b2 = rng.normal(size=(8, 1)) * 0.5, np.zeros(1)

h = relu(x @ W1 + b1)
out = h @ W2 + b2
print('hidden', h.round(3))
print('output', out.round(3))

# ---------------------------------------------------------------------
# Remember: Depth without non-linearity is width. Check that every hidden layer has an activation.
# Common mistake: Initialising all weights to zero, so every neuron gets the same gradient and learns the same thing.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
