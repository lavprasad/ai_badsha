# Day 58 — Handling imbalanced data

Today's goal: work through **Handling imbalanced data** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Why accuracy lies here |
| 2 | Class weights |
| 3 | Threshold moving |
| 4 | Random over- and under-sampling |
| 5 | SMOTE and synthetic minority points |
| 6 | Where resampling must happen in the pipeline |
| 7 | Anomaly detection framing instead |
| 8 | Cost-sensitive learning |
| 9 | Choosing PR-AUC over ROC-AUC |
| 10 | A fraud detection walkthrough |

---

## 1. Why accuracy lies here

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

## 2. Class weights

When one class is 1% of the data, the model learns to always say 'no'. Fix it with class weights (cheap, first choice), threshold tuning, or resampling. SMOTE synthesises minority points — and must only ever be applied to the training fold.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import recall_score

X, y = make_classification(n_samples=3000, weights=[0.97, 0.03], random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, stratify=y, test_size=0.3, random_state=0)

plain = LogisticRegression(max_iter=1000).fit(Xtr, ytr)
weighted = LogisticRegression(max_iter=1000, class_weight='balanced').fit(Xtr, ytr)
print('recall plain   ', round(recall_score(yte, plain.predict(Xte)), 3))
print('recall balanced', round(recall_score(yte, weighted.predict(Xte)), 3))
```

**Remember:** Try `class_weight='balanced'` before installing anything.

**Common mistake:** Applying SMOTE before the split so synthetic copies of test rows appear in training.

## 3. Threshold moving

When one class is 1% of the data, the model learns to always say 'no'. Fix it with class weights (cheap, first choice), threshold tuning, or resampling. SMOTE synthesises minority points — and must only ever be applied to the training fold.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import recall_score

X, y = make_classification(n_samples=3000, weights=[0.97, 0.03], random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, stratify=y, test_size=0.3, random_state=0)

plain = LogisticRegression(max_iter=1000).fit(Xtr, ytr)
weighted = LogisticRegression(max_iter=1000, class_weight='balanced').fit(Xtr, ytr)
print('recall plain   ', round(recall_score(yte, plain.predict(Xte)), 3))
print('recall balanced', round(recall_score(yte, weighted.predict(Xte)), 3))
```

**Remember:** Try `class_weight='balanced'` before installing anything.

**Common mistake:** Applying SMOTE before the split so synthetic copies of test rows appear in training.

## 4. Random over- and under-sampling

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

## 5. SMOTE and synthetic minority points

When one class is 1% of the data, the model learns to always say 'no'. Fix it with class weights (cheap, first choice), threshold tuning, or resampling. SMOTE synthesises minority points — and must only ever be applied to the training fold.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import recall_score

X, y = make_classification(n_samples=3000, weights=[0.97, 0.03], random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, stratify=y, test_size=0.3, random_state=0)

plain = LogisticRegression(max_iter=1000).fit(Xtr, ytr)
weighted = LogisticRegression(max_iter=1000, class_weight='balanced').fit(Xtr, ytr)
print('recall plain   ', round(recall_score(yte, plain.predict(Xte)), 3))
print('recall balanced', round(recall_score(yte, weighted.predict(Xte)), 3))
```

**Remember:** Try `class_weight='balanced'` before installing anything.

**Common mistake:** Applying SMOTE before the split so synthetic copies of test rows appear in training.

## 6. Where resampling must happen in the pipeline

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

## 7. Anomaly detection framing instead

When one class is 1% of the data, the model learns to always say 'no'. Fix it with class weights (cheap, first choice), threshold tuning, or resampling. SMOTE synthesises minority points — and must only ever be applied to the training fold.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import recall_score

X, y = make_classification(n_samples=3000, weights=[0.97, 0.03], random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, stratify=y, test_size=0.3, random_state=0)

plain = LogisticRegression(max_iter=1000).fit(Xtr, ytr)
weighted = LogisticRegression(max_iter=1000, class_weight='balanced').fit(Xtr, ytr)
print('recall plain   ', round(recall_score(yte, plain.predict(Xte)), 3))
print('recall balanced', round(recall_score(yte, weighted.predict(Xte)), 3))
```

**Remember:** Try `class_weight='balanced'` before installing anything.

**Common mistake:** Applying SMOTE before the split so synthetic copies of test rows appear in training.

## 8. Cost-sensitive learning

When one class is 1% of the data, the model learns to always say 'no'. Fix it with class weights (cheap, first choice), threshold tuning, or resampling. SMOTE synthesises minority points — and must only ever be applied to the training fold.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import recall_score

X, y = make_classification(n_samples=3000, weights=[0.97, 0.03], random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, stratify=y, test_size=0.3, random_state=0)

plain = LogisticRegression(max_iter=1000).fit(Xtr, ytr)
weighted = LogisticRegression(max_iter=1000, class_weight='balanced').fit(Xtr, ytr)
print('recall plain   ', round(recall_score(yte, plain.predict(Xte)), 3))
print('recall balanced', round(recall_score(yte, weighted.predict(Xte)), 3))
```

**Remember:** Try `class_weight='balanced'` before installing anything.

**Common mistake:** Applying SMOTE before the split so synthetic copies of test rows appear in training.

## 9. Choosing PR-AUC over ROC-AUC

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

## 10. A fraud detection walkthrough

When one class is 1% of the data, the model learns to always say 'no'. Fix it with class weights (cheap, first choice), threshold tuning, or resampling. SMOTE synthesises minority points — and must only ever be applied to the training fold.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import recall_score

X, y = make_classification(n_samples=3000, weights=[0.97, 0.03], random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, stratify=y, test_size=0.3, random_state=0)

plain = LogisticRegression(max_iter=1000).fit(Xtr, ytr)
weighted = LogisticRegression(max_iter=1000, class_weight='balanced').fit(Xtr, ytr)
print('recall plain   ', round(recall_score(yte, plain.predict(Xte)), 3))
print('recall balanced', round(recall_score(yte, weighted.predict(Xte)), 3))
```

**Remember:** Try `class_weight='balanced'` before installing anything.

**Common mistake:** Applying SMOTE before the split so synthetic copies of test rows appear in training.

---

## What you should be able to do after Day 58

- Explain **Why accuracy lies here** to someone else without notes.
- Explain **Class weights** to someone else without notes.
- Explain **Threshold moving** to someone else without notes.
- Explain **Random over- and under-sampling** to someone else without notes.
- Explain **SMOTE and synthetic minority points** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
