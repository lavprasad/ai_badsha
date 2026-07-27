# Day 45 — Your first model, end to end

Today's goal: work through **your first model, end to end** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | The scikit-learn estimator API |
| 2 | fit, predict, score |
| 3 | Loading a built-in dataset |
| 4 | Splitting the data |
| 5 | Training a logistic regression |
| 6 | Reading the accuracy honestly |
| 7 | Comparing against a dummy baseline |
| 8 | Inspecting the coefficients |
| 9 | Saving and reloading the model |
| 10 | The seven-line template you will reuse forever |

---

## 1. The scikit-learn estimator API

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

## 2. fit, predict, score

Every scikit-learn model has the same three methods, which means swapping algorithms is a one-line change. Start every problem with `DummyClassifier` — if your real model cannot beat 'always predict the majority class' by a clear margin, something is wrong with the data, not the model.

```python
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, stratify=y, random_state=0)

baseline = DummyClassifier(strategy='most_frequent').fit(Xtr, ytr)
model = RandomForestClassifier(n_estimators=200, random_state=0).fit(Xtr, ytr)
print(f'dummy {baseline.score(Xte, yte):.3f}   model {model.score(Xte, yte):.3f}')
```

**Remember:** Report your model's score next to the dummy's. A number alone means nothing.

**Common mistake:** Celebrating 92% accuracy on data where 91% of rows are one class.

## 3. Loading a built-in dataset

Every scikit-learn model has the same three methods, which means swapping algorithms is a one-line change. Start every problem with `DummyClassifier` — if your real model cannot beat 'always predict the majority class' by a clear margin, something is wrong with the data, not the model.

```python
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, stratify=y, random_state=0)

baseline = DummyClassifier(strategy='most_frequent').fit(Xtr, ytr)
model = RandomForestClassifier(n_estimators=200, random_state=0).fit(Xtr, ytr)
print(f'dummy {baseline.score(Xte, yte):.3f}   model {model.score(Xte, yte):.3f}')
```

**Remember:** Report your model's score next to the dummy's. A number alone means nothing.

**Common mistake:** Celebrating 92% accuracy on data where 91% of rows are one class.

## 4. Splitting the data

Today's idea — **Splitting the data** — sits inside the theme of Your first model, end to end. Read it as a tool, not trivia: what job does it do, what does it assume about your data, and what breaks when that assumption is false?

```python
# Explore: Splitting the data
print("practice: Splitting the data")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Remember:** State one assumption `Splitting the data` makes about your data before you use it.

**Common mistake:** Copy-pasting `Splitting the data` from a tutorial without knowing what it assumes or when it fails.

## 5. Training a logistic regression

Logistic regression squashes a linear score through a sigmoid to get a probability. The coefficients are log-odds: +0.7 means the odds roughly double per unit. It stays the default for anything where you must explain the decision to a regulator.

```python
import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-np.clip(z, -500, 500)))

rng = np.random.default_rng(0)
X = rng.normal(size=(400, 2))
y = (X[:, 0] + X[:, 1] > 0).astype(float)

w, b, lr = np.zeros(2), 0.0, 0.5
for _ in range(500):
    p = sigmoid(X @ w + b)
    w -= lr * (X.T @ (p - y)) / len(y)
    b -= lr * float((p - y).mean())
print('weights', np.round(w, 2), 'acc', ((sigmoid(X @ w + b) > 0.5) == y).mean())
```

**Remember:** Clip the sigmoid input — `exp` of a large negative number overflows and returns NaN.

**Common mistake:** Reading the raw output as a calibrated probability without ever checking a calibration curve.

## 6. Reading the accuracy honestly

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

## 7. Comparing against a dummy baseline

Every scikit-learn model has the same three methods, which means swapping algorithms is a one-line change. Start every problem with `DummyClassifier` — if your real model cannot beat 'always predict the majority class' by a clear margin, something is wrong with the data, not the model.

```python
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, stratify=y, random_state=0)

baseline = DummyClassifier(strategy='most_frequent').fit(Xtr, ytr)
model = RandomForestClassifier(n_estimators=200, random_state=0).fit(Xtr, ytr)
print(f'dummy {baseline.score(Xte, yte):.3f}   model {model.score(Xte, yte):.3f}')
```

**Remember:** Report your model's score next to the dummy's. A number alone means nothing.

**Common mistake:** Celebrating 92% accuracy on data where 91% of rows are one class.

## 8. Inspecting the coefficients

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

## 9. Saving and reloading the model

Today's idea — **Saving and reloading the model** — sits inside the theme of Your first model, end to end. Read it as a tool, not trivia: what job does it do, what does it assume about your data, and what breaks when that assumption is false?

```python
# Explore: Saving and reloading the model
print("practice: Saving and reloading the model")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Remember:** State one assumption `Saving and reloading the model` makes about your data before you use it.

**Common mistake:** Copy-pasting `Saving and reloading the model` from a tutorial without knowing what it assumes or when it fails.

## 10. The seven-line template you will reuse forever

Every scikit-learn model has the same three methods, which means swapping algorithms is a one-line change. Start every problem with `DummyClassifier` — if your real model cannot beat 'always predict the majority class' by a clear margin, something is wrong with the data, not the model.

```python
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, stratify=y, random_state=0)

baseline = DummyClassifier(strategy='most_frequent').fit(Xtr, ytr)
model = RandomForestClassifier(n_estimators=200, random_state=0).fit(Xtr, ytr)
print(f'dummy {baseline.score(Xte, yte):.3f}   model {model.score(Xte, yte):.3f}')
```

**Remember:** Report your model's score next to the dummy's. A number alone means nothing.

**Common mistake:** Celebrating 92% accuracy on data where 91% of rows are one class.

---

## What you should be able to do after Day 45

- Explain **The scikit-learn estimator API** to someone else without notes.
- Explain **fit, predict, score** to someone else without notes.
- Explain **Loading a built-in dataset** to someone else without notes.
- Explain **Splitting the data** to someone else without notes.
- Explain **Training a logistic regression** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
