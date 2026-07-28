# Day 141 — Multimodal models

Today's goal: work through **Multimodal models** — ten concepts, ten runnable examples, five questions.

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

Practice: open `examples/01_text_plus_image_inputs.py`, predict the output, change one line, predict again.

## 2. How images become tokens

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

Practice: open `examples/02_how_images_become_tokens.py`, predict the output, change one line, predict again.

## 3. Document and chart understanding

Plot before you model. A histogram exposes skew and outliers, a scatter exposes non-linearity, and a line of residuals exposes a model that is systematically wrong. Five minutes of plotting saves hours of confused tuning.

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

**Remember:** Label the axes. An unlabelled plot is a decoration, not evidence.

**Common mistake:** Judging a model by its accuracy number alone without ever looking at the data.

Practice: open `examples/03_document_and_chart_understanding.py`, predict the output, change one line, predict again.

## 4. Video understanding with LLMs

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

Practice: open `examples/04_video_understanding_with_llms.py`, predict the output, change one line, predict again.

## 5. Audio-native models

Audio becomes a spectrogram — time on one axis, frequency on the other — and from there it is an image problem. ASR transcribes speech to text; TTS goes the other way. Watch for accent and background-noise bias in the training data.

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

**Remember:** Resample everything to the model's expected sample rate before inference.

**Common mistake:** Evaluating ASR only on clean studio audio, then deploying to a noisy call centre.

Practice: open `examples/05_audio_native_models.py`, predict the output, change one line, predict again.

## 6. Multimodal prompting patterns

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

Practice: open `examples/06_multimodal_prompting_patterns.py`, predict the output, change one line, predict again.

## 7. Failure modes on fine detail

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

Practice: open `examples/07_failure_modes_on_fine_detail.py`, predict the output, change one line, predict again.

## 8. Cost of image tokens

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

Practice: open `examples/08_cost_of_image_tokens.py`, predict the output, change one line, predict again.

## 9. Choosing OCR vs a vision model

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

Practice: open `examples/09_choosing_ocr_vs_a_vision_model.py`, predict the output, change one line, predict again.

## 10. A screenshot-to-data pipeline

A Pipeline chains preprocessing and the model into one object that fits and predicts as a unit. This is the single best defence against leakage, and it means deployment ships one artefact instead of six loose steps you must remember to repeat.

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

**Remember:** `handle_unknown='ignore'` stops production crashing on a category you never saw in training.

**Common mistake:** Preprocessing in a notebook and then forgetting one step when writing the serving code.

Practice: open `examples/10_a_screenshot_to_data_pipeline.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 141

- Explain **Text plus image inputs** to someone else without notes.
- Explain **How images become tokens** to someone else without notes.
- Explain **Document and chart understanding** to someone else without notes.
- Explain **Video understanding with LLMs** to someone else without notes.
- Explain **Audio-native models** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
