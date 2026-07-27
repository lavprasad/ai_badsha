# Day 89 — CNN architectures

Today's goal: work through **cnn architectures** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | LeNet and AlexNet |
| 2 | VGG and stacked small kernels |
| 3 | Inception and multi-scale |
| 4 | ResNet and residual connections |
| 5 | DenseNet |
| 6 | MobileNet and depthwise separable convolutions |
| 7 | EfficientNet and compound scaling |
| 8 | Vision transformers as the alternative |
| 9 | Choosing an architecture for your constraints |
| 10 | Reading an architecture diagram |

---

## 1. LeNet and AlexNet

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

## 2. VGG and stacked small kernels

Notebooks keep state between cells, which is great for exploring and terrible for reproducibility. Treat the notebook as a scratchpad; once logic settles, move it into a `.py` module you can import and test.

```python
# In a notebook, cell order != execution order.
# Restart & Run All before you trust any result.
import pandas as pd
df = pd.DataFrame({'x': [1, 2, 3]})
df.head()
```

**Remember:** 'Restart kernel and run all' is the only honest test that a notebook works.

**Common mistake:** Shipping a notebook whose results depend on a deleted cell you ran ten minutes ago.

## 3. Inception and multi-scale

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

## 4. ResNet and residual connections

Linear regression fits a straight line by minimising squared error. It is the honest baseline for every regression problem: fast, interpretable, and the thing your fancy model must beat before it earns its complexity.

```python
import numpy as np

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 1))
y = 3.0 * X[:, 0] + 2.0 + rng.normal(scale=0.5, size=200)

Xb = np.c_[np.ones(len(X)), X]                 # add bias column
w = np.linalg.lstsq(Xb, y, rcond=None)[0]      # solves the normal equations safely
print(f'intercept {w[0]:.3f}  slope {w[1]:.3f}')

resid = y - Xb @ w
print('residual mean (should be ~0):', round(float(resid.mean()), 6))
```

**Remember:** Plot residuals against predictions — any visible pattern means the linear form is wrong.

**Common mistake:** Reporting R² on training data and calling it model performance.

## 5. DenseNet

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

## 6. MobileNet and depthwise separable convolutions

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

## 7. EfficientNet and compound scaling

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

## 8. Vision transformers as the alternative

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

## 9. Choosing an architecture for your constraints

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

## 10. Reading an architecture diagram

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

---

## What you should be able to do after Day 89

- Explain **LeNet and AlexNet** to someone else without notes.
- Explain **VGG and stacked small kernels** to someone else without notes.
- Explain **Inception and multi-scale** to someone else without notes.
- Explain **ResNet and residual connections** to someone else without notes.
- Explain **DenseNet** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
