# Day 108 — Image segmentation

Today's goal: work through **Image segmentation** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Semantic vs instance vs panoptic |
| 2 | Per-pixel classification |
| 3 | U-Net architecture |
| 4 | Encoder-decoder with skip connections |
| 5 | Dice and IoU losses |
| 6 | Mask R-CNN |
| 7 | Segment Anything and promptable segmentation |
| 8 | Medical imaging considerations |
| 9 | Annotation cost and weak supervision |
| 10 | Evaluating segmentation quality |

---

## 1. Semantic vs instance vs panoptic

Classification says what; detection says what and where. Boxes are scored by IoU (intersection over union) and duplicates are removed with non-maximum suppression. Segmentation goes further and labels every pixel.

```python
def iou(a, b):
    """Boxes as (x1, y1, x2, y2)."""
    x1, y1 = max(a[0], b[0]), max(a[1], b[1])
    x2, y2 = min(a[2], b[2]), min(a[3], b[3])
    inter = max(0, x2 - x1) * max(0, y2 - y1)
    area_a = (a[2] - a[0]) * (a[3] - a[1])
    area_b = (b[2] - b[0]) * (b[3] - b[1])
    return inter / (area_a + area_b - inter)

print(round(iou((0, 0, 10, 10), (5, 5, 15, 15)), 4))   # 0.1429
```

**Remember:** IoU >= 0.5 is the usual 'correct detection' threshold; report mAP, not accuracy.

**Common mistake:** Mixing box formats (xywh vs xyxy) between the model and the evaluation code.

## 2. Per-pixel classification

Classification says what; detection says what and where. Boxes are scored by IoU (intersection over union) and duplicates are removed with non-maximum suppression. Segmentation goes further and labels every pixel.

```python
def iou(a, b):
    """Boxes as (x1, y1, x2, y2)."""
    x1, y1 = max(a[0], b[0]), max(a[1], b[1])
    x2, y2 = min(a[2], b[2]), min(a[3], b[3])
    inter = max(0, x2 - x1) * max(0, y2 - y1)
    area_a = (a[2] - a[0]) * (a[3] - a[1])
    area_b = (b[2] - b[0]) * (b[3] - b[1])
    return inter / (area_a + area_b - inter)

print(round(iou((0, 0, 10, 10), (5, 5, 15, 15)), 4))   # 0.1429
```

**Remember:** IoU >= 0.5 is the usual 'correct detection' threshold; report mAP, not accuracy.

**Common mistake:** Mixing box formats (xywh vs xyxy) between the model and the evaluation code.

## 3. U-Net architecture

Classification says what; detection says what and where. Boxes are scored by IoU (intersection over union) and duplicates are removed with non-maximum suppression. Segmentation goes further and labels every pixel.

```python
def iou(a, b):
    """Boxes as (x1, y1, x2, y2)."""
    x1, y1 = max(a[0], b[0]), max(a[1], b[1])
    x2, y2 = min(a[2], b[2]), min(a[3], b[3])
    inter = max(0, x2 - x1) * max(0, y2 - y1)
    area_a = (a[2] - a[0]) * (a[3] - a[1])
    area_b = (b[2] - b[0]) * (b[3] - b[1])
    return inter / (area_a + area_b - inter)

print(round(iou((0, 0, 10, 10), (5, 5, 15, 15)), 4))   # 0.1429
```

**Remember:** IoU >= 0.5 is the usual 'correct detection' threshold; report mAP, not accuracy.

**Common mistake:** Mixing box formats (xywh vs xyxy) between the model and the evaluation code.

## 4. Encoder-decoder with skip connections

Multiplying many small derivatives makes gradients vanish; many large ones makes them explode. Residual connections give the gradient a straight path back, which is why 100-layer networks became trainable. Clipping caps the update norm so one bad batch cannot blow up the weights.

```python
import numpy as np

def clip_by_norm(grads, max_norm=1.0):
    total = np.sqrt(sum(float((g ** 2).sum()) for g in grads))
    if total <= max_norm:
        return grads, total
    scale = max_norm / (total + 1e-6)
    return [g * scale for g in grads], total

grads = [np.array([10.0, 20.0]), np.array([30.0])]
clipped, before = clip_by_norm(grads)
print('norm before', round(before, 2))
print('norm after ', round(float(np.sqrt(sum((g ** 2).sum() for g in clipped))), 2))
```

**Remember:** Log the gradient norm during training — a sudden spike explains a sudden loss spike.

**Common mistake:** Chasing an architecture change when a `clip_grad_norm_(1.0)` would have fixed the instability.

## 5. Dice and IoU losses

Classification says what; detection says what and where. Boxes are scored by IoU (intersection over union) and duplicates are removed with non-maximum suppression. Segmentation goes further and labels every pixel.

```python
def iou(a, b):
    """Boxes as (x1, y1, x2, y2)."""
    x1, y1 = max(a[0], b[0]), max(a[1], b[1])
    x2, y2 = min(a[2], b[2]), min(a[3], b[3])
    inter = max(0, x2 - x1) * max(0, y2 - y1)
    area_a = (a[2] - a[0]) * (a[3] - a[1])
    area_b = (b[2] - b[0]) * (b[3] - b[1])
    return inter / (area_a + area_b - inter)

print(round(iou((0, 0, 10, 10), (5, 5, 15, 15)), 4))   # 0.1429
```

