# Day 196 — Reading research

Aaj ka goal: **Reading research** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Where papers appear: arXiv and conferences |
| 2 | The three-pass reading method |
| 3 | Distinguishing contribution from packaging |
| 4 | Reading the limitations section first |
| 5 | Checking baselines for fairness |
| 6 | Reproducibility red flags |
| 7 | Following citation trails |
| 8 | Keeping a paper notebook |
| 9 | Implementing one idea per month |
| 10 | Staying current without drowning |

---

## 1. Where papers appear: arXiv and conferences

### Aasaan Bhasha

Teen pass me padho: title/abstract/figures (5 minute, tay karo ki matlab hai ya nahi), method aur results (30 minute, idea samjho), phir poori detail sirf tab jab aap implement karoge. Limitations section aam taur par paper ka sabse imaandaar paragraph hota hai — use jaldi padho.

### Chhota code

```python
PASS_1 = ['title', 'abstract', 'figures and captions', 'conclusion']
PASS_2 = ['method section', 'experimental setup', 'baselines used', 'results tables']
PASS_3 = ['every equation', 'appendix', 'reimplement the core idea']

for i, (name, items) in enumerate([('5 min', PASS_1), ('30 min', PASS_2), ('hours', PASS_3)], 1):
    print(f'Pass {i} ({name}): ' + ', '.join(items))
print('\nStop after pass 1 for 90% of papers. That is not laziness, that is triage.')
```

**Yaad rakho:** Dekho unhone kin baselines se compare kiya. Kamzor baseline har method ko strong dikha deta hai.

**Aam galti:** Bees papers padhna aur ek bhi implement na karna — bina banaye samajh ek hafte me udd jaati hai.

Practice: `examples/01_where_papers_appear_arxiv_and_conference.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. The three-pass reading method

### Aasaan Bhasha

Teen pass me padho: title/abstract/figures (5 minute, tay karo ki matlab hai ya nahi), method aur results (30 minute, idea samjho), phir poori detail sirf tab jab aap implement karoge. Limitations section aam taur par paper ka sabse imaandaar paragraph hota hai — use jaldi padho.

### Chhota code

```python
PASS_1 = ['title', 'abstract', 'figures and captions', 'conclusion']
PASS_2 = ['method section', 'experimental setup', 'baselines used', 'results tables']
PASS_3 = ['every equation', 'appendix', 'reimplement the core idea']

for i, (name, items) in enumerate([('5 min', PASS_1), ('30 min', PASS_2), ('hours', PASS_3)], 1):
    print(f'Pass {i} ({name}): ' + ', '.join(items))
print('\nStop after pass 1 for 90% of papers. That is not laziness, that is triage.')
```

**Yaad rakho:** Dekho unhone kin baselines se compare kiya. Kamzor baseline har method ko strong dikha deta hai.

**Aam galti:** Bees papers padhna aur ek bhi implement na karna — bina banaye samajh ek hafte me udd jaati hai.

Practice: `examples/02_the_three_pass_reading_method.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Distinguishing contribution from packaging

### Aasaan Bhasha

Teen pass me padho: title/abstract/figures (5 minute, tay karo ki matlab hai ya nahi), method aur results (30 minute, idea samjho), phir poori detail sirf tab jab aap implement karoge. Limitations section aam taur par paper ka sabse imaandaar paragraph hota hai — use jaldi padho.

### Chhota code

```python
PASS_1 = ['title', 'abstract', 'figures and captions', 'conclusion']
PASS_2 = ['method section', 'experimental setup', 'baselines used', 'results tables']
PASS_3 = ['every equation', 'appendix', 'reimplement the core idea']

for i, (name, items) in enumerate([('5 min', PASS_1), ('30 min', PASS_2), ('hours', PASS_3)], 1):
    print(f'Pass {i} ({name}): ' + ', '.join(items))
print('\nStop after pass 1 for 90% of papers. That is not laziness, that is triage.')
```

