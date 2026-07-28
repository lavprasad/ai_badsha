# Day 105 — Image fundamentals

Aaj ka goal: **Image fundamentals** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

Practice: `examples/01_pixels_channels_and_bit_depth.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Colour spaces: RGB, HSV, grayscale

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

Practice: `examples/02_colour_spaces_rgb_hsv_grayscale.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Image file formats and compression

### Aasaan Bhasha

Aaj ka idea — **Image file formats and compression** — Image fundamentals ke theme ke andar aata hai. Ise trivia nahi, ek tool ki tarah padho: ye kaam kya karta hai, aapke data ke baare me kya maan kar chalta hai, aur wo maanyata jhooth nikle to kya tootta hai?

### Chhota code

```python
# Explore: Image file formats and compression
print("practice: Image file formats and compression")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Yaad rakho:** `Image file formats and compression` use karne se pehle ek assumption likho jo ye aapke data ke baare me maanta hai.

**Aam galti:** `Image file formats and compression` ko tutorial se copy-paste kar lena bina jaane ki wo kya maanta hai aur kab fail hota hai.

Practice: `examples/03_image_file_formats_and_compression.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Loading images with PIL and OpenCV

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

Practice: `examples/04_loading_images_with_pil_and_opencv.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Resizing and interpolation methods

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

Practice: `examples/05_resizing_and_interpolation_methods.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Aspect ratio and letterboxing

### Aasaan Bhasha

Aaj ka idea — **Aspect ratio and letterboxing** — Image fundamentals ke theme ke andar aata hai. Ise trivia nahi, ek tool ki tarah padho: ye kaam kya karta hai, aapke data ke baare me kya maan kar chalta hai, aur wo maanyata jhooth nikle to kya tootta hai?

### Chhota code

```python
# Explore: Aspect ratio and letterboxing
print("practice: Aspect ratio and letterboxing")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Yaad rakho:** `Aspect ratio and letterboxing` use karne se pehle ek assumption likho jo ye aapke data ke baare me maanta hai.

**Aam galti:** `Aspect ratio and letterboxing` ko tutorial se copy-paste kar lena bina jaane ki wo kya maanta hai aur kab fail hota hai.

Practice: `examples/06_aspect_ratio_and_letterboxing.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Normalisation for pretrained models

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

Practice: `examples/07_normalisation_for_pretrained_models.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Batching images efficiently

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

Practice: `examples/08_batching_images_efficiently.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. EXIF orientation gotchas

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

Practice: `examples/09_exif_orientation_gotchas.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Building an image loading utility

### Aasaan Bhasha

Projects wahi jagah hain jahan seekha hua chipakta hai. Pehle ek patli end-to-end slice banao — data load, kuch bewakoof train, evaluate, ek prediction serve — phir ek-ek layer sudharo. Pehle din chalne wala baseline us perfect model se behtar hai jo kabhi ship hi nahi hota.

### Chhota code

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

**Yaad rakho:** Hyperparameters tune karne me ek din lagane se pehle galat predictions dekhne me ek ghanta lagao.

**Aam galti:** Chhe hafte feature engineering karna bina kisi baseline ke jo sabit kare ki kisi cheez se fayda hua.

Practice: `examples/10_building_an_image_loading_utility.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 105 ke baad aapko ye aana chahiye

- **Pixels, channels and bit depth** ko bina notes dekhe kisi dost ko samjha sakna.
- **Colour spaces: RGB, HSV, grayscale** ko bina notes dekhe kisi dost ko samjha sakna.
- **Image file formats and compression** ko bina notes dekhe kisi dost ko samjha sakna.
- **Loading images with PIL and OpenCV** ko bina notes dekhe kisi dost ko samjha sakna.
- **Resizing and interpolation methods** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
