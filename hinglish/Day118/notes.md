# Day 118 — Vision system design

Aaj ka goal: **Vision system design** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Requirements: accuracy, latency, cost |
| 2 | Data collection plan |
| 3 | Annotation strategy and quality control |
| 4 | Choosing the model family |
| 5 | Handling class imbalance in vision |
| 6 | Monitoring in production |
| 7 | Human-in-the-loop review |
| 8 | Failure modes and fallbacks |
| 9 | Cost per inference |
| 10 | Writing the system design document |

---

## 1. Requirements: accuracy, latency, cost

### Aasaan Bhasha

Imbalanced data par accuracy sab chhupa leti hai. Precision poochti hai 'jinhe maine flag kiya unme se kitne asli the'; recall poochti hai 'jo asli the unme se kitne maine pakde'. Threshold se aap ek ko doosre ke badle bechte ho, aur kaunsi galti zyada mehngi hai ye business tay karta hai.

### Chhota code

```python
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=2000, weights=[0.95, 0.05], random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, stratify=y, random_state=0)
m = LogisticRegression(max_iter=1000).fit(Xtr, ytr)
print(confusion_matrix(yte, m.predict(Xte)))
print(classification_report(yte, m.predict(Xte), digits=3))
print('roc auc', round(roc_auc_score(yte, m.predict_proba(Xte)[:, 1]), 4))
```

**Yaad rakho:** Decision threshold validation data par tune karo; 0.5 ek default hai, decision nahi.

**Aam galti:** Bhaari imbalanced problem par ROC-AUC optimise karna jahan imaandaar metric precision-recall AUC hai.

Practice: `examples/01_requirements_accuracy_latency_cost.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Data collection plan

### Aasaan Bhasha

System design document wo sawaal poochne par majboor karta hai jo projects ko der se maarte hain: data kahan se aayega, model unsure ho to kya hoga, review kaun karega, ek inference ki cost kya hai, aur service down hone par kya hoga. Ise pehli training run se pehle likho.

### Chhota code

```python
DESIGN = {
    'decision supported': 'auto-approve low-risk claims',
    'metric + target': 'precision >= 0.98 at >= 40% coverage',
    'fallback': 'route to human queue (must handle 100% of volume)',
    'confidence gate': 'auto-approve only above calibrated p=0.95',
    'human review': '2% random audit + all rejections',
    'cost per inference': 'Rs 0.004 (batch) / Rs 0.02 (realtime)',
    'failure mode': 'model down -> everything to human queue, alert on-call',
    'monitoring': 'daily PSI on inputs, weekly precision on audited sample',
}
for k, v in DESIGN.items():
    print(f'{k:>20}: {v}')
```

**Yaad rakho:** Fallback path ko 100% traffic sambhalna hi chahiye. Nahi sambhal sakta to aapne single point of failure banaya hai.

**Aam galti:** Sirf happy path ke liye design karna aur raat 3 baje pata chalna ki low-confidence cases ka koi raasta hi nahi hai.

Practice: `examples/02_data_collection_plan.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Annotation strategy and quality control

### Aasaan Bhasha

System design document wo sawaal poochne par majboor karta hai jo projects ko der se maarte hain: data kahan se aayega, model unsure ho to kya hoga, review kaun karega, ek inference ki cost kya hai, aur service down hone par kya hoga. Ise pehli training run se pehle likho.

### Chhota code

```python
DESIGN = {
    'decision supported': 'auto-approve low-risk claims',
    'metric + target': 'precision >= 0.98 at >= 40% coverage',
    'fallback': 'route to human queue (must handle 100% of volume)',
    'confidence gate': 'auto-approve only above calibrated p=0.95',
    'human review': '2% random audit + all rejections',
    'cost per inference': 'Rs 0.004 (batch) / Rs 0.02 (realtime)',
    'failure mode': 'model down -> everything to human queue, alert on-call',
    'monitoring': 'daily PSI on inputs, weekly precision on audited sample',
}
for k, v in DESIGN.items():
    print(f'{k:>20}: {v}')
```

**Yaad rakho:** Fallback path ko 100% traffic sambhalna hi chahiye. Nahi sambhal sakta to aapne single point of failure banaya hai.

**Aam galti:** Sirf happy path ke liye design karna aur raat 3 baje pata chalna ki low-confidence cases ka koi raasta hi nahi hai.

