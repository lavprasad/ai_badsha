# Day 64 — Ensembling your own models

Aaj ka goal: **Ensembling your own models** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Why ensembles work |
| 2 | Voting classifiers: hard and soft |
| 3 | Averaging regressors |
| 4 | Weighted blending |
| 5 | Stacking with a meta-learner |
| 6 | Out-of-fold predictions for stacking |
| 7 | Diversity beats individual strength |
| 8 | Complexity cost in production |
| 9 | When a single model is the right call |
| 10 | Building a stacked ensemble correctly |

---

## 1. Why ensembles work

### Aasaan Bhasha

Bagging bahut saare trees ko bootstrap samples aur random feature subsets par train karke average kar leta hai. Averaging wo variance kaat deta hai jo single trees ko unpredictable banata hai. Tabular data par jab bina tuning ke kuch chalta hua chahiye, random forest best default hai.

### Chhota code

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score

X, y = load_breast_cancer(return_X_y=True)
rf = RandomForestClassifier(n_estimators=300, min_samples_leaf=2, n_jobs=-1, random_state=0)
print('cv accuracy', cross_val_score(rf, X, y, cv=5).mean().round(4))

rf.fit(X, y)
top = sorted(zip(load_breast_cancer().feature_names, rf.feature_importances_), key=lambda t: -t[1])[:5]
print('top features', [(n, round(v, 3)) for n, v in top])
```

**Yaad rakho:** Zyada trees kabhi overfit nahi karte — sirf time lagta hai. Depth aur leaf size hi fit control karte hain.

**Aam galti:** Business decisions ke liye impurity-based importances use karna, permutation importance ke bajaye.

Practice: `examples/01_why_ensembles_work.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Voting classifiers: hard and soft

### Aasaan Bhasha

Ensembles tab kaam karte hain jab members **alag** galtiyan karte hain. Correlated models ka average kuch nahi deta. Stacking meta-model ko out-of-fold predictions par train karta hai — in-fold predictions leak karte hain aur aisa meta-model dete hain jo perfect dikhta hai aur turant fail hota hai.

### Chhota code

```python
import numpy as np
from sklearn.model_selection import cross_val_predict, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
cv = StratifiedKFold(5, shuffle=True, random_state=0)

base = [RandomForestClassifier(n_estimators=200, random_state=0),
        LogisticRegression(max_iter=5000)]
oof = np.column_stack([
    cross_val_predict(m, X, y, cv=cv, method='predict_proba')[:, 1] for m in base
])
print('correlation between members:', round(float(np.corrcoef(oof.T)[0, 1]), 3))
meta = LogisticRegression().fit(oof, y)
print('meta weights:', meta.coef_.round(3))
```

**Yaad rakho:** Stacking sirf out-of-fold predictions par karo. In-fold predictions bhes badle hue leak hain.

**Aam galti:** 0.2% faayde ke liye paanch-model ensemble ship karna aur inference cost aur failure modes paanch guna kar dena.

Practice: `examples/02_voting_classifiers_hard_and_soft.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Averaging regressors

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

Practice: `examples/03_averaging_regressors.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Weighted blending

### Aasaan Bhasha

Ensembles tab kaam karte hain jab members **alag** galtiyan karte hain. Correlated models ka average kuch nahi deta. Stacking meta-model ko out-of-fold predictions par train karta hai — in-fold predictions leak karte hain aur aisa meta-model dete hain jo perfect dikhta hai aur turant fail hota hai.

### Chhota code

```python
import numpy as np
from sklearn.model_selection import cross_val_predict, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
cv = StratifiedKFold(5, shuffle=True, random_state=0)

base = [RandomForestClassifier(n_estimators=200, random_state=0),
        LogisticRegression(max_iter=5000)]
oof = np.column_stack([
    cross_val_predict(m, X, y, cv=cv, method='predict_proba')[:, 1] for m in base
])
print('correlation between members:', round(float(np.corrcoef(oof.T)[0, 1]), 3))
meta = LogisticRegression().fit(oof, y)
print('meta weights:', meta.coef_.round(3))
```

