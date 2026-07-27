# Day 115 — Image generation in practice

Today's goal: work through **image generation in practice** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Text-to-image workflow |
| 2 | Prompting for images |
| 3 | Negative prompts |
| 4 | Image-to-image and inpainting |
| 5 | Guidance scale and steps |
| 6 | Seeds and reproducibility |
| 7 | LoRA for style adaptation |
| 8 | Upscaling |
| 9 | Content provenance and watermarking |
| 10 | Copyright and dataset questions |

---

## 1. Text-to-image workflow

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

## 2. Prompting for images

A prompt is a program written in English. Be specific about role, task, format and constraints. Few-shot examples teach format better than any description. Asking for reasoning steps helps on multi-step problems and wastes tokens on simple lookups.

```python
prompt = '''You are a support triage assistant.

Classify the ticket into exactly one of: BILLING, BUG, FEATURE, OTHER.
Return JSON only: {"label": ..., "confidence": 0.0-1.0}

Examples:
Ticket: "charged twice this month" -> {"label": "BILLING", "confidence": 0.95}
Ticket: "app crashes on upload"    -> {"label": "BUG", "confidence": 0.92}

Ticket: "can you add dark mode?"
'''
print(prompt)
print('Structure: role -> task -> allowed outputs -> format -> examples -> input.')
```

**Remember:** Put the output format last and show it as an example — models copy the nearest pattern.

**Common mistake:** Writing a vague prompt, getting vague output, and blaming the model.

## 3. Negative prompts

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

## 4. Image-to-image and inpainting

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

## 5. Guidance scale and steps

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

## 6. Seeds and reproducibility

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

## 7. LoRA for style adaptation

LoRA freezes the base weights and trains two small low-rank matrices whose product is added to each target layer. You update ~0.1% of the parameters, the checkpoint is megabytes not gigabytes, and you can swap adapters per customer. QLoRA adds 4-bit base weights so a 7B model fits on one consumer GPU.

```python
import numpy as np

d, r = 512, 8                      # full dim vs LoRA rank
rng = np.random.default_rng(0)
W = rng.normal(size=(d, d)) * 0.02  # frozen base weight
A = rng.normal(size=(d, r)) * 0.01  # trainable
B = np.zeros((r, d))                # trainable, starts at zero -> no change at step 0

delta = A @ B
print('base params   ', W.size)
print('lora params   ', A.size + B.size, f'({100 * (A.size + B.size) / W.size:.1f}%)')
print('effective W = W + A@B, shape', (W + delta).shape)
```

**Remember:** Initialise B to zeros so the adapted model starts exactly equal to the base model.

**Common mistake:** Setting rank far too high — you lose the efficiency and gain the overfitting.

## 8. Upscaling

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

## 9. Content provenance and watermarking

Missing data is information, not just noise. Before filling anything, ask *why* it is missing: a sensor that fails only under load is not missing at random. Then choose: drop rows, drop the column, fill with a statistic, or add an explicit 'was missing' indicator column.

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'age': [25, np.nan, 40, np.nan]})
print(df.isna().sum())

df['age_missing'] = df['age'].isna().astype(int)   # keep the signal
df['age'] = df['age'].fillna(df['age'].median())    # then fill
print(df)
```

**Remember:** Compute the fill statistic on the TRAIN split only, then apply it to test.

**Common mistake:** Filling with the mean computed over the full dataset — that leaks test information into training.

## 10. Copyright and dataset questions

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

## What you should be able to do after Day 115

- Explain **Text-to-image workflow** to someone else without notes.
- Explain **Prompting for images** to someone else without notes.
- Explain **Negative prompts** to someone else without notes.
- Explain **Image-to-image and inpainting** to someone else without notes.
- Explain **Guidance scale and steps** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