Practice: `examples/03_annotation_strategy_and_quality_control.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Choosing the model family

### Aasaan Bhasha

System design document wo sawaal poochne par majboor karta hai jo projects ko der se maarte hain: data kahan se aayega, model unsure ho to kya hoga, review kaun karega, ek inference ki cost kya hai, aur service down hone par kya hoga. Ise pehli training run se pehle likho.

### Chhota code

```python
DESIGN = {
    'decision supported': 'auto-approve low-risk claims',
    'metric + target': 'precision >= 0.98 at >= 40% coverage',
    'fallback': 'route to human queue (must handle 100% of volume)',
    'confidence gate': 'auto-approve only above calibrated p=0.95',
    'human review': '2% random audit + all rejections',
    'cost per inference': 'Rs 0.004 (batch) / Rs 0.02 (realtime)',
    'failure mode': 'model down -> everything to human queue, alert on-call',
    'monitoring': 'daily PSI on inputs, weekly precision on audited sample',
}
for k, v in DESIGN.items():
    print(f'{k:>20}: {v}')
```

**Yaad rakho:** Fallback path ko 100% traffic sambhalna hi chahiye. Nahi sambhal sakta to aapne single point of failure banaya hai.

**Aam galti:** Sirf happy path ke liye design karna aur raat 3 baje pata chalna ki low-confidence cases ka koi raasta hi nahi hai.

Practice: `examples/04_choosing_the_model_family.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Handling class imbalance in vision

### Aasaan Bhasha

Aaj ka idea — **Handling class imbalance in vision** — Vision system design ke theme ke andar aata hai. Ise trivia nahi, ek tool ki tarah padho: ye kaam kya karta hai, aapke data ke baare me kya maan kar chalta hai, aur wo maanyata jhooth nikle to kya tootta hai?

### Chhota code

```python
# Explore: Handling class imbalance in vision
print("practice: Handling class imbalance in vision")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Yaad rakho:** `Handling class imbalance in vision` use karne se pehle ek assumption likho jo ye aapke data ke baare me maanta hai.

**Aam galti:** `Handling class imbalance in vision` ko tutorial se copy-paste kar lena bina jaane ki wo kya maanta hai aur kab fail hota hai.

Practice: `examples/05_handling_class_imbalance_in_vision.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Monitoring in production

### Aasaan Bhasha

Models sadte hain. Duniya badalti hai, inputs shift hote hain (data drift) ya rishta hi badal jaata hai (concept drift). Input aur prediction distributions roz monitor karo, kyunki ground-truth labels aksar hafton baad aate hain.

### Chhota code

```python
import numpy as np

def psi(expected, actual, bins=10):
    """Population Stability Index: >0.2 means investigate."""
    edges = np.percentile(expected, np.linspace(0, 100, bins + 1))
    edges[0], edges[-1] = -np.inf, np.inf
    e = np.histogram(expected, edges)[0] / len(expected) + 1e-6
    a = np.histogram(actual, edges)[0] / len(actual) + 1e-6
    return float(np.sum((a - e) * np.log(a / e)))

rng = np.random.default_rng(0)
baseline = rng.normal(0, 1, 10_000)
print('same dist  PSI', round(psi(baseline, rng.normal(0, 1, 5_000)), 4))
print('shifted    PSI', round(psi(baseline, rng.normal(0.6, 1.2, 5_000)), 4))
```

**Yaad rakho:** PSI 0.1 se kam stable, 0.1-0.2 nazar rakho, 0.2 se upar jaanch karo. Prediction distribution par bhi alert lagao.

**Aam galti:** Sirf uptime monitor karna, jisse 200 OK lautaata hua bilkul galat model bhi healthy dikhta hai.

Practice: `examples/06_monitoring_in_production.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Human-in-the-loop review

### Aasaan Bhasha

System design document wo sawaal poochne par majboor karta hai jo projects ko der se maarte hain: data kahan se aayega, model unsure ho to kya hoga, review kaun karega, ek inference ki cost kya hai, aur service down hone par kya hoga. Ise pehli training run se pehle likho.

### Chhota code

```python
DESIGN = {
    'decision supported': 'auto-approve low-risk claims',
    'metric + target': 'precision >= 0.98 at >= 40% coverage',
    'fallback': 'route to human queue (must handle 100% of volume)',
    'confidence gate': 'auto-approve only above calibrated p=0.95',
    'human review': '2% random audit + all rejections',
    'cost per inference': 'Rs 0.004 (batch) / Rs 0.02 (realtime)',
    'failure mode': 'model down -> everything to human queue, alert on-call',
    'monitoring': 'daily PSI on inputs, weekly precision on audited sample',
}
for k, v in DESIGN.items():
    print(f'{k:>20}: {v}')
```

**Yaad rakho:** Fallback path ko 100% traffic sambhalna hi chahiye. Nahi sambhal sakta to aapne single point of failure banaya hai.

**Aam galti:** Sirf happy path ke liye design karna aur raat 3 baje pata chalna ki low-confidence cases ka koi raasta hi nahi hai.

Practice: `examples/07_human_in_the_loop_review.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Failure modes and fallbacks

