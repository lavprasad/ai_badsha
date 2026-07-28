# Day 58 — Handling imbalanced data

Aaj ka goal: **Handling imbalanced data** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

Practice: `examples/01_why_accuracy_lies_here.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Class weights

### Aasaan Bhasha

Jab ek class data ka 1% ho, model hamesha 'no' bolna seekh leta hai. Ise class weights (sasta, pehli choice), threshold tuning, ya resampling se theek karo. SMOTE minority points banata hai — aur use sirf training fold par hi lagana chahiye.

### Chhota code

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

**Yaad rakho:** Kuch bhi install karne se pehle `class_weight='balanced'` try karo.

**Aam galti:** Split se pehle SMOTE lagana, jisse test rows ki synthetic copies training me aa jaati hain.

Practice: `examples/02_class_weights.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Threshold moving

### Aasaan Bhasha

Jab ek class data ka 1% ho, model hamesha 'no' bolna seekh leta hai. Ise class weights (sasta, pehli choice), threshold tuning, ya resampling se theek karo. SMOTE minority points banata hai — aur use sirf training fold par hi lagana chahiye.

### Chhota code

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

**Yaad rakho:** Kuch bhi install karne se pehle `class_weight='balanced'` try karo.

**Aam galti:** Split se pehle SMOTE lagana, jisse test rows ki synthetic copies training me aa jaati hain.

Practice: `examples/03_threshold_moving.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Random over- and under-sampling

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

Practice: `examples/04_random_over_and_under_sampling.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. SMOTE and synthetic minority points

### Aasaan Bhasha

Jab ek class data ka 1% ho, model hamesha 'no' bolna seekh leta hai. Ise class weights (sasta, pehli choice), threshold tuning, ya resampling se theek karo. SMOTE minority points banata hai — aur use sirf training fold par hi lagana chahiye.

### Chhota code

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

**Yaad rakho:** Kuch bhi install karne se pehle `class_weight='balanced'` try karo.

**Aam galti:** Split se pehle SMOTE lagana, jisse test rows ki synthetic copies training me aa jaati hain.

Practice: `examples/05_smote_and_synthetic_minority_points.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Where resampling must happen in the pipeline

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

Practice: `examples/06_where_resampling_must_happen_in_the_pipe.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Anomaly detection framing instead

### Aasaan Bhasha

Jab ek class data ka 1% ho, model hamesha 'no' bolna seekh leta hai. Ise class weights (sasta, pehli choice), threshold tuning, ya resampling se theek karo. SMOTE minority points banata hai — aur use sirf training fold par hi lagana chahiye.

### Chhota code

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

**Yaad rakho:** Kuch bhi install karne se pehle `class_weight='balanced'` try karo.

**Aam galti:** Split se pehle SMOTE lagana, jisse test rows ki synthetic copies training me aa jaati hain.

Practice: `examples/07_anomaly_detection_framing_instead.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Cost-sensitive learning

### Aasaan Bhasha

Jab ek class data ka 1% ho, model hamesha 'no' bolna seekh leta hai. Ise class weights (sasta, pehli choice), threshold tuning, ya resampling se theek karo. SMOTE minority points banata hai — aur use sirf training fold par hi lagana chahiye.

### Chhota code

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

**Yaad rakho:** Kuch bhi install karne se pehle `class_weight='balanced'` try karo.

**Aam galti:** Split se pehle SMOTE lagana, jisse test rows ki synthetic copies training me aa jaati hain.

Practice: `examples/08_cost_sensitive_learning.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Choosing PR-AUC over ROC-AUC

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

Practice: `examples/09_choosing_pr_auc_over_roc_auc.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. A fraud detection walkthrough

### Aasaan Bhasha

Jab ek class data ka 1% ho, model hamesha 'no' bolna seekh leta hai. Ise class weights (sasta, pehli choice), threshold tuning, ya resampling se theek karo. SMOTE minority points banata hai — aur use sirf training fold par hi lagana chahiye.

### Chhota code

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

**Yaad rakho:** Kuch bhi install karne se pehle `class_weight='balanced'` try karo.

**Aam galti:** Split se pehle SMOTE lagana, jisse test rows ki synthetic copies training me aa jaati hain.

Practice: `examples/10_a_fraud_detection_walkthrough.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 58 ke baad aapko ye aana chahiye

- **Why accuracy lies here** ko bina notes dekhe kisi dost ko samjha sakna.
- **Class weights** ko bina notes dekhe kisi dost ko samjha sakna.
- **Threshold moving** ko bina notes dekhe kisi dost ko samjha sakna.
- **Random over- and under-sampling** ko bina notes dekhe kisi dost ko samjha sakna.
- **SMOTE and synthetic minority points** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
