# Day 70 — Working with images, classically

Today's goal: work through **Working with images, classically** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Images as arrays |
| 2 | Colour spaces and channels |
| 3 | Resizing, cropping, normalising |
| 4 | Histogram features |
| 5 | Edge detection and filters |
| 6 | HOG and SIFT descriptors |
| 7 | Classical image classification |
| 8 | Data augmentation before deep learning |
| 9 | When classical CV still wins |
| 10 | Loading an image dataset efficiently |

---

## 1. Images as arrays

An image is an array of shape (height, width, channels) with values 0-255 or 0-1. Everything else — filters, edges, resizing — is arithmetic on that array. Classical CV still wins when the scene is controlled: fixed camera, fixed lighting, known object.

```python
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
```

**Remember:** Check the channel order (RGB vs BGR) and the value range (0-255 vs 0-1) before every model call.

**Common mistake:** Feeding BGR from OpenCV into a model trained on RGB and losing accuracy for no visible reason.

## 2. Colour spaces and channels

An image is an array of shape (height, width, channels) with values 0-255 or 0-1. Everything else — filters, edges, resizing — is arithmetic on that array. Classical CV still wins when the scene is controlled: fixed camera, fixed lighting, known object.

```python
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
```

**Remember:** Check the channel order (RGB vs BGR) and the value range (0-255 vs 0-1) before every model call.

**Common mistake:** Feeding BGR from OpenCV into a model trained on RGB and losing accuracy for no visible reason.

## 3. Resizing, cropping, normalising

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

## 4. Histogram features

Plot before you model. A histogram exposes skew and outliers, a scatter exposes non-linearity, and a line of residuals exposes a model that is systematically wrong. Five minutes of plotting saves hours of confused tuning.

```python
import matplotlib
matplotlib.use('Agg')          # headless-safe for scripts/CI
import matplotlib.pyplot as plt
import numpy as np

x = np.random.default_rng(0).normal(size=500)
fig, ax = plt.subplots()
ax.hist(x, bins=30)
ax.set_title('sample distribution')
fig.savefig('hist.png', dpi=120)
print('wrote hist.png')
```

**Remember:** Label the axes. An unlabelled plot is a decoration, not evidence.

**Common mistake:** Judging a model by its accuracy number alone without ever looking at the data.

## 5. Edge detection and filters

An image is an array of shape (height, width, channels) with values 0-255 or 0-1. Everything else — filters, edges, resizing — is arithmetic on that array. Classical CV still wins when the scene is controlled: fixed camera, fixed lighting, known object.

```python
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
```

**Remember:** Check the channel order (RGB vs BGR) and the value range (0-255 vs 0-1) before every model call.

**Common mistake:** Feeding BGR from OpenCV into a model trained on RGB and losing accuracy for no visible reason.

## 6. HOG and SIFT descriptors

An image is an array of shape (height, width, channels) with values 0-255 or 0-1. Everything else — filters, edges, resizing — is arithmetic on that array. Classical CV still wins when the scene is controlled: fixed camera, fixed lighting, known object.

```python
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
```

**Remember:** Check the channel order (RGB vs BGR) and the value range (0-255 vs 0-1) before every model call.

**Common mistake:** Feeding BGR from OpenCV into a model trained on RGB and losing accuracy for no visible reason.

## 7. Classical image classification

Almost nobody trains a vision model from scratch. Take a network pretrained on millions of images, replace the last layer, and either freeze the backbone (small data) or fine-tune it at a low learning rate (more data). This is the highest-leverage trick in applied vision.

```python
# Requires torch + torchvision
# import torchvision.models as models, torch.nn as nn
#
# model = models.resnet18(weights='IMAGENET1K_V1')
# for p in model.parameters():
#     p.requires_grad = False          # freeze the backbone
# model.fc = nn.Linear(model.fc.in_features, 3)   # 3 of your classes
# # only model.fc trains -> works with a few hundred images
print('Transfer learning: freeze backbone, replace head, train head, then unfreeze at low LR.')
```

**Remember:** Use the exact normalisation statistics the pretrained model was trained with.

**Common mistake:** Fine-tuning the whole network at 1e-3 and washing away everything ImageNet taught it.

## 8. Data augmentation before deep learning

Dropout randomly zeroes activations during training so the network cannot rely on any single path. Early stopping halts when validation loss stops improving. Augmentation invents more training data from what you have — usually the highest-return of the three for vision.

```python
import numpy as np

def dropout(x, p=0.5, training=True, rng=None):
    if not training or p == 0:
        return x
    rng = rng or np.random.default_rng(0)
    mask = (rng.random(x.shape) > p) / (1 - p)   # inverted dropout: scale at train time
    return x * mask

x = np.ones((2, 6))
print(dropout(x, p=0.5).round(2))
print(dropout(x, training=False))   # unchanged at inference
```

**Remember:** Inverted dropout scales during training so inference needs no change at all.

**Common mistake:** Leaving dropout active at inference and getting different predictions on every call.

## 9. When classical CV still wins

An image is an array of shape (height, width, channels) with values 0-255 or 0-1. Everything else — filters, edges, resizing — is arithmetic on that array. Classical CV still wins when the scene is controlled: fixed camera, fixed lighting, known object.

```python
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
```

**Remember:** Check the channel order (RGB vs BGR) and the value range (0-255 vs 0-1) before every model call.

**Common mistake:** Feeding BGR from OpenCV into a model trained on RGB and losing accuracy for no visible reason.

## 10. Loading an image dataset efficiently

ML code needs the same tests as any code, plus data tests: schema, ranges, null rates, class balance. Add one behavioural test per known failure mode — a test that would have caught last quarter's outage is worth more than 90% coverage.

```python
import numpy as np

def preprocess(x):
    x = np.asarray(x, dtype=float)
    if np.isnan(x).any():
        raise ValueError('NaN in input')
    return (x - x.mean()) / (x.std() + 1e-8)

def test_preprocess():
    out = preprocess([1.0, 2.0, 3.0])
    assert abs(float(out.mean())) < 1e-6, 'should be zero-centred'
    assert abs(float(out.std()) - 1.0) < 1e-6, 'should be unit variance'
    try:
        preprocess([1.0, float('nan')])
    except ValueError:
        pass
    else:
        raise AssertionError('NaN should have raised')
    print('ok')

test_preprocess()
```

**Remember:** Test the data contract, not just the function — bad data breaks more models than bad code.

**Common mistake:** Testing only the happy path, so an all-null column silently trains a constant model.

---

## What you should be able to do after Day 70

- Explain **Images as arrays** to someone else without notes.
- Explain **Colour spaces and channels** to someone else without notes.
- Explain **Resizing, cropping, normalising** to someone else without notes.
- Explain **Histogram features** to someone else without notes.
- Explain **Edge detection and filters** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
