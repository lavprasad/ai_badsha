# Day 73 — Error analysis

Aaj ka goal: **Error analysis** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Why aggregate metrics hide the problem |
| 2 | Slicing errors by segment |
| 3 | Building an error taxonomy |
| 4 | Hand-labelling 50 wrong predictions |
| 5 | Identifying the biggest error bucket |
| 6 | Deciding: more data, better features, or new model |
| 7 | Confusion matrix deep dive |
| 8 | Finding annotation errors in the labels |
| 9 | Prioritising fixes by business impact |
| 10 | Turning error analysis into a backlog |

---

## 1. Why aggregate metrics hide the problem

### Aasaan Bhasha

Ek accuracy number aapko ye nahi batata ki kya theek karna hai. Galat predictions nikaalo, pachaas haath se padho, aur unhe buckets me baanto. Aam taur par ek bucket 40% errors ka hota hai aur uska fix obvious hota hai — aur hairaani ki baat ye ki achha khaasa hissa galat labels nikalta hai, galat predictions nahi.

### Chhota code

```python
import numpy as np
import pandas as pd

rng = np.random.default_rng(0)
df = pd.DataFrame({
    'segment': rng.choice(['new', 'returning', 'enterprise'], 600, p=[.5, .3, .2]),
    'y': rng.integers(0, 2, 600),
})
df['pred'] = np.where(df.segment == 'enterprise', 1 - df.y, df.y)   # broken on one segment

report = (df.assign(wrong=df.pred != df.y)
            .groupby('segment')
            .agg(n=('wrong', 'size'), errors=('wrong', 'sum')))
report['error_rate'] = (report.errors / report.n).round(3)
report['share_of_all_errors'] = (report.errors / report.errors.sum()).round(3)
print(report.sort_values('share_of_all_errors', ascending=False))
```

**Yaad rakho:** Error buckets ko total errors ke share se rank karo, error rate se nahi — wahi theek karo jo sach me mehnga pad raha hai.

**Aam galti:** Overall accuracy optimise karte rehna jab ek segment chupchap 0% de raha ho aur saari shikaayatein wahi se aa rahi hon.

Practice: `examples/01_why_aggregate_metrics_hide_the_problem.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Slicing errors by segment

### Aasaan Bhasha

ML code ko baaki code jaise tests chahiye, plus data tests: schema, ranges, null rates, class balance. Har known failure mode ke liye ek behavioural test jodo — ek test jo pichhli baar ka outage pakad leta, wo 90% coverage se zyada keemti hai.

### Chhota code

```python
import numpy as np

def preprocess(x):
    x = np.asarray(x, dtype=float)
    if np.isnan(x).any():
        raise ValueError('NaN in input')
    return (x - x.mean()) / (x.std() + 1e-8)

def test_preprocess():
    out = preprocess([1.0, 2.0, 3.0])
    assert abs(float(out.mean())) < 1e-6, 'should be zero-centred'
    assert abs(float(out.std()) - 1.0) < 1e-6, 'should be unit variance'
    try:
        preprocess([1.0, float('nan')])
    except ValueError:
        pass
    else:
        raise AssertionError('NaN should have raised')
    print('ok')

test_preprocess()
```

**Yaad rakho:** Data contract test karo, sirf function nahi — kharab data kharab code se zyada models todta hai.

**Aam galti:** Sirf happy path test karna, jisse poora-null column chupchap constant model train kar deta hai.

Practice: `examples/02_slicing_errors_by_segment.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Building an error taxonomy

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

Practice: `examples/03_building_an_error_taxonomy.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Hand-labelling 50 wrong predictions

### Aasaan Bhasha

Ek accuracy number aapko ye nahi batata ki kya theek karna hai. Galat predictions nikaalo, pachaas haath se padho, aur unhe buckets me baanto. Aam taur par ek bucket 40% errors ka hota hai aur uska fix obvious hota hai — aur hairaani ki baat ye ki achha khaasa hissa galat labels nikalta hai, galat predictions nahi.

### Chhota code

```python
import numpy as np
import pandas as pd

rng = np.random.default_rng(0)
df = pd.DataFrame({
    'segment': rng.choice(['new', 'returning', 'enterprise'], 600, p=[.5, .3, .2]),
    'y': rng.integers(0, 2, 600),
})
df['pred'] = np.where(df.segment == 'enterprise', 1 - df.y, df.y)   # broken on one segment

report = (df.assign(wrong=df.pred != df.y)
            .groupby('segment')
            .agg(n=('wrong', 'size'), errors=('wrong', 'sum')))