**Yaad rakho:** Stacking sirf out-of-fold predictions par karo. In-fold predictions bhes badle hue leak hain.

**Aam galti:** 0.2% faayde ke liye paanch-model ensemble ship karna aur inference cost aur failure modes paanch guna kar dena.

Practice: `examples/04_weighted_blending.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Stacking with a meta-learner

### Aasaan Bhasha

NumPy ki taakat bina loops ke select aur combine karna hai. Boolean mask condition se rows chunta hai, fancy indexing position se, `np.where` condition se naya array banata hai, aur `argsort` ordering deta hai taaki aap kai arrays ko ek hi tarah sort kar sako.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
x = rng.integers(0, 100, size=10)
print('data      ', x)

mask = x > 50
print('mask      ', mask)
print('selected  ', x[mask])                 # boolean mask
print('positions ', x[[0, 3, 5]])            # fancy indexing
print('clipped   ', np.where(x > 50, 50, x)) # conditional build

order = np.argsort(-x)
print('top 3     ', x[order[:3]])
```

**Yaad rakho:** Boolean mask copy lautata hai; saada slice view lautata hai. Ek ko badalna doosre par ek jaisa asar nahi karta.

**Aam galti:** `arr[mask][0] = 5` chain karna aur sochna ki original array kyun nahi badla — aapne copy par likha.

Practice: `examples/05_stacking_with_a_meta_learner.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Out-of-fold predictions for stacking

### Aasaan Bhasha

NumPy ki taakat bina loops ke select aur combine karna hai. Boolean mask condition se rows chunta hai, fancy indexing position se, `np.where` condition se naya array banata hai, aur `argsort` ordering deta hai taaki aap kai arrays ko ek hi tarah sort kar sako.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
x = rng.integers(0, 100, size=10)
print('data      ', x)

mask = x > 50
print('mask      ', mask)
print('selected  ', x[mask])                 # boolean mask
print('positions ', x[[0, 3, 5]])            # fancy indexing
print('clipped   ', np.where(x > 50, 50, x)) # conditional build

order = np.argsort(-x)
print('top 3     ', x[order[:3]])
```

**Yaad rakho:** Boolean mask copy lautata hai; saada slice view lautata hai. Ek ko badalna doosre par ek jaisa asar nahi karta.

**Aam galti:** `arr[mask][0] = 5` chain karna aur sochna ki original array kyun nahi badla — aapne copy par likha.

Practice: `examples/06_out_of_fold_predictions_for_stacking.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Diversity beats individual strength

### Aasaan Bhasha

Ensembles tab kaam karte hain jab members **alag** galtiyan karte hain. Correlated models ka average kuch nahi deta. Stacking meta-model ko out-of-fold predictions par train karta hai — in-fold predictions leak karte hain aur aisa meta-model dete hain jo perfect dikhta hai aur turant fail hota hai.

### Chhota code

```python
import numpy as np
from sklearn.model_selection import cross_val_predict, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
cv = StratifiedKFold(5, shuffle=True, random_state=0)

base = [RandomForestClassifier(n_estimators=200, random_state=0),
        LogisticRegression(max_iter=5000)]
oof = np.column_stack([
    cross_val_predict(m, X, y, cv=cv, method='predict_proba')[:, 1] for m in base
])
print('correlation between members:', round(float(np.corrcoef(oof.T)[0, 1]), 3))
meta = LogisticRegression().fit(oof, y)
print('meta weights:', meta.coef_.round(3))
```

**Yaad rakho:** Stacking sirf out-of-fold predictions par karo. In-fold predictions bhes badle hue leak hain.

**Aam galti:** 0.2% faayde ke liye paanch-model ensemble ship karna aur inference cost aur failure modes paanch guna kar dena.

Practice: `examples/07_diversity_beats_individual_strength.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Complexity cost in production

