"""Day 168 — Data flywheels
Concept 4: Active learning: label what is uncertain

Run:  python 04_active_learning_label_what_is_uncertain.py
"""

import numpy as np

def select_for_labelling(probs, budget=5):
    """Label where the model is least certain — uncertainty sampling."""
    margin = np.abs(probs - 0.5)
    return np.argsort(margin)[:budget]

rng = np.random.default_rng(0)
probs = rng.random(20)
pick = select_for_labelling(probs)
print('label these rows first:', pick)
print('their probabilities    :', probs[pick].round(3))
print('\n50 uncertain labels beat 5000 random ones.')

# ---------------------------------------------------------------------
# Remember: Capture the correction, not just the thumbs-down. 'What should it have said' is the training signal.
# Common mistake: Shipping without logging, then having no data to improve on after three months of traffic.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
