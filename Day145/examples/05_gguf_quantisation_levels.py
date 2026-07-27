"""Day 145 — Small models and local AI
Concept 5: GGUF quantisation levels

Run:  python 05_gguf_quantisation_levels.py
"""

import numpy as np

d, r = 512, 8                      # full dim vs LoRA rank
rng = np.random.default_rng(0)
W = rng.normal(size=(d, d)) * 0.02  # frozen base weight
A = rng.normal(size=(d, r)) * 0.01  # trainable
B = np.zeros((r, d))                # trainable, starts at zero -> no change at step 0

delta = A @ B
print('base params   ', W.size)
print('lora params   ', A.size + B.size, f'({100 * (A.size + B.size) / W.size:.1f}%)')
print('effective W = W + A@B, shape', (W + delta).shape)

# ---------------------------------------------------------------------
# Remember: Initialise B to zeros so the adapted model starts exactly equal to the base model.
# Common mistake: Setting rank far too high — you lose the efficiency and gain the overfitting.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
