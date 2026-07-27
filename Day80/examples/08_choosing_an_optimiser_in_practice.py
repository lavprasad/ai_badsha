"""Day 80 — Optimisers
Concept 8: Choosing an optimiser in practice

Run:  python 08_choosing_an_optimiser_in_practice.py
"""

import numpy as np

# Adam on a 1-D bowl, from scratch
w, m, v = 5.0, 0.0, 0.0
lr, b1, b2, eps = 0.1, 0.9, 0.999, 1e-8
for t in range(1, 101):
    g = 2 * (w - 3)                       # gradient of (w-3)^2
    m = b1 * m + (1 - b1) * g
    v = b2 * v + (1 - b2) * g ** 2
    mhat = m / (1 - b1 ** t)
    vhat = v / (1 - b2 ** t)
    w -= lr * mhat / (np.sqrt(vhat) + eps)
print(f'w = {w:.4f} (target 3.0)')

# ---------------------------------------------------------------------
# Remember: Adam's default lr 1e-3 is a good start for scratch training; 1e-5 to 5e-5 for fine-tuning.
# Common mistake: Using the same learning rate for pretraining and fine-tuning and destroying the pretrained weights.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
