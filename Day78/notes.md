# Day 78 — Loss functions

Today's goal: work through **Loss functions** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Loss as the objective you actually optimise |
| 2 | Mean squared error |
| 3 | Mean absolute error and Huber |
| 4 | Binary cross-entropy |
| 5 | Categorical cross-entropy |
| 6 | Logits vs probabilities in loss functions |
| 7 | Class weights inside the loss |
| 8 | Label smoothing |
| 9 | Contrastive and triplet loss |
| 10 | Custom losses for business costs |

---

## 1. Loss as the objective you actually optimise

The loss is the only thing the model actually optimises — everything else is decoration. Pass logits (not probabilities) to cross-entropy implementations that expect them. If a false negative costs ten times a false positive, encode that in the loss or the threshold, not in a slide.

```python
import numpy as np

def weighted_bce(y, p, w_pos=10.0, eps=1e-12):
    p = np.clip(p, eps, 1 - eps)
    return float(-np.mean(w_pos * y * np.log(p) + (1 - y) * np.log(1 - p)))

y = np.array([1.0, 0.0, 0.0, 1.0])
misses_positive = np.array([0.2, 0.1, 0.1, 0.3])
misses_negative = np.array([0.9, 0.8, 0.7, 0.9])
print('missing positives costs', round(weighted_bce(y, misses_positive), 3))
print('false alarms cost      ', round(weighted_bce(y, misses_negative), 3))
```

**Remember:** Encode the real cost of each error type in the loss or the threshold — the model cannot guess it.

**Common mistake:** Optimising plain accuracy for a fraud model where a miss costs 10,000x a false alarm.

## 2. Mean squared error

The mean is pulled around by outliers; the median is not. Report both, plus a spread measure. When mean and median disagree sharply, the distribution is skewed and averages are lying to you.

```python
import numpy as np

salaries = np.array([30, 32, 35, 33, 31, 900])   # one founder
print('mean  ', salaries.mean())     # 176.8 — misleading
print('median', np.median(salaries)) # 32.5  — honest
print('p95   ', np.percentile(salaries, 95))

q1, q3 = np.percentile(salaries, [25, 75])
iqr = q3 - q1
print('outliers', salaries[(salaries < q1 - 1.5 * iqr) | (salaries > q3 + 1.5 * iqr)])
```

**Remember:** Quote median + IQR for skewed data, mean + std only for roughly symmetric data.

**Common mistake:** Removing 'outliers' automatically when they are the exact events you were hired to predict.

## 3. Mean absolute error and Huber

The mean is pulled around by outliers; the median is not. Report both, plus a spread measure. When mean and median disagree sharply, the distribution is skewed and averages are lying to you.

```python
import numpy as np

salaries = np.array([30, 32, 35, 33, 31, 900])   # one founder
print('mean  ', salaries.mean())     # 176.8 — misleading
print('median', np.median(salaries)) # 32.5  — honest
print('p95   ', np.percentile(salaries, 95))

q1, q3 = np.percentile(salaries, [25, 75])
iqr = q3 - q1
print('outliers', salaries[(salaries < q1 - 1.5 * iqr) | (salaries > q3 + 1.5 * iqr)])
```

**Remember:** Quote median + IQR for skewed data, mean + std only for roughly symmetric data.

**Common mistake:** Removing 'outliers' automatically when they are the exact events you were hired to predict.

## 4. Binary cross-entropy

Entropy measures surprise: a fair coin has 1 bit, a two-headed coin has 0. Cross-entropy measures how surprised your model is by the truth — which is why it is the loss for classifiers and language models. Perplexity is just exp(cross-entropy), read as 'effective number of choices'.

```python
import numpy as np

def cross_entropy(p_true, p_pred, eps=1e-12):
    p_pred = np.clip(p_pred, eps, 1 - eps)
    return -np.sum(p_true * np.log(p_pred))

truth = np.array([0, 1, 0])              # class 1 is correct
confident = np.array([0.05, 0.90, 0.05])
unsure = np.array([0.33, 0.34, 0.33])
print('confident loss', round(cross_entropy(truth, confident), 3))
print('unsure loss   ', round(cross_entropy(truth, unsure), 3))
print('perplexity    ', round(float(np.exp(cross_entropy(truth, unsure))), 3))
```

**Remember:** Clip probabilities before `log` — `log(0)` is `-inf` and poisons the whole batch.

**Common mistake:** Applying softmax twice (once in the model, once in the loss) and getting flat, untrainable gradients.

## 5. Categorical cross-entropy

Entropy measures surprise: a fair coin has 1 bit, a two-headed coin has 0. Cross-entropy measures how surprised your model is by the truth — which is why it is the loss for classifiers and language models. Perplexity is just exp(cross-entropy), read as 'effective number of choices'.

```python
import numpy as np

def cross_entropy(p_true, p_pred, eps=1e-12):
    p_pred = np.clip(p_pred, eps, 1 - eps)
    return -np.sum(p_true * np.log(p_pred))

truth = np.array([0, 1, 0])              # class 1 is correct
confident = np.array([0.05, 0.90, 0.05])
unsure = np.array([0.33, 0.34, 0.33])
print('confident loss', round(cross_entropy(truth, confident), 3))
print('unsure loss   ', round(cross_entropy(truth, unsure), 3))
print('perplexity    ', round(float(np.exp(cross_entropy(truth, unsure))), 3))
```

