# Day 36 — Getting data

Today's goal: work through **Getting data** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Public dataset sources |
| 2 | APIs and pagination |
| 3 | Web scraping ethics and robots.txt |
| 4 | Database extracts |
| 5 | File formats: CSV, Parquet, JSONL |
| 6 | Parquet and columnar storage |
| 7 | Data licensing and terms of use |
| 8 | Personally identifiable information |
| 9 | Sampling a large source safely |
| 10 | Documenting data provenance |

---

## 1. Public dataset sources

Where data comes from decides what you may do with it. Check the licence before you train, strip or hash personal identifiers early, and record provenance so you can answer 'where did this row come from' a year later. Paginated APIs need backoff and idempotent resume.

```python
import hashlib, time

def pseudonymise(email, salt='project-salt'):
    return hashlib.sha256((salt + email.lower()).encode()).hexdigest()[:16]

print(pseudonymise('User@Example.com'))

def fetch_pages(fetch, max_pages=5):
    """fetch(page) -> (rows, has_more). Backs off on failure."""
    out, page, delay = [], 1, 1.0
    while page <= max_pages:
        rows, has_more = fetch(page)
        out.extend(rows)
        if not has_more:
            break
        page += 1
    return out

print(fetch_pages(lambda p: ([f'row{p}'], p < 3)))
```

**Remember:** Hash or drop identifiers at ingestion, not at report time — by then copies already exist.

**Common mistake:** Scraping a source whose terms forbid it and discovering the problem after the model is in production.

Practice: open `examples/01_public_dataset_sources.py`, predict the output, change one line, predict again.

## 2. APIs and pagination

Where data comes from decides what you may do with it. Check the licence before you train, strip or hash personal identifiers early, and record provenance so you can answer 'where did this row come from' a year later. Paginated APIs need backoff and idempotent resume.

```python
import hashlib, time

def pseudonymise(email, salt='project-salt'):
    return hashlib.sha256((salt + email.lower()).encode()).hexdigest()[:16]

print(pseudonymise('User@Example.com'))

def fetch_pages(fetch, max_pages=5):
    """fetch(page) -> (rows, has_more). Backs off on failure."""
    out, page, delay = [], 1, 1.0
    while page <= max_pages:
        rows, has_more = fetch(page)
        out.extend(rows)
        if not has_more:
            break
        page += 1
    return out

print(fetch_pages(lambda p: ([f'row{p}'], p < 3)))
```

**Remember:** Hash or drop identifiers at ingestion, not at report time — by then copies already exist.

**Common mistake:** Scraping a source whose terms forbid it and discovering the problem after the model is in production.

Practice: open `examples/02_apis_and_pagination.py`, predict the output, change one line, predict again.

## 3. Web scraping ethics and robots.txt

Models learn the bias in their training data and then apply it at scale with a veneer of objectivity. Measure error rates per group, not just overall. Fairness definitions genuinely conflict with each other — you must choose one explicitly and document why.

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

**Remember:** Dropping the sensitive attribute does not remove bias; proxies (pincode, name) carry it right back in.

**Common mistake:** Auditing fairness once at launch and never again as the data drifts.

Practice: open `examples/03_web_scraping_ethics_and_robots_txt.py`, predict the output, change one line, predict again.

## 4. Database extracts

Where data comes from decides what you may do with it. Check the licence before you train, strip or hash personal identifiers early, and record provenance so you can answer 'where did this row come from' a year later. Paginated APIs need backoff and idempotent resume.

```python
import hashlib, time

def pseudonymise(email, salt='project-salt'):
    return hashlib.sha256((salt + email.lower()).encode()).hexdigest()[:16]

print(pseudonymise('User@Example.com'))

def fetch_pages(fetch, max_pages=5):
    """fetch(page) -> (rows, has_more). Backs off on failure."""
    out, page, delay = [], 1, 1.0
    while page <= max_pages:
        rows, has_more = fetch(page)
        out.extend(rows)
        if not has_more:
            break
        page += 1
    return out

print(fetch_pages(lambda p: ([f'row{p}'], p < 3)))
```

**Remember:** Hash or drop identifiers at ingestion, not at report time — by then copies already exist.

**Common mistake:** Scraping a source whose terms forbid it and discovering the problem after the model is in production.

Practice: open `examples/04_database_extracts.py`, predict the output, change one line, predict again.

## 5. File formats: CSV, Parquet, JSONL

A DataFrame is a table with labelled columns and an index. Most real ML work is 80% reshaping tables: load, clean, group, join, aggregate. Learn `groupby` and `merge` well and you can answer most data questions without writing loops.

```python
import pandas as pd

df = pd.DataFrame({
    'city': ['pune', 'pune', 'delhi', 'delhi'],
    'sales': [10, 20, 5, 7],
})
print(df.groupby('city')['sales'].sum())

lookup = pd.DataFrame({'city': ['pune', 'delhi'], 'zone': ['west', 'north']})
print(df.merge(lookup, on='city', how='left'))
```

