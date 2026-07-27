"""Day 70 — Working with images, classically
Concept 8: Data augmentation before deep learning

Run:  python 08_data_augmentation_before_deep_learning.py
"""

import numpy as np

def dropout(x, p=0.5, training=True, rng=None):
    if not training or p == 0:
        return x
    rng = rng or np.random.default_rng(0)
    mask = (rng.random(x.shape) > p) / (1 - p)   # inverted dropout: scale at train time
    return x * mask

x = np.ones((2, 6))
print(dropout(x, p=0.5).round(2))
print(dropout(x, training=False))   # unchanged at inference

# ---------------------------------------------------------------------
# Remember: Inverted dropout scales during training so inference needs no change at all.
# Common mistake: Leaving dropout active at inference and getting different predictions on every call.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
