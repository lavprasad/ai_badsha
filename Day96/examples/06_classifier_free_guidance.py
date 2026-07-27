"""Day 96 — Diffusion models
Concept 6: Classifier-free guidance

Run:  python 06_classifier_free_guidance.py
"""

import numpy as np

rng = np.random.default_rng(0)
image = np.ones(8) * 0.5
betas = np.linspace(1e-4, 0.02, 10)   # noise schedule

x = image.copy()
for t, b in enumerate(betas):
    x = np.sqrt(1 - b) * x + np.sqrt(b) * rng.normal(size=x.shape)
print('after forward diffusion:', x.round(2))
print('Reverse process = a network predicting the noise added at each step.')

# ---------------------------------------------------------------------
# Remember: More sampling steps means better quality and linearly more compute — that is the whole trade.
# Common mistake: Assuming generated images are free of copyright or bias concerns because 'the model made them'.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
