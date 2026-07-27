"""Day 188 — AI system architecture
Concept 8: Build vs buy per component

Run:  python 08_build_vs_buy_per_component.py
"""

import numpy as np

def positional_encoding(seq_len, d_model):
    pos = np.arange(seq_len)[:, None]
    i = np.arange(d_model)[None, :]
    angle = pos / np.power(10_000, (2 * (i // 2)) / d_model)
    pe = np.zeros((seq_len, d_model))
    pe[:, 0::2] = np.sin(angle[:, 0::2])
    pe[:, 1::2] = np.cos(angle[:, 1::2])
    return pe

pe = positional_encoding(6, 8)
print(pe.round(2))
print('shape', pe.shape)

# ---------------------------------------------------------------------
# Remember: Block = LayerNorm -> Attention -> add residual -> LayerNorm -> MLP -> add residual. Memorise it.
# Common mistake: Assuming a bigger context window is free — attention cost grows with the square of sequence length.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
