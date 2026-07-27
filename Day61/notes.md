# Day 61 — Anomaly detection

Today's goal: work through **anomaly detection** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Framing: rare, unlabelled, costly |
| 2 | Statistical thresholds and z-scores |
| 3 | Isolation Forest |
| 4 | One-class SVM |
| 5 | Local Outlier Factor |
| 6 | Reconstruction error methods |
| 7 | Time-series anomaly detection |
| 8 | Evaluating with few or no labels |
| 9 | Alert fatigue and precision |
| 10 | A server-metrics anomaly detector |

---

## 1. Framing: rare, unlabelled, costly

Anomaly detection is classification without labels for the interesting class. Isolation Forest works because anomalies are easier to isolate with random splits. Whatever method you pick, the hard part is the threshold: too sensitive and nobody reads the alerts.

```python
import numpy as np
from sklearn.ensemble import IsolationForest

rng = np.random.default_rng(0)
normal = rng.normal(0, 1, size=(500, 2))
weird = np.array([[6.0, 6.0], [-7.0, 5.0]])
X = np.vstack([normal, weird])

model = IsolationForest(contamination=0.01, random_state=0).fit(X)
scores = model.score_samples(X)
flagged = np.argsort(scores)[:5]
print('most anomalous rows:', flagged)
print('the two planted outliers were rows', len(normal), 'and', len(normal) + 1)
```

**Remember:** Tune the threshold against how many alerts a human can actually review per day.

**Common mistake:** Setting contamination to a guess and drowning the on-call rota in false alarms.

## 2. Statistical thresholds and z-scores

Anomaly detection is classification without labels for the interesting class. Isolation Forest works because anomalies are easier to isolate with random splits. Whatever method you pick, the hard part is the threshold: too sensitive and nobody reads the alerts.

```python
import numpy as np
from sklearn.ensemble import IsolationForest

rng = np.random.default_rng(0)
normal = rng.normal(0, 1, size=(500, 2))
weird = np.array([[6.0, 6.0], [-7.0, 5.0]])
X = np.vstack([normal, weird])

model = IsolationForest(contamination=0.01, random_state=0).fit(X)
scores = model.score_samples(X)
flagged = np.argsort(scores)[:5]
print('most anomalous rows:', flagged)
print('the two planted outliers were rows', len(normal), 'and', len(normal) + 1)
```

**Remember:** Tune the threshold against how many alerts a human can actually review per day.

**Common mistake:** Setting contamination to a guess and drowning the on-call rota in false alarms.

## 3. Isolation Forest

Anomaly detection is classification without labels for the interesting class. Isolation Forest works because anomalies are easier to isolate with random splits. Whatever method you pick, the hard part is the threshold: too sensitive and nobody reads the alerts.

```python
import numpy as np
from sklearn.ensemble import IsolationForest

rng = np.random.default_rng(0)
normal = rng.normal(0, 1, size=(500, 2))
weird = np.array([[6.0, 6.0], [-7.0, 5.0]])
X = np.vstack([normal, weird])

model = IsolationForest(contamination=0.01, random_state=0).fit(X)
scores = model.score_samples(X)
flagged = np.argsort(scores)[:5]
print('most anomalous rows:', flagged)
print('the two planted outliers were rows', len(normal), 'and', len(normal) + 1)
```

**Remember:** Tune the threshold against how many alerts a human can actually review per day.

**Common mistake:** Setting contamination to a guess and drowning the on-call rota in false alarms.

## 4. One-class SVM

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

## 5. Local Outlier Factor

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

## 6. Reconstruction error methods

Anomaly detection is classification without labels for the interesting class. Isolation Forest works because anomalies are easier to isolate with random splits. Whatever method you pick, the hard part is the threshold: too sensitive and nobody reads the alerts.

```python
import numpy as np
from sklearn.ensemble import IsolationForest

rng = np.random.default_rng(0)
normal = rng.normal(0, 1, size=(500, 2))
weird = np.array([[6.0, 6.0], [-7.0, 5.0]])
X = np.vstack([normal, weird])

model = IsolationForest(contamination=0.01, random_state=0).fit(X)
scores = model.score_samples(X)
flagged = np.argsort(scores)[:5]
print('most anomalous rows:', flagged)
print('the two planted outliers were rows', len(normal), 'and', len(normal) + 1)
```

**Remember:** Tune the threshold against how many alerts a human can actually review per day.

**Common mistake:** Setting contamination to a guess and drowning the on-call rota in false alarms.

## 7. Time-series anomaly detection

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

## 8. Evaluating with few or no labels

Vibes do not survive a prompt change. Build a small golden set of real inputs with expected outputs, run it on every change, and track the score. Use an LLM judge for open-ended quality, but calibrate the judge against human ratings first.

```python
GOLDEN = [
    {'input': 'charged twice', 'expect': 'BILLING'},
    {'input': 'crashes on upload', 'expect': 'BUG'},
    {'input': 'please add dark mode', 'expect': 'FEATURE'},
]

def classify(text):                      # stand-in for the real model call
    t = text.lower()
    if 'charg' in t or 'bill' in t:
        return 'BILLING'
    if 'crash' in t or 'error' in t:
        return 'BUG'
    return 'FEATURE'

hits = sum(classify(c['input']) == c['expect'] for c in GOLDEN)
print(f'eval score {hits}/{len(GOLDEN)}')
assert hits == len(GOLDEN), 'regression: fix before shipping'
```

**Remember:** 50 real examples you curated beat 5000 synthetic ones nobody checked.

**Common mistake:** Changing the prompt on Friday with no eval and finding out from customers on Monday.

## 9. Alert fatigue and precision

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

## 10. A server-metrics anomaly detector

Anomaly detection is classification without labels for the interesting class. Isolation Forest works because anomalies are easier to isolate with random splits. Whatever method you pick, the hard part is the threshold: too sensitive and nobody reads the alerts.

```python
import numpy as np
from sklearn.ensemble import IsolationForest

rng = np.random.default_rng(0)
normal = rng.normal(0, 1, size=(500, 2))
weird = np.array([[6.0, 6.0], [-7.0, 5.0]])
X = np.vstack([normal, weird])

model = IsolationForest(contamination=0.01, random_state=0).fit(X)
scores = model.score_samples(X)
flagged = np.argsort(scores)[:5]
print('most anomalous rows:', flagged)
print('the two planted outliers were rows', len(normal), 'and', len(normal) + 1)
```

**Remember:** Tune the threshold against how many alerts a human can actually review per day.

**Common mistake:** Setting contamination to a guess and drowning the on-call rota in false alarms.

---

## What you should be able to do after Day 61

- Explain **Framing: rare, unlabelled, costly** to someone else without notes.
- Explain **Statistical thresholds and z-scores** to someone else without notes.
- Explain **Isolation Forest** to someone else without notes.
- Explain **One-class SVM** to someone else without notes.
- Explain **Local Outlier Factor** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
