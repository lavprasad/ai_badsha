# Day 41 — Data splitting done right

Aaj ka goal: **Data splitting done right** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Train, validation and test roles |
| 2 | Random split |
| 3 | Stratified split for imbalance |
| 4 | Group split to avoid entity leakage |
| 5 | Time-based split for temporal data |
| 6 | K-fold cross-validation |
| 7 | Stratified and grouped K-fold |
| 8 | Nested cross-validation |
| 9 | How many splits is too many |
| 10 | Locking the test set away |

---

## 1. Train, validation and test roles

### Aasaan Bhasha

Train parameters fit karta hai, validation baaki sab chunta hai, test ek hi baar khulta hai. Classes imbalanced hon to stratify karo, ek hi entity baar-baar aaye to group karo, aur agar aap future predict kar rahe ho to time se split karo. Galat split uske baad ke har number ko bekaar kar deta hai.

### Chhota code

```python
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit, GroupShuffleSplit

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 3))
y = (rng.random(200) < 0.1).astype(int)      # 10% positive
groups = rng.integers(0, 40, size=200)       # 40 customers

_, _, ytr, yte = train_test_split(X, y, test_size=0.3, stratify=y, random_state=0)
print('stratified positive rate  train %.3f  test %.3f' % (ytr.mean(), yte.mean()))

tr, te = next(GroupShuffleSplit(test_size=0.3, random_state=0).split(X, y, groups))
print('group overlap (must be 0):', len(set(groups[tr]) & set(groups[te])))
```

**Yaad rakho:** Ek entity split ke theek ek hi taraf honi chahiye. Overlap check karo, maan mat lo.

**Aam galti:** Repeated customers wale data par random split, jisse model customer ko pehchanta hai, pattern ko nahi.

Practice: `examples/01_train_validation_and_test_roles.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Random split

### Aasaan Bhasha

Train parameters fit karta hai, validation baaki sab chunta hai, test ek hi baar khulta hai. Classes imbalanced hon to stratify karo, ek hi entity baar-baar aaye to group karo, aur agar aap future predict kar rahe ho to time se split karo. Galat split uske baad ke har number ko bekaar kar deta hai.

### Chhota code

```python
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit, GroupShuffleSplit

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 3))
y = (rng.random(200) < 0.1).astype(int)      # 10% positive
groups = rng.integers(0, 40, size=200)       # 40 customers

_, _, ytr, yte = train_test_split(X, y, test_size=0.3, stratify=y, random_state=0)
print('stratified positive rate  train %.3f  test %.3f' % (ytr.mean(), yte.mean()))

tr, te = next(GroupShuffleSplit(test_size=0.3, random_state=0).split(X, y, groups))
print('group overlap (must be 0):', len(set(groups[tr]) & set(groups[te])))
```

**Yaad rakho:** Ek entity split ke theek ek hi taraf honi chahiye. Overlap check karo, maan mat lo.

**Aam galti:** Repeated customers wale data par random split, jisse model customer ko pehchanta hai, pattern ko nahi.

Practice: `examples/02_random_split.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Stratified split for imbalance

### Aasaan Bhasha

Train parameters fit karta hai, validation baaki sab chunta hai, test ek hi baar khulta hai. Classes imbalanced hon to stratify karo, ek hi entity baar-baar aaye to group karo, aur agar aap future predict kar rahe ho to time se split karo. Galat split uske baad ke har number ko bekaar kar deta hai.

### Chhota code

```python
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit, GroupShuffleSplit

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 3))
y = (rng.random(200) < 0.1).astype(int)      # 10% positive
groups = rng.integers(0, 40, size=200)       # 40 customers

_, _, ytr, yte = train_test_split(X, y, test_size=0.3, stratify=y, random_state=0)
print('stratified positive rate  train %.3f  test %.3f' % (ytr.mean(), yte.mean()))

tr, te = next(GroupShuffleSplit(test_size=0.3, random_state=0).split(X, y, groups))
print('group overlap (must be 0):', len(set(groups[tr]) & set(groups[te])))
```

**Yaad rakho:** Ek entity split ke theek ek hi taraf honi chahiye. Overlap check karo, maan mat lo.

**Aam galti:** Repeated customers wale data par random split, jisse model customer ko pehchanta hai, pattern ko nahi.

