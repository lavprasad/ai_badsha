"""Day 94 — Autoencoders
Concept 7: Variational autoencoders

Run:  python 07_variational_autoencoders.py
"""

import numpy as np

# Linear autoencoder == PCA. Reconstruction error flags anomalies.
rng = np.random.default_rng(0)
normal = rng.normal(size=(500, 10))
U, S, Vt = np.linalg.svd(normal - normal.mean(0), full_matrices=False)
code = Vt[:3]                              # 3-D bottleneck

def recon_error(x):
    z = (x - normal.mean(0)) @ code.T
    return float(np.linalg.norm((x - normal.mean(0)) - z @ code))

print('normal point ', round(recon_error(normal[0]), 3))
print('anomaly      ', round(recon_error(np.full(10, 12.0)), 3))

# ---------------------------------------------------------------------
# Remember: Reconstruction error is a ready-made anomaly score — no labels required.
# Common mistake: Making the bottleneck as wide as the input, so the network learns the identity function.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