report['error_rate'] = (report.errors / report.n).round(3)
report['share_of_all_errors'] = (report.errors / report.errors.sum()).round(3)
print(report.sort_values('share_of_all_errors', ascending=False))
```

**Yaad rakho:** Error buckets ko total errors ke share se rank karo, error rate se nahi — wahi theek karo jo sach me mehnga pad raha hai.

**Aam galti:** Overall accuracy optimise karte rehna jab ek segment chupchap 0% de raha ho aur saari shikaayatein wahi se aa rahi hon.

Practice: `examples/04_hand_labelling_50_wrong_predictions.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Identifying the biggest error bucket

### Aasaan Bhasha

Ek accuracy number aapko ye nahi batata ki kya theek karna hai. Galat predictions nikaalo, pachaas haath se padho, aur unhe buckets me baanto. Aam taur par ek bucket 40% errors ka hota hai aur uska fix obvious hota hai — aur hairaani ki baat ye ki achha khaasa hissa galat labels nikalta hai, galat predictions nahi.

### Chhota code

```python
import numpy as np
import pandas as pd

rng = np.random.default_rng(0)
df = pd.DataFrame({
    'segment': rng.choice(['new', 'returning', 'enterprise'], 600, p=[.5, .3, .2]),
    'y': rng.integers(0, 2, 600),
})
df['pred'] = np.where(df.segment == 'enterprise', 1 - df.y, df.y)   # broken on one segment

report = (df.assign(wrong=df.pred != df.y)
            .groupby('segment')
            .agg(n=('wrong', 'size'), errors=('wrong', 'sum')))
report['error_rate'] = (report.errors / report.n).round(3)
report['share_of_all_errors'] = (report.errors / report.errors.sum()).round(3)
print(report.sort_values('share_of_all_errors', ascending=False))
```

**Yaad rakho:** Error buckets ko total errors ke share se rank karo, error rate se nahi — wahi theek karo jo sach me mehnga pad raha hai.

**Aam galti:** Overall accuracy optimise karte rehna jab ek segment chupchap 0% de raha ho aur saari shikaayatein wahi se aa rahi hon.

Practice: `examples/05_identifying_the_biggest_error_bucket.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Deciding: more data, better features, or new model

### Aasaan Bhasha

ML code ko baaki code jaise tests chahiye, plus data tests: schema, ranges, null rates, class balance. Har known failure mode ke liye ek behavioural test jodo — ek test jo pichhli baar ka outage pakad leta, wo 90% coverage se zyada keemti hai.

### Chhota code

```python
import numpy as np

def preprocess(x):
    x = np.asarray(x, dtype=float)
    if np.isnan(x).any():
        raise ValueError('NaN in input')
    return (x - x.mean()) / (x.std() + 1e-8)

def test_preprocess():
    out = preprocess([1.0, 2.0, 3.0])
    assert abs(float(out.mean())) < 1e-6, 'should be zero-centred'
    assert abs(float(out.std()) - 1.0) < 1e-6, 'should be unit variance'
    try:
        preprocess([1.0, float('nan')])
    except ValueError:
        pass
    else:
        raise AssertionError('NaN should have raised')
    print('ok')

test_preprocess()
```

**Yaad rakho:** Data contract test karo, sirf function nahi — kharab data kharab code se zyada models todta hai.

**Aam galti:** Sirf happy path test karna, jisse poora-null column chupchap constant model train kar deta hai.

Practice: `examples/06_deciding_more_data_better_features_or_ne.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Confusion matrix deep dive

### Aasaan Bhasha

Matrix ek linear transformation hai. Matrices ko multiply karna transformations ko jodta hai — neural network ki layers stack karna bilkul yahi hai. Shapes milni chahiye: (m,k) @ (k,n) -> (m,n); andar wale dimensions match hone chahiye aur wahi gayab ho jaate hain.

### Chhota code

```python
import numpy as np

A = np.random.default_rng(0).normal(size=(3, 4))
B = np.random.default_rng(1).normal(size=(4, 2))

print((A @ B).shape)      # (3, 2)
print(A.T.shape)          # (4, 3)
print(np.eye(3) @ A is not A, np.allclose(np.eye(3) @ A, A))
```

**Yaad rakho:** Har shape error ko 'andar wale dimensions match nahi hue' padho aur shapes print kar do.

**Aam galti:** `Ax=b` solve karne ke liye `np.linalg.inv` uthana, jabki `np.linalg.solve` zyada safe hai.

