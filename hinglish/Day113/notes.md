# Day 113 — CLIP and multimodal vision

Aaj ka goal: **CLIP and multimodal vision** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

### Aasaan Bhasha

DataFrame ek table hai jisme labelled columns aur ek index hota hai. Asli ML ka 80% kaam tables ko reshape karna hi hai: load, clean, group, join, aggregate. `groupby` aur `merge` acche se seekh lo to zyadatar data sawaal bina loop likhe hal ho jaate hain.

### Chhota code

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

**Yaad rakho:** Merge se pehle aur baad me `df.shape` zaroor check karo — chupke se rows badhna matlab duplicate keys.

**Aam galti:** Chained assignment (`df[df.a > 1]['b'] = 0`) jo copy par likhta hai aur kuch nahi badalta.

Practice: `examples/01_joint_image_text_embedding_space.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Contrastive pretraining at scale

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

Practice: `examples/02_contrastive_pretraining_at_scale.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Zero-shot classification

### Aasaan Bhasha

Prompt English me likha gaya program hai. Role, task, format aur constraints ke baare me specific raho. Few-shot examples format kisi bhi description se behtar sikhaate hain. Reasoning steps maangna multi-step problems par madad karta hai aur simple lookups par tokens barbaad karta hai.

### Chhota code

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

**Yaad rakho:** Output format sabse aakhir me rakho aur use example ki tarah dikhao — models sabse paas wala pattern copy karte hain.

**Aam galti:** Dhundhla prompt likhna, dhundhla output paana, aur model ko dosh dena.

Practice: `examples/03_zero_shot_classification.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Prompt templates for CLIP

### Aasaan Bhasha

Multimodal models images aur text ko ek hi shared embedding space me daal dete hain, isliye kutte ki photo 'a dog' shabdon ke paas girti hai. Isi ek trick se aapko zero-shot classification, description se image search, aur captioning mil jaate hain — bina kisi task-specific training ke.

### Chhota code

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

**Yaad rakho:** Zero-shot quality prompt ki wording par bahut depend karti hai — 'a photo of a {}' saade noun se behtar hai.

**Aam galti:** Image ko galat resolution ya normalisation par dena aur chupchap quality khona.

Practice: `examples/04_prompt_templates_for_clip.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Image search by description

### Aasaan Bhasha

Multimodal models images aur text ko ek hi shared embedding space me daal dete hain, isliye kutte ki photo 'a dog' shabdon ke paas girti hai. Isi ek trick se aapko zero-shot classification, description se image search, aur captioning mil jaate hain — bina kisi task-specific training ke.

### Chhota code

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

**Yaad rakho:** Zero-shot quality prompt ki wording par bahut depend karti hai — 'a photo of a {}' saade noun se behtar hai.

**Aam galti:** Image ko galat resolution ya normalisation par dena aur chupchap quality khona.

Practice: `examples/05_image_search_by_description.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Image captioning

### Aasaan Bhasha

Multimodal models images aur text ko ek hi shared embedding space me daal dete hain, isliye kutte ki photo 'a dog' shabdon ke paas girti hai. Isi ek trick se aapko zero-shot classification, description se image search, aur captioning mil jaate hain — bina kisi task-specific training ke.

### Chhota code

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

**Yaad rakho:** Zero-shot quality prompt ki wording par bahut depend karti hai — 'a photo of a {}' saade noun se behtar hai.

**Aam galti:** Image ko galat resolution ya normalisation par dena aur chupchap quality khona.

Practice: `examples/06_image_captioning.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Visual question answering

### Aasaan Bhasha

Multimodal models images aur text ko ek hi shared embedding space me daal dete hain, isliye kutte ki photo 'a dog' shabdon ke paas girti hai. Isi ek trick se aapko zero-shot classification, description se image search, aur captioning mil jaate hain — bina kisi task-specific training ke.

### Chhota code

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

**Yaad rakho:** Zero-shot quality prompt ki wording par bahut depend karti hai — 'a photo of a {}' saade noun se behtar hai.

**Aam galti:** Image ko galat resolution ya normalisation par dena aur chupchap quality khona.

Practice: `examples/07_visual_question_answering.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Vision-language models today

### Aasaan Bhasha

Multimodal models images aur text ko ek hi shared embedding space me daal dete hain, isliye kutte ki photo 'a dog' shabdon ke paas girti hai. Isi ek trick se aapko zero-shot classification, description se image search, aur captioning mil jaate hain — bina kisi task-specific training ke.

### Chhota code

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

**Yaad rakho:** Zero-shot quality prompt ki wording par bahut depend karti hai — 'a photo of a {}' saade noun se behtar hai.

**Aam galti:** Image ko galat resolution ya normalisation par dena aur chupchap quality khona.

Practice: `examples/08_vision_language_models_today.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Failure modes of zero-shot

### Aasaan Bhasha

Prompt English me likha gaya program hai. Role, task, format aur constraints ke baare me specific raho. Few-shot examples format kisi bhi description se behtar sikhaate hain. Reasoning steps maangna multi-step problems par madad karta hai aur simple lookups par tokens barbaad karta hai.

### Chhota code

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

**Yaad rakho:** Output format sabse aakhir me rakho aur use example ki tarah dikhao — models sabse paas wala pattern copy karte hain.

**Aam galti:** Dhundhla prompt likhna, dhundhla output paana, aur model ko dosh dena.

Practice: `examples/09_failure_modes_of_zero_shot.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Building a semantic image search

### Aasaan Bhasha

Multimodal models images aur text ko ek hi shared embedding space me daal dete hain, isliye kutte ki photo 'a dog' shabdon ke paas girti hai. Isi ek trick se aapko zero-shot classification, description se image search, aur captioning mil jaate hain — bina kisi task-specific training ke.

### Chhota code

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

**Yaad rakho:** Zero-shot quality prompt ki wording par bahut depend karti hai — 'a photo of a {}' saade noun se behtar hai.

**Aam galti:** Image ko galat resolution ya normalisation par dena aur chupchap quality khona.

Practice: `examples/10_building_a_semantic_image_search.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 113 ke baad aapko ye aana chahiye

- **Joint image-text embedding space** ko bina notes dekhe kisi dost ko samjha sakna.
- **Contrastive pretraining at scale** ko bina notes dekhe kisi dost ko samjha sakna.
- **Zero-shot classification** ko bina notes dekhe kisi dost ko samjha sakna.
- **Prompt templates for CLIP** ko bina notes dekhe kisi dost ko samjha sakna.
- **Image search by description** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
