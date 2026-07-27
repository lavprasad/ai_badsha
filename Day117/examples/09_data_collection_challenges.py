"""Day 117 — 3D and depth
Concept 9: Data collection challenges

Run:  python 09_data_collection_challenges.py
"""

import numpy as np

# Depth from stereo disparity: Z = f * B / d
focal_px, baseline_m = 700.0, 0.12
for disparity in (5, 20, 90):
    z = focal_px * baseline_m / disparity
    print(f'disparity {disparity:>3} px -> depth {z:6.2f} m')

# Permutation invariance: max-pool over points, PointNet-style
pts = np.random.default_rng(0).normal(size=(100, 3))
feat_a = pts.max(axis=0)
feat_b = pts[np.random.default_rng(1).permutation(100)].max(axis=0)
print('order-independent feature:', np.allclose(feat_a, feat_b))

# ---------------------------------------------------------------------
# Remember: Stereo depth error grows with the square of distance — far objects are barely measurable.
# Common mistake: Feeding a point cloud to a model that depends on point order and getting different answers per run.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
