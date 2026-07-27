"""Day 92 — Sequence models: RNNs
Concept 2: The recurrent cell and hidden state

Run:  python 02_the_recurrent_cell_and_hidden_state.py
"""

import numpy as np

def rnn_forward(xs, Wx, Wh, b):
    h = np.zeros(Wh.shape[0])
    states = []
    for x in xs:
        h = np.tanh(Wx @ x + Wh @ h + b)   # state carries forward
        states.append(h.copy())
    return np.array(states)

rng = np.random.default_rng(0)
xs = rng.normal(size=(5, 3))
states = rnn_forward(xs, rng.normal(size=(4, 3)) * 0.3, rng.normal(size=(4, 4)) * 0.3, np.zeros(4))
print('states shape', states.shape)

# ---------------------------------------------------------------------
# Remember: RNNs are inherently sequential — they cannot parallelise across time, which is why transformers won.
# Common mistake: Feeding unsorted variable-length sequences without padding masks, so padding tokens pollute the state.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
