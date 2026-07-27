"""Day 20 — Optimisation theory
Concept 7: Newton's method and why we rarely use it

Run:  python 07_newton_s_method_and_why_we_rarely_use_it.py
"""

import numpy as np

def loss(w):
    return (w - 3) ** 2 + 1        # convex bowl, minimum at w=3

w, lr = 0.0, 0.1
for step in range(30):
    grad = 2 * (w - 3)
    w -= lr * grad
print(f'converged to w={w:.4f}, loss={loss(w):.4f}')

# ---------------------------------------------------------------------
# Remember: If the loss oscillates or explodes, halve the learning rate before changing anything else.
# Common mistake: Blaming the model architecture for what is really a learning rate ten times too large.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
