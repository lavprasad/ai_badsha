"""Day 26 — Information theory
Concept 10: Computing all of these in NumPy

Run:  python 10_computing_all_of_these_in_numpy.py
"""

import numpy as np

def cross_entropy(p_true, p_pred, eps=1e-12):
    p_pred = np.clip(p_pred, eps, 1 - eps)
    return -np.sum(p_true * np.log(p_pred))

truth = np.array([0, 1, 0])              # class 1 is correct
confident = np.array([0.05, 0.90, 0.05])
unsure = np.array([0.33, 0.34, 0.33])
print('confident loss', round(cross_entropy(truth, confident), 3))
print('unsure loss   ', round(cross_entropy(truth, unsure), 3))
print('perplexity    ', round(float(np.exp(cross_entropy(truth, unsure))), 3))

# ---------------------------------------------------------------------
# Remember: Clip probabilities before `log` — `log(0)` is `-inf` and poisons the whole batch.
# Common mistake: Applying softmax twice (once in the model, once in the loss) and getting flat, untrainable gradients.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
