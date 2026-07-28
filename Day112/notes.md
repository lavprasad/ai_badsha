# Day 112 — Self-supervised vision

Today's goal: work through **Self-supervised vision** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Learning without labels |
| 2 | Contrastive learning: SimCLR |
| 3 | MoCo and memory banks |
| 4 | BYOL without negatives |
| 5 | Masked autoencoders |
| 6 | DINO and self-distillation |
| 7 | Evaluating with linear probes |
| 8 | Pretraining on your own unlabelled data |
| 9 | When self-supervision pays off |
| 10 | Compute realities |

---

## 1. Learning without labels

Self-supervised learning invents a task from the data itself — match two augmented views of the same image, or reconstruct masked patches — so you can pretrain on unlabelled data. It pays off when you have millions of unlabelled samples and few labels, and it is expensive otherwise.

```python
import numpy as np

def nt_xent(z1, z2, temperature=0.5):
    """Contrastive loss: two views of the same item should be closest to each other."""
    z1 = z1 / np.linalg.norm(z1, axis=1, keepdims=True)
    z2 = z2 / np.linalg.norm(z2, axis=1, keepdims=True)
    sim = z1 @ z2.T / temperature
    sim -= sim.max(axis=1, keepdims=True)
    p = np.exp(sim) / np.exp(sim).sum(axis=1, keepdims=True)
    return float(-np.mean(np.log(np.diag(p) + 1e-12)))

rng = np.random.default_rng(0)
base = rng.normal(size=(8, 16))
print('aligned views loss  ', round(nt_xent(base, base + 0.01 * rng.normal(size=base.shape)), 4))
print('unrelated views loss', round(nt_xent(base, rng.normal(size=(8, 16))), 4))
```

**Remember:** The augmentations *are* the supervision — they define what the model learns to treat as irrelevant.

**Common mistake:** Spending weeks on self-supervised pretraining when a public pretrained backbone was already better.

## 2. Contrastive learning: SimCLR

Self-supervised learning invents a task from the data itself — match two augmented views of the same image, or reconstruct masked patches — so you can pretrain on unlabelled data. It pays off when you have millions of unlabelled samples and few labels, and it is expensive otherwise.

```python
import numpy as np

def nt_xent(z1, z2, temperature=0.5):
    """Contrastive loss: two views of the same item should be closest to each other."""
    z1 = z1 / np.linalg.norm(z1, axis=1, keepdims=True)
    z2 = z2 / np.linalg.norm(z2, axis=1, keepdims=True)
    sim = z1 @ z2.T / temperature
    sim -= sim.max(axis=1, keepdims=True)
    p = np.exp(sim) / np.exp(sim).sum(axis=1, keepdims=True)
    return float(-np.mean(np.log(np.diag(p) + 1e-12)))

rng = np.random.default_rng(0)
base = rng.normal(size=(8, 16))
print('aligned views loss  ', round(nt_xent(base, base + 0.01 * rng.normal(size=base.shape)), 4))
print('unrelated views loss', round(nt_xent(base, rng.normal(size=(8, 16))), 4))
```

**Remember:** The augmentations *are* the supervision — they define what the model learns to treat as irrelevant.

**Common mistake:** Spending weeks on self-supervised pretraining when a public pretrained backbone was already better.

## 3. MoCo and memory banks

Self-supervised learning invents a task from the data itself — match two augmented views of the same image, or reconstruct masked patches — so you can pretrain on unlabelled data. It pays off when you have millions of unlabelled samples and few labels, and it is expensive otherwise.

```python
import numpy as np

def nt_xent(z1, z2, temperature=0.5):
    """Contrastive loss: two views of the same item should be closest to each other."""
    z1 = z1 / np.linalg.norm(z1, axis=1, keepdims=True)
    z2 = z2 / np.linalg.norm(z2, axis=1, keepdims=True)
    sim = z1 @ z2.T / temperature
    sim -= sim.max(axis=1, keepdims=True)
    p = np.exp(sim) / np.exp(sim).sum(axis=1, keepdims=True)
    return float(-np.mean(np.log(np.diag(p) + 1e-12)))

rng = np.random.default_rng(0)
base = rng.normal(size=(8, 16))
print('aligned views loss  ', round(nt_xent(base, base + 0.01 * rng.normal(size=base.shape)), 4))
print('unrelated views loss', round(nt_xent(base, rng.normal(size=(8, 16))), 4))
```

**Remember:** The augmentations *are* the supervision — they define what the model learns to treat as irrelevant.

