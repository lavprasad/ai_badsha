"""Day 112 — Self-supervised vision
Concept 3: MoCo and memory banks

Run:  python 03_moco_and_memory_banks.py
"""

import numpy as np

def nt_xent(z1, z2, temperature=0.5):
    """Contrastive loss: two views of the same item should be closest to each other."""
    z1 = z1 / np.linalg.norm(z1, axis=1, keepdims=True)
    z2 = z2 / np.linalg.norm(z2, axis=1, keepdims=True)
    sim = z1 @ z2.T / temperature
    sim -= sim.max(axis=1, keepdims=True)
    p = np.exp(sim) / np.exp(sim).sum(axis=1, keepdims=True)
    return float(-np.mean(np.log(np.diag(p) + 1e-12)))

rng = np.random.default_rng(0)
base = rng.normal(size=(8, 16))
print('aligned views loss  ', round(nt_xent(base, base + 0.01 * rng.normal(size=base.shape)), 4))
print('unrelated views loss', round(nt_xent(base, rng.normal(size=(8, 16))), 4))

# ---------------------------------------------------------------------
# Remember: The augmentations *are* the supervision — they define what the model learns to treat as irrelevant.
# Common mistake: Spending weeks on self-supervised pretraining when a public pretrained backbone was already better.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
