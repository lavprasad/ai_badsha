"""Day 144 — Knowledge in language models
Concept 4: Knowledge graphs alongside LLMs

Run:  python 04_knowledge_graphs_alongside_llms.py
"""

import numpy as np

# One round of mean-aggregation message passing
A = np.array([[0, 1, 1, 0],
              [1, 0, 1, 0],
              [1, 1, 0, 1],
              [0, 0, 1, 0]], dtype=float)
H = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0], [0.5, 0.5]])

deg = A.sum(axis=1, keepdims=True)
H_next = np.tanh((A @ H) / np.maximum(deg, 1))
print(H_next.round(3))

# ---------------------------------------------------------------------
# Remember: Too many message-passing layers causes over-smoothing — every node converges to the same vector.
# Common mistake: Splitting graph data randomly so a node's own neighbours end up in both train and test.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