**Remember:** Always check `df.shape` before and after a merge — a silent row explosion means duplicate keys.

**Common mistake:** Chained assignment (`df[df.a > 1]['b'] = 0`) that writes to a copy and changes nothing.

Practice: open `examples/05_file_formats_csv_parquet_jsonl.py`, predict the output, change one line, predict again.

## 6. Parquet and columnar storage

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

Practice: open `examples/06_parquet_and_columnar_storage.py`, predict the output, change one line, predict again.

## 7. Data licensing and terms of use

Where data comes from decides what you may do with it. Check the licence before you train, strip or hash personal identifiers early, and record provenance so you can answer 'where did this row come from' a year later. Paginated APIs need backoff and idempotent resume.

```python
import hashlib, time

def pseudonymise(email, salt='project-salt'):
    return hashlib.sha256((salt + email.lower()).encode()).hexdigest()[:16]

print(pseudonymise('User@Example.com'))

def fetch_pages(fetch, max_pages=5):
    """fetch(page) -> (rows, has_more). Backs off on failure."""
    out, page, delay = [], 1, 1.0
    while page <= max_pages:
        rows, has_more = fetch(page)
        out.extend(rows)
        if not has_more:
            break
        page += 1
    return out

print(fetch_pages(lambda p: ([f'row{p}'], p < 3)))
```

**Remember:** Hash or drop identifiers at ingestion, not at report time — by then copies already exist.

**Common mistake:** Scraping a source whose terms forbid it and discovering the problem after the model is in production.

Practice: open `examples/07_data_licensing_and_terms_of_use.py`, predict the output, change one line, predict again.

## 8. Personally identifiable information

Where data comes from decides what you may do with it. Check the licence before you train, strip or hash personal identifiers early, and record provenance so you can answer 'where did this row come from' a year later. Paginated APIs need backoff and idempotent resume.

```python
import hashlib, time

def pseudonymise(email, salt='project-salt'):
    return hashlib.sha256((salt + email.lower()).encode()).hexdigest()[:16]

print(pseudonymise('User@Example.com'))

def fetch_pages(fetch, max_pages=5):
    """fetch(page) -> (rows, has_more). Backs off on failure."""
    out, page, delay = [], 1, 1.0
    while page <= max_pages:
        rows, has_more = fetch(page)
        out.extend(rows)
        if not has_more:
            break
        page += 1
    return out

print(fetch_pages(lambda p: ([f'row{p}'], p < 3)))
```

**Remember:** Hash or drop identifiers at ingestion, not at report time — by then copies already exist.

**Common mistake:** Scraping a source whose terms forbid it and discovering the problem after the model is in production.

Practice: open `examples/08_personally_identifiable_information.py`, predict the output, change one line, predict again.

## 9. Sampling a large source safely

A distribution says which values are likely. Gaussian for measurement noise, Bernoulli for yes/no, Poisson for counts per interval. Choosing the right one is choosing your loss function: Gaussian likelihood gives MSE, Bernoulli gives cross-entropy.

```python
import numpy as np

rng = np.random.default_rng(0)
normal = rng.normal(loc=0, scale=1, size=10_000)
coin = rng.binomial(n=1, p=0.3, size=10_000)

print('normal mean/std', round(normal.mean(), 3), round(normal.std(), 3))
print('coin heads rate ', coin.mean())
```

**Remember:** Always seed your RNG (`default_rng(0)`) when you want a result someone else can reproduce.

**Common mistake:** Assuming Gaussian for skewed, bounded, or count data and then being surprised by the residuals.

Practice: open `examples/09_sampling_a_large_source_safely.py`, predict the output, change one line, predict again.

## 10. Documenting data provenance

Missing data is information, not just noise. Before filling anything, ask *why* it is missing: a sensor that fails only under load is not missing at random. Then choose: drop rows, drop the column, fill with a statistic, or add an explicit 'was missing' indicator column.

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'age': [25, np.nan, 40, np.nan]})
print(df.isna().sum())

df['age_missing'] = df['age'].isna().astype(int)   # keep the signal
df['age'] = df['age'].fillna(df['age'].median())    # then fill
print(df)
```

**Remember:** Compute the fill statistic on the TRAIN split only, then apply it to test.

**Common mistake:** Filling with the mean computed over the full dataset — that leaks test information into training.

Practice: open `examples/10_documenting_data_provenance.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 36

- Explain **Public dataset sources** to someone else without notes.
- Explain **APIs and pagination** to someone else without notes.
- Explain **Web scraping ethics and robots.txt** to someone else without notes.
- Explain **Database extracts** to someone else without notes.
- Explain **File formats: CSV, Parquet, JSONL** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