**Remember:** IoU >= 0.5 is the usual 'correct detection' threshold; report mAP, not accuracy.

**Common mistake:** Mixing box formats (xywh vs xyxy) between the model and the evaluation code.

## 6. Mask R-CNN

A convolution slides a small learned filter over the image, so the same edge detector works anywhere in the frame. That weight sharing is why a CNN needs far fewer parameters than a dense net. Pooling shrinks the map and adds a little translation tolerance.

```python
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
```

**Remember:** Output size = (in - kernel + 2*pad)/stride + 1. Print shapes when a layer refuses to connect.

**Common mistake:** Forgetting the channel dimension and feeding (H,W) where the layer expects (N,C,H,W).

## 7. Segment Anything and promptable segmentation

Classification says what; detection says what and where. Boxes are scored by IoU (intersection over union) and duplicates are removed with non-maximum suppression. Segmentation goes further and labels every pixel.

```python
def iou(a, b):
    """Boxes as (x1, y1, x2, y2)."""
    x1, y1 = max(a[0], b[0]), max(a[1], b[1])
    x2, y2 = min(a[2], b[2]), min(a[3], b[3])
    inter = max(0, x2 - x1) * max(0, y2 - y1)
    area_a = (a[2] - a[0]) * (a[3] - a[1])
    area_b = (b[2] - b[0]) * (b[3] - b[1])
    return inter / (area_a + area_b - inter)

print(round(iou((0, 0, 10, 10), (5, 5, 15, 15)), 4))   # 0.1429
```

**Remember:** IoU >= 0.5 is the usual 'correct detection' threshold; report mAP, not accuracy.

**Common mistake:** Mixing box formats (xywh vs xyxy) between the model and the evaluation code.

## 8. Medical imaging considerations

Classification says what; detection says what and where. Boxes are scored by IoU (intersection over union) and duplicates are removed with non-maximum suppression. Segmentation goes further and labels every pixel.

```python
def iou(a, b):
    """Boxes as (x1, y1, x2, y2)."""
    x1, y1 = max(a[0], b[0]), max(a[1], b[1])
    x2, y2 = min(a[2], b[2]), min(a[3], b[3])
    inter = max(0, x2 - x1) * max(0, y2 - y1)
    area_a = (a[2] - a[0]) * (a[3] - a[1])
    area_b = (b[2] - b[0]) * (b[3] - b[1])
    return inter / (area_a + area_b - inter)

print(round(iou((0, 0, 10, 10), (5, 5, 15, 15)), 4))   # 0.1429
```

**Remember:** IoU >= 0.5 is the usual 'correct detection' threshold; report mAP, not accuracy.

**Common mistake:** Mixing box formats (xywh vs xyxy) between the model and the evaluation code.

## 9. Annotation cost and weak supervision

Classification says what; detection says what and where. Boxes are scored by IoU (intersection over union) and duplicates are removed with non-maximum suppression. Segmentation goes further and labels every pixel.

```python
def iou(a, b):
    """Boxes as (x1, y1, x2, y2)."""
    x1, y1 = max(a[0], b[0]), max(a[1], b[1])
    x2, y2 = min(a[2], b[2]), min(a[3], b[3])
    inter = max(0, x2 - x1) * max(0, y2 - y1)
    area_a = (a[2] - a[0]) * (a[3] - a[1])
    area_b = (b[2] - b[0]) * (b[3] - b[1])
    return inter / (area_a + area_b - inter)

print(round(iou((0, 0, 10, 10), (5, 5, 15, 15)), 4))   # 0.1429
```

**Remember:** IoU >= 0.5 is the usual 'correct detection' threshold; report mAP, not accuracy.

**Common mistake:** Mixing box formats (xywh vs xyxy) between the model and the evaluation code.

## 10. Evaluating segmentation quality

Classification says what; detection says what and where. Boxes are scored by IoU (intersection over union) and duplicates are removed with non-maximum suppression. Segmentation goes further and labels every pixel.

```python
def iou(a, b):
    """Boxes as (x1, y1, x2, y2)."""
    x1, y1 = max(a[0], b[0]), max(a[1], b[1])
    x2, y2 = min(a[2], b[2]), min(a[3], b[3])
    inter = max(0, x2 - x1) * max(0, y2 - y1)
    area_a = (a[2] - a[0]) * (a[3] - a[1])
    area_b = (b[2] - b[0]) * (b[3] - b[1])
    return inter / (area_a + area_b - inter)

print(round(iou((0, 0, 10, 10), (5, 5, 15, 15)), 4))   # 0.1429
```

**Remember:** IoU >= 0.5 is the usual 'correct detection' threshold; report mAP, not accuracy.

**Common mistake:** Mixing box formats (xywh vs xyxy) between the model and the evaluation code.

---

## What you should be able to do after Day 108

- Explain **Semantic vs instance vs panoptic** to someone else without notes.
- Explain **Per-pixel classification** to someone else without notes.
- Explain **U-Net architecture** to someone else without notes.
- Explain **Encoder-decoder with skip connections** to someone else without notes.
- Explain **Dice and IoU losses** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
