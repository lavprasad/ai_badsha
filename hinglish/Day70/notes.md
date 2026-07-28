# Day 70 — Working with images, classically

Aaj ka goal: **Working with images, classically** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

### Aasaan Bhasha

Image (height, width, channels) shape ka array hai jiski values 0-255 ya 0-1 hoti hain. Baaki sab — filters, edges, resizing — usi array par arithmetic hai. Classical CV aaj bhi tab jeetta hai jab scene controlled ho: fixed camera, fixed lighting, known object.

### Chhota code

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

**Yaad rakho:** Har model call se pehle channel order (RGB vs BGR) aur value range (0-255 vs 0-1) check karo.

**Aam galti:** OpenCV ka BGR aise model me daalna jo RGB par train hua tha, aur bina kisi dikhne wali wajah ke accuracy khona.

Practice: `examples/01_images_as_arrays.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Colour spaces and channels

### Aasaan Bhasha

Image (height, width, channels) shape ka array hai jiski values 0-255 ya 0-1 hoti hain. Baaki sab — filters, edges, resizing — usi array par arithmetic hai. Classical CV aaj bhi tab jeetta hai jab scene controlled ho: fixed camera, fixed lighting, known object.

### Chhota code

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

**Yaad rakho:** Har model call se pehle channel order (RGB vs BGR) aur value range (0-255 vs 0-1) check karo.

**Aam galti:** OpenCV ka BGR aise model me daalna jo RGB par train hua tha, aur bina kisi dikhne wali wajah ke accuracy khona.

Practice: `examples/02_colour_spaces_and_channels.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Resizing, cropping, normalising

### Aasaan Bhasha

Vector numbers ki list hai jiski ek direction aur lambai hoti hai. Dot product alignment naapta hai: same direction par bada positive, perpendicular par zero. Cosine similarity wahi dot product hai lambai hata kar — isliye wo alag-alag magnitude ke embeddings ko theek se compare karta hai.

### Chhota code

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 4.0, 6.0])

print('dot   ', a @ b)
print('norm  ', np.linalg.norm(a))
cos = (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))
print('cosine', cos)   # 1.0 -> same direction
```

**Yaad rakho:** Cosine similarity magnitude ignore karti hai; Euclidean distance nahi. Apne sawaal ke hisaab se chuno.

**Aam galti:** Raw embeddings ko Euclidean distance se compare karna jab sirf direction ka matlab hai.

Practice: `examples/03_resizing_cropping_normalising.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Histogram features

### Aasaan Bhasha

Model se pehle plot karo. Histogram skew aur outliers dikhata hai, scatter non-linearity, aur residuals ka plot batata hai ki model systematically galat kahan hai. Paanch minute ka plotting ghanton ki confused tuning bacha deta hai.

### Chhota code

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

**Yaad rakho:** Axes par label lagao. Bina label ka plot sajावat hai, evidence nahi.

**Aam galti:** Sirf accuracy number dekh kar model judge karna, data ko kabhi dekhe bina.

Practice: `examples/04_histogram_features.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Edge detection and filters

### Aasaan Bhasha

Image (height, width, channels) shape ka array hai jiski values 0-255 ya 0-1 hoti hain. Baaki sab — filters, edges, resizing — usi array par arithmetic hai. Classical CV aaj bhi tab jeetta hai jab scene controlled ho: fixed camera, fixed lighting, known object.

### Chhota code

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

**Yaad rakho:** Har model call se pehle channel order (RGB vs BGR) aur value range (0-255 vs 0-1) check karo.

**Aam galti:** OpenCV ka BGR aise model me daalna jo RGB par train hua tha, aur bina kisi dikhne wali wajah ke accuracy khona.

Practice: `examples/05_edge_detection_and_filters.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. HOG and SIFT descriptors

### Aasaan Bhasha

Image (height, width, channels) shape ka array hai jiski values 0-255 ya 0-1 hoti hain. Baaki sab — filters, edges, resizing — usi array par arithmetic hai. Classical CV aaj bhi tab jeetta hai jab scene controlled ho: fixed camera, fixed lighting, known object.

### Chhota code

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

**Yaad rakho:** Har model call se pehle channel order (RGB vs BGR) aur value range (0-255 vs 0-1) check karo.

**Aam galti:** OpenCV ka BGR aise model me daalna jo RGB par train hua tha, aur bina kisi dikhne wali wajah ke accuracy khona.

Practice: `examples/06_hog_and_sift_descriptors.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Classical image classification

### Aasaan Bhasha

Lagbhag koi bhi vision model scratch se train nahi karta. Laakhon images par pretrained network lo, aakhri layer badlo, aur ya to backbone freeze karo (kam data) ya use kam learning rate par fine-tune karo (zyada data). Applied vision me yahi sabse zyada leverage wala trick hai.

### Chhota code

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

**Yaad rakho:** Wahi normalisation statistics use karo jinke saath pretrained model train hua tha.

**Aam galti:** Poora network 1e-3 par fine-tune karke wo sab bahaa dena jo ImageNet ne sikhaya tha.

Practice: `examples/07_classical_image_classification.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Data augmentation before deep learning

### Aasaan Bhasha

Dropout training ke dauraan random activations zero kar deta hai taaki network kisi ek raaste par nirbhar na rahe. Early stopping tab rok deta hai jab validation loss sudharna band kar de. Augmentation aapke paas jo hai usi se aur training data bana leta hai — vision me teeno me sabse zyada return isi ka hai.

### Chhota code

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

**Yaad rakho:** Inverted dropout training ke waqt scale kar deta hai, isliye inference me kuch badalna nahi padta.

**Aam galti:** Inference par dropout chalu chhod dena aur har call par alag predictions paana.

Practice: `examples/08_data_augmentation_before_deep_learning.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. When classical CV still wins

### Aasaan Bhasha

Image (height, width, channels) shape ka array hai jiski values 0-255 ya 0-1 hoti hain. Baaki sab — filters, edges, resizing — usi array par arithmetic hai. Classical CV aaj bhi tab jeetta hai jab scene controlled ho: fixed camera, fixed lighting, known object.

### Chhota code

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

**Yaad rakho:** Har model call se pehle channel order (RGB vs BGR) aur value range (0-255 vs 0-1) check karo.

**Aam galti:** OpenCV ka BGR aise model me daalna jo RGB par train hua tha, aur bina kisi dikhne wali wajah ke accuracy khona.

Practice: `examples/09_when_classical_cv_still_wins.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Loading an image dataset efficiently

### Aasaan Bhasha

ML code ko baaki code jaise tests chahiye, plus data tests: schema, ranges, null rates, class balance. Har known failure mode ke liye ek behavioural test jodo — ek test jo pichhli baar ka outage pakad leta, wo 90% coverage se zyada keemti hai.

### Chhota code

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

**Yaad rakho:** Data contract test karo, sirf function nahi — kharab data kharab code se zyada models todta hai.

**Aam galti:** Sirf happy path test karna, jisse poora-null column chupchap constant model train kar deta hai.

Practice: `examples/10_loading_an_image_dataset_efficiently.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 70 ke baad aapko ye aana chahiye

- **Images as arrays** ko bina notes dekhe kisi dost ko samjha sakna.
- **Colour spaces and channels** ko bina notes dekhe kisi dost ko samjha sakna.
- **Resizing, cropping, normalising** ko bina notes dekhe kisi dost ko samjha sakna.
- **Histogram features** ko bina notes dekhe kisi dost ko samjha sakna.
- **Edge detection and filters** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
