"""Day 17 — Matrices and linear transformations
Concept 3: Identity and inverse matrices

Run:  python 03_identity_and_inverse_matrices.py
"""

import numpy as np

A = np.random.default_rng(0).normal(size=(3, 4))
B = np.random.default_rng(1).normal(size=(4, 2))

print((A @ B).shape)      # (3, 2)
print(A.T.shape)          # (4, 3)
print(np.eye(3) @ A is not A, np.allclose(np.eye(3) @ A, A))

# ---------------------------------------------------------------------
# Remember: Read every shape error as 'the inner dimensions did not match' and print the shapes.
# Common mistake: Reaching for `np.linalg.inv` to solve `Ax=b` instead of the numerically safer `np.linalg.solve`.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
