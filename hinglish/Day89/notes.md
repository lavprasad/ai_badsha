# Day 89 — CNN architectures

Aaj ka goal: **CNN architectures** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

Practice: `examples/01_lenet_and_alexnet.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. VGG and stacked small kernels

### Aasaan Bhasha

Notebooks cells ke beech state rakhte hain — exploring ke liye badhiya, reproducibility ke liye bekaar. Notebook ko scratchpad samjho; jab logic pakka ho jaaye to use `.py` module me daal do jise aap import aur test kar sako.

### Chhota code

```python
# In a notebook, cell order != execution order.
# Restart & Run All before you trust any result.
import pandas as pd
df = pd.DataFrame({'x': [1, 2, 3]})
df.head()
```

**Yaad rakho:** 'Restart kernel and run all' hi ek imaandaar test hai ki notebook sach me chalta hai.

**Aam galti:** Aisa notebook dena jiska result das minute pehle delete ki gayi cell par depend karta hai.

Practice: `examples/02_vgg_and_stacked_small_kernels.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Inception and multi-scale

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

Practice: `examples/03_inception_and_multi_scale.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. ResNet and residual connections

### Aasaan Bhasha

Linear regression squared error minimise karke seedhi line fit karta hai. Ye har regression problem ka imaandaar baseline hai: tez, samajhne layak, aur wahi cheez jise aapke fancy model ko harana padega tabhi wo apni complexity kamata hai.

### Chhota code

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

**Yaad rakho:** Predictions ke saamne residuals plot karo — koi bhi dikhne wala pattern matlab linear form galat hai.

**Aam galti:** Training data ka R² report karke use model performance bata dena.

Practice: `examples/04_resnet_and_residual_connections.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. DenseNet

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

Practice: `examples/05_densenet.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. MobileNet and depthwise separable convolutions

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

Practice: `examples/06_mobilenet_and_depthwise_separable_convol.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. EfficientNet and compound scaling

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

Practice: `examples/07_efficientnet_and_compound_scaling.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Vision transformers as the alternative

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

Practice: `examples/08_vision_transformers_as_the_alternative.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Choosing an architecture for your constraints

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

Practice: `examples/09_choosing_an_architecture_for_your_constr.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Reading an architecture diagram

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

Practice: `examples/10_reading_an_architecture_diagram.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 89 ke baad aapko ye aana chahiye

- **LeNet and AlexNet** ko bina notes dekhe kisi dost ko samjha sakna.
- **VGG and stacked small kernels** ko bina notes dekhe kisi dost ko samjha sakna.
- **Inception and multi-scale** ko bina notes dekhe kisi dost ko samjha sakna.
- **ResNet and residual connections** ko bina notes dekhe kisi dost ko samjha sakna.
- **DenseNet** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
