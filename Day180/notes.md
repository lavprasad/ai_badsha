# Day 180 — Experiment tracking and reproducibility

Today's goal: work through **Experiment tracking and reproducibility** — ten concepts, ten runnable examples, five questions.

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

An experiment you cannot reproduce is an anecdote. Track for every run: code commit, data version, hyperparameters, metrics and the artefact. Six months later, 'which run produced the model in production' must have an answer.

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

**Remember:** Log the data version alongside the code version — data changes silently, code changes loudly.

**Common mistake:** Naming files `model_final_v2_REAL_use_this.pkl` instead of using a registry.

Practice: open `examples/01_what_to_record_for_every_run.py`, predict the output, change one line, predict again.

## 2. MLflow and alternatives

An experiment you cannot reproduce is an anecdote. Track for every run: code commit, data version, hyperparameters, metrics and the artefact. Six months later, 'which run produced the model in production' must have an answer.

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

**Remember:** Log the data version alongside the code version — data changes silently, code changes loudly.

**Common mistake:** Naming files `model_final_v2_REAL_use_this.pkl` instead of using a registry.

Practice: open `examples/02_mlflow_and_alternatives.py`, predict the output, change one line, predict again.

## 3. Artefact storage

RAG grounds answers in your documents: chunk, embed, store, retrieve the top-k for the question, and put them in the prompt. Retrieval quality is the whole ballgame — a perfect model answering from the wrong three chunks is still wrong.

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

**Remember:** Always show the source of each retrieved chunk in the answer so users can verify it.

**Common mistake:** Chunking blindly at 1000 characters and cutting tables and code blocks in half.

Practice: open `examples/03_artefact_storage.py`, predict the output, change one line, predict again.

## 4. Data versioning with DVC

An experiment you cannot reproduce is an anecdote. Track for every run: code commit, data version, hyperparameters, metrics and the artefact. Six months later, 'which run produced the model in production' must have an answer.

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

**Remember:** Log the data version alongside the code version — data changes silently, code changes loudly.

**Common mistake:** Naming files `model_final_v2_REAL_use_this.pkl` instead of using a registry.

Practice: open `examples/04_data_versioning_with_dvc.py`, predict the output, change one line, predict again.

## 5. Seeding everything

An experiment you cannot reproduce is an anecdote. Track for every run: code commit, data version, hyperparameters, metrics and the artefact. Six months later, 'which run produced the model in production' must have an answer.

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

**Remember:** Log the data version alongside the code version — data changes silently, code changes loudly.

**Common mistake:** Naming files `model_final_v2_REAL_use_this.pkl` instead of using a registry.

Practice: open `examples/05_seeding_everything.py`, predict the output, change one line, predict again.

## 6. Environment capture

An experiment you cannot reproduce is an anecdote. Track for every run: code commit, data version, hyperparameters, metrics and the artefact. Six months later, 'which run produced the model in production' must have an answer.

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

**Remember:** Log the data version alongside the code version — data changes silently, code changes loudly.

**Common mistake:** Naming files `model_final_v2_REAL_use_this.pkl` instead of using a registry.

Practice: open `examples/06_environment_capture.py`, predict the output, change one line, predict again.

## 7. Comparing runs

An experiment you cannot reproduce is an anecdote. Track for every run: code commit, data version, hyperparameters, metrics and the artefact. Six months later, 'which run produced the model in production' must have an answer.

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

**Remember:** Log the data version alongside the code version — data changes silently, code changes loudly.

**Common mistake:** Naming files `model_final_v2_REAL_use_this.pkl` instead of using a registry.

Practice: open `examples/07_comparing_runs.py`, predict the output, change one line, predict again.

## 8. Linking a production model to its run

An experiment you cannot reproduce is an anecdote. Track for every run: code commit, data version, hyperparameters, metrics and the artefact. Six months later, 'which run produced the model in production' must have an answer.

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

**Remember:** Log the data version alongside the code version — data changes silently, code changes loudly.

**Common mistake:** Naming files `model_final_v2_REAL_use_this.pkl` instead of using a registry.

Practice: open `examples/08_linking_a_production_model_to_its_run.py`, predict the output, change one line, predict again.

## 9. Reproducing a six-month-old result

An experiment you cannot reproduce is an anecdote. Track for every run: code commit, data version, hyperparameters, metrics and the artefact. Six months later, 'which run produced the model in production' must have an answer.

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

**Remember:** Log the data version alongside the code version — data changes silently, code changes loudly.

**Common mistake:** Naming files `model_final_v2_REAL_use_this.pkl` instead of using a registry.

Practice: open `examples/09_reproducing_a_six_month_old_result.py`, predict the output, change one line, predict again.

## 10. A tracking habit that costs 5 minutes

An experiment you cannot reproduce is an anecdote. Track for every run: code commit, data version, hyperparameters, metrics and the artefact. Six months later, 'which run produced the model in production' must have an answer.

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

**Remember:** Log the data version alongside the code version — data changes silently, code changes loudly.

**Common mistake:** Naming files `model_final_v2_REAL_use_this.pkl` instead of using a registry.

Practice: open `examples/10_a_tracking_habit_that_costs_5_minutes.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 180

- Explain **What to record for every run** to someone else without notes.
- Explain **MLflow and alternatives** to someone else without notes.
- Explain **Artefact storage** to someone else without notes.
- Explain **Data versioning with DVC** to someone else without notes.
- Explain **Seeding everything** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
