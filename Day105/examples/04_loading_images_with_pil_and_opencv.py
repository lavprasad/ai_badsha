"""Day 105 — Image fundamentals
Concept 4: Loading images with PIL and OpenCV

Run:  python 04_loading_images_with_pil_and_opencv.py
"""

import numpy as np

# 8x8 synthetic image: dark left half, bright right half
img = np.zeros((8, 8), dtype=float)
img[:, 4:] = 1.0
print('shape', img.shape, 'range', img.min(), img.max())

sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=float)
h, w = img.shape[0] - 2, img.shape[1] - 2
edges = np.zeros((h, w))
for i in range(h):
    for j in range(w):
        edges[i, j] = float((img[i:i + 3, j:j + 3] * sobel_x).sum())
print('vertical edge column found at x =', int(np.argmax(np.abs(edges).sum(axis=0))))

# ---------------------------------------------------------------------
# Remember: Check the channel order (RGB vs BGR) and the value range (0-255 vs 0-1) before every model call.
# Common mistake: Feeding BGR from OpenCV into a model trained on RGB and losing accuracy for no visible reason.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
