# Day 113 — CLIP and multimodal vision

Today's goal: work through **CLIP and multimodal vision** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Joint image-text embedding space |
| 2 | Contrastive pretraining at scale |
| 3 | Zero-shot classification |
| 4 | Prompt templates for CLIP |
| 5 | Image search by description |
| 6 | Image captioning |
| 7 | Visual question answering |
| 8 | Vision-language models today |
| 9 | Failure modes of zero-shot |
| 10 | Building a semantic image search |

---

## 1. Joint image-text embedding space

A DataFrame is a table with labelled columns and an index. Most real ML work is 80% reshaping tables: load, clean, group, join, aggregate. Learn `groupby` and `merge` well and you can answer most data questions without writing loops.

```python
import pandas as pd

df = pd.DataFrame({
    'city': ['pune', 'pune', 'delhi', 'delhi'],
    'sales': [10, 20, 5, 7],
})
print(df.groupby('city')['sales'].sum())

lookup = pd.DataFrame({'city': ['pune', 'delhi'], 'zone': ['west', 'north']})
print(df.merge(lookup, on='city', how='left'))
```

**Remember:** Always check `df.shape` before and after a merge — a silent row explosion means duplicate keys.

**Common mistake:** Chained assignment (`df[df.a > 1]['b'] = 0`) that writes to a copy and changes nothing.

## 2. Contrastive pretraining at scale

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

## 3. Zero-shot classification

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

## 4. Prompt templates for CLIP

Multimodal models put images and text in one shared embedding space, so a picture of a dog lands near the words 'a dog'. That single trick gives you zero-shot classification, image search by description, and captioning — with no task-specific training.

```python
import numpy as np

# CLIP-style zero-shot: embed image and candidate captions, pick the closest
rng = np.random.default_rng(0)
image_vec = rng.normal(size=16)
image_vec /= np.linalg.norm(image_vec)

labels = ['a photo of a dog', 'a photo of a car', 'a photo of a plate of food']
label_vecs = rng.normal(size=(3, 16))
label_vecs /= np.linalg.norm(label_vecs, axis=1, keepdims=True)

scores = label_vecs @ image_vec
print('zero-shot pick:', labels[int(np.argmax(scores))], scores.round(3))
```

**Remember:** Zero-shot quality depends heavily on prompt wording — 'a photo of a {}' beats a bare noun.

**Common mistake:** Feeding an image at the wrong resolution or normalisation and getting silent quality loss.

## 5. Image search by description

Multimodal models put images and text in one shared embedding space, so a picture of a dog lands near the words 'a dog'. That single trick gives you zero-shot classification, image search by description, and captioning — with no task-specific training.

```python
import numpy as np

# CLIP-style zero-shot: embed image and candidate captions, pick the closest
rng = np.random.default_rng(0)
image_vec = rng.normal(size=16)
image_vec /= np.linalg.norm(image_vec)

labels = ['a photo of a dog', 'a photo of a car', 'a photo of a plate of food']
label_vecs = rng.normal(size=(3, 16))
label_vecs /= np.linalg.norm(label_vecs, axis=1, keepdims=True)

scores = label_vecs @ image_vec
print('zero-shot pick:', labels[int(np.argmax(scores))], scores.round(3))
```

**Remember:** Zero-shot quality depends heavily on prompt wording — 'a photo of a {}' beats a bare noun.

**Common mistake:** Feeding an image at the wrong resolution or normalisation and getting silent quality loss.

## 6. Image captioning

Multimodal models put images and text in one shared embedding space, so a picture of a dog lands near the words 'a dog'. That single trick gives you zero-shot classification, image search by description, and captioning — with no task-specific training.

