"""Day 78 — Loss functions
Concept 9: Contrastive and triplet loss

Run:  python 09_contrastive_and_triplet_loss.py
"""

import numpy as np

def weighted_bce(y, p, w_pos=10.0, eps=1e-12):
    p = np.clip(p, eps, 1 - eps)
    return float(-np.mean(w_pos * y * np.log(p) + (1 - y) * np.log(1 - p)))

y = np.array([1.0, 0.0, 0.0, 1.0])
misses_positive = np.array([0.2, 0.1, 0.1, 0.3])
misses_negative = np.array([0.9, 0.8, 0.7, 0.9])
print('missing positives costs', round(weighted_bce(y, misses_positive), 3))
print('false alarms cost      ', round(weighted_bce(y, misses_negative), 3))

# ---------------------------------------------------------------------
# Remember: Encode the real cost of each error type in the loss or the threshold — the model cannot guess it.
# Common mistake: Optimising plain accuracy for a fraud model where a miss costs 10,000x a false alarm.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
