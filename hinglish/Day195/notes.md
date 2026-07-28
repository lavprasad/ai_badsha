# Day 195 — Writing about your work

Aaj ka goal: **Writing about your work** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Structure of a good technical write-up |
| 2 | Leading with the result |
| 3 | Explaining the method without jargon |
| 4 | Charts that carry the argument |
| 5 | Reporting limitations builds trust |
| 6 | Reproducibility section |
| 7 | README as the front door |
| 8 | Blog post vs repository documentation |
| 9 | Getting feedback before publishing |
| 10 | Publishing on GitHub Pages |

---

## 1. Structure of a good technical write-up

### Aasaan Bhasha

Pehle result, phir method, phir caveats. Zyadatar padhne wale do paragraph ke baad ruk jaate hain, isliye pehle do me finding aur uski ahmiyat honi chahiye. Aisa README jo problem, number aur chalane ka tarika batata ho, kisi perfect architecture diagram se zyada keemti hai.

### Chhota code

```python
README = '''
# Ticket Router

Routes support tickets to the right team. **Macro F1 0.84** vs 0.61 for the
keyword rules it replaces, measured on 4,000 held-out tickets from Q1.

## Run it
    pip install -r requirements.txt
    python -m router.train --config configs/base.yaml
    python -m router.serve

## How it works
TF-IDF + linear SVM baseline, then a fine-tuned small transformer.
The transformer wins by 0.06 F1 at 12x the inference cost — see `docs/tradeoff.md`.

## Limitations
- Trained on English tickets only; Hinglish accuracy drops to 0.71.
- Degrades on tickets under 10 words (18% of volume).
'''
print(README)
```

**Yaad rakho:** Number pehle paragraph me daalo. Agar aap use chhupa rahe ho to padhne wala maan lega ki wo bura hai.

**Aam galti:** Aisa README jo 400 lines me architecture samjhaata hai aur kabhi nahi batata ki score kya aaya.

Practice: `examples/01_structure_of_a_good_technical_write_up.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Leading with the result

### Aasaan Bhasha

Pehle result, phir method, phir caveats. Zyadatar padhne wale do paragraph ke baad ruk jaate hain, isliye pehle do me finding aur uski ahmiyat honi chahiye. Aisa README jo problem, number aur chalane ka tarika batata ho, kisi perfect architecture diagram se zyada keemti hai.

### Chhota code

```python
README = '''
# Ticket Router

Routes support tickets to the right team. **Macro F1 0.84** vs 0.61 for the
keyword rules it replaces, measured on 4,000 held-out tickets from Q1.

## Run it
    pip install -r requirements.txt
    python -m router.train --config configs/base.yaml
    python -m router.serve

## How it works
TF-IDF + linear SVM baseline, then a fine-tuned small transformer.
The transformer wins by 0.06 F1 at 12x the inference cost — see `docs/tradeoff.md`.

## Limitations
- Trained on English tickets only; Hinglish accuracy drops to 0.71.
- Degrades on tickets under 10 words (18% of volume).
'''
print(README)
```

**Yaad rakho:** Number pehle paragraph me daalo. Agar aap use chhupa rahe ho to padhne wala maan lega ki wo bura hai.

**Aam galti:** Aisa README jo 400 lines me architecture samjhaata hai aur kabhi nahi batata ki score kya aaya.

Practice: `examples/02_leading_with_the_result.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Explaining the method without jargon

### Aasaan Bhasha

Pehle result, phir method, phir caveats. Zyadatar padhne wale do paragraph ke baad ruk jaate hain, isliye pehle do me finding aur uski ahmiyat honi chahiye. Aisa README jo problem, number aur chalane ka tarika batata ho, kisi perfect architecture diagram se zyada keemti hai.

### Chhota code

```python
README = '''
# Ticket Router

Routes support tickets to the right team. **Macro F1 0.84** vs 0.61 for the
keyword rules it replaces, measured on 4,000 held-out tickets from Q1.

## Run it
    pip install -r requirements.txt
    python -m router.train --config configs/base.yaml
    python -m router.serve

## How it works
TF-IDF + linear SVM baseline, then a fine-tuned small transformer.
The transformer wins by 0.06 F1 at 12x the inference cost — see `docs/tradeoff.md`.

## Limitations
- Trained on English tickets only; Hinglish accuracy drops to 0.71.
- Degrades on tickets under 10 words (18% of volume).
'''
print(README)
```

