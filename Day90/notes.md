# Day 90 — Training a CNN properly

Today's goal: work through **Training a CNN properly** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Dataset preparation and splits |
| 2 | Normalisation statistics |
| 3 | Augmentation strategy |
| 4 | Choosing batch size |
| 5 | Learning rate finder |
| 6 | Monitoring train vs validation |
| 7 | Confusion matrix on validation |
| 8 | Test-time augmentation |
| 9 | Class imbalance in images |
| 10 | An image classifier walkthrough |

---

## 1. Dataset preparation and splits

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

Practice: open `examples/01_dataset_preparation_and_splits.py`, predict the output, change one line, predict again.

## 2. Normalisation statistics

A vector is a list of numbers with a direction and length. The dot product measures alignment: large and positive when two vectors point the same way, zero when perpendicular. Cosine similarity is the dot product with length divided out, which is why it compares embeddings of different magnitudes fairly.

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 4.0, 6.0])

print('dot   ', a @ b)
print('norm  ', np.linalg.norm(a))
cos = (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))
print('cosine', cos)   # 1.0 -> same direction
```

**Remember:** Cosine similarity ignores magnitude; Euclidean distance does not. Pick the one that matches your question.

**Common mistake:** Comparing raw embeddings with Euclidean distance when only direction carries meaning.

Practice: open `examples/02_normalisation_statistics.py`, predict the output, change one line, predict again.

## 3. Augmentation strategy

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

Practice: open `examples/03_augmentation_strategy.py`, predict the output, change one line, predict again.

## 4. Choosing batch size

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

Practice: open `examples/04_choosing_batch_size.py`, predict the output, change one line, predict again.

## 5. Learning rate finder

Gradient descent repeatedly steps against the gradient. Full-batch is stable but slow; stochastic is noisy but escapes shallow traps; mini-batch is the practical middle. The learning rate is the single most important knob you will ever turn.

```python
import numpy as np

rng = np.random.default_rng(0)
X = rng.normal(size=(1000, 3))
true_w = np.array([1.0, -2.0, 0.5])
y = X @ true_w + rng.normal(scale=0.1, size=1000)

w, lr, batch = np.zeros(3), 0.1, 32
for epoch in range(20):
    idx = rng.permutation(len(X))
    for start in range(0, len(X), batch):
        b = idx[start:start + batch]
        grad = 2 * X[b].T @ (X[b] @ w - y[b]) / len(b)
        w -= lr * grad
print('learned', np.round(w, 3), 'target', true_w)
```

**Remember:** Shuffle every epoch, otherwise the model learns the order of your file.

**Common mistake:** Leaving the learning rate fixed forever instead of decaying it once the loss plateaus.

Practice: open `examples/05_learning_rate_finder.py`, predict the output, change one line, predict again.

## 6. Monitoring train vs validation

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

Practice: open `examples/06_monitoring_train_vs_validation.py`, predict the output, change one line, predict again.

## 7. Confusion matrix on validation

A matrix is a linear transformation. Multiplying matrices composes transformations, which is exactly what stacking neural network layers does. Shapes must line up: (m,k) @ (k,n) -> (m,n); the inner dimensions must match and they vanish.

```python
import numpy as np

A = np.random.default_rng(0).normal(size=(3, 4))
B = np.random.default_rng(1).normal(size=(4, 2))

print((A @ B).shape)      # (3, 2)
print(A.T.shape)          # (4, 3)
print(np.eye(3) @ A is not A, np.allclose(np.eye(3) @ A, A))
```

**Remember:** Read every shape error as 'the inner dimensions did not match' and print the shapes.

**Common mistake:** Reaching for `np.linalg.inv` to solve `Ax=b` instead of the numerically safer `np.linalg.solve`.

Practice: open `examples/07_confusion_matrix_on_validation.py`, predict the output, change one line, predict again.

## 8. Test-time augmentation

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

Practice: open `examples/08_test_time_augmentation.py`, predict the output, change one line, predict again.

## 9. Class imbalance in images

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

Practice: open `examples/09_class_imbalance_in_images.py`, predict the output, change one line, predict again.

## 10. An image classifier walkthrough

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

Practice: open `examples/10_an_image_classifier_walkthrough.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 90

- Explain **Dataset preparation and splits** to someone else without notes.
- Explain **Normalisation statistics** to someone else without notes.
- Explain **Augmentation strategy** to someone else without notes.
- Explain **Choosing batch size** to someone else without notes.
- Explain **Learning rate finder** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