**Yaad rakho:** Dekho unhone kin baselines se compare kiya. Kamzor baseline har method ko strong dikha deta hai.

**Aam galti:** Bees papers padhna aur ek bhi implement na karna — bina banaye samajh ek hafte me udd jaati hai.

Practice: `examples/03_distinguishing_contribution_from_packagi.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Reading the limitations section first

### Aasaan Bhasha

Teen pass me padho: title/abstract/figures (5 minute, tay karo ki matlab hai ya nahi), method aur results (30 minute, idea samjho), phir poori detail sirf tab jab aap implement karoge. Limitations section aam taur par paper ka sabse imaandaar paragraph hota hai — use jaldi padho.

### Chhota code

```python
PASS_1 = ['title', 'abstract', 'figures and captions', 'conclusion']
PASS_2 = ['method section', 'experimental setup', 'baselines used', 'results tables']
PASS_3 = ['every equation', 'appendix', 'reimplement the core idea']

for i, (name, items) in enumerate([('5 min', PASS_1), ('30 min', PASS_2), ('hours', PASS_3)], 1):
    print(f'Pass {i} ({name}): ' + ', '.join(items))
print('\nStop after pass 1 for 90% of papers. That is not laziness, that is triage.')
```

**Yaad rakho:** Dekho unhone kin baselines se compare kiya. Kamzor baseline har method ko strong dikha deta hai.

**Aam galti:** Bees papers padhna aur ek bhi implement na karna — bina banaye samajh ek hafte me udd jaati hai.

Practice: `examples/04_reading_the_limitations_section_first.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Checking baselines for fairness

### Aasaan Bhasha

Models apne training data ka bias seekh lete hain aur phir use objectivity ke mulamme ke saath scale par lagu karte hain. Har group ke error rates naapo, sirf overall nahi. Fairness ki definitions ek doosre se sach me takraati hain — aapko ek explicitly chunni padegi aur wajah likhni padegi.

### Chhota code

```python
import numpy as np
import pandas as pd

df = pd.DataFrame({
    'group': ['a'] * 100 + ['b'] * 100,
    'y':     [1] * 50 + [0] * 50 + [1] * 50 + [0] * 50,
    'pred':  [1] * 45 + [0] * 55 + [1] * 30 + [0] * 70,
})
for g, sub in df.groupby('group'):
    tpr = ((sub.pred == 1) & (sub.y == 1)).sum() / max((sub.y == 1).sum(), 1)
    rate = (sub.pred == 1).mean()
    print(f'group {g}: selection rate {rate:.2f}  recall {tpr:.2f}')
print('Large gaps here are the finding — investigate before shipping.')
```

**Yaad rakho:** Sensitive attribute hataane se bias nahi jaata; proxies (pincode, naam) use wapas le aate hain.

**Aam galti:** Fairness ka audit sirf launch par ek baar karna aur data drift hone par dobara kabhi nahi.

Practice: `examples/05_checking_baselines_for_fairness.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Reproducibility red flags

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

Practice: `examples/06_reproducibility_red_flags.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Following citation trails

### Aasaan Bhasha

Language model plausible tokens predict karta hai, sach wale nahi. Fluent aur galat uska default failure mode hai. Ise kam karo jawaabon ko retrieved sources me ground karke, citations maang kar, 'mujhe nahi pata' ki ijaazat de kar, aur mehnge claims verify karke.

### Chhota code

```python
def answer_with_guard(question, chunks, threshold=0.35):
    if not chunks or max(c['score'] for c in chunks) < threshold:
        return "I don't have information about that in the provided documents."
    best = max(chunks, key=lambda c: c['score'])
    return f"{best['text']}  [source: {best['id']}]"

print(answer_with_guard('refund policy?', [{'id': 'policy.pdf#3', 'text': 'Refunds take 5 days.', 'score': 0.81}]))
print(answer_with_guard('CEO home address?', [{'id': 'policy.pdf#3', 'text': 'Refunds take 5 days.', 'score': 0.11}]))
```

