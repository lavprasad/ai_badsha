# Day 96 — Diffusion models

Aaj ka goal: **Diffusion models** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | The forward noising process |
| 2 | Learning to denoise |
| 3 | The noise schedule |
| 4 | U-Net as the denoiser |
| 5 | Sampling steps and quality trade-off |
| 6 | Classifier-free guidance |
| 7 | Latent diffusion |
| 8 | Text conditioning |
| 9 | ControlNet and structural conditioning |
| 10 | Compute cost of generation |

---

## 1. The forward noising process

### Aasaan Bhasha

Imbalanced data par accuracy sab chhupa leti hai. Precision poochti hai 'jinhe maine flag kiya unme se kitne asli the'; recall poochti hai 'jo asli the unme se kitne maine pakde'. Threshold se aap ek ko doosre ke badle bechte ho, aur kaunsi galti zyada mehngi hai ye business tay karta hai.

### Chhota code

```python
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=2000, weights=[0.95, 0.05], random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, stratify=y, random_state=0)
m = LogisticRegression(max_iter=1000).fit(Xtr, ytr)
print(confusion_matrix(yte, m.predict(Xte)))
print(classification_report(yte, m.predict(Xte), digits=3))
print('roc auc', round(roc_auc_score(yte, m.predict_proba(Xte)[:, 1]), 4))
```

**Yaad rakho:** Decision threshold validation data par tune karo; 0.5 ek default hai, decision nahi.

**Aam galti:** Bhaari imbalanced problem par ROC-AUC optimise karna jahan imaandaar metric precision-recall AUC hai.

Practice: `examples/01_the_forward_noising_process.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Learning to denoise

### Aasaan Bhasha

Diffusion noise ulta karna seekhta hai: images me chhote steps me Gaussian noise daalo, phir network ko ek step wapas karna sikhao. Generation me aap pure noise se shuru karke baar-baar denoise karte ho, text embedding ke ishaare par. Ye GAN training se zyada stable hai aur ab images ka default hai.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
image = np.ones(8) * 0.5
betas = np.linspace(1e-4, 0.02, 10)   # noise schedule

x = image.copy()
for t, b in enumerate(betas):
    x = np.sqrt(1 - b) * x + np.sqrt(b) * rng.normal(size=x.shape)
print('after forward diffusion:', x.round(2))
print('Reverse process = a network predicting the noise added at each step.')
```

**Yaad rakho:** Zyada sampling steps matlab behtar quality aur usi hisaab se zyada compute — bas yahi poora sauda hai.

**Aam galti:** Ye maan lena ki generated images copyright ya bias se aazad hain kyunki 'model ne banayi hai'.

Practice: `examples/02_learning_to_denoise.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. The noise schedule

### Aasaan Bhasha

Diffusion noise ulta karna seekhta hai: images me chhote steps me Gaussian noise daalo, phir network ko ek step wapas karna sikhao. Generation me aap pure noise se shuru karke baar-baar denoise karte ho, text embedding ke ishaare par. Ye GAN training se zyada stable hai aur ab images ka default hai.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
image = np.ones(8) * 0.5
betas = np.linspace(1e-4, 0.02, 10)   # noise schedule

x = image.copy()
for t, b in enumerate(betas):
    x = np.sqrt(1 - b) * x + np.sqrt(b) * rng.normal(size=x.shape)
print('after forward diffusion:', x.round(2))
print('Reverse process = a network predicting the noise added at each step.')
```

**Yaad rakho:** Zyada sampling steps matlab behtar quality aur usi hisaab se zyada compute — bas yahi poora sauda hai.

**Aam galti:** Ye maan lena ki generated images copyright ya bias se aazad hain kyunki 'model ne banayi hai'.

Practice: `examples/03_the_noise_schedule.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. U-Net as the denoiser

### Aasaan Bhasha

Diffusion noise ulta karna seekhta hai: images me chhote steps me Gaussian noise daalo, phir network ko ek step wapas karna sikhao. Generation me aap pure noise se shuru karke baar-baar denoise karte ho, text embedding ke ishaare par. Ye GAN training se zyada stable hai aur ab images ka default hai.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
image = np.ones(8) * 0.5
betas = np.linspace(1e-4, 0.02, 10)   # noise schedule

x = image.copy()
for t, b in enumerate(betas):
    x = np.sqrt(1 - b) * x + np.sqrt(b) * rng.normal(size=x.shape)
print('after forward diffusion:', x.round(2))
print('Reverse process = a network predicting the noise added at each step.')
```

**Yaad rakho:** Zyada sampling steps matlab behtar quality aur usi hisaab se zyada compute — bas yahi poora sauda hai.

**Aam galti:** Ye maan lena ki generated images copyright ya bias se aazad hain kyunki 'model ne banayi hai'.

Practice: `examples/04_u_net_as_the_denoiser.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Sampling steps and quality trade-off

### Aasaan Bhasha

Distribution batati hai kaunsi values likely hain. Measurement noise ke liye Gaussian, haan/na ke liye Bernoulli, per-interval counts ke liye Poisson. Sahi distribution chunna hi apna loss function chunna hai: Gaussian likelihood se MSE aata hai, Bernoulli se cross-entropy.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
normal = rng.normal(loc=0, scale=1, size=10_000)
coin = rng.binomial(n=1, p=0.3, size=10_000)

print('normal mean/std', round(normal.mean(), 3), round(normal.std(), 3))
print('coin heads rate ', coin.mean())
```

**Yaad rakho:** Jab result dobara banana ho to RNG hamesha seed karo (`default_rng(0)`).

**Aam galti:** Skewed, bounded ya count data par Gaussian maan lena aur phir residuals dekh kar hairan hona.