**Yaad rakho:** Number pehle paragraph me daalo. Agar aap use chhupa rahe ho to padhne wala maan lega ki wo bura hai.

**Aam galti:** Aisa README jo 400 lines me architecture samjhaata hai aur kabhi nahi batata ki score kya aaya.

Practice: `examples/03_explaining_the_method_without_jargon.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Charts that carry the argument

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

Practice: `examples/04_charts_that_carry_the_argument.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Reporting limitations builds trust

### Aasaan Bhasha

Projects wahi jagah hain jahan seekha hua chipakta hai. Pehle ek patli end-to-end slice banao — data load, kuch bewakoof train, evaluate, ek prediction serve — phir ek-ek layer sudharo. Pehle din chalne wala baseline us perfect model se behtar hai jo kabhi ship hi nahi hota.

### Chhota code

```python
STEPS = [
    '1. Define the decision the model supports and the metric that measures it',
    '2. Get the data; write the loader; assert the schema',
    '3. Dumb baseline (mean / majority class) -> this is the bar',
    '4. Simple model + honest validation split',
    '5. Error analysis: look at 30 wrong predictions by hand',
    '6. Improve the biggest error bucket, not the leaderboard',
    '7. Serve it, log inputs and outputs, monitor drift',
]
for s in STEPS:
    print(s)
```

**Yaad rakho:** Hyperparameters tune karne me ek din lagane se pehle galat predictions dekhne me ek ghanta lagao.

**Aam galti:** Chhe hafte feature engineering karna bina kisi baseline ke jo sabit kare ki kisi cheez se fayda hua.

Practice: `examples/05_reporting_limitations_builds_trust.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Reproducibility section

### Aasaan Bhasha

Jo experiment aap dobara nahi bana sakte wo kissa hai. Har run ke liye track karo: code commit, data version, hyperparameters, metrics aur artefact. Chhe mahine baad 'production wala model kis run se aaya' ka jawab hona hi chahiye.

### Chhota code

```python
import json, hashlib, subprocess

def run_record(params, metrics, data_path=None):
    try:
        commit = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'], text=True).strip()
    except Exception:
        commit = 'unknown'
    return {
        'commit': commit,
        'params': params,
        'metrics': metrics,
        'data_sha': hashlib.sha256((data_path or 'none').encode()).hexdigest()[:12],
    }

print(json.dumps(run_record({'lr': 0.01, 'depth': 6}, {'auc': 0.912}, 'data/train.csv'), indent=2))
```

**Yaad rakho:** Code version ke saath data version bhi log karo — data chupchap badalta hai, code shor machaa kar.

**Aam galti:** Registry use karne ke bajaye files ko `model_final_v2_REAL_use_this.pkl` naam dena.

Practice: `examples/06_reproducibility_section.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. README as the front door

### Aasaan Bhasha

Pehle result, phir method, phir caveats. Zyadatar padhne wale do paragraph ke baad ruk jaate hain, isliye pehle do me finding aur uski ahmiyat honi chahiye. Aisa README jo problem, number aur chalane ka tarika batata ho, kisi perfect architecture diagram se zyada keemti hai.

### Chhota code

```python
README = '''
# Ticket Router

Routes support tickets to the right team. **Macro F1 0.84** vs 0.61 for the
keyword rules it replaces, measured on 4,000 held-out tickets from Q1.

## Run it
    pip install -r requirements.txt
    python -m router.train --config configs/base.yaml
    python -m router.serve

## How it works
TF-IDF + linear SVM baseline, then a fine-tuned small transformer.
The transformer wins by 0.06 F1 at 12x the inference cost — see `docs/tradeoff.md`.

## Limitations
- Trained on English tickets only; Hinglish accuracy drops to 0.71.
- Degrades on tickets under 10 words (18% of volume).
'''
print(README)
```

**Yaad rakho:** Number pehle paragraph me daalo. Agar aap use chhupa rahe ho to padhne wala maan lega ki wo bura hai.

**Aam galti:** Aisa README jo 400 lines me architecture samjhaata hai aur kabhi nahi batata ki score kya aaya.

