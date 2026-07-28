# Day 53 — Ensembles: bagging and random forests

Aaj ka goal: **Ensembles: bagging and random forests** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Wisdom of uncorrelated errors |
| 2 | Bootstrap sampling |
| 3 | Bagging |
| 4 | Random feature subsets |
| 5 | Out-of-bag error estimation |
| 6 | Tuning a random forest |
| 7 | Feature importance and its bias |
| 8 | Permutation importance |
| 9 | Extremely randomised trees |
| 10 | Random forest as the tabular default |

---

## 1. Wisdom of uncorrelated errors

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

Practice: `examples/01_wisdom_of_uncorrelated_errors.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Bootstrap sampling

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

Practice: `examples/02_bootstrap_sampling.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Bagging

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

Practice: `examples/03_bagging.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Random feature subsets

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

Practice: `examples/04_random_feature_subsets.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Out-of-bag error estimation

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

Practice: `examples/05_out_of_bag_error_estimation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Tuning a random forest

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

Practice: `examples/06_tuning_a_random_forest.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Feature importance and its bias

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

Practice: `examples/07_feature_importance_and_its_bias.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Permutation importance

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

Practice: `examples/08_permutation_importance.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Extremely randomised trees

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

Practice: `examples/09_extremely_randomised_trees.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Random forest as the tabular default

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

Practice: `examples/10_random_forest_as_the_tabular_default.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 53 ke baad aapko ye aana chahiye

- **Wisdom of uncorrelated errors** ko bina notes dekhe kisi dost ko samjha sakna.
- **Bootstrap sampling** ko bina notes dekhe kisi dost ko samjha sakna.
- **Bagging** ko bina notes dekhe kisi dost ko samjha sakna.
- **Random feature subsets** ko bina notes dekhe kisi dost ko samjha sakna.
- **Out-of-bag error estimation** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