Practice: `examples/03_stratified_split_for_imbalance.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Group split to avoid entity leakage

### Aasaan Bhasha

Leakage matlab training me aisi information jo prediction ke waqt hogi hi nahi. Isse namumkin validation scores aate hain aur model production me dhah jaata hai. Agar accuracy shak ke laayak chhalaang lagaye, to jashn se pehle leak dhoondho.

### Chhota code

```python
# Three classic leaks, all silent:
# 1. Scaling/imputing before the train/test split
# 2. A column filled in only after the outcome ('refund_amount' when predicting refunds)
# 3. Random split on time-series so the model sees the future

import pandas as pd
df = pd.DataFrame({'ts': pd.date_range('2024-01-01', periods=100, freq='D')})
cut = int(len(df) * 0.8)
train, test = df.iloc[:cut], df.iloc[cut:]     # time-ordered split, no look-ahead
print(train['ts'].max(), '<', test['ts'].min())
```

**Yaad rakho:** Mushkil business problem par 0.999 AUC ek bug report hai, result nahi.

**Aam galti:** Leaked model ship karke asli accuracy gusse wale users se pata chalna.

Practice: `examples/04_group_split_to_avoid_entity_leakage.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Time-based split for temporal data

### Aasaan Bhasha

Train parameters fit karta hai, validation baaki sab chunta hai, test ek hi baar khulta hai. Classes imbalanced hon to stratify karo, ek hi entity baar-baar aaye to group karo, aur agar aap future predict kar rahe ho to time se split karo. Galat split uske baad ke har number ko bekaar kar deta hai.

### Chhota code

```python
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit, GroupShuffleSplit

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 3))
y = (rng.random(200) < 0.1).astype(int)      # 10% positive
groups = rng.integers(0, 40, size=200)       # 40 customers

_, _, ytr, yte = train_test_split(X, y, test_size=0.3, stratify=y, random_state=0)
print('stratified positive rate  train %.3f  test %.3f' % (ytr.mean(), yte.mean()))

tr, te = next(GroupShuffleSplit(test_size=0.3, random_state=0).split(X, y, groups))
print('group overlap (must be 0):', len(set(groups[tr]) & set(groups[te])))
```

**Yaad rakho:** Ek entity split ke theek ek hi taraf honi chahiye. Overlap check karo, maan mat lo.

**Aam galti:** Repeated customers wale data par random split, jisse model customer ko pehchanta hai, pattern ko nahi.

Practice: `examples/05_time_based_split_for_temporal_data.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. K-fold cross-validation

### Aasaan Bhasha

Teen split, teen kaam: train parameters fit karta hai, validation hyperparameters chunta hai, test ek imaandaar final number deta hai. K-fold cross-validation validation slice ghuma kar data dobara use karta hai — jab aapke paas kuch hazaar rows hi hon to ye zaroori hai.

### Chhota code

```python
from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, StratifiedKFold

X, y = load_wine(return_X_y=True)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
scores = cross_val_score(RandomForestClassifier(random_state=0), X, y, cv=cv)
print('folds', scores.round(3))
print(f'mean {scores.mean():.3f} +/- {scores.std():.3f}')
```

**Yaad rakho:** Folds ke beech ka spread bhi batao, sirf mean nahi — zyada variance matlab mean par bharosa mat karo.

**Aam galti:** Time-series ya grouped data (ek hi patient train aur test dono me) par random K-fold — dono leak karte hain.

Practice: `examples/06_k_fold_cross_validation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Stratified and grouped K-fold

### Aasaan Bhasha

Teen split, teen kaam: train parameters fit karta hai, validation hyperparameters chunta hai, test ek imaandaar final number deta hai. K-fold cross-validation validation slice ghuma kar data dobara use karta hai — jab aapke paas kuch hazaar rows hi hon to ye zaroori hai.

### Chhota code

```python
from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, StratifiedKFold

X, y = load_wine(return_X_y=True)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
scores = cross_val_score(RandomForestClassifier(random_state=0), X, y, cv=cv)
print('folds', scores.round(3))
print(f'mean {scores.mean():.3f} +/- {scores.std():.3f}')
```

