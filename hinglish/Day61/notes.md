# Day 61 — Anomaly detection

Aaj ka goal: **Anomaly detection** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

### Aasaan Bhasha

Anomaly detection matlab classification jisme interesting class ke labels hi nahi hain. Isolation Forest isliye kaam karta hai kyunki anomalies random splits se alag karna aasan hota hai. Method jo bhi ho, mushkil hissa threshold hai: zyada sensitive rakho to alerts koi padhta hi nahi.

### Chhota code

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

**Yaad rakho:** Threshold ko is hisaab se tune karo ki ek insaan roz kitne alerts sach me review kar sakta hai.

**Aam galti:** Contamination ka andaaza laga kar set karna aur on-call rota ko false alarms me duba dena.

Practice: `examples/01_framing_rare_unlabelled_costly.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Statistical thresholds and z-scores

### Aasaan Bhasha

Anomaly detection matlab classification jisme interesting class ke labels hi nahi hain. Isolation Forest isliye kaam karta hai kyunki anomalies random splits se alag karna aasan hota hai. Method jo bhi ho, mushkil hissa threshold hai: zyada sensitive rakho to alerts koi padhta hi nahi.

### Chhota code

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

**Yaad rakho:** Threshold ko is hisaab se tune karo ki ek insaan roz kitne alerts sach me review kar sakta hai.

**Aam galti:** Contamination ka andaaza laga kar set karna aur on-call rota ko false alarms me duba dena.

Practice: `examples/02_statistical_thresholds_and_z_scores.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Isolation Forest

### Aasaan Bhasha

Anomaly detection matlab classification jisme interesting class ke labels hi nahi hain. Isolation Forest isliye kaam karta hai kyunki anomalies random splits se alag karna aasan hota hai. Method jo bhi ho, mushkil hissa threshold hai: zyada sensitive rakho to alerts koi padhta hi nahi.

### Chhota code

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

**Yaad rakho:** Threshold ko is hisaab se tune karo ki ek insaan roz kitne alerts sach me review kar sakta hai.

**Aam galti:** Contamination ka andaaza laga kar set karna aur on-call rota ko false alarms me duba dena.

Practice: `examples/03_isolation_forest.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. One-class SVM

### Aasaan Bhasha

SVM classes ke beech sabse chaudi margin wali boundary dhoondta hai. Kernel trick use tedhi boundaries khinchne deta hai, higher-dimensional space me inner products nikaal kar, bina wo space kabhi banaye. Chhote, saaf, high-dimensional datasets (jaise text) par strong.

### Chhota code

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

**Yaad rakho:** SVM rows ke saath lagbhag quadratically badhta hai — ~100k samples se upar boosting uthao.

**Aam galti:** Feature scaling chhod dena, jo chupke se RBF kernel barbaad kar deta hai.

Practice: `examples/04_one_class_svm.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Local Outlier Factor

### Aasaan Bhasha

Mean ko outliers kheench lete hain; median ko nahi. Dono report karo, saath me spread bhi. Jab mean aur median me bada farq ho to distribution skewed hai aur average aapse jhooth bol raha hai.

### Chhota code

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

**Yaad rakho:** Skewed data ke liye median + IQR batao, mean + std sirf roughly symmetric data ke liye.

**Aam galti:** 'Outliers' ko apne aap hata dena jabki wahi events aapko predict karne ke liye rakha gaya tha.

Practice: `examples/05_local_outlier_factor.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Reconstruction error methods

### Aasaan Bhasha

Anomaly detection matlab classification jisme interesting class ke labels hi nahi hain. Isolation Forest isliye kaam karta hai kyunki anomalies random splits se alag karna aasan hota hai. Method jo bhi ho, mushkil hissa threshold hai: zyada sensitive rakho to alerts koi padhta hi nahi.

### Chhota code

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

**Yaad rakho:** Threshold ko is hisaab se tune karo ki ek insaan roz kitne alerts sach me review kar sakta hai.

**Aam galti:** Contamination ka andaaza laga kar set karna aur on-call rota ko false alarms me duba dena.

Practice: `examples/06_reconstruction_error_methods.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Time-series anomaly detection

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

Practice: `examples/07_time_series_anomaly_detection.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Evaluating with few or no labels

### Aasaan Bhasha

Vibes prompt change se nahi bachte. Asli inputs ka chhota golden set banao expected outputs ke saath, har change par chalao, aur score track karo. Open-ended quality ke liye LLM judge use karo, par pehle judge ko human ratings se calibrate karo.

### Chhota code

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

**Yaad rakho:** Aapke chune hue 50 asli examples 5000 synthetic examples se behtar hain jinhe kisi ne check hi nahi kiya.

**Aam galti:** Shukravaar ko bina eval ke prompt badalna aur somvaar ko customers se pata chalna.

Practice: `examples/08_evaluating_with_few_or_no_labels.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Alert fatigue and precision

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

Practice: `examples/09_alert_fatigue_and_precision.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. A server-metrics anomaly detector

### Aasaan Bhasha

Anomaly detection matlab classification jisme interesting class ke labels hi nahi hain. Isolation Forest isliye kaam karta hai kyunki anomalies random splits se alag karna aasan hota hai. Method jo bhi ho, mushkil hissa threshold hai: zyada sensitive rakho to alerts koi padhta hi nahi.

### Chhota code

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

**Yaad rakho:** Threshold ko is hisaab se tune karo ki ek insaan roz kitne alerts sach me review kar sakta hai.

**Aam galti:** Contamination ka andaaza laga kar set karna aur on-call rota ko false alarms me duba dena.

Practice: `examples/10_a_server_metrics_anomaly_detector.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 61 ke baad aapko ye aana chahiye

- **Framing: rare, unlabelled, costly** ko bina notes dekhe kisi dost ko samjha sakna.
- **Statistical thresholds and z-scores** ko bina notes dekhe kisi dost ko samjha sakna.
- **Isolation Forest** ko bina notes dekhe kisi dost ko samjha sakna.
- **One-class SVM** ko bina notes dekhe kisi dost ko samjha sakna.
- **Local Outlier Factor** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
