# Day 185 — Data engineering for AI

Today's goal: work through **Data engineering for AI** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Batch vs streaming ingestion |
| 2 | ETL and ELT patterns |
| 3 | Orchestration with Airflow or Prefect |
| 4 | Idempotent pipeline design |
| 5 | Partitioning and file formats |
| 6 | Data lake vs warehouse |
| 7 | Incremental processing |
| 8 | Backfills without breaking things |
| 9 | Data quality monitoring |
| 10 | Cost of storage and compute |

---

## 1. Batch vs streaming ingestion

Pipelines must be idempotent: re-running the same day must produce the same result, not duplicates. Partition output by date so backfills rewrite one partition instead of the whole table. Batch first — streaming doubles the operational cost and most teams do not need the latency.

```python
from pathlib import Path

def write_partition(root, date, rows):
    """Idempotent: rewriting a partition replaces it, never appends."""
    part = Path(root) / f'dt={date}'
    part.mkdir(parents=True, exist_ok=True)
    out = part / 'data.csv'
    out.write_text('\n'.join(rows), encoding='utf-8')
    return out

root = 'demo_lake'
print(write_partition(root, '2024-03-01', ['a,1', 'b,2']))
print(write_partition(root, '2024-03-01', ['a,1', 'b,2']))   # re-run: same result

import shutil; shutil.rmtree(root)
```

**Remember:** Idempotent + partitioned = safe backfills. Append-only pipelines make every rerun a data corruption event.

**Common mistake:** A pipeline that appends, so a retried job silently doubles yesterday's numbers.

## 2. ETL and ELT patterns

Pipelines must be idempotent: re-running the same day must produce the same result, not duplicates. Partition output by date so backfills rewrite one partition instead of the whole table. Batch first — streaming doubles the operational cost and most teams do not need the latency.

```python
from pathlib import Path

def write_partition(root, date, rows):
    """Idempotent: rewriting a partition replaces it, never appends."""
    part = Path(root) / f'dt={date}'
    part.mkdir(parents=True, exist_ok=True)
    out = part / 'data.csv'
    out.write_text('\n'.join(rows), encoding='utf-8')
    return out

root = 'demo_lake'
print(write_partition(root, '2024-03-01', ['a,1', 'b,2']))
print(write_partition(root, '2024-03-01', ['a,1', 'b,2']))   # re-run: same result

import shutil; shutil.rmtree(root)
```

**Remember:** Idempotent + partitioned = safe backfills. Append-only pipelines make every rerun a data corruption event.

**Common mistake:** A pipeline that appends, so a retried job silently doubles yesterday's numbers.

## 3. Orchestration with Airflow or Prefect

Pipelines must be idempotent: re-running the same day must produce the same result, not duplicates. Partition output by date so backfills rewrite one partition instead of the whole table. Batch first — streaming doubles the operational cost and most teams do not need the latency.

```python
from pathlib import Path

def write_partition(root, date, rows):
    """Idempotent: rewriting a partition replaces it, never appends."""
    part = Path(root) / f'dt={date}'
    part.mkdir(parents=True, exist_ok=True)
    out = part / 'data.csv'
    out.write_text('\n'.join(rows), encoding='utf-8')
    return out

root = 'demo_lake'
print(write_partition(root, '2024-03-01', ['a,1', 'b,2']))
print(write_partition(root, '2024-03-01', ['a,1', 'b,2']))   # re-run: same result

import shutil; shutil.rmtree(root)
```

**Remember:** Idempotent + partitioned = safe backfills. Append-only pipelines make every rerun a data corruption event.

**Common mistake:** A pipeline that appends, so a retried job silently doubles yesterday's numbers.

## 4. Idempotent pipeline design

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

## 5. Partitioning and file formats

Pipelines must be idempotent: re-running the same day must produce the same result, not duplicates. Partition output by date so backfills rewrite one partition instead of the whole table. Batch first — streaming doubles the operational cost and most teams do not need the latency.