### Aasaan Bhasha

System design document wo sawaal poochne par majboor karta hai jo projects ko der se maarte hain: data kahan se aayega, model unsure ho to kya hoga, review kaun karega, ek inference ki cost kya hai, aur service down hone par kya hoga. Ise pehli training run se pehle likho.

### Chhota code

```python
DESIGN = {
    'decision supported': 'auto-approve low-risk claims',
    'metric + target': 'precision >= 0.98 at >= 40% coverage',
    'fallback': 'route to human queue (must handle 100% of volume)',
    'confidence gate': 'auto-approve only above calibrated p=0.95',
    'human review': '2% random audit + all rejections',
    'cost per inference': 'Rs 0.004 (batch) / Rs 0.02 (realtime)',
    'failure mode': 'model down -> everything to human queue, alert on-call',
    'monitoring': 'daily PSI on inputs, weekly precision on audited sample',
}
for k, v in DESIGN.items():
    print(f'{k:>20}: {v}')
```

**Yaad rakho:** Fallback path ko 100% traffic sambhalna hi chahiye. Nahi sambhal sakta to aapne single point of failure banaya hai.

**Aam galti:** Sirf happy path ke liye design karna aur raat 3 baje pata chalna ki low-confidence cases ka koi raasta hi nahi hai.

Practice: `examples/08_failure_modes_and_fallbacks.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Cost per inference

### Aasaan Bhasha

System design document wo sawaal poochne par majboor karta hai jo projects ko der se maarte hain: data kahan se aayega, model unsure ho to kya hoga, review kaun karega, ek inference ki cost kya hai, aur service down hone par kya hoga. Ise pehli training run se pehle likho.

### Chhota code

```python
DESIGN = {
    'decision supported': 'auto-approve low-risk claims',
    'metric + target': 'precision >= 0.98 at >= 40% coverage',
    'fallback': 'route to human queue (must handle 100% of volume)',
    'confidence gate': 'auto-approve only above calibrated p=0.95',
    'human review': '2% random audit + all rejections',
    'cost per inference': 'Rs 0.004 (batch) / Rs 0.02 (realtime)',
    'failure mode': 'model down -> everything to human queue, alert on-call',
    'monitoring': 'daily PSI on inputs, weekly precision on audited sample',
}
for k, v in DESIGN.items():
    print(f'{k:>20}: {v}')
```

**Yaad rakho:** Fallback path ko 100% traffic sambhalna hi chahiye. Nahi sambhal sakta to aapne single point of failure banaya hai.

**Aam galti:** Sirf happy path ke liye design karna aur raat 3 baje pata chalna ki low-confidence cases ka koi raasta hi nahi hai.

Practice: `examples/09_cost_per_inference.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Writing the system design document

### Aasaan Bhasha

System design document wo sawaal poochne par majboor karta hai jo projects ko der se maarte hain: data kahan se aayega, model unsure ho to kya hoga, review kaun karega, ek inference ki cost kya hai, aur service down hone par kya hoga. Ise pehli training run se pehle likho.

### Chhota code

```python
DESIGN = {
    'decision supported': 'auto-approve low-risk claims',
    'metric + target': 'precision >= 0.98 at >= 40% coverage',
    'fallback': 'route to human queue (must handle 100% of volume)',
    'confidence gate': 'auto-approve only above calibrated p=0.95',
    'human review': '2% random audit + all rejections',
    'cost per inference': 'Rs 0.004 (batch) / Rs 0.02 (realtime)',
    'failure mode': 'model down -> everything to human queue, alert on-call',
    'monitoring': 'daily PSI on inputs, weekly precision on audited sample',
}
for k, v in DESIGN.items():
    print(f'{k:>20}: {v}')
```

**Yaad rakho:** Fallback path ko 100% traffic sambhalna hi chahiye. Nahi sambhal sakta to aapne single point of failure banaya hai.

**Aam galti:** Sirf happy path ke liye design karna aur raat 3 baje pata chalna ki low-confidence cases ka koi raasta hi nahi hai.

Practice: `examples/10_writing_the_system_design_document.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 118 ke baad aapko ye aana chahiye

- **Requirements: accuracy, latency, cost** ko bina notes dekhe kisi dost ko samjha sakna.
- **Data collection plan** ko bina notes dekhe kisi dost ko samjha sakna.
- **Annotation strategy and quality control** ko bina notes dekhe kisi dost ko samjha sakna.
- **Choosing the model family** ko bina notes dekhe kisi dost ko samjha sakna.
- **Handling class imbalance in vision** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
