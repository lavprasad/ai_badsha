"""Day 156 — Vector databases
Concept 9: Index rebuild and update costs

Run:  python 09_index_rebuild_and_update_costs.py
"""

import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 4.0, 6.0])

print('dot   ', a @ b)
print('norm  ', np.linalg.norm(a))
cos = (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))
print('cosine', cos)   # 1.0 -> same direction

# ---------------------------------------------------------------------
# Remember: Cosine similarity ignores magnitude; Euclidean distance does not. Pick the one that matches your question.
# Common mistake: Comparing raw embeddings with Euclidean distance when only direction carries meaning.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