**Common mistake:** Spending weeks on self-supervised pretraining when a public pretrained backbone was already better.

## 4. BYOL without negatives

Self-supervised learning invents a task from the data itself — match two augmented views of the same image, or reconstruct masked patches — so you can pretrain on unlabelled data. It pays off when you have millions of unlabelled samples and few labels, and it is expensive otherwise.

```python
import numpy as np

def nt_xent(z1, z2, temperature=0.5):
    """Contrastive loss: two views of the same item should be closest to each other."""
    z1 = z1 / np.linalg.norm(z1, axis=1, keepdims=True)
    z2 = z2 / np.linalg.norm(z2, axis=1, keepdims=True)
    sim = z1 @ z2.T / temperature
    sim -= sim.max(axis=1, keepdims=True)
    p = np.exp(sim) / np.exp(sim).sum(axis=1, keepdims=True)
    return float(-np.mean(np.log(np.diag(p) + 1e-12)))

rng = np.random.default_rng(0)
base = rng.normal(size=(8, 16))
print('aligned views loss  ', round(nt_xent(base, base + 0.01 * rng.normal(size=base.shape)), 4))
print('unrelated views loss', round(nt_xent(base, rng.normal(size=(8, 16))), 4))
```

**Remember:** The augmentations *are* the supervision — they define what the model learns to treat as irrelevant.

**Common mistake:** Spending weeks on self-supervised pretraining when a public pretrained backbone was already better.

## 5. Masked autoencoders

An autoencoder squeezes input through a narrow bottleneck and reconstructs it, forcing a compact representation. A VAE makes that bottleneck a distribution so you can sample new data from it. Both are useful for anomaly detection: high reconstruction error means 'unlike anything I trained on'.

```python
import numpy as np

# Linear autoencoder == PCA. Reconstruction error flags anomalies.
rng = np.random.default_rng(0)
normal = rng.normal(size=(500, 10))
U, S, Vt = np.linalg.svd(normal - normal.mean(0), full_matrices=False)
code = Vt[:3]                              # 3-D bottleneck

def recon_error(x):
    z = (x - normal.mean(0)) @ code.T
    return float(np.linalg.norm((x - normal.mean(0)) - z @ code))

print('normal point ', round(recon_error(normal[0]), 3))
print('anomaly      ', round(recon_error(np.full(10, 12.0)), 3))
```

**Remember:** Reconstruction error is a ready-made anomaly score — no labels required.

**Common mistake:** Making the bottleneck as wide as the input, so the network learns the identity function.

## 6. DINO and self-distillation

Self-supervised learning invents a task from the data itself — match two augmented views of the same image, or reconstruct masked patches — so you can pretrain on unlabelled data. It pays off when you have millions of unlabelled samples and few labels, and it is expensive otherwise.

```python
import numpy as np

def nt_xent(z1, z2, temperature=0.5):
    """Contrastive loss: two views of the same item should be closest to each other."""
    z1 = z1 / np.linalg.norm(z1, axis=1, keepdims=True)
    z2 = z2 / np.linalg.norm(z2, axis=1, keepdims=True)
    sim = z1 @ z2.T / temperature
    sim -= sim.max(axis=1, keepdims=True)
    p = np.exp(sim) / np.exp(sim).sum(axis=1, keepdims=True)
    return float(-np.mean(np.log(np.diag(p) + 1e-12)))

rng = np.random.default_rng(0)
base = rng.normal(size=(8, 16))
print('aligned views loss  ', round(nt_xent(base, base + 0.01 * rng.normal(size=base.shape)), 4))
print('unrelated views loss', round(nt_xent(base, rng.normal(size=(8, 16))), 4))
```

**Remember:** The augmentations *are* the supervision — they define what the model learns to treat as irrelevant.

**Common mistake:** Spending weeks on self-supervised pretraining when a public pretrained backbone was already better.

## 7. Evaluating with linear probes

Vibes do not survive a prompt change. Build a small golden set of real inputs with expected outputs, run it on every change, and track the score. Use an LLM judge for open-ended quality, but calibrate the judge against human ratings first.

```python
GOLDEN = [
    {'input': 'charged twice', 'expect': 'BILLING'},
    {'input': 'crashes on upload', 'expect': 'BUG'},
    {'input': 'please add dark mode', 'expect': 'FEATURE'},
]

def classify(text):                      # stand-in for the real model call
    t = text.lower()
    if 'charg' in t or 'bill' in t:
        return 'BILLING'
    if 'crash' in t or 'error' in t:
        return 'BUG'
    return 'FEATURE'

hits = sum(classify(c['input']) == c['expect'] for c in GOLDEN)
print(f'eval score {hits}/{len(GOLDEN)}')
assert hits == len(GOLDEN), 'regression: fix before shipping'
```

