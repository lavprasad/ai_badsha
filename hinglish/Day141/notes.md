# Day 141 — Multimodal models

Aaj ka goal: **Multimodal models** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Text plus image inputs |
| 2 | How images become tokens |
| 3 | Document and chart understanding |
| 4 | Video understanding with LLMs |
| 5 | Audio-native models |
| 6 | Multimodal prompting patterns |
| 7 | Failure modes on fine detail |
| 8 | Cost of image tokens |
| 9 | Choosing OCR vs a vision model |
| 10 | A screenshot-to-data pipeline |

---

## 1. Text plus image inputs

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

Practice: `examples/01_text_plus_image_inputs.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. How images become tokens

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

Practice: `examples/02_how_images_become_tokens.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Document and chart understanding

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

Practice: `examples/03_document_and_chart_understanding.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Video understanding with LLMs

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

Practice: `examples/04_video_understanding_with_llms.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Audio-native models

### Aasaan Bhasha

Audio spectrogram ban jaata hai — ek axis par time, doosri par frequency — aur uske baad ye image problem hi hai. ASR speech ko text me badalta hai; TTS ulta karta hai. Training data me accent aur background-noise bias par nazar rakho.

### Chhota code

```python
import numpy as np

sr = 16_000
t = np.linspace(0, 1, sr, endpoint=False)
signal = np.sin(2 * np.pi * 440 * t) + 0.5 * np.sin(2 * np.pi * 880 * t)

spectrum = np.abs(np.fft.rfft(signal))
freqs = np.fft.rfftfreq(len(signal), 1 / sr)
peaks = freqs[np.argsort(-spectrum)[:2]]
print('dominant frequencies (Hz):', np.sort(peaks))   # ~440 and ~880
```

**Yaad rakho:** Inference se pehle sab kuch model ke expected sample rate par resample karo.

**Aam galti:** ASR ko sirf saaf studio audio par evaluate karna, phir shor wale call centre me deploy kar dena.

Practice: `examples/05_audio_native_models.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Multimodal prompting patterns

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

Practice: `examples/06_multimodal_prompting_patterns.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Failure modes on fine detail

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

Practice: `examples/07_failure_modes_on_fine_detail.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Cost of image tokens

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

Practice: `examples/08_cost_of_image_tokens.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Choosing OCR vs a vision model

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

Practice: `examples/09_choosing_ocr_vs_a_vision_model.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. A screenshot-to-data pipeline

### Aasaan Bhasha

Pipeline preprocessing aur model ko ek hi object me jod deta hai jo ek unit ki tarah fit aur predict karta hai. Leakage ke khilaaf yahi sabse achhi dhaal hai, aur deployment ko chhe alag steps ke bajaye ek artefact milta hai jise yaad rakhne ki zaroorat nahi.

### Chhota code

```python
import numpy as np, pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression

df = pd.DataFrame({'age': [25, np.nan, 40, 33], 'city': ['pune', 'delhi', 'pune', 'delhi']})
y = [0, 1, 0, 1]

pre = ColumnTransformer([
    ('num', Pipeline([('imp', SimpleImputer(strategy='median')), ('sc', StandardScaler())]), ['age']),
    ('cat', OneHotEncoder(handle_unknown='ignore'), ['city']),
])
model = Pipeline([('pre', pre), ('clf', LogisticRegression())]).fit(df, y)
print(model.predict(df))
```

**Yaad rakho:** `handle_unknown='ignore'` production ko us category par crash hone se bachata hai jo training me kabhi nahi dikhi.

**Aam galti:** Notebook me preprocess karna aur serving code likhte waqt ek step bhool jaana.

Practice: `examples/10_a_screenshot_to_data_pipeline.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 141 ke baad aapko ye aana chahiye

- **Text plus image inputs** ko bina notes dekhe kisi dost ko samjha sakna.
- **How images become tokens** ko bina notes dekhe kisi dost ko samjha sakna.
- **Document and chart understanding** ko bina notes dekhe kisi dost ko samjha sakna.
- **Video understanding with LLMs** ko bina notes dekhe kisi dost ko samjha sakna.
- **Audio-native models** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
