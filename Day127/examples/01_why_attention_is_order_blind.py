"""Day 127 — Positional information
Concept 1: Why attention is order-blind

Run:  python 01_why_attention_is_order_blind.py
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
