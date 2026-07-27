"""Day 103 — Neural network design decisions
Concept 3: Skip connections by default

Run:  python 03_skip_connections_by_default.py
"""

import numpy as np

def clip_by_norm(grads, max_norm=1.0):
    total = np.sqrt(sum(float((g ** 2).sum()) for g in grads))
    if total <= max_norm:
        return grads, total
    scale = max_norm / (total + 1e-6)
    return [g * scale for g in grads], total

grads = [np.array([10.0, 20.0]), np.array([30.0])]
clipped, before = clip_by_norm(grads)
print('norm before', round(before, 2))
print('norm after ', round(float(np.sqrt(sum((g ** 2).sum() for g in clipped))), 2))

# ---------------------------------------------------------------------
# Remember: Log the gradient norm during training — a sudden spike explains a sudden loss spike.
# Common mistake: Chasing an architecture change when a `clip_grad_norm_(1.0)` would have fixed the instability.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
