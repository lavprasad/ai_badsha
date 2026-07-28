# Day 180 — Experiment tracking and reproducibility

Aaj ka goal: **Experiment tracking and reproducibility** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | What to record for every run |
| 2 | MLflow and alternatives |
| 3 | Artefact storage |
| 4 | Data versioning with DVC |
| 5 | Seeding everything |
| 6 | Environment capture |
| 7 | Comparing runs |
| 8 | Linking a production model to its run |
| 9 | Reproducing a six-month-old result |
| 10 | A tracking habit that costs 5 minutes |

---

## 1. What to record for every run

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

Practice: `examples/01_what_to_record_for_every_run.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. MLflow and alternatives

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

Practice: `examples/02_mlflow_and_alternatives.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Artefact storage

### Aasaan Bhasha

RAG jawaabon ko aapke documents me jodta hai: chunk karo, embed karo, store karo, sawaal ke liye top-k retrieve karo, aur prompt me daal do. Retrieval ki quality hi poora khel hai — galat teen chunks se perfect model ka jawab bhi galat hi rahega.

### Chhota code

```python
import numpy as np

docs = [
    'Refunds are processed within 5 business days.',
    'Our office is in Pune, open 9am to 6pm.',
    'Enterprise plans include a dedicated support engineer.',
]

def fake_embed(text):                       # stand-in for a real embedding model
    rng = np.random.default_rng(abs(hash(text)) % (2 ** 32))
    v = rng.normal(size=32)
    return v / np.linalg.norm(v)

index = np.array([fake_embed(d) for d in docs])
q = fake_embed('how long do refunds take')
top = int(np.argmax(index @ q))
print('retrieved:', docs[top])
print('\\nReal pipeline: chunk 300-800 tokens with overlap -> embed -> ANN index -> rerank -> prompt.')
```

**Yaad rakho:** Jawab me har retrieved chunk ka source dikhao taaki users use verify kar sakein.

**Aam galti:** Aankh band karke 1000 characters par chunk karna aur tables aur code blocks ko beech se kaat dena.

Practice: `examples/03_artefact_storage.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Data versioning with DVC

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

Practice: `examples/04_data_versioning_with_dvc.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Seeding everything

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

Practice: `examples/05_seeding_everything.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Environment capture

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

Practice: `examples/06_environment_capture.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Comparing runs

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

Practice: `examples/07_comparing_runs.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Linking a production model to its run

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

Practice: `examples/08_linking_a_production_model_to_its_run.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Reproducing a six-month-old result

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

Practice: `examples/09_reproducing_a_six_month_old_result.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. A tracking habit that costs 5 minutes

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

Practice: `examples/10_a_tracking_habit_that_costs_5_minutes.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 180 ke baad aapko ye aana chahiye

- **What to record for every run** ko bina notes dekhe kisi dost ko samjha sakna.
- **MLflow and alternatives** ko bina notes dekhe kisi dost ko samjha sakna.
- **Artefact storage** ko bina notes dekhe kisi dost ko samjha sakna.
- **Data versioning with DVC** ko bina notes dekhe kisi dost ko samjha sakna.
- **Seeding everything** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
