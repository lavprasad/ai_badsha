# Day 105 — Image fundamentals

Today's goal: work through **Image fundamentals** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Pixels, channels and bit depth |
| 2 | Colour spaces: RGB, HSV, grayscale |
| 3 | Image file formats and compression |
| 4 | Loading images with PIL and OpenCV |
| 5 | Resizing and interpolation methods |
| 6 | Aspect ratio and letterboxing |
| 7 | Normalisation for pretrained models |
| 8 | Batching images efficiently |
| 9 | EXIF orientation gotchas |
| 10 | Building an image loading utility |

---

## 1. Pixels, channels and bit depth

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

Practice: open `examples/01_pixels_channels_and_bit_depth.py`, predict the output, change one line, predict again.

## 2. Colour spaces: RGB, HSV, grayscale

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

Practice: open `examples/02_colour_spaces_rgb_hsv_grayscale.py`, predict the output, change one line, predict again.

## 3. Image file formats and compression

Today's idea — **Image file formats and compression** — sits inside the theme of Image fundamentals. Read it as a tool, not trivia: what job does it do, what does it assume about your data, and what breaks when that assumption is false?

```python
# Explore: Image file formats and compression
print("practice: Image file formats and compression")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Remember:** State one assumption `Image file formats and compression` makes about your data before you use it.

**Common mistake:** Copy-pasting `Image file formats and compression` from a tutorial without knowing what it assumes or when it fails.

Practice: open `examples/03_image_file_formats_and_compression.py`, predict the output, change one line, predict again.

## 4. Loading images with PIL and OpenCV

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

Practice: open `examples/04_loading_images_with_pil_and_opencv.py`, predict the output, change one line, predict again.

## 5. Resizing and interpolation methods

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

Practice: open `examples/05_resizing_and_interpolation_methods.py`, predict the output, change one line, predict again.

## 6. Aspect ratio and letterboxing

Today's idea — **Aspect ratio and letterboxing** — sits inside the theme of Image fundamentals. Read it as a tool, not trivia: what job does it do, what does it assume about your data, and what breaks when that assumption is false?

```python
# Explore: Aspect ratio and letterboxing
print("practice: Aspect ratio and letterboxing")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Remember:** State one assumption `Aspect ratio and letterboxing` makes about your data before you use it.

**Common mistake:** Copy-pasting `Aspect ratio and letterboxing` from a tutorial without knowing what it assumes or when it fails.

Practice: open `examples/06_aspect_ratio_and_letterboxing.py`, predict the output, change one line, predict again.

## 7. Normalisation for pretrained models

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

Practice: open `examples/07_normalisation_for_pretrained_models.py`, predict the output, change one line, predict again.

## 8. Batching images efficiently

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

Practice: open `examples/08_batching_images_efficiently.py`, predict the output, change one line, predict again.

## 9. EXIF orientation gotchas

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

Practice: open `examples/09_exif_orientation_gotchas.py`, predict the output, change one line, predict again.

## 10. Building an image loading utility

Projects are where the learning sticks. Build a thin end-to-end slice first — load data, train something dumb, evaluate, serve one prediction — then improve one layer at a time. A working baseline on day one beats a perfect model that never ships.

```python
STEPS = [
    '1. Define the decision the model supports and the metric that measures it',
    '2. Get the data; write the loader; assert the schema',
    '3. Dumb baseline (mean / majority class) -> this is the bar',
    '4. Simple model + honest validation split',
    '5. Error analysis: look at 30 wrong predictions by hand',
    '6. Improve the biggest error bucket, not the leaderboard',
    '7. Serve it, log inputs and outputs, monitor drift',
]
for s in STEPS:
    print(s)
```

**Remember:** Spend an hour looking at wrong predictions before you spend a day tuning hyperparameters.

**Common mistake:** Six weeks of feature engineering with no baseline to prove any of it helped.

Practice: open `examples/10_building_an_image_loading_utility.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 105

- Explain **Pixels, channels and bit depth** to someone else without notes.
- Explain **Colour spaces: RGB, HSV, grayscale** to someone else without notes.
- Explain **Image file formats and compression** to someone else without notes.
- Explain **Loading images with PIL and OpenCV** to someone else without notes.
- Explain **Resizing and interpolation methods** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
