"""Day 123 — Word embeddings
Concept 9: Static vs contextual embeddings

Run:  python 09_static_vs_contextual_embeddings.py
"""

import numpy as np

# Toy 3-D 'embeddings' to show the mechanics
vecs = {
    'king':  np.array([0.9, 0.8, 0.1]),
    'queen': np.array([0.9, 0.1, 0.8]),
    'man':   np.array([0.4, 0.9, 0.1]),
    'woman': np.array([0.4, 0.1, 0.9]),
}

def cos(a, b):
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))

analogy = vecs['king'] - vecs['man'] + vecs['woman']
best = max(vecs, key=lambda w: cos(analogy, vecs[w]) if w != 'king' else -1)
print('king - man + woman ~', best)

# ---------------------------------------------------------------------
# Remember: Normalise embeddings, then cosine similarity is just a dot product — much faster at scale.
# Common mistake: Mixing vectors from two different embedding models in one index; the spaces are unrelated.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