**Yaad rakho:** Ek saaf 'mere sources me nahi hai' wala raasta kisi bhi confidence score se zyada keemti hai.

**Aam galti:** Bina abstain path ke chatbot ship karna, jo dabaav me policy khud gadh leta hai.

Practice: `examples/07_following_citation_trails.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Keeping a paper notebook

### Aasaan Bhasha

Notebooks cells ke beech state rakhte hain — exploring ke liye badhiya, reproducibility ke liye bekaar. Notebook ko scratchpad samjho; jab logic pakka ho jaaye to use `.py` module me daal do jise aap import aur test kar sako.

### Chhota code

```python
# In a notebook, cell order != execution order.
# Restart & Run All before you trust any result.
import pandas as pd
df = pd.DataFrame({'x': [1, 2, 3]})
df.head()
```

**Yaad rakho:** 'Restart kernel and run all' hi ek imaandaar test hai ki notebook sach me chalta hai.

**Aam galti:** Aisa notebook dena jiska result das minute pehle delete ki gayi cell par depend karta hai.

Practice: `examples/08_keeping_a_paper_notebook.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Implementing one idea per month

### Aasaan Bhasha

Teen pass me padho: title/abstract/figures (5 minute, tay karo ki matlab hai ya nahi), method aur results (30 minute, idea samjho), phir poori detail sirf tab jab aap implement karoge. Limitations section aam taur par paper ka sabse imaandaar paragraph hota hai — use jaldi padho.

### Chhota code

```python
PASS_1 = ['title', 'abstract', 'figures and captions', 'conclusion']
PASS_2 = ['method section', 'experimental setup', 'baselines used', 'results tables']
PASS_3 = ['every equation', 'appendix', 'reimplement the core idea']

for i, (name, items) in enumerate([('5 min', PASS_1), ('30 min', PASS_2), ('hours', PASS_3)], 1):
    print(f'Pass {i} ({name}): ' + ', '.join(items))
print('\nStop after pass 1 for 90% of papers. That is not laziness, that is triage.')
```

**Yaad rakho:** Dekho unhone kin baselines se compare kiya. Kamzor baseline har method ko strong dikha deta hai.

**Aam galti:** Bees papers padhna aur ek bhi implement na karna — bina banaye samajh ek hafte me udd jaati hai.

Practice: `examples/09_implementing_one_idea_per_month.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Staying current without drowning

### Aasaan Bhasha

Interviews me depth breadth se jeetti hai: ek project jise aap end-to-end defend kar sako — wo metric kyun, wo split kyun, kya fail hua — das tutorial notebooks se behtar hai. Papers ko three-pass method se padho: abstract aur figures, phir method, phir details sirf tab jab aap use implement karoge.

### Chhota code

```python
PAPER_CHECKLIST = [
    'What problem, and what was the previous best?',
    'What is the single new idea? (usually one sentence)',
    'What is the evidence? Which baselines, which datasets?',
    'What did they NOT test? (the limitations section is the honest part)',
    'Could I implement the core idea in 50 lines?',
]
for q in PAPER_CHECKLIST:
    print('-', q)
```

**Yaad rakho:** Agar aap ye nahi samjha sakte ki aapka validation split imaandaar kyun hai, to project abhi aapka nahi hua.

**Aam galti:** CV par bees frameworks likhna aur kisi ek me bhi shape error debug na kar paana.

Practice: `examples/10_staying_current_without_drowning.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 196 ke baad aapko ye aana chahiye

- **Where papers appear: arXiv and conferences** ko bina notes dekhe kisi dost ko samjha sakna.
- **The three-pass reading method** ko bina notes dekhe kisi dost ko samjha sakna.
- **Distinguishing contribution from packaging** ko bina notes dekhe kisi dost ko samjha sakna.
- **Reading the limitations section first** ko bina notes dekhe kisi dost ko samjha sakna.
- **Checking baselines for fairness** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
