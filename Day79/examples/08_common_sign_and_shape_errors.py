"""Day 79 — Backpropagation from scratch
Concept 8: Common sign and shape errors

Run:  python 08_common_sign_and_shape_errors.py
"""

import numpy as np

# y = (w*x + b)^2 ; d y/d w by hand
x, w, b = 2.0, 3.0, 1.0
z = w * x + b        # forward
y = z ** 2

dy_dz = 2 * z        # backward
dz_dw = x
dz_db = 1.0
print('dy/dw', dy_dz * dz_dw)   # 28.0
print('dy/db', dy_dz * dz_db)   # 14.0

h = 1e-6
print('numeric dy/dw', (((w + h) * x + b) ** 2 - ((w - h) * x + b) ** 2) / (2 * h))

# ---------------------------------------------------------------------
# Remember: Gradient-check any hand-written backward pass against a numeric estimate before trusting it.
# Common mistake: Forgetting to zero gradients between steps, so they accumulate and the model diverges.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
