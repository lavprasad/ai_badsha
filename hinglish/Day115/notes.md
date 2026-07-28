# Day 115 — Image generation in practice

Aaj ka goal: **Image generation in practice** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

Practice: `examples/01_text_to_image_workflow.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Prompting for images

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

Practice: `examples/02_prompting_for_images.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Negative prompts

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

Practice: `examples/03_negative_prompts.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Image-to-image and inpainting

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

Practice: `examples/04_image_to_image_and_inpainting.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Guidance scale and steps

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

Practice: `examples/05_guidance_scale_and_steps.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Seeds and reproducibility

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

Practice: `examples/06_seeds_and_reproducibility.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. LoRA for style adaptation

### Aasaan Bhasha

LoRA base weights freeze kar deta hai aur do chhoti low-rank matrices train karta hai jinka product har target layer me joda jaata hai. Aap ~0.1% parameters update karte ho, checkpoint gigabytes ke bajaye megabytes ka hota hai, aur har customer ke liye adapter badla ja sakta hai. QLoRA 4-bit base weights jodta hai taaki 7B model ek consumer GPU par aa jaaye.

### Chhota code

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

**Yaad rakho:** B ko zeros se initialise karo taaki adapted model bilkul base model ke barabar shuru ho.

**Aam galti:** Rank bahut zyada rakh dena — efficiency chali jaati hai aur overfitting aa jaati hai.

Practice: `examples/07_lora_for_style_adaptation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Upscaling

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

Practice: `examples/08_upscaling.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Content provenance and watermarking

### Aasaan Bhasha

Missing data information hai, sirf noise nahi. Kuch bharne se pehle poochho ki **kyun** missing hai: jo sensor sirf load par fail hota hai wo randomly missing nahi hai. Phir chuno: rows drop, column drop, statistic se fill, ya ek explicit 'ye missing tha' indicator column.

### Chhota code

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'age': [25, np.nan, 40, np.nan]})
print(df.isna().sum())

df['age_missing'] = df['age'].isna().astype(int)   # keep the signal
df['age'] = df['age'].fillna(df['age'].median())    # then fill
print(df)
```

**Yaad rakho:** Fill karne wali statistic sirf TRAIN split par nikalo, phir test par lagao.

**Aam galti:** Poore dataset ke mean se fill karna — ye test ki information training me leak kar deta hai.

Practice: `examples/09_content_provenance_and_watermarking.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Copyright and dataset questions

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

Practice: `examples/10_copyright_and_dataset_questions.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 115 ke baad aapko ye aana chahiye

- **Text-to-image workflow** ko bina notes dekhe kisi dost ko samjha sakna.
- **Prompting for images** ko bina notes dekhe kisi dost ko samjha sakna.
- **Negative prompts** ko bina notes dekhe kisi dost ko samjha sakna.
- **Image-to-image and inpainting** ko bina notes dekhe kisi dost ko samjha sakna.
- **Guidance scale and steps** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
