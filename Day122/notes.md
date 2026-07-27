# Day 122 — Classical NLP baselines

Today's goal: work through **classical nlp baselines** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Bag of words revisited |
| 2 | TF-IDF for classification |
| 3 | N-gram language models |
| 4 | Naive Bayes for text |
| 5 | Linear SVM for text |
| 6 | Named entity recognition, classically |
| 7 | Rule-based systems that still work |
| 8 | Keyword search and BM25 |
| 9 | Measuring the baseline properly |
| 10 | Deciding whether you need an LLM at all |

---

## 1. Bag of words revisited

Before embeddings, text became numbers by counting. TF-IDF weights a word by how often it appears here and how rare it is overall, so 'the' scores near zero. It is still an excellent, near-free baseline for classification and keyword search.

```python
from sklearn.feature_extraction.text import TfidfVectorizer

docs = [
    'the cat sat on the mat',
    'the dog sat on the log',
    'machine learning models learn patterns',
]
vec = TfidfVectorizer(stop_words='english')
X = vec.fit_transform(docs)
print(vec.get_feature_names_out())
print(X.toarray().round(2))
```

**Remember:** TF-IDF + logistic regression is the baseline every LLM text classifier must beat to be worth its cost.

**Common mistake:** Reaching for a 7B model to classify support tickets that TF-IDF handles at 94% for free.

## 2. TF-IDF for classification

Before embeddings, text became numbers by counting. TF-IDF weights a word by how often it appears here and how rare it is overall, so 'the' scores near zero. It is still an excellent, near-free baseline for classification and keyword search.

```python
from sklearn.feature_extraction.text import TfidfVectorizer

docs = [
    'the cat sat on the mat',
    'the dog sat on the log',
    'machine learning models learn patterns',
]
vec = TfidfVectorizer(stop_words='english')
X = vec.fit_transform(docs)
print(vec.get_feature_names_out())
print(X.toarray().round(2))
```

**Remember:** TF-IDF + logistic regression is the baseline every LLM text classifier must beat to be worth its cost.

**Common mistake:** Reaching for a 7B model to classify support tickets that TF-IDF handles at 94% for free.

## 3. N-gram language models

Before embeddings, text became numbers by counting. TF-IDF weights a word by how often it appears here and how rare it is overall, so 'the' scores near zero. It is still an excellent, near-free baseline for classification and keyword search.

```python
from sklearn.feature_extraction.text import TfidfVectorizer

docs = [
    'the cat sat on the mat',
    'the dog sat on the log',
    'machine learning models learn patterns',
]
vec = TfidfVectorizer(stop_words='english')
X = vec.fit_transform(docs)
print(vec.get_feature_names_out())
print(X.toarray().round(2))
```

**Remember:** TF-IDF + logistic regression is the baseline every LLM text classifier must beat to be worth its cost.

**Common mistake:** Reaching for a 7B model to classify support tickets that TF-IDF handles at 94% for free.

## 4. Naive Bayes for text

Bayes' rule updates a belief with evidence: posterior = likelihood x prior / evidence. The most common mistake in applied ML is ignoring the prior — a 99%-accurate test for a 1-in-10000 disease still gives mostly false positives.

```python
prior = 1 / 10_000          # base rate of the disease
sensitivity = 0.99          # P(positive | sick)
false_positive = 0.01       # P(positive | healthy)

evidence = sensitivity * prior + false_positive * (1 - prior)
posterior = sensitivity * prior / evidence
print(f'P(sick | positive) = {posterior:.4f}')   # ~0.0098
```

**Remember:** Rare events make precision collapse no matter how good the classifier looks on accuracy.

**Common mistake:** Reporting accuracy on an imbalanced problem where predicting 'no' always scores 99%.

## 5. Linear SVM for text

An SVM finds the boundary with the widest margin between classes. The kernel trick lets it draw curved boundaries by computing inner products in a higher-dimensional space without ever building that space. Strong on small, clean, high-dimensional datasets like text.

```python
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons
from sklearn.model_selection import cross_val_score

X, y = make_moons(n_samples=500, noise=0.2, random_state=0)
linear = make_pipeline(StandardScaler(), SVC(kernel='linear'))
rbf = make_pipeline(StandardScaler(), SVC(kernel='rbf', C=1.0, gamma='scale'))
print('linear', cross_val_score(linear, X, y, cv=5).mean().round(3))
print('rbf   ', cross_val_score(rbf, X, y, cv=5).mean().round(3))
```

**Remember:** SVMs scale roughly quadratically with rows — above ~100k samples reach for boosting instead.

**Common mistake:** Skipping feature scaling, which silently wrecks the RBF kernel.

## 6. Named entity recognition, classically

Not everything needs a model. Regex and a gazetteer still beat a fine-tuned model for well-formed IDs, dates and codes — with zero latency and total explainability. BM25 keyword search remains a strong retrieval baseline and is what hybrid search combines with embeddings.

