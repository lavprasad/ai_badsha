# Day 112 — Self-supervised vision

Aaj ka goal: **Self-supervised vision** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

### Aasaan Bhasha

Self-supervised learning data se hi ek task gadh leta hai — ek image ke do augmented views match karo, ya masked patches wapas banao — taaki aap bina labels wale data par pretrain kar sako. Ye tab faayda deta hai jab aapke paas laakhon unlabelled samples hon aur labels kam, warna ye mehnga hai.

### Chhota code

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

**Yaad rakho:** Augmentations hi supervision hain — wahi tay karte hain ki model kis cheez ko bemaani maanega.

**Aam galti:** Hafton self-supervised pretraining karna jab ek public pretrained backbone pehle se behtar tha.

Practice: `examples/01_learning_without_labels.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Contrastive learning: SimCLR

### Aasaan Bhasha

Self-supervised learning data se hi ek task gadh leta hai — ek image ke do augmented views match karo, ya masked patches wapas banao — taaki aap bina labels wale data par pretrain kar sako. Ye tab faayda deta hai jab aapke paas laakhon unlabelled samples hon aur labels kam, warna ye mehnga hai.

### Chhota code

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

**Yaad rakho:** Augmentations hi supervision hain — wahi tay karte hain ki model kis cheez ko bemaani maanega.

**Aam galti:** Hafton self-supervised pretraining karna jab ek public pretrained backbone pehle se behtar tha.

Practice: `examples/02_contrastive_learning_simclr.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. MoCo and memory banks

### Aasaan Bhasha

Self-supervised learning data se hi ek task gadh leta hai — ek image ke do augmented views match karo, ya masked patches wapas banao — taaki aap bina labels wale data par pretrain kar sako. Ye tab faayda deta hai jab aapke paas laakhon unlabelled samples hon aur labels kam, warna ye mehnga hai.

### Chhota code

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

**Yaad rakho:** Augmentations hi supervision hain — wahi tay karte hain ki model kis cheez ko bemaani maanega.

**Aam galti:** Hafton self-supervised pretraining karna jab ek public pretrained backbone pehle se behtar tha.

Practice: `examples/03_moco_and_memory_banks.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. BYOL without negatives

### Aasaan Bhasha

Self-supervised learning data se hi ek task gadh leta hai — ek image ke do augmented views match karo, ya masked patches wapas banao — taaki aap bina labels wale data par pretrain kar sako. Ye tab faayda deta hai jab aapke paas laakhon unlabelled samples hon aur labels kam, warna ye mehnga hai.

### Chhota code

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

**Yaad rakho:** Augmentations hi supervision hain — wahi tay karte hain ki model kis cheez ko bemaani maanega.

**Aam galti:** Hafton self-supervised pretraining karna jab ek public pretrained backbone pehle se behtar tha.

Practice: `examples/04_byol_without_negatives.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Masked autoencoders

### Aasaan Bhasha

Autoencoder input ko ek patli bottleneck se nichodta hai aur wapas banata hai, jisse ek compact representation banna majboori ho jaati hai. VAE us bottleneck ko distribution bana deta hai taaki aap usse naya data sample kar sako. Dono anomaly detection ke liye kaam ke hain: zyada reconstruction error matlab 'jaisa maine train kiya usse alag'.

### Chhota code

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

**Yaad rakho:** Reconstruction error khud hi ek anomaly score hai — labels ki zaroorat hi nahi.

**Aam galti:** Bottleneck ko input jitna hi chauda kar dena, jisse network sirf identity function seekh leta hai.

Practice: `examples/05_masked_autoencoders.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. DINO and self-distillation

### Aasaan Bhasha

Self-supervised learning data se hi ek task gadh leta hai — ek image ke do augmented views match karo, ya masked patches wapas banao — taaki aap bina labels wale data par pretrain kar sako. Ye tab faayda deta hai jab aapke paas laakhon unlabelled samples hon aur labels kam, warna ye mehnga hai.

### Chhota code

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

**Yaad rakho:** Augmentations hi supervision hain — wahi tay karte hain ki model kis cheez ko bemaani maanega.

**Aam galti:** Hafton self-supervised pretraining karna jab ek public pretrained backbone pehle se behtar tha.

Practice: `examples/06_dino_and_self_distillation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Evaluating with linear probes

### Aasaan Bhasha

Vibes prompt change se nahi bachte. Asli inputs ka chhota golden set banao expected outputs ke saath, har change par chalao, aur score track karo. Open-ended quality ke liye LLM judge use karo, par pehle judge ko human ratings se calibrate karo.

### Chhota code

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

**Yaad rakho:** Aapke chune hue 50 asli examples 5000 synthetic examples se behtar hain jinhe kisi ne check hi nahi kiya.

**Aam galti:** Shukravaar ko bina eval ke prompt badalna aur somvaar ko customers se pata chalna.

Practice: `examples/07_evaluating_with_linear_probes.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Pretraining on your own unlabelled data

### Aasaan Bhasha

Pretraining ek behad simple objective hai bade paimane par: agla token predict karo. Baaki sab — grammar, facts, reasoning, style — trillions tokens par ise achhe se karne se hi nikal aata hai. Scaling laws kehte hain ki model size, data aur compute saath badhne par loss predictably girta hai.

### Chhota code

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

**Yaad rakho:** Bahut kam data par bada model barbaadi hai — compute, parameters aur tokens saath scale hote hain.

**Aam galti:** Ye maanna ki base model instructions follow karega; wo behaviour baad ke tuning stages se aata hai.

Practice: `examples/08_pretraining_on_your_own_unlabelled_data.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. When self-supervision pays off

### Aasaan Bhasha

Self-supervised learning data se hi ek task gadh leta hai — ek image ke do augmented views match karo, ya masked patches wapas banao — taaki aap bina labels wale data par pretrain kar sako. Ye tab faayda deta hai jab aapke paas laakhon unlabelled samples hon aur labels kam, warna ye mehnga hai.

### Chhota code

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

**Yaad rakho:** Augmentations hi supervision hain — wahi tay karte hain ki model kis cheez ko bemaani maanega.

**Aam galti:** Hafton self-supervised pretraining karna jab ek public pretrained backbone pehle se behtar tha.

Practice: `examples/09_when_self_supervision_pays_off.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Compute realities

### Aasaan Bhasha

Self-supervised learning data se hi ek task gadh leta hai — ek image ke do augmented views match karo, ya masked patches wapas banao — taaki aap bina labels wale data par pretrain kar sako. Ye tab faayda deta hai jab aapke paas laakhon unlabelled samples hon aur labels kam, warna ye mehnga hai.

### Chhota code

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

**Yaad rakho:** Augmentations hi supervision hain — wahi tay karte hain ki model kis cheez ko bemaani maanega.

**Aam galti:** Hafton self-supervised pretraining karna jab ek public pretrained backbone pehle se behtar tha.

Practice: `examples/10_compute_realities.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 112 ke baad aapko ye aana chahiye

- **Learning without labels** ko bina notes dekhe kisi dost ko samjha sakna.
- **Contrastive learning: SimCLR** ko bina notes dekhe kisi dost ko samjha sakna.
- **MoCo and memory banks** ko bina notes dekhe kisi dost ko samjha sakna.
- **BYOL without negatives** ko bina notes dekhe kisi dost ko samjha sakna.
- **Masked autoencoders** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