Practice: `examples/07_confusion_matrix_deep_dive.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Finding annotation errors in the labels

### Aasaan Bhasha

Ek accuracy number aapko ye nahi batata ki kya theek karna hai. Galat predictions nikaalo, pachaas haath se padho, aur unhe buckets me baanto. Aam taur par ek bucket 40% errors ka hota hai aur uska fix obvious hota hai — aur hairaani ki baat ye ki achha khaasa hissa galat labels nikalta hai, galat predictions nahi.

### Chhota code

```python
import numpy as np
import pandas as pd

rng = np.random.default_rng(0)
df = pd.DataFrame({
    'segment': rng.choice(['new', 'returning', 'enterprise'], 600, p=[.5, .3, .2]),
    'y': rng.integers(0, 2, 600),
})
df['pred'] = np.where(df.segment == 'enterprise', 1 - df.y, df.y)   # broken on one segment

report = (df.assign(wrong=df.pred != df.y)
            .groupby('segment')
            .agg(n=('wrong', 'size'), errors=('wrong', 'sum')))
report['error_rate'] = (report.errors / report.n).round(3)
report['share_of_all_errors'] = (report.errors / report.errors.sum()).round(3)
print(report.sort_values('share_of_all_errors', ascending=False))
```

**Yaad rakho:** Error buckets ko total errors ke share se rank karo, error rate se nahi — wahi theek karo jo sach me mehnga pad raha hai.

**Aam galti:** Overall accuracy optimise karte rehna jab ek segment chupchap 0% de raha ho aur saari shikaayatein wahi se aa rahi hon.

Practice: `examples/08_finding_annotation_errors_in_the_labels.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Prioritising fixes by business impact

### Aasaan Bhasha

Bayes rule evidence ke saath belief update karta hai: posterior = likelihood x prior / evidence. Applied ML ki sabse common galti prior ignore karna hai — 10000 me 1 wali bimari ke liye 99% accurate test bhi zyadatar false positives hi deta hai.

### Chhota code

```python
prior = 1 / 10_000          # base rate of the disease
sensitivity = 0.99          # P(positive | sick)
false_positive = 0.01       # P(positive | healthy)

evidence = sensitivity * prior + false_positive * (1 - prior)
posterior = sensitivity * prior / evidence
print(f'P(sick | positive) = {posterior:.4f}')   # ~0.0098
```

**Yaad rakho:** Rare events par precision gir hi jaati hai, chahe classifier accuracy par kitna bhi accha lage.

**Aam galti:** Imbalanced problem par accuracy report karna jahan hamesha 'no' bolne se 99% mil jaata hai.

Practice: `examples/09_prioritising_fixes_by_business_impact.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Turning error analysis into a backlog

### Aasaan Bhasha

Ek accuracy number aapko ye nahi batata ki kya theek karna hai. Galat predictions nikaalo, pachaas haath se padho, aur unhe buckets me baanto. Aam taur par ek bucket 40% errors ka hota hai aur uska fix obvious hota hai — aur hairaani ki baat ye ki achha khaasa hissa galat labels nikalta hai, galat predictions nahi.

### Chhota code

```python
import numpy as np
import pandas as pd

rng = np.random.default_rng(0)
df = pd.DataFrame({
    'segment': rng.choice(['new', 'returning', 'enterprise'], 600, p=[.5, .3, .2]),
    'y': rng.integers(0, 2, 600),
})
df['pred'] = np.where(df.segment == 'enterprise', 1 - df.y, df.y)   # broken on one segment

report = (df.assign(wrong=df.pred != df.y)
            .groupby('segment')
            .agg(n=('wrong', 'size'), errors=('wrong', 'sum')))
report['error_rate'] = (report.errors / report.n).round(3)
report['share_of_all_errors'] = (report.errors / report.errors.sum()).round(3)
print(report.sort_values('share_of_all_errors', ascending=False))
```

**Yaad rakho:** Error buckets ko total errors ke share se rank karo, error rate se nahi — wahi theek karo jo sach me mehnga pad raha hai.

**Aam galti:** Overall accuracy optimise karte rehna jab ek segment chupchap 0% de raha ho aur saari shikaayatein wahi se aa rahi hon.

Practice: `examples/10_turning_error_analysis_into_a_backlog.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 73 ke baad aapko ye aana chahiye

- **Why aggregate metrics hide the problem** ko bina notes dekhe kisi dost ko samjha sakna.
- **Slicing errors by segment** ko bina notes dekhe kisi dost ko samjha sakna.
- **Building an error taxonomy** ko bina notes dekhe kisi dost ko samjha sakna.
- **Hand-labelling 50 wrong predictions** ko bina notes dekhe kisi dost ko samjha sakna.
- **Identifying the biggest error bucket** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