**Remember:** Clip probabilities before `log` — `log(0)` is `-inf` and poisons the whole batch.

**Common mistake:** Applying softmax twice (once in the model, once in the loss) and getting flat, untrainable gradients.

## 6. Logits vs probabilities in loss functions

The loss is the only thing the model actually optimises — everything else is decoration. Pass logits (not probabilities) to cross-entropy implementations that expect them. If a false negative costs ten times a false positive, encode that in the loss or the threshold, not in a slide.

```python
import numpy as np

def weighted_bce(y, p, w_pos=10.0, eps=1e-12):
    p = np.clip(p, eps, 1 - eps)
    return float(-np.mean(w_pos * y * np.log(p) + (1 - y) * np.log(1 - p)))

y = np.array([1.0, 0.0, 0.0, 1.0])
misses_positive = np.array([0.2, 0.1, 0.1, 0.3])
misses_negative = np.array([0.9, 0.8, 0.7, 0.9])
print('missing positives costs', round(weighted_bce(y, misses_positive), 3))
print('false alarms cost      ', round(weighted_bce(y, misses_negative), 3))
```

**Remember:** Encode the real cost of each error type in the loss or the threshold — the model cannot guess it.

**Common mistake:** Optimising plain accuracy for a fraud model where a miss costs 10,000x a false alarm.

## 7. Class weights inside the loss

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

## 8. Label smoothing

The loss is the only thing the model actually optimises — everything else is decoration. Pass logits (not probabilities) to cross-entropy implementations that expect them. If a false negative costs ten times a false positive, encode that in the loss or the threshold, not in a slide.

```python
import numpy as np

def weighted_bce(y, p, w_pos=10.0, eps=1e-12):
    p = np.clip(p, eps, 1 - eps)
    return float(-np.mean(w_pos * y * np.log(p) + (1 - y) * np.log(1 - p)))

y = np.array([1.0, 0.0, 0.0, 1.0])
misses_positive = np.array([0.2, 0.1, 0.1, 0.3])
misses_negative = np.array([0.9, 0.8, 0.7, 0.9])
print('missing positives costs', round(weighted_bce(y, misses_positive), 3))
print('false alarms cost      ', round(weighted_bce(y, misses_negative), 3))
```

**Remember:** Encode the real cost of each error type in the loss or the threshold — the model cannot guess it.

**Common mistake:** Optimising plain accuracy for a fraud model where a miss costs 10,000x a false alarm.

## 9. Contrastive and triplet loss

The loss is the only thing the model actually optimises — everything else is decoration. Pass logits (not probabilities) to cross-entropy implementations that expect them. If a false negative costs ten times a false positive, encode that in the loss or the threshold, not in a slide.

```python
import numpy as np

def weighted_bce(y, p, w_pos=10.0, eps=1e-12):
    p = np.clip(p, eps, 1 - eps)
    return float(-np.mean(w_pos * y * np.log(p) + (1 - y) * np.log(1 - p)))

y = np.array([1.0, 0.0, 0.0, 1.0])
misses_positive = np.array([0.2, 0.1, 0.1, 0.3])
misses_negative = np.array([0.9, 0.8, 0.7, 0.9])
print('missing positives costs', round(weighted_bce(y, misses_positive), 3))
print('false alarms cost      ', round(weighted_bce(y, misses_negative), 3))
```

**Remember:** Encode the real cost of each error type in the loss or the threshold — the model cannot guess it.

**Common mistake:** Optimising plain accuracy for a fraud model where a miss costs 10,000x a false alarm.

## 10. Custom losses for business costs

The loss is the only thing the model actually optimises — everything else is decoration. Pass logits (not probabilities) to cross-entropy implementations that expect them. If a false negative costs ten times a false positive, encode that in the loss or the threshold, not in a slide.

```python
import numpy as np

def weighted_bce(y, p, w_pos=10.0, eps=1e-12):
    p = np.clip(p, eps, 1 - eps)
    return float(-np.mean(w_pos * y * np.log(p) + (1 - y) * np.log(1 - p)))

y = np.array([1.0, 0.0, 0.0, 1.0])
misses_positive = np.array([0.2, 0.1, 0.1, 0.3])
misses_negative = np.array([0.9, 0.8, 0.7, 0.9])
print('missing positives costs', round(weighted_bce(y, misses_positive), 3))
print('false alarms cost      ', round(weighted_bce(y, misses_negative), 3))
```

**Remember:** Encode the real cost of each error type in the loss or the threshold — the model cannot guess it.

**Common mistake:** Optimising plain accuracy for a fraud model where a miss costs 10,000x a false alarm.

---

## What you should be able to do after Day 78

- Explain **Loss as the objective you actually optimise** to someone else without notes.
- Explain **Mean squared error** to someone else without notes.
- Explain **Mean absolute error and Huber** to someone else without notes.
- Explain **Binary cross-entropy** to someone else without notes.
- Explain **Categorical cross-entropy** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