```python
import numpy as np

# CLIP-style zero-shot: embed image and candidate captions, pick the closest
rng = np.random.default_rng(0)
image_vec = rng.normal(size=16)
image_vec /= np.linalg.norm(image_vec)

labels = ['a photo of a dog', 'a photo of a car', 'a photo of a plate of food']
label_vecs = rng.normal(size=(3, 16))
label_vecs /= np.linalg.norm(label_vecs, axis=1, keepdims=True)

scores = label_vecs @ image_vec
print('zero-shot pick:', labels[int(np.argmax(scores))], scores.round(3))
```

**Remember:** Zero-shot quality depends heavily on prompt wording — 'a photo of a {}' beats a bare noun.

**Common mistake:** Feeding an image at the wrong resolution or normalisation and getting silent quality loss.

## 7. Visual question answering

Multimodal models put images and text in one shared embedding space, so a picture of a dog lands near the words 'a dog'. That single trick gives you zero-shot classification, image search by description, and captioning — with no task-specific training.

```python
import numpy as np

# CLIP-style zero-shot: embed image and candidate captions, pick the closest
rng = np.random.default_rng(0)
image_vec = rng.normal(size=16)
image_vec /= np.linalg.norm(image_vec)

labels = ['a photo of a dog', 'a photo of a car', 'a photo of a plate of food']
label_vecs = rng.normal(size=(3, 16))
label_vecs /= np.linalg.norm(label_vecs, axis=1, keepdims=True)

scores = label_vecs @ image_vec
print('zero-shot pick:', labels[int(np.argmax(scores))], scores.round(3))
```

**Remember:** Zero-shot quality depends heavily on prompt wording — 'a photo of a {}' beats a bare noun.

**Common mistake:** Feeding an image at the wrong resolution or normalisation and getting silent quality loss.

## 8. Vision-language models today

Multimodal models put images and text in one shared embedding space, so a picture of a dog lands near the words 'a dog'. That single trick gives you zero-shot classification, image search by description, and captioning — with no task-specific training.

```python
import numpy as np

# CLIP-style zero-shot: embed image and candidate captions, pick the closest
rng = np.random.default_rng(0)
image_vec = rng.normal(size=16)
image_vec /= np.linalg.norm(image_vec)

labels = ['a photo of a dog', 'a photo of a car', 'a photo of a plate of food']
label_vecs = rng.normal(size=(3, 16))
label_vecs /= np.linalg.norm(label_vecs, axis=1, keepdims=True)

scores = label_vecs @ image_vec
print('zero-shot pick:', labels[int(np.argmax(scores))], scores.round(3))
```

**Remember:** Zero-shot quality depends heavily on prompt wording — 'a photo of a {}' beats a bare noun.

**Common mistake:** Feeding an image at the wrong resolution or normalisation and getting silent quality loss.

## 9. Failure modes of zero-shot

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

## 10. Building a semantic image search

Multimodal models put images and text in one shared embedding space, so a picture of a dog lands near the words 'a dog'. That single trick gives you zero-shot classification, image search by description, and captioning — with no task-specific training.

```python
import numpy as np

# CLIP-style zero-shot: embed image and candidate captions, pick the closest
rng = np.random.default_rng(0)
image_vec = rng.normal(size=16)
image_vec /= np.linalg.norm(image_vec)

labels = ['a photo of a dog', 'a photo of a car', 'a photo of a plate of food']
label_vecs = rng.normal(size=(3, 16))
label_vecs /= np.linalg.norm(label_vecs, axis=1, keepdims=True)

scores = label_vecs @ image_vec
print('zero-shot pick:', labels[int(np.argmax(scores))], scores.round(3))
```

**Remember:** Zero-shot quality depends heavily on prompt wording — 'a photo of a {}' beats a bare noun.

**Common mistake:** Feeding an image at the wrong resolution or normalisation and getting silent quality loss.

---

## What you should be able to do after Day 113

- Explain **Joint image-text embedding space** to someone else without notes.
- Explain **Contrastive pretraining at scale** to someone else without notes.
- Explain **Zero-shot classification** to someone else without notes.
- Explain **Prompt templates for CLIP** to someone else without notes.
- Explain **Image search by description** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