```python
from pathlib import Path

def write_partition(root, date, rows):
    """Idempotent: rewriting a partition replaces it, never appends."""
    part = Path(root) / f'dt={date}'
    part.mkdir(parents=True, exist_ok=True)
    out = part / 'data.csv'
    out.write_text('\n'.join(rows), encoding='utf-8')
    return out

root = 'demo_lake'
print(write_partition(root, '2024-03-01', ['a,1', 'b,2']))
print(write_partition(root, '2024-03-01', ['a,1', 'b,2']))   # re-run: same result

import shutil; shutil.rmtree(root)
```

**Remember:** Idempotent + partitioned = safe backfills. Append-only pipelines make every rerun a data corruption event.

**Common mistake:** A pipeline that appends, so a retried job silently doubles yesterday's numbers.

## 6. Data lake vs warehouse

Pipelines must be idempotent: re-running the same day must produce the same result, not duplicates. Partition output by date so backfills rewrite one partition instead of the whole table. Batch first — streaming doubles the operational cost and most teams do not need the latency.

```python
from pathlib import Path

def write_partition(root, date, rows):
    """Idempotent: rewriting a partition replaces it, never appends."""
    part = Path(root) / f'dt={date}'
    part.mkdir(parents=True, exist_ok=True)
    out = part / 'data.csv'
    out.write_text('\n'.join(rows), encoding='utf-8')
    return out

root = 'demo_lake'
print(write_partition(root, '2024-03-01', ['a,1', 'b,2']))
print(write_partition(root, '2024-03-01', ['a,1', 'b,2']))   # re-run: same result

import shutil; shutil.rmtree(root)
```

**Remember:** Idempotent + partitioned = safe backfills. Append-only pipelines make every rerun a data corruption event.

**Common mistake:** A pipeline that appends, so a retried job silently doubles yesterday's numbers.

## 7. Incremental processing

Accuracy hides everything on imbalanced data. Precision asks 'of the ones I flagged, how many were real'; recall asks 'of the real ones, how many did I catch'. You trade one for the other with the threshold, and the business decides which error hurts more.

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

**Remember:** Tune the decision threshold on validation data; 0.5 is a default, not a decision.

**Common mistake:** Optimising ROC-AUC on a heavily imbalanced problem where precision-recall AUC is the honest metric.

## 8. Backfills without breaking things

Pipelines must be idempotent: re-running the same day must produce the same result, not duplicates. Partition output by date so backfills rewrite one partition instead of the whole table. Batch first — streaming doubles the operational cost and most teams do not need the latency.

```python
from pathlib import Path

def write_partition(root, date, rows):
    """Idempotent: rewriting a partition replaces it, never appends."""
    part = Path(root) / f'dt={date}'
    part.mkdir(parents=True, exist_ok=True)
    out = part / 'data.csv'
    out.write_text('\n'.join(rows), encoding='utf-8')
    return out

root = 'demo_lake'
print(write_partition(root, '2024-03-01', ['a,1', 'b,2']))
print(write_partition(root, '2024-03-01', ['a,1', 'b,2']))   # re-run: same result

import shutil; shutil.rmtree(root)
```

**Remember:** Idempotent + partitioned = safe backfills. Append-only pipelines make every rerun a data corruption event.

**Common mistake:** A pipeline that appends, so a retried job silently doubles yesterday's numbers.

## 9. Data quality monitoring

Models rot. The world moves, inputs shift (data drift) or the relationship itself changes (concept drift). Monitor input distributions and prediction distributions daily, because ground-truth labels usually arrive weeks late.

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

**Remember:** PSI under 0.1 stable, 0.1-0.2 watch, above 0.2 investigate. Alert on the prediction distribution too.

**Common mistake:** Only monitoring uptime, so a model that returns 200 OK while being badly wrong looks healthy.

## 10. Cost of storage and compute

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

---

## What you should be able to do after Day 185

- Explain **Batch vs streaming ingestion** to someone else without notes.
- Explain **ETL and ELT patterns** to someone else without notes.
- Explain **Orchestration with Airflow or Prefect** to someone else without notes.
- Explain **Idempotent pipeline design** to someone else without notes.
- Explain **Partitioning and file formats** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