**Yaad rakho:** Folds ke beech ka spread bhi batao, sirf mean nahi — zyada variance matlab mean par bharosa mat karo.

**Aam galti:** Time-series ya grouped data (ek hi patient train aur test dono me) par random K-fold — dono leak karte hain.

Practice: `examples/07_stratified_and_grouped_k_fold.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Nested cross-validation

### Aasaan Bhasha

Teen split, teen kaam: train parameters fit karta hai, validation hyperparameters chunta hai, test ek imaandaar final number deta hai. K-fold cross-validation validation slice ghuma kar data dobara use karta hai — jab aapke paas kuch hazaar rows hi hon to ye zaroori hai.

### Chhota code

```python
from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, StratifiedKFold

X, y = load_wine(return_X_y=True)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
scores = cross_val_score(RandomForestClassifier(random_state=0), X, y, cv=cv)
print('folds', scores.round(3))
print(f'mean {scores.mean():.3f} +/- {scores.std():.3f}')
```

**Yaad rakho:** Folds ke beech ka spread bhi batao, sirf mean nahi — zyada variance matlab mean par bharosa mat karo.

**Aam galti:** Time-series ya grouped data (ek hi patient train aur test dono me) par random K-fold — dono leak karte hain.

Practice: `examples/08_nested_cross_validation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. How many splits is too many

### Aasaan Bhasha

Train parameters fit karta hai, validation baaki sab chunta hai, test ek hi baar khulta hai. Classes imbalanced hon to stratify karo, ek hi entity baar-baar aaye to group karo, aur agar aap future predict kar rahe ho to time se split karo. Galat split uske baad ke har number ko bekaar kar deta hai.

### Chhota code

```python
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit, GroupShuffleSplit

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 3))
y = (rng.random(200) < 0.1).astype(int)      # 10% positive
groups = rng.integers(0, 40, size=200)       # 40 customers

_, _, ytr, yte = train_test_split(X, y, test_size=0.3, stratify=y, random_state=0)
print('stratified positive rate  train %.3f  test %.3f' % (ytr.mean(), yte.mean()))

tr, te = next(GroupShuffleSplit(test_size=0.3, random_state=0).split(X, y, groups))
print('group overlap (must be 0):', len(set(groups[tr]) & set(groups[te])))
```

**Yaad rakho:** Ek entity split ke theek ek hi taraf honi chahiye. Overlap check karo, maan mat lo.

**Aam galti:** Repeated customers wale data par random split, jisse model customer ko pehchanta hai, pattern ko nahi.

Practice: `examples/09_how_many_splits_is_too_many.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Locking the test set away

### Aasaan Bhasha

Train parameters fit karta hai, validation baaki sab chunta hai, test ek hi baar khulta hai. Classes imbalanced hon to stratify karo, ek hi entity baar-baar aaye to group karo, aur agar aap future predict kar rahe ho to time se split karo. Galat split uske baad ke har number ko bekaar kar deta hai.

### Chhota code

```python
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit, GroupShuffleSplit

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 3))
y = (rng.random(200) < 0.1).astype(int)      # 10% positive
groups = rng.integers(0, 40, size=200)       # 40 customers

_, _, ytr, yte = train_test_split(X, y, test_size=0.3, stratify=y, random_state=0)
print('stratified positive rate  train %.3f  test %.3f' % (ytr.mean(), yte.mean()))

tr, te = next(GroupShuffleSplit(test_size=0.3, random_state=0).split(X, y, groups))
print('group overlap (must be 0):', len(set(groups[tr]) & set(groups[te])))
```

**Yaad rakho:** Ek entity split ke theek ek hi taraf honi chahiye. Overlap check karo, maan mat lo.

**Aam galti:** Repeated customers wale data par random split, jisse model customer ko pehchanta hai, pattern ko nahi.

Practice: `examples/10_locking_the_test_set_away.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 41 ke baad aapko ye aana chahiye

- **Train, validation and test roles** ko bina notes dekhe kisi dost ko samjha sakna.
- **Random split** ko bina notes dekhe kisi dost ko samjha sakna.
- **Stratified split for imbalance** ko bina notes dekhe kisi dost ko samjha sakna.
- **Group split to avoid entity leakage** ko bina notes dekhe kisi dost ko samjha sakna.
- **Time-based split for temporal data** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
