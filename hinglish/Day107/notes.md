# Day 107 — Object detection

Aaj ka goal: **Object detection** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

### Aasaan Bhasha

Classification batati hai kya; detection batata hai kya aur kahan. Boxes ko IoU (intersection over union) se score kiya jaata hai aur duplicates non-maximum suppression se hataye jaate hain. Segmentation isse aage ja kar har pixel ko label karta hai.

### Chhota code

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

**Yaad rakho:** IoU >= 0.5 aam 'sahi detection' threshold hai; accuracy nahi, mAP report karo.

**Aam galti:** Model aur evaluation code ke beech box formats mila dena (xywh vs xyxy).

Practice: `examples/01_detection_vs_classification.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Bounding box formats

### Aasaan Bhasha

Classification batati hai kya; detection batata hai kya aur kahan. Boxes ko IoU (intersection over union) se score kiya jaata hai aur duplicates non-maximum suppression se hataye jaate hain. Segmentation isse aage ja kar har pixel ko label karta hai.

### Chhota code

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

**Yaad rakho:** IoU >= 0.5 aam 'sahi detection' threshold hai; accuracy nahi, mAP report karo.

**Aam galti:** Model aur evaluation code ke beech box formats mila dena (xywh vs xyxy).

Practice: `examples/02_bounding_box_formats.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Intersection over union

### Aasaan Bhasha

Classification batati hai kya; detection batata hai kya aur kahan. Boxes ko IoU (intersection over union) se score kiya jaata hai aur duplicates non-maximum suppression se hataye jaate hain. Segmentation isse aage ja kar har pixel ko label karta hai.

### Chhota code

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

**Yaad rakho:** IoU >= 0.5 aam 'sahi detection' threshold hai; accuracy nahi, mAP report karo.

**Aam galti:** Model aur evaluation code ke beech box formats mila dena (xywh vs xyxy).

Practice: `examples/03_intersection_over_union.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Anchor boxes

### Aasaan Bhasha

Classification batati hai kya; detection batata hai kya aur kahan. Boxes ko IoU (intersection over union) se score kiya jaata hai aur duplicates non-maximum suppression se hataye jaate hain. Segmentation isse aage ja kar har pixel ko label karta hai.

### Chhota code

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

**Yaad rakho:** IoU >= 0.5 aam 'sahi detection' threshold hai; accuracy nahi, mAP report karo.

**Aam galti:** Model aur evaluation code ke beech box formats mila dena (xywh vs xyxy).

Practice: `examples/04_anchor_boxes.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Two-stage detectors: R-CNN family

### Aasaan Bhasha

Convolution ek chhota seekha hua filter image par sarkata hai, isliye wahi edge detector frame me kahin bhi kaam karta hai. Yahi weight sharing wajah hai ki CNN ko dense net se kahin kam parameters chahiye. Pooling map chhota karta hai aur thodi translation tolerance deta hai.

### Chhota code

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

**Yaad rakho:** Output size = (in - kernel + 2*pad)/stride + 1. Jab layer jud na rahi ho to shapes print karo.

**Aam galti:** Channel dimension bhool jaana aur (H,W) dena jahan layer (N,C,H,W) maang rahi hai.

Practice: `examples/05_two_stage_detectors_r_cnn_family.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. One-stage detectors: YOLO and SSD

### Aasaan Bhasha

Classification batati hai kya; detection batata hai kya aur kahan. Boxes ko IoU (intersection over union) se score kiya jaata hai aur duplicates non-maximum suppression se hataye jaate hain. Segmentation isse aage ja kar har pixel ko label karta hai.

### Chhota code

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

**Yaad rakho:** IoU >= 0.5 aam 'sahi detection' threshold hai; accuracy nahi, mAP report karo.

**Aam galti:** Model aur evaluation code ke beech box formats mila dena (xywh vs xyxy).

Practice: `examples/06_one_stage_detectors_yolo_and_ssd.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Non-maximum suppression

### Aasaan Bhasha

Classification batati hai kya; detection batata hai kya aur kahan. Boxes ko IoU (intersection over union) se score kiya jaata hai aur duplicates non-maximum suppression se hataye jaate hain. Segmentation isse aage ja kar har pixel ko label karta hai.

### Chhota code

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

**Yaad rakho:** IoU >= 0.5 aam 'sahi detection' threshold hai; accuracy nahi, mAP report karo.

**Aam galti:** Model aur evaluation code ke beech box formats mila dena (xywh vs xyxy).

Practice: `examples/07_non_maximum_suppression.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. mAP as the detection metric

### Aasaan Bhasha

Classification batati hai kya; detection batata hai kya aur kahan. Boxes ko IoU (intersection over union) se score kiya jaata hai aur duplicates non-maximum suppression se hataye jaate hain. Segmentation isse aage ja kar har pixel ko label karta hai.

### Chhota code

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

**Yaad rakho:** IoU >= 0.5 aam 'sahi detection' threshold hai; accuracy nahi, mAP report karo.

**Aam galti:** Model aur evaluation code ke beech box formats mila dena (xywh vs xyxy).

Practice: `examples/08_map_as_the_detection_metric.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Annotating a detection dataset

### Aasaan Bhasha

Classification batati hai kya; detection batata hai kya aur kahan. Boxes ko IoU (intersection over union) se score kiya jaata hai aur duplicates non-maximum suppression se hataye jaate hain. Segmentation isse aage ja kar har pixel ko label karta hai.

### Chhota code

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

**Yaad rakho:** IoU >= 0.5 aam 'sahi detection' threshold hai; accuracy nahi, mAP report karo.

**Aam galti:** Model aur evaluation code ke beech box formats mila dena (xywh vs xyxy).

Practice: `examples/09_annotating_a_detection_dataset.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Fine-tuning a detector

### Aasaan Bhasha

Hyperparameters wo settings hain jo aap chunte ho, seekhi nahi jaatin. Grid search poora chhaanta hai aur barbaad karta hai; random search high dimensions me acche ilaake jaldi dhoondta hai; Bayesian search pichhle trials se seekhta hai. Search hamesha cross-validation ke andar karo.

### Chhota code

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

**Yaad rakho:** Random seed fix karo aur har trial log karo, warna aap apna hi best model dobara nahi bana paoge.

**Aam galti:** 400 rows par 40 hyperparameters tune karna — ab aap validation set hi fit kar rahe ho.

Practice: `examples/10_fine_tuning_a_detector.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 107 ke baad aapko ye aana chahiye

- **Detection vs classification** ko bina notes dekhe kisi dost ko samjha sakna.
- **Bounding box formats** ko bina notes dekhe kisi dost ko samjha sakna.
- **Intersection over union** ko bina notes dekhe kisi dost ko samjha sakna.
- **Anchor boxes** ko bina notes dekhe kisi dost ko samjha sakna.
- **Two-stage detectors: R-CNN family** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
