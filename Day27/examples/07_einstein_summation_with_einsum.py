"""Day 27 — Linear algebra in practice
Concept 7: Einstein summation with einsum

Run:  python 07_einstein_summation_with_einsum.py
"""

import numpy as np

A = np.random.default_rng(0).normal(size=(4, 5))
B = np.random.default_rng(1).normal(size=(5, 3))

print(np.allclose(A @ B, np.einsum('ik,kj->ij', A, B)))
print('batched trace:', np.einsum('ii->', A @ A.T).round(3))

small = A.astype(np.float32)
print('float64 bytes', A.nbytes, '| float32 bytes', small.nbytes)

# ---------------------------------------------------------------------
# Remember: Train in float32 (or bf16); reserve float64 for numerically delicate accumulations.
# Common mistake: Mixing float32 and float64 accidentally and silently doubling memory across a pipeline.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