### Aasaan Bhasha

Aaj ka idea — **Complexity cost in production** — Ensembling your own models ke theme ke andar aata hai. Ise trivia nahi, ek tool ki tarah padho: ye kaam kya karta hai, aapke data ke baare me kya maan kar chalta hai, aur wo maanyata jhooth nikle to kya tootta hai?

### Chhota code

```python
# Explore: Complexity cost in production
print("practice: Complexity cost in production")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Yaad rakho:** `Complexity cost in production` use karne se pehle ek assumption likho jo ye aapke data ke baare me maanta hai.

**Aam galti:** `Complexity cost in production` ko tutorial se copy-paste kar lena bina jaane ki wo kya maanta hai aur kab fail hota hai.

Practice: `examples/08_complexity_cost_in_production.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. When a single model is the right call

### Aasaan Bhasha

Ensembles tab kaam karte hain jab members **alag** galtiyan karte hain. Correlated models ka average kuch nahi deta. Stacking meta-model ko out-of-fold predictions par train karta hai — in-fold predictions leak karte hain aur aisa meta-model dete hain jo perfect dikhta hai aur turant fail hota hai.

### Chhota code

```python
import numpy as np
from sklearn.model_selection import cross_val_predict, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
cv = StratifiedKFold(5, shuffle=True, random_state=0)

base = [RandomForestClassifier(n_estimators=200, random_state=0),
        LogisticRegression(max_iter=5000)]
oof = np.column_stack([
    cross_val_predict(m, X, y, cv=cv, method='predict_proba')[:, 1] for m in base
])
print('correlation between members:', round(float(np.corrcoef(oof.T)[0, 1]), 3))
meta = LogisticRegression().fit(oof, y)
print('meta weights:', meta.coef_.round(3))
```

**Yaad rakho:** Stacking sirf out-of-fold predictions par karo. In-fold predictions bhes badle hue leak hain.

**Aam galti:** 0.2% faayde ke liye paanch-model ensemble ship karna aur inference cost aur failure modes paanch guna kar dena.

Practice: `examples/09_when_a_single_model_is_the_right_call.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Building a stacked ensemble correctly

### Aasaan Bhasha

Bagging bahut saare trees ko bootstrap samples aur random feature subsets par train karke average kar leta hai. Averaging wo variance kaat deta hai jo single trees ko unpredictable banata hai. Tabular data par jab bina tuning ke kuch chalta hua chahiye, random forest best default hai.

### Chhota code

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score

X, y = load_breast_cancer(return_X_y=True)
rf = RandomForestClassifier(n_estimators=300, min_samples_leaf=2, n_jobs=-1, random_state=0)
print('cv accuracy', cross_val_score(rf, X, y, cv=5).mean().round(4))

rf.fit(X, y)
top = sorted(zip(load_breast_cancer().feature_names, rf.feature_importances_), key=lambda t: -t[1])[:5]
print('top features', [(n, round(v, 3)) for n, v in top])
```

**Yaad rakho:** Zyada trees kabhi overfit nahi karte — sirf time lagta hai. Depth aur leaf size hi fit control karte hain.

**Aam galti:** Business decisions ke liye impurity-based importances use karna, permutation importance ke bajaye.

Practice: `examples/10_building_a_stacked_ensemble_correctly.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 64 ke baad aapko ye aana chahiye

- **Why ensembles work** ko bina notes dekhe kisi dost ko samjha sakna.
- **Voting classifiers: hard and soft** ko bina notes dekhe kisi dost ko samjha sakna.
- **Averaging regressors** ko bina notes dekhe kisi dost ko samjha sakna.
- **Weighted blending** ko bina notes dekhe kisi dost ko samjha sakna.
- **Stacking with a meta-learner** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
