"""Day 77 — Activation functions
Concept 5: Leaky ReLU and PReLU

Run:  python 05_leaky_relu_and_prelu.py
"""

import numpy as np

def softmax(z):
    z = z - z.max(axis=-1, keepdims=True)   # subtract max for numerical stability
    e = np.exp(z)
    return e / e.sum(axis=-1, keepdims=True)

logits = np.array([2.0, 1.0, 0.1])
print('softmax', softmax(logits).round(4), 'sums to', softmax(logits).sum())
print('relu   ', np.maximum(0, np.array([-1.0, 0.0, 2.0])))

# ---------------------------------------------------------------------
# Remember: Always subtract the max before `exp` in softmax, or large logits overflow to inf/NaN.
# Common mistake: Putting a softmax on the final layer AND using a loss that applies softmax internally.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
