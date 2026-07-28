# Day 149 — PROJECT: fine-tuned domain assistant

Aaj ka goal: **PROJECT: fine-tuned domain assistant** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Goal: a small model specialised to one task |
| 2 | Collecting and curating examples |
| 3 | Formatting an SFT dataset |
| 4 | Choosing base model and LoRA settings |
| 5 | Training run and monitoring |
| 6 | Evaluating against the base model |
| 7 | Comparing against a prompted large model |
| 8 | Cost and latency comparison |
| 9 | Deciding whether tuning was worth it |
| 10 | Packaging the adapter |

---

## 1. Goal: a small model specialised to one task

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

Practice: `examples/01_goal_a_small_model_specialised_to_one_ta.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Collecting and curating examples

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

Practice: `examples/02_collecting_and_curating_examples.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Formatting an SFT dataset

### Aasaan Bhasha

Fine-tuning pretrained model ko aapke examples par aur train karta hai. Ye format, tone aur task ki shape naye facts se kahin behtar sikhata hai — facts ke liye retrieval use karo. Kuch sau behtareen examples aksar das hazaar aam examples se behtar hote hain.

### Chhota code

```python
# Typical SFT record: the model learns the assistant turn only.
example = {
    'messages': [
        {'role': 'system', 'content': 'You extract invoice fields as JSON.'},
        {'role': 'user', 'content': 'Invoice 4471, dated 2024-03-02, total Rs 15,300.'},
        {'role': 'assistant', 'content': '{"id": "4471", "date": "2024-03-02", "total": 15300}'},
    ]
}
import json
print(json.dumps(example, indent=2))
print('\\nRule: mask the loss on system+user tokens; train only on the assistant response.')
```

**Yaad rakho:** Behaviour aur format ke liye fine-tune karo. Jo knowledge badalti rehti hai uske liye RAG.

**Aam galti:** Company facts daalne ke liye fine-tune karna, phir har policy document badalne par dobara train karna.

Practice: `examples/03_formatting_an_sft_dataset.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Choosing base model and LoRA settings

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

Practice: `examples/04_choosing_base_model_and_lora_settings.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Training run and monitoring

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

Practice: `examples/05_training_run_and_monitoring.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Evaluating against the base model

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

Practice: `examples/06_evaluating_against_the_base_model.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Comparing against a prompted large model

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

Practice: `examples/07_comparing_against_a_prompted_large_model.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Cost and latency comparison

### Aasaan Bhasha

Data parallelism model ki copies banata hai aur batch baant deta hai; model parallelism model ko baantta hai jab wo ek device par na aaye. Profiling ke baad hi scale karo — 'humein aur GPUs chahiye' wali zyadatar problems asal me dheema data loader hoti hain.

### Chhota code

```python
# Effective batch = per_device_batch * n_devices * grad_accum_steps
per_device, devices, accum = 8, 4, 4
print('effective batch size', per_device * devices * accum)
print('\\nGradient accumulation gives a large effective batch on small memory:')
print('  for i, batch in enumerate(loader):')
print('      loss = model(batch).loss / accum')
print('      loss.backward()')
print('      if (i + 1) % accum == 0:')
print('          opt.step(); opt.zero_grad()')
```

**Yaad rakho:** Pehle profile karo. GPU 30% utilisation par matlab bottleneck data pipeline hai, GPU nahi.

**Aam galti:** Batch scale karte waqt learning rate galat scale karna — bade batch ko aam taur par bada LR chahiye.

Practice: `examples/08_cost_and_latency_comparison.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Deciding whether tuning was worth it

### Aasaan Bhasha

Hyperparameters wo settings hain jo aap chunte ho, seekhi nahi jaatin. Grid search poora chhaanta hai aur barbaad karta hai; random search high dimensions me acche ilaake jaldi dhoondta hai; Bayesian search pichhle trials se seekhta hai. Search hamesha cross-validation ke andar karo.

### Chhota code

```python
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
import numpy as np

X, y = load_breast_cancer(return_X_y=True)
space = {
    'n_estimators': [100, 300, 600],
    'max_depth': [None, 4, 8, 16],
    'min_samples_leaf': [1, 2, 4, 8],
}
search = RandomizedSearchCV(
    RandomForestClassifier(random_state=0, n_jobs=-1),
    space, n_iter=12, cv=5, random_state=0,
).fit(X, y)
print(search.best_params_, round(search.best_score_, 4))
```

**Yaad rakho:** Random seed fix karo aur har trial log karo, warna aap apna hi best model dobara nahi bana paoge.

**Aam galti:** 400 rows par 40 hyperparameters tune karna — ab aap validation set hi fit kar rahe ho.

Practice: `examples/09_deciding_whether_tuning_was_worth_it.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Packaging the adapter

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

Practice: `examples/10_packaging_the_adapter.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 149 ke baad aapko ye aana chahiye

- **Goal: a small model specialised to one task** ko bina notes dekhe kisi dost ko samjha sakna.
- **Collecting and curating examples** ko bina notes dekhe kisi dost ko samjha sakna.
- **Formatting an SFT dataset** ko bina notes dekhe kisi dost ko samjha sakna.
- **Choosing base model and LoRA settings** ko bina notes dekhe kisi dost ko samjha sakna.
- **Training run and monitoring** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
