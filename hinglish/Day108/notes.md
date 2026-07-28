# Day 108 — Image segmentation

Aaj ka goal: **Image segmentation** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

Practice: `examples/01_semantic_vs_instance_vs_panoptic.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Per-pixel classification

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

Practice: `examples/02_per_pixel_classification.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. U-Net architecture

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

Practice: `examples/03_u_net_architecture.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Encoder-decoder with skip connections

### Aasaan Bhasha

Bahut saare chhote derivatives multiply hone se gradients gayab ho jaate hain; bade se explode. Residual connections gradient ko wapas jaane ka seedha raasta dete hain, isiliye 100-layer networks trainable bane. Clipping update norm ko cap karta hai taaki ek kharab batch weights uda na de.

### Chhota code

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

**Yaad rakho:** Training ke dauraan gradient norm log karo — achanak spike achanak loss spike ko samjha deta hai.

**Aam galti:** Architecture badalne ke peeche bhaagna jab `clip_grad_norm_(1.0)` hi instability theek kar deta.

Practice: `examples/04_encoder_decoder_with_skip_connections.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Dice and IoU losses

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

Practice: `examples/05_dice_and_iou_losses.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Mask R-CNN

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

Practice: `examples/06_mask_r_cnn.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Segment Anything and promptable segmentation

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

Practice: `examples/07_segment_anything_and_promptable_segmenta.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Medical imaging considerations

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

Practice: `examples/08_medical_imaging_considerations.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Annotation cost and weak supervision

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

Practice: `examples/09_annotation_cost_and_weak_supervision.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Evaluating segmentation quality

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

Practice: `examples/10_evaluating_segmentation_quality.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 108 ke baad aapko ye aana chahiye

- **Semantic vs instance vs panoptic** ko bina notes dekhe kisi dost ko samjha sakna.
- **Per-pixel classification** ko bina notes dekhe kisi dost ko samjha sakna.
- **U-Net architecture** ko bina notes dekhe kisi dost ko samjha sakna.
- **Encoder-decoder with skip connections** ko bina notes dekhe kisi dost ko samjha sakna.
- **Dice and IoU losses** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
