# Day 185 — Data engineering for AI

Aaj ka goal: **Data engineering for AI** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

### Aasaan Bhasha

Pipelines idempotent honi chahiye: wahi din dobara chalane par wahi result aaye, duplicates nahi. Output ko date se partition karo taaki backfill poori table ke bajaye ek partition dobara likhe. Pehle batch — streaming operational cost double kar deta hai aur zyadatar teams ko wo latency chahiye hi nahi.

### Chhota code

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

**Yaad rakho:** Idempotent + partitioned = safe backfills. Append-only pipelines har rerun ko data corruption bana deti hain.

**Aam galti:** Aisi pipeline jo append karti hai, jisse retry hua job chupchap kal ke numbers double kar deta hai.

Practice: `examples/01_batch_vs_streaming_ingestion.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. ETL and ELT patterns

### Aasaan Bhasha

Pipelines idempotent honi chahiye: wahi din dobara chalane par wahi result aaye, duplicates nahi. Output ko date se partition karo taaki backfill poori table ke bajaye ek partition dobara likhe. Pehle batch — streaming operational cost double kar deta hai aur zyadatar teams ko wo latency chahiye hi nahi.

### Chhota code

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

**Yaad rakho:** Idempotent + partitioned = safe backfills. Append-only pipelines har rerun ko data corruption bana deti hain.

**Aam galti:** Aisi pipeline jo append karti hai, jisse retry hua job chupchap kal ke numbers double kar deta hai.

Practice: `examples/02_etl_and_elt_patterns.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Orchestration with Airflow or Prefect

### Aasaan Bhasha

Pipelines idempotent honi chahiye: wahi din dobara chalane par wahi result aaye, duplicates nahi. Output ko date se partition karo taaki backfill poori table ke bajaye ek partition dobara likhe. Pehle batch — streaming operational cost double kar deta hai aur zyadatar teams ko wo latency chahiye hi nahi.

### Chhota code

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

**Yaad rakho:** Idempotent + partitioned = safe backfills. Append-only pipelines har rerun ko data corruption bana deti hain.

**Aam galti:** Aisi pipeline jo append karti hai, jisse retry hua job chupchap kal ke numbers double kar deta hai.

Practice: `examples/03_orchestration_with_airflow_or_prefect.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Idempotent pipeline design

### Aasaan Bhasha

Pipeline preprocessing aur model ko ek hi object me jod deta hai jo ek unit ki tarah fit aur predict karta hai. Leakage ke khilaaf yahi sabse achhi dhaal hai, aur deployment ko chhe alag steps ke bajaye ek artefact milta hai jise yaad rakhne ki zaroorat nahi.

### Chhota code

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

**Yaad rakho:** `handle_unknown='ignore'` production ko us category par crash hone se bachata hai jo training me kabhi nahi dikhi.

**Aam galti:** Notebook me preprocess karna aur serving code likhte waqt ek step bhool jaana.

Practice: `examples/04_idempotent_pipeline_design.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Partitioning and file formats

### Aasaan Bhasha

Pipelines idempotent honi chahiye: wahi din dobara chalane par wahi result aaye, duplicates nahi. Output ko date se partition karo taaki backfill poori table ke bajaye ek partition dobara likhe. Pehle batch — streaming operational cost double kar deta hai aur zyadatar teams ko wo latency chahiye hi nahi.

### Chhota code

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

**Yaad rakho:** Idempotent + partitioned = safe backfills. Append-only pipelines har rerun ko data corruption bana deti hain.

**Aam galti:** Aisi pipeline jo append karti hai, jisse retry hua job chupchap kal ke numbers double kar deta hai.

Practice: `examples/05_partitioning_and_file_formats.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Data lake vs warehouse

### Aasaan Bhasha

Pipelines idempotent honi chahiye: wahi din dobara chalane par wahi result aaye, duplicates nahi. Output ko date se partition karo taaki backfill poori table ke bajaye ek partition dobara likhe. Pehle batch — streaming operational cost double kar deta hai aur zyadatar teams ko wo latency chahiye hi nahi.

### Chhota code

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

**Yaad rakho:** Idempotent + partitioned = safe backfills. Append-only pipelines har rerun ko data corruption bana deti hain.

**Aam galti:** Aisi pipeline jo append karti hai, jisse retry hua job chupchap kal ke numbers double kar deta hai.

Practice: `examples/06_data_lake_vs_warehouse.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Incremental processing

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

Practice: `examples/07_incremental_processing.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Backfills without breaking things

### Aasaan Bhasha

Pipelines idempotent honi chahiye: wahi din dobara chalane par wahi result aaye, duplicates nahi. Output ko date se partition karo taaki backfill poori table ke bajaye ek partition dobara likhe. Pehle batch — streaming operational cost double kar deta hai aur zyadatar teams ko wo latency chahiye hi nahi.

### Chhota code

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

**Yaad rakho:** Idempotent + partitioned = safe backfills. Append-only pipelines har rerun ko data corruption bana deti hain.

**Aam galti:** Aisi pipeline jo append karti hai, jisse retry hua job chupchap kal ke numbers double kar deta hai.

Practice: `examples/08_backfills_without_breaking_things.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Data quality monitoring

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

Practice: `examples/09_data_quality_monitoring.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Cost of storage and compute

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

Practice: `examples/10_cost_of_storage_and_compute.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 185 ke baad aapko ye aana chahiye

- **Batch vs streaming ingestion** ko bina notes dekhe kisi dost ko samjha sakna.
- **ETL and ELT patterns** ko bina notes dekhe kisi dost ko samjha sakna.
- **Orchestration with Airflow or Prefect** ko bina notes dekhe kisi dost ko samjha sakna.
- **Idempotent pipeline design** ko bina notes dekhe kisi dost ko samjha sakna.
- **Partitioning and file formats** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
