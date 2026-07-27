"""Day 110 — Video understanding
Concept 6: Temporal models over frame features

Run:  python 06_temporal_models_over_frame_features.py
"""

def sample_frames(total_frames, fps, target_fps=2):
    """Indices of frames to keep — full-rate video is almost never necessary."""
    step = max(1, round(fps / target_fps))
    return list(range(0, total_frames, step))

keep = sample_frames(total_frames=900, fps=30, target_fps=2)
print(f'900 frames at 30fps -> {len(keep)} sampled frames ({len(keep)/900:.1%} of the work)')

def iou(a, b):
    x1, y1 = max(a[0], b[0]), max(a[1], b[1])
    x2, y2 = min(a[2], b[2]), min(a[3], b[3])
    inter = max(0, x2 - x1) * max(0, y2 - y1)
    ua = (a[2]-a[0])*(a[3]-a[1]) + (b[2]-b[0])*(b[3]-b[1]) - inter
    return inter / ua
print('same object across frames?', iou((10,10,50,50), (12,11,52,51)) > 0.5)

# ---------------------------------------------------------------------
# Remember: Sample frames to the lowest rate that still answers the question — it is the biggest cost lever in video.
# Common mistake: Processing every frame of 30fps footage when 2fps would have given the same answer for 1/15th the cost.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