```python
import re
from collections import Counter
import math

text = 'Invoice INV-2024-0031 dated 2024-03-02 for Rs 15,300 to Acme Ltd.'
print('ids  ', re.findall(r'\bINV-\d{4}-\d{4}\b', text))
print('dates', re.findall(r'\b\d{4}-\d{2}-\d{2}\b', text))

docs = ['refund policy takes five days', 'office hours in pune', 'refund of enterprise plans']
query = 'refund'
df = sum(query in d for d in docs)
idf = math.log((len(docs) - df + 0.5) / (df + 0.5) + 1)
for d in docs:
    tf = Counter(d.split())[query]
    print(round(idf * tf / (tf + 1.2), 3), '|', d)
```

**Remember:** Try the regex first. If it hits 95% with no infrastructure, the model has to justify replacing it.

**Common mistake:** Fine-tuning a transformer to extract dates that `dateutil` already parses correctly.

## 7. Rule-based systems that still work

Not everything needs a model. Regex and a gazetteer still beat a fine-tuned model for well-formed IDs, dates and codes — with zero latency and total explainability. BM25 keyword search remains a strong retrieval baseline and is what hybrid search combines with embeddings.

```python
import re
from collections import Counter
import math

text = 'Invoice INV-2024-0031 dated 2024-03-02 for Rs 15,300 to Acme Ltd.'
print('ids  ', re.findall(r'\bINV-\d{4}-\d{4}\b', text))
print('dates', re.findall(r'\b\d{4}-\d{2}-\d{2}\b', text))

docs = ['refund policy takes five days', 'office hours in pune', 'refund of enterprise plans']
query = 'refund'
df = sum(query in d for d in docs)
idf = math.log((len(docs) - df + 0.5) / (df + 0.5) + 1)
for d in docs:
    tf = Counter(d.split())[query]
    print(round(idf * tf / (tf + 1.2), 3), '|', d)
```

**Remember:** Try the regex first. If it hits 95% with no infrastructure, the model has to justify replacing it.

**Common mistake:** Fine-tuning a transformer to extract dates that `dateutil` already parses correctly.

## 8. Keyword search and BM25

Not everything needs a model. Regex and a gazetteer still beat a fine-tuned model for well-formed IDs, dates and codes — with zero latency and total explainability. BM25 keyword search remains a strong retrieval baseline and is what hybrid search combines with embeddings.

```python
import re
from collections import Counter
import math

text = 'Invoice INV-2024-0031 dated 2024-03-02 for Rs 15,300 to Acme Ltd.'
print('ids  ', re.findall(r'\bINV-\d{4}-\d{4}\b', text))
print('dates', re.findall(r'\b\d{4}-\d{2}-\d{2}\b', text))

docs = ['refund policy takes five days', 'office hours in pune', 'refund of enterprise plans']
query = 'refund'
df = sum(query in d for d in docs)
idf = math.log((len(docs) - df + 0.5) / (df + 0.5) + 1)
for d in docs:
    tf = Counter(d.split())[query]
    print(round(idf * tf / (tf + 1.2), 3), '|', d)
```

**Remember:** Try the regex first. If it hits 95% with no infrastructure, the model has to justify replacing it.

**Common mistake:** Fine-tuning a transformer to extract dates that `dateutil` already parses correctly.

## 9. Measuring the baseline properly

Not everything needs a model. Regex and a gazetteer still beat a fine-tuned model for well-formed IDs, dates and codes — with zero latency and total explainability. BM25 keyword search remains a strong retrieval baseline and is what hybrid search combines with embeddings.

```python
import re
from collections import Counter
import math

text = 'Invoice INV-2024-0031 dated 2024-03-02 for Rs 15,300 to Acme Ltd.'
print('ids  ', re.findall(r'\bINV-\d{4}-\d{4}\b', text))
print('dates', re.findall(r'\b\d{4}-\d{2}-\d{2}\b', text))

docs = ['refund policy takes five days', 'office hours in pune', 'refund of enterprise plans']
query = 'refund'
df = sum(query in d for d in docs)
idf = math.log((len(docs) - df + 0.5) / (df + 0.5) + 1)
for d in docs:
    tf = Counter(d.split())[query]
    print(round(idf * tf / (tf + 1.2), 3), '|', d)
```

**Remember:** Try the regex first. If it hits 95% with no infrastructure, the model has to justify replacing it.

**Common mistake:** Fine-tuning a transformer to extract dates that `dateutil` already parses correctly.

## 10. Deciding whether you need an LLM at all

ML code needs the same tests as any code, plus data tests: schema, ranges, null rates, class balance. Add one behavioural test per known failure mode — a test that would have caught last quarter's outage is worth more than 90% coverage.

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

**Remember:** Test the data contract, not just the function — bad data breaks more models than bad code.

**Common mistake:** Testing only the happy path, so an all-null column silently trains a constant model.

---

## What you should be able to do after Day 122

- Explain **Bag of words revisited** to someone else without notes.
- Explain **TF-IDF for classification** to someone else without notes.
- Explain **N-gram language models** to someone else without notes.
- Explain **Naive Bayes for text** to someone else without notes.
- Explain **Linear SVM for text** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
