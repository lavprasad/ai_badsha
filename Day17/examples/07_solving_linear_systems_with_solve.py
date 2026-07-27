"""Day 17 — Matrices and linear transformations
Concept 7: Solving linear systems with solve

Run:  python 07_solving_linear_systems_with_solve.py
"""

import numpy as np

rng = np.random.default_rng(0)
A = rng.normal(size=(500, 500)) + np.eye(500) * 5
b = rng.normal(size=500)

x_solve = np.linalg.solve(A, b)
x_inv = np.linalg.inv(A) @ b
print('same answer:', np.allclose(x_solve, x_inv))
print('residual solve:', float(np.linalg.norm(A @ x_solve - b)))
print('residual inv  :', float(np.linalg.norm(A @ x_inv - b)))

# ---------------------------------------------------------------------
# Remember: `np.linalg.solve(A, b)` over `inv(A) @ b`, always.
# Common mistake: Densifying a sparse TF-IDF matrix with `.toarray()` and exhausting memory.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