**Remember:** 50 real examples you curated beat 5000 synthetic ones nobody checked.

**Common mistake:** Changing the prompt on Friday with no eval and finding out from customers on Monday.

## 8. Pretraining on your own unlabelled data

Pretraining is one absurdly simple objective at enormous scale: predict the next token. Everything else — grammar, facts, reasoning traces, style — falls out of doing that well over trillions of tokens. Scaling laws say loss falls predictably with model size, data and compute together.

```python
from collections import defaultdict, Counter
import random

text = 'the cat sat on the mat the cat ate the rat'.split()
model = defaultdict(Counter)
for a, b in zip(text, text[1:]):
    model[a][b] += 1

random.seed(0)
word, out = 'the', ['the']
for _ in range(6):
    nxt = model[word].most_common(1)[0][0] if model[word] else 'the'
    out.append(nxt)
    word = nxt
print(' '.join(out))   # a 2-gram LM: same objective, 10 orders of magnitude smaller
```

**Remember:** A bigger model trained on too little data is a waste — compute, parameters and tokens scale together.

**Common mistake:** Believing a base model will follow instructions; that behaviour comes from the tuning stages after.

## 9. When self-supervision pays off

Self-supervised learning invents a task from the data itself — match two augmented views of the same image, or reconstruct masked patches — so you can pretrain on unlabelled data. It pays off when you have millions of unlabelled samples and few labels, and it is expensive otherwise.

```python
import numpy as np

def nt_xent(z1, z2, temperature=0.5):
    """Contrastive loss: two views of the same item should be closest to each other."""
    z1 = z1 / np.linalg.norm(z1, axis=1, keepdims=True)
    z2 = z2 / np.linalg.norm(z2, axis=1, keepdims=True)
    sim = z1 @ z2.T / temperature
    sim -= sim.max(axis=1, keepdims=True)
    p = np.exp(sim) / np.exp(sim).sum(axis=1, keepdims=True)
    return float(-np.mean(np.log(np.diag(p) + 1e-12)))

rng = np.random.default_rng(0)
base = rng.normal(size=(8, 16))
print('aligned views loss  ', round(nt_xent(base, base + 0.01 * rng.normal(size=base.shape)), 4))
print('unrelated views loss', round(nt_xent(base, rng.normal(size=(8, 16))), 4))
```

**Remember:** The augmentations *are* the supervision — they define what the model learns to treat as irrelevant.

**Common mistake:** Spending weeks on self-supervised pretraining when a public pretrained backbone was already better.

## 10. Compute realities

Self-supervised learning invents a task from the data itself — match two augmented views of the same image, or reconstruct masked patches — so you can pretrain on unlabelled data. It pays off when you have millions of unlabelled samples and few labels, and it is expensive otherwise.

```python
import numpy as np

def nt_xent(z1, z2, temperature=0.5):
    """Contrastive loss: two views of the same item should be closest to each other."""
    z1 = z1 / np.linalg.norm(z1, axis=1, keepdims=True)
    z2 = z2 / np.linalg.norm(z2, axis=1, keepdims=True)
    sim = z1 @ z2.T / temperature
    sim -= sim.max(axis=1, keepdims=True)
    p = np.exp(sim) / np.exp(sim).sum(axis=1, keepdims=True)
    return float(-np.mean(np.log(np.diag(p) + 1e-12)))

rng = np.random.default_rng(0)
base = rng.normal(size=(8, 16))
print('aligned views loss  ', round(nt_xent(base, base + 0.01 * rng.normal(size=base.shape)), 4))
print('unrelated views loss', round(nt_xent(base, rng.normal(size=(8, 16))), 4))
```

**Remember:** The augmentations *are* the supervision — they define what the model learns to treat as irrelevant.

**Common mistake:** Spending weeks on self-supervised pretraining when a public pretrained backbone was already better.

---

## What you should be able to do after Day 112

- Explain **Learning without labels** to someone else without notes.
- Explain **Contrastive learning: SimCLR** to someone else without notes.
- Explain **MoCo and memory banks** to someone else without notes.
- Explain **BYOL without negatives** to someone else without notes.
- Explain **Masked autoencoders** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
