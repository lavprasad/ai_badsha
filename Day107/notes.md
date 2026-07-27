# Day 107 — Object detection

Today's goal: work through **object detection** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Detection vs classification |
| 2 | Bounding box formats |
| 3 | Intersection over union |
| 4 | Anchor boxes |
| 5 | Two-stage detectors: R-CNN family |
| 6 | One-stage detectors: YOLO and SSD |
| 7 | Non-maximum suppression |
| 8 | mAP as the detection metric |
| 9 | Annotating a detection dataset |
| 10 | Fine-tuning a detector |

---

## 1. Detection vs classification

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

## 2. Bounding box formats

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

## 3. Intersection over union

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

## 4. Anchor boxes

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

## 5. Two-stage detectors: R-CNN family

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

## 6. One-stage detectors: YOLO and SSD

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

## 7. Non-maximum suppression

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

## 8. mAP as the detection metric

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

## 9. Annotating a detection dataset

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

## 10. Fine-tuning a detector

Hyperparameters are the settings you choose, not learn. Grid search is exhaustive and wasteful; random search finds good regions faster in high dimensions; Bayesian search learns from previous trials. Always search inside cross-validation.

```python
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
import numpy as np

X, y = load_breast_cancer(return_X_y=True)
space = {
    'n_estimators': [100, 300, 600],
    'max_depth': [None, 4, 8, 16],
    'min_samples_leaf': [1, 2, 4, 8],
}
search = RandomizedSearchCV(
    RandomForestClassifier(random_state=0, n_jobs=-1),
    space, n_iter=12, cv=5, random_state=0,
).fit(X, y)
print(search.best_params_, round(search.best_score_, 4))
```

**Remember:** Fix the random seed and log every trial, or you cannot reproduce your own best model.

**Common mistake:** Tuning 40 hyperparameters on 400 rows — you are now fitting the validation set.

---

## What you should be able to do after Day 107

- Explain **Detection vs classification** to someone else without notes.
- Explain **Bounding box formats** to someone else without notes.
- Explain **Intersection over union** to someone else without notes.
- Explain **Anchor boxes** to someone else without notes.
- Explain **Two-stage detectors: R-CNN family** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
