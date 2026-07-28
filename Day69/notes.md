# Day 69 — Working with text, classically

Today's goal: work through **Working with text, classically** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Text preprocessing pipeline |
| 2 | Tokenisation basics |
| 3 | Stopwords, stemming, lemmatisation |
| 4 | Bag of words |
| 5 | TF-IDF |
| 6 | N-grams |
| 7 | Character n-grams for noisy text |
| 8 | Text classification with linear models |
| 9 | Topic modelling with LDA |
| 10 | The baseline every LLM must beat |

---

## 1. Text preprocessing pipeline

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

## 2. Tokenisation basics

Models see token IDs, not text. Byte-pair encoding merges frequent character pairs so common words are one token and rare words split into pieces. Tokens are why you are billed per token, why context limits are in tokens, and why models are bad at counting letters.

```python
from collections import Counter

def bpe_merges(words, n_merges=3):
    corpus = {' '.join(w) + ' </w>': c for w, c in words.items()}
    for _ in range(n_merges):
        pairs = Counter()
        for word, freq in corpus.items():
            syms = word.split()
            for a, b in zip(syms, syms[1:]):
                pairs[(a, b)] += freq
        if not pairs:
            break
        best = max(pairs, key=pairs.get)
        merged = ''.join(best)
        corpus = {w.replace(' '.join(best), merged): c for w, c in corpus.items()}
        print('merged', best, '->', merged)
    return corpus

bpe_merges({'low': 5, 'lower': 2, 'newest': 6, 'widest': 3})
```

**Remember:** Roughly 1 token ~ 4 characters of English; other languages cost far more tokens per word.

**Common mistake:** Estimating cost or context usage in words instead of tokens and overflowing the window in production.

## 3. Stopwords, stemming, lemmatisation

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

## 4. Bag of words

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

## 5. TF-IDF

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

## 6. N-grams

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

## 7. Character n-grams for noisy text

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

## 8. Text classification with linear models

Today's idea — **Text classification with linear models** — sits inside the theme of Working with text, classically. Read it as a tool, not trivia: what job does it do, what does it assume about your data, and what breaks when that assumption is false?

```python
# Explore: Text classification with linear models
print("practice: Text classification with linear models")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Remember:** State one assumption `Text classification with linear models` makes about your data before you use it.

**Common mistake:** Copy-pasting `Text classification with linear models` from a tutorial without knowing what it assumes or when it fails.

## 9. Topic modelling with LDA

Today's idea — **Topic modelling with LDA** — sits inside the theme of Working with text, classically. Read it as a tool, not trivia: what job does it do, what does it assume about your data, and what breaks when that assumption is false?

```python
# Explore: Topic modelling with LDA
print("practice: Topic modelling with LDA")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Remember:** State one assumption `Topic modelling with LDA` makes about your data before you use it.

**Common mistake:** Copy-pasting `Topic modelling with LDA` from a tutorial without knowing what it assumes or when it fails.

## 10. The baseline every LLM must beat

Today's idea — **The baseline every LLM must beat** — sits inside the theme of Working with text, classically. Read it as a tool, not trivia: what job does it do, what does it assume about your data, and what breaks when that assumption is false?

```python
# Explore: The baseline every LLM must beat
print("practice: The baseline every LLM must beat")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Remember:** State one assumption `The baseline every LLM must beat` makes about your data before you use it.

**Common mistake:** Copy-pasting `The baseline every LLM must beat` from a tutorial without knowing what it assumes or when it fails.

---

## What you should be able to do after Day 69

- Explain **Text preprocessing pipeline** to someone else without notes.
- Explain **Tokenisation basics** to someone else without notes.
- Explain **Stopwords, stemming, lemmatisation** to someone else without notes.
- Explain **Bag of words** to someone else without notes.
- Explain **TF-IDF** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