Practice: `examples/05_sampling_steps_and_quality_trade_off.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Classifier-free guidance

### Aasaan Bhasha

Diffusion noise ulta karna seekhta hai: images me chhote steps me Gaussian noise daalo, phir network ko ek step wapas karna sikhao. Generation me aap pure noise se shuru karke baar-baar denoise karte ho, text embedding ke ishaare par. Ye GAN training se zyada stable hai aur ab images ka default hai.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
image = np.ones(8) * 0.5
betas = np.linspace(1e-4, 0.02, 10)   # noise schedule

x = image.copy()
for t, b in enumerate(betas):
    x = np.sqrt(1 - b) * x + np.sqrt(b) * rng.normal(size=x.shape)
print('after forward diffusion:', x.round(2))
print('Reverse process = a network predicting the noise added at each step.')
```

**Yaad rakho:** Zyada sampling steps matlab behtar quality aur usi hisaab se zyada compute — bas yahi poora sauda hai.

**Aam galti:** Ye maan lena ki generated images copyright ya bias se aazad hain kyunki 'model ne banayi hai'.

Practice: `examples/06_classifier_free_guidance.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Latent diffusion

### Aasaan Bhasha

Diffusion noise ulta karna seekhta hai: images me chhote steps me Gaussian noise daalo, phir network ko ek step wapas karna sikhao. Generation me aap pure noise se shuru karke baar-baar denoise karte ho, text embedding ke ishaare par. Ye GAN training se zyada stable hai aur ab images ka default hai.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
image = np.ones(8) * 0.5
betas = np.linspace(1e-4, 0.02, 10)   # noise schedule

x = image.copy()
for t, b in enumerate(betas):
    x = np.sqrt(1 - b) * x + np.sqrt(b) * rng.normal(size=x.shape)
print('after forward diffusion:', x.round(2))
print('Reverse process = a network predicting the noise added at each step.')
```

**Yaad rakho:** Zyada sampling steps matlab behtar quality aur usi hisaab se zyada compute — bas yahi poora sauda hai.

**Aam galti:** Ye maan lena ki generated images copyright ya bias se aazad hain kyunki 'model ne banayi hai'.

Practice: `examples/07_latent_diffusion.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Text conditioning

### Aasaan Bhasha

Diffusion noise ulta karna seekhta hai: images me chhote steps me Gaussian noise daalo, phir network ko ek step wapas karna sikhao. Generation me aap pure noise se shuru karke baar-baar denoise karte ho, text embedding ke ishaare par. Ye GAN training se zyada stable hai aur ab images ka default hai.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
image = np.ones(8) * 0.5
betas = np.linspace(1e-4, 0.02, 10)   # noise schedule

x = image.copy()
for t, b in enumerate(betas):
    x = np.sqrt(1 - b) * x + np.sqrt(b) * rng.normal(size=x.shape)
print('after forward diffusion:', x.round(2))
print('Reverse process = a network predicting the noise added at each step.')
```

**Yaad rakho:** Zyada sampling steps matlab behtar quality aur usi hisaab se zyada compute — bas yahi poora sauda hai.

**Aam galti:** Ye maan lena ki generated images copyright ya bias se aazad hain kyunki 'model ne banayi hai'.

Practice: `examples/08_text_conditioning.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. ControlNet and structural conditioning

### Aasaan Bhasha

Diffusion noise ulta karna seekhta hai: images me chhote steps me Gaussian noise daalo, phir network ko ek step wapas karna sikhao. Generation me aap pure noise se shuru karke baar-baar denoise karte ho, text embedding ke ishaare par. Ye GAN training se zyada stable hai aur ab images ka default hai.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
image = np.ones(8) * 0.5
betas = np.linspace(1e-4, 0.02, 10)   # noise schedule

x = image.copy()
for t, b in enumerate(betas):
    x = np.sqrt(1 - b) * x + np.sqrt(b) * rng.normal(size=x.shape)
print('after forward diffusion:', x.round(2))
print('Reverse process = a network predicting the noise added at each step.')
```

**Yaad rakho:** Zyada sampling steps matlab behtar quality aur usi hisaab se zyada compute — bas yahi poora sauda hai.

**Aam galti:** Ye maan lena ki generated images copyright ya bias se aazad hain kyunki 'model ne banayi hai'.

Practice: `examples/09_controlnet_and_structural_conditioning.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Compute cost of generation

### Aasaan Bhasha

Diffusion noise ulta karna seekhta hai: images me chhote steps me Gaussian noise daalo, phir network ko ek step wapas karna sikhao. Generation me aap pure noise se shuru karke baar-baar denoise karte ho, text embedding ke ishaare par. Ye GAN training se zyada stable hai aur ab images ka default hai.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
image = np.ones(8) * 0.5
betas = np.linspace(1e-4, 0.02, 10)   # noise schedule

x = image.copy()
for t, b in enumerate(betas):
    x = np.sqrt(1 - b) * x + np.sqrt(b) * rng.normal(size=x.shape)
print('after forward diffusion:', x.round(2))
print('Reverse process = a network predicting the noise added at each step.')
```

**Yaad rakho:** Zyada sampling steps matlab behtar quality aur usi hisaab se zyada compute — bas yahi poora sauda hai.

**Aam galti:** Ye maan lena ki generated images copyright ya bias se aazad hain kyunki 'model ne banayi hai'.

Practice: `examples/10_compute_cost_of_generation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 96 ke baad aapko ye aana chahiye

- **The forward noising process** ko bina notes dekhe kisi dost ko samjha sakna.
- **Learning to denoise** ko bina notes dekhe kisi dost ko samjha sakna.
- **The noise schedule** ko bina notes dekhe kisi dost ko samjha sakna.
- **U-Net as the denoiser** ko bina notes dekhe kisi dost ko samjha sakna.
- **Sampling steps and quality trade-off** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
