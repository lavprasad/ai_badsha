# Day 36 — Getting data

Aaj ka goal: **Getting data** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

### Aasaan Bhasha

Data kahan se aaya ye tay karta hai ki aap uske saath kya kar sakte ho. Train karne se pehle licence check karo, personal identifiers shuru me hi hata ya hash kar do, aur provenance record karo taaki saal bhar baad 'ye row kahan se aayi' ka jawab de sako. Paginated APIs ko backoff aur idempotent resume chahiye.

### Chhota code

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

**Yaad rakho:** Identifiers ingestion par hash ya drop karo, report ke waqt nahi — tab tak copies ban chuki hoti hain.

**Aam galti:** Aise source ko scrape karna jiske terms mana karte hain, aur problem model production me jaane ke baad pata chalna.

Practice: `examples/01_public_dataset_sources.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. APIs and pagination

### Aasaan Bhasha

Data kahan se aaya ye tay karta hai ki aap uske saath kya kar sakte ho. Train karne se pehle licence check karo, personal identifiers shuru me hi hata ya hash kar do, aur provenance record karo taaki saal bhar baad 'ye row kahan se aayi' ka jawab de sako. Paginated APIs ko backoff aur idempotent resume chahiye.

### Chhota code

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

**Yaad rakho:** Identifiers ingestion par hash ya drop karo, report ke waqt nahi — tab tak copies ban chuki hoti hain.

**Aam galti:** Aise source ko scrape karna jiske terms mana karte hain, aur problem model production me jaane ke baad pata chalna.

Practice: `examples/02_apis_and_pagination.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Web scraping ethics and robots.txt

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

Practice: `examples/03_web_scraping_ethics_and_robots_txt.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Database extracts

### Aasaan Bhasha

Data kahan se aaya ye tay karta hai ki aap uske saath kya kar sakte ho. Train karne se pehle licence check karo, personal identifiers shuru me hi hata ya hash kar do, aur provenance record karo taaki saal bhar baad 'ye row kahan se aayi' ka jawab de sako. Paginated APIs ko backoff aur idempotent resume chahiye.

### Chhota code

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

**Yaad rakho:** Identifiers ingestion par hash ya drop karo, report ke waqt nahi — tab tak copies ban chuki hoti hain.

**Aam galti:** Aise source ko scrape karna jiske terms mana karte hain, aur problem model production me jaane ke baad pata chalna.

Practice: `examples/04_database_extracts.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. File formats: CSV, Parquet, JSONL

### Aasaan Bhasha

DataFrame ek table hai jisme labelled columns aur ek index hota hai. Asli ML ka 80% kaam tables ko reshape karna hi hai: load, clean, group, join, aggregate. `groupby` aur `merge` acche se seekh lo to zyadatar data sawaal bina loop likhe hal ho jaate hain.

### Chhota code

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

**Yaad rakho:** Merge se pehle aur baad me `df.shape` zaroor check karo — chupke se rows badhna matlab duplicate keys.

**Aam galti:** Chained assignment (`df[df.a > 1]['b'] = 0`) jo copy par likhta hai aur kuch nahi badalta.

Practice: `examples/05_file_formats_csv_parquet_jsonl.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Parquet and columnar storage

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

Practice: `examples/06_parquet_and_columnar_storage.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Data licensing and terms of use

### Aasaan Bhasha

Data kahan se aaya ye tay karta hai ki aap uske saath kya kar sakte ho. Train karne se pehle licence check karo, personal identifiers shuru me hi hata ya hash kar do, aur provenance record karo taaki saal bhar baad 'ye row kahan se aayi' ka jawab de sako. Paginated APIs ko backoff aur idempotent resume chahiye.

### Chhota code

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

**Yaad rakho:** Identifiers ingestion par hash ya drop karo, report ke waqt nahi — tab tak copies ban chuki hoti hain.

**Aam galti:** Aise source ko scrape karna jiske terms mana karte hain, aur problem model production me jaane ke baad pata chalna.

Practice: `examples/07_data_licensing_and_terms_of_use.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Personally identifiable information

### Aasaan Bhasha

Data kahan se aaya ye tay karta hai ki aap uske saath kya kar sakte ho. Train karne se pehle licence check karo, personal identifiers shuru me hi hata ya hash kar do, aur provenance record karo taaki saal bhar baad 'ye row kahan se aayi' ka jawab de sako. Paginated APIs ko backoff aur idempotent resume chahiye.

### Chhota code

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

**Yaad rakho:** Identifiers ingestion par hash ya drop karo, report ke waqt nahi — tab tak copies ban chuki hoti hain.

**Aam galti:** Aise source ko scrape karna jiske terms mana karte hain, aur problem model production me jaane ke baad pata chalna.

Practice: `examples/08_personally_identifiable_information.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Sampling a large source safely

### Aasaan Bhasha

Distribution batati hai kaunsi values likely hain. Measurement noise ke liye Gaussian, haan/na ke liye Bernoulli, per-interval counts ke liye Poisson. Sahi distribution chunna hi apna loss function chunna hai: Gaussian likelihood se MSE aata hai, Bernoulli se cross-entropy.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
normal = rng.normal(loc=0, scale=1, size=10_000)
coin = rng.binomial(n=1, p=0.3, size=10_000)

print('normal mean/std', round(normal.mean(), 3), round(normal.std(), 3))
print('coin heads rate ', coin.mean())
```

**Yaad rakho:** Jab result dobara banana ho to RNG hamesha seed karo (`default_rng(0)`).

**Aam galti:** Skewed, bounded ya count data par Gaussian maan lena aur phir residuals dekh kar hairan hona.

Practice: `examples/09_sampling_a_large_source_safely.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Documenting data provenance

### Aasaan Bhasha

Missing data information hai, sirf noise nahi. Kuch bharne se pehle poochho ki **kyun** missing hai: jo sensor sirf load par fail hota hai wo randomly missing nahi hai. Phir chuno: rows drop, column drop, statistic se fill, ya ek explicit 'ye missing tha' indicator column.

### Chhota code

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'age': [25, np.nan, 40, np.nan]})
print(df.isna().sum())

df['age_missing'] = df['age'].isna().astype(int)   # keep the signal
df['age'] = df['age'].fillna(df['age'].median())    # then fill
print(df)
```

**Yaad rakho:** Fill karne wali statistic sirf TRAIN split par nikalo, phir test par lagao.

**Aam galti:** Poore dataset ke mean se fill karna — ye test ki information training me leak kar deta hai.

Practice: `examples/10_documenting_data_provenance.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 36 ke baad aapko ye aana chahiye

- **Public dataset sources** ko bina notes dekhe kisi dost ko samjha sakna.
- **APIs and pagination** ko bina notes dekhe kisi dost ko samjha sakna.
- **Web scraping ethics and robots.txt** ko bina notes dekhe kisi dost ko samjha sakna.
- **Database extracts** ko bina notes dekhe kisi dost ko samjha sakna.
- **File formats: CSV, Parquet, JSONL** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
