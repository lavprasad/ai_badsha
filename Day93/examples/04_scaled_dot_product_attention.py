"""Day 93 — Attention mechanisms
Concept 4: Scaled dot-product attention

Run:  python 04_scaled_dot_product_attention.py
"""

import numpy as np

def softmax(z):
    z = z - z.max(axis=-1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=-1, keepdims=True)

rng = np.random.default_rng(0)
seq, d = 4, 8
Q, K, V = (rng.normal(size=(seq, d)) for _ in range(3))

scores = Q @ K.T / np.sqrt(d)             # scale keeps softmax out of saturation
mask = np.triu(np.ones((seq, seq)), k=1) * -1e9   # causal: no peeking ahead
weights = softmax(scores + mask)
print(weights.round(3))
print('output shape', (weights @ V).shape)

# ---------------------------------------------------------------------
# Remember: The 1/sqrt(d) scale is not cosmetic — without it softmax saturates and gradients die.
# Common mistake: Omitting the causal mask in a decoder, so the model trivially cheats by reading the next token.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
