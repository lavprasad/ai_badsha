# Day 96 — Diffusion models

Today's goal: work through **Diffusion models** — ten concepts, ten runnable examples, five questions.

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

Accuracy hides everything on imbalanced data. Precision asks 'of the ones I flagged, how many were real'; recall asks 'of the real ones, how many did I catch'. You trade one for the other with the threshold, and the business decides which error hurts more.

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

**Remember:** Tune the decision threshold on validation data; 0.5 is a default, not a decision.

**Common mistake:** Optimising ROC-AUC on a heavily imbalanced problem where precision-recall AUC is the honest metric.

## 2. Learning to denoise

Diffusion learns to reverse noise: add Gaussian noise to images in small steps, then train a network to undo one step. At generation you start from pure noise and denoise repeatedly, steered by a text embedding. It is more stable than GAN training and now the default for images.

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

**Remember:** More sampling steps means better quality and linearly more compute — that is the whole trade.

**Common mistake:** Assuming generated images are free of copyright or bias concerns because 'the model made them'.

## 3. The noise schedule

Diffusion learns to reverse noise: add Gaussian noise to images in small steps, then train a network to undo one step. At generation you start from pure noise and denoise repeatedly, steered by a text embedding. It is more stable than GAN training and now the default for images.

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

**Remember:** More sampling steps means better quality and linearly more compute — that is the whole trade.

**Common mistake:** Assuming generated images are free of copyright or bias concerns because 'the model made them'.

## 4. U-Net as the denoiser

Diffusion learns to reverse noise: add Gaussian noise to images in small steps, then train a network to undo one step. At generation you start from pure noise and denoise repeatedly, steered by a text embedding. It is more stable than GAN training and now the default for images.

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

**Remember:** More sampling steps means better quality and linearly more compute — that is the whole trade.

**Common mistake:** Assuming generated images are free of copyright or bias concerns because 'the model made them'.

## 5. Sampling steps and quality trade-off

A distribution says which values are likely. Gaussian for measurement noise, Bernoulli for yes/no, Poisson for counts per interval. Choosing the right one is choosing your loss function: Gaussian likelihood gives MSE, Bernoulli gives cross-entropy.

```python
import numpy as np

rng = np.random.default_rng(0)
normal = rng.normal(loc=0, scale=1, size=10_000)
coin = rng.binomial(n=1, p=0.3, size=10_000)

print('normal mean/std', round(normal.mean(), 3), round(normal.std(), 3))
print('coin heads rate ', coin.mean())
```

**Remember:** Always seed your RNG (`default_rng(0)`) when you want a result someone else can reproduce.

**Common mistake:** Assuming Gaussian for skewed, bounded, or count data and then being surprised by the residuals.

## 6. Classifier-free guidance

Diffusion learns to reverse noise: add Gaussian noise to images in small steps, then train a network to undo one step. At generation you start from pure noise and denoise repeatedly, steered by a text embedding. It is more stable than GAN training and now the default for images.

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

**Remember:** More sampling steps means better quality and linearly more compute — that is the whole trade.

**Common mistake:** Assuming generated images are free of copyright or bias concerns because 'the model made them'.

## 7. Latent diffusion

Diffusion learns to reverse noise: add Gaussian noise to images in small steps, then train a network to undo one step. At generation you start from pure noise and denoise repeatedly, steered by a text embedding. It is more stable than GAN training and now the default for images.

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

**Remember:** More sampling steps means better quality and linearly more compute — that is the whole trade.

**Common mistake:** Assuming generated images are free of copyright or bias concerns because 'the model made them'.

## 8. Text conditioning

Diffusion learns to reverse noise: add Gaussian noise to images in small steps, then train a network to undo one step. At generation you start from pure noise and denoise repeatedly, steered by a text embedding. It is more stable than GAN training and now the default for images.

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

**Remember:** More sampling steps means better quality and linearly more compute — that is the whole trade.

**Common mistake:** Assuming generated images are free of copyright or bias concerns because 'the model made them'.

## 9. ControlNet and structural conditioning

Diffusion learns to reverse noise: add Gaussian noise to images in small steps, then train a network to undo one step. At generation you start from pure noise and denoise repeatedly, steered by a text embedding. It is more stable than GAN training and now the default for images.

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

**Remember:** More sampling steps means better quality and linearly more compute — that is the whole trade.

**Common mistake:** Assuming generated images are free of copyright or bias concerns because 'the model made them'.

## 10. Compute cost of generation

Diffusion learns to reverse noise: add Gaussian noise to images in small steps, then train a network to undo one step. At generation you start from pure noise and denoise repeatedly, steered by a text embedding. It is more stable than GAN training and now the default for images.

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

**Remember:** More sampling steps means better quality and linearly more compute — that is the whole trade.

**Common mistake:** Assuming generated images are free of copyright or bias concerns because 'the model made them'.

---

## What you should be able to do after Day 96

- Explain **The forward noising process** to someone else without notes.
- Explain **Learning to denoise** to someone else without notes.
- Explain **The noise schedule** to someone else without notes.
- Explain **U-Net as the denoiser** to someone else without notes.
- Explain **Sampling steps and quality trade-off** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
