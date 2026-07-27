"""Day 27 — Linear algebra in practice
Concept 6: Broadcasting pitfalls in real code

Run:  python 06_broadcasting_pitfalls_in_real_code.py
"""

import numpy as np

a = np.arange(6).reshape(2, 3)
print(a.shape, a.dtype)

b = np.array([10, 20, 30])       # shape (3,)
print(a + b)                     # broadcast over rows

print(a.sum(axis=0))             # column sums
print(a.sum(axis=1))             # row sums

# ---------------------------------------------------------------------
# Remember: `axis=0` collapses rows (down the columns); `axis=1` collapses columns (across a row).
# Common mistake: Looping over array elements in Python instead of using a vectorised operation.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
