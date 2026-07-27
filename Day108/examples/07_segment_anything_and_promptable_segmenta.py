"""Day 108 — Image segmentation
Concept 7: Segment Anything and promptable segmentation

Run:  python 07_segment_anything_and_promptable_segmenta.py
"""

def iou(a, b):
    """Boxes as (x1, y1, x2, y2)."""
    x1, y1 = max(a[0], b[0]), max(a[1], b[1])
    x2, y2 = min(a[2], b[2]), min(a[3], b[3])
    inter = max(0, x2 - x1) * max(0, y2 - y1)
    area_a = (a[2] - a[0]) * (a[3] - a[1])
    area_b = (b[2] - b[0]) * (b[3] - b[1])
    return inter / (area_a + area_b - inter)

print(round(iou((0, 0, 10, 10), (5, 5, 15, 15)), 4))   # 0.1429

# ---------------------------------------------------------------------
# Remember: IoU >= 0.5 is the usual 'correct detection' threshold; report mAP, not accuracy.
# Common mistake: Mixing box formats (xywh vs xyxy) between the model and the evaluation code.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