Practice: `examples/07_readme_as_the_front_door.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Blog post vs repository documentation

### Aasaan Bhasha

Pehle result, phir method, phir caveats. Zyadatar padhne wale do paragraph ke baad ruk jaate hain, isliye pehle do me finding aur uski ahmiyat honi chahiye. Aisa README jo problem, number aur chalane ka tarika batata ho, kisi perfect architecture diagram se zyada keemti hai.

### Chhota code

```python
README = '''
# Ticket Router

Routes support tickets to the right team. **Macro F1 0.84** vs 0.61 for the
keyword rules it replaces, measured on 4,000 held-out tickets from Q1.

## Run it
    pip install -r requirements.txt
    python -m router.train --config configs/base.yaml
    python -m router.serve

## How it works
TF-IDF + linear SVM baseline, then a fine-tuned small transformer.
The transformer wins by 0.06 F1 at 12x the inference cost — see `docs/tradeoff.md`.

## Limitations
- Trained on English tickets only; Hinglish accuracy drops to 0.71.
- Degrades on tickets under 10 words (18% of volume).
'''
print(README)
```

**Yaad rakho:** Number pehle paragraph me daalo. Agar aap use chhupa rahe ho to padhne wala maan lega ki wo bura hai.

**Aam galti:** Aisa README jo 400 lines me architecture samjhaata hai aur kabhi nahi batata ki score kya aaya.

Practice: `examples/08_blog_post_vs_repository_documentation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Getting feedback before publishing

### Aasaan Bhasha

Pehle result, phir method, phir caveats. Zyadatar padhne wale do paragraph ke baad ruk jaate hain, isliye pehle do me finding aur uski ahmiyat honi chahiye. Aisa README jo problem, number aur chalane ka tarika batata ho, kisi perfect architecture diagram se zyada keemti hai.

### Chhota code

```python
README = '''
# Ticket Router

Routes support tickets to the right team. **Macro F1 0.84** vs 0.61 for the
keyword rules it replaces, measured on 4,000 held-out tickets from Q1.

## Run it
    pip install -r requirements.txt
    python -m router.train --config configs/base.yaml
    python -m router.serve

## How it works
TF-IDF + linear SVM baseline, then a fine-tuned small transformer.
The transformer wins by 0.06 F1 at 12x the inference cost — see `docs/tradeoff.md`.

## Limitations
- Trained on English tickets only; Hinglish accuracy drops to 0.71.
- Degrades on tickets under 10 words (18% of volume).
'''
print(README)
```

**Yaad rakho:** Number pehle paragraph me daalo. Agar aap use chhupa rahe ho to padhne wala maan lega ki wo bura hai.

**Aam galti:** Aisa README jo 400 lines me architecture samjhaata hai aur kabhi nahi batata ki score kya aaya.

Practice: `examples/09_getting_feedback_before_publishing.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Publishing on GitHub Pages

### Aasaan Bhasha

Pehle result, phir method, phir caveats. Zyadatar padhne wale do paragraph ke baad ruk jaate hain, isliye pehle do me finding aur uski ahmiyat honi chahiye. Aisa README jo problem, number aur chalane ka tarika batata ho, kisi perfect architecture diagram se zyada keemti hai.

### Chhota code

```python
README = '''
# Ticket Router

Routes support tickets to the right team. **Macro F1 0.84** vs 0.61 for the
keyword rules it replaces, measured on 4,000 held-out tickets from Q1.

## Run it
    pip install -r requirements.txt
    python -m router.train --config configs/base.yaml
    python -m router.serve

## How it works
TF-IDF + linear SVM baseline, then a fine-tuned small transformer.
The transformer wins by 0.06 F1 at 12x the inference cost — see `docs/tradeoff.md`.

## Limitations
- Trained on English tickets only; Hinglish accuracy drops to 0.71.
- Degrades on tickets under 10 words (18% of volume).
'''
print(README)
```

**Yaad rakho:** Number pehle paragraph me daalo. Agar aap use chhupa rahe ho to padhne wala maan lega ki wo bura hai.

**Aam galti:** Aisa README jo 400 lines me architecture samjhaata hai aur kabhi nahi batata ki score kya aaya.

Practice: `examples/10_publishing_on_github_pages.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 195 ke baad aapko ye aana chahiye

- **Structure of a good technical write-up** ko bina notes dekhe kisi dost ko samjha sakna.
- **Leading with the result** ko bina notes dekhe kisi dost ko samjha sakna.
- **Explaining the method without jargon** ko bina notes dekhe kisi dost ko samjha sakna.
- **Charts that carry the argument** ko bina notes dekhe kisi dost ko samjha sakna.
- **Reporting limitations builds trust** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
