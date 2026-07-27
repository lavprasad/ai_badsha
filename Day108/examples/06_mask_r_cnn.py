"""Day 108 — Image segmentation
Concept 6: Mask R-CNN

Run:  python 06_mask_r_cnn.py
"""

import numpy as np

image = np.array([
    [0, 0, 1, 1],
    [0, 0, 1, 1],
    [0, 0, 1, 1],
    [0, 0, 1, 1],
], dtype=float)
kernel = np.array([[-1, 1], [-1, 1]], dtype=float)   # vertical edge detector

h, w = image.shape[0] - 1, image.shape[1] - 1
out = np.zeros((h, w))
for i in range(h):
    for j in range(w):
        out[i, j] = float((image[i:i + 2, j:j + 2] * kernel).sum())
print(out)   # the edge column lights up

# ---------------------------------------------------------------------
# Remember: Output size = (in - kernel + 2*pad)/stride + 1. Print shapes when a layer refuses to connect.
# Common mistake: Forgetting the channel dimension and feeding (H,W) where the layer expects (N,C,H,W).
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
