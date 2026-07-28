# Day 47 — Regularised linear models

Aaj ka goal: **Regularised linear models** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Why unregularised models overfit wide data |
| 2 | Ridge regression |
| 3 | Lasso and automatic feature selection |
| 4 | Elastic net |
| 5 | Choosing alpha with cross-validation |
| 6 | The scaling requirement |
| 7 | Coefficient paths |
| 8 | Regularisation for logistic regression |
| 9 | Sparse models for interpretability |
| 10 | Comparing all four on one dataset |

---

## 1. Why unregularised models overfit wide data

### Aasaan Bhasha

Aaj ka idea — **Why unregularised models overfit wide data** — Regularised linear models ke theme ke andar aata hai. Ise trivia nahi, ek tool ki tarah padho: ye kaam kya karta hai, aapke data ke baare me kya maan kar chalta hai, aur wo maanyata jhooth nikle to kya tootta hai?

### Chhota code

```python
# Explore: Why unregularised models overfit wide data
print("practice: Why unregularised models overfit wide data")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Yaad rakho:** `Why unregularised models overfit wide data` use karne se pehle ek assumption likho jo ye aapke data ke baare me maanta hai.

**Aam galti:** `Why unregularised models overfit wide data` ko tutorial se copy-paste kar lena bina jaane ki wo kya maanta hai aur kab fail hota hai.

Practice: `examples/01_why_unregularised_models_overfit_wide_da.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Ridge regression

### Aasaan Bhasha

Regularisation bade weights par penalty lagata hai taaki model simple explanation pasand kare. L2 (ridge) sab kuch smoothly chhota karta hai; L1 (lasso) kuch weights ko bilkul zero kar deta hai aur isi tarah features chunta hai. Elastic net dono milata hai.

### Chhota code

```python
import numpy as np
from sklearn.linear_model import Ridge, Lasso
from sklearn.datasets import make_regression

X, y = make_regression(n_samples=200, n_features=20, n_informative=5, noise=10, random_state=0)

ridge = Ridge(alpha=1.0).fit(X, y)
lasso = Lasso(alpha=1.0).fit(X, y)
print('ridge non-zero coefs', int(np.sum(np.abs(ridge.coef_) > 1e-6)))
print('lasso non-zero coefs', int(np.sum(np.abs(lasso.coef_) > 1e-6)))
```

**Yaad rakho:** Regularise karne se pehle features scale karo, warna penalty usi column ko sazaa deta hai jiski units chhoti hain.

**Aam galti:** Test set par `alpha` tune karna — use sirf train par cross-validation se chuno.

Practice: `examples/02_ridge_regression.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Lasso and automatic feature selection

### Aasaan Bhasha

Regularisation bade weights par penalty lagata hai taaki model simple explanation pasand kare. L2 (ridge) sab kuch smoothly chhota karta hai; L1 (lasso) kuch weights ko bilkul zero kar deta hai aur isi tarah features chunta hai. Elastic net dono milata hai.

### Chhota code

```python
import numpy as np
from sklearn.linear_model import Ridge, Lasso
from sklearn.datasets import make_regression

X, y = make_regression(n_samples=200, n_features=20, n_informative=5, noise=10, random_state=0)

ridge = Ridge(alpha=1.0).fit(X, y)
lasso = Lasso(alpha=1.0).fit(X, y)
print('ridge non-zero coefs', int(np.sum(np.abs(ridge.coef_) > 1e-6)))
print('lasso non-zero coefs', int(np.sum(np.abs(lasso.coef_) > 1e-6)))
```

**Yaad rakho:** Regularise karne se pehle features scale karo, warna penalty usi column ko sazaa deta hai jiski units chhoti hain.

**Aam galti:** Test set par `alpha` tune karna — use sirf train par cross-validation se chuno.

Practice: `examples/03_lasso_and_automatic_feature_selection.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Elastic net

### Aasaan Bhasha

Regularisation bade weights par penalty lagata hai taaki model simple explanation pasand kare. L2 (ridge) sab kuch smoothly chhota karta hai; L1 (lasso) kuch weights ko bilkul zero kar deta hai aur isi tarah features chunta hai. Elastic net dono milata hai.

### Chhota code

```python
import numpy as np
from sklearn.linear_model import Ridge, Lasso
from sklearn.datasets import make_regression

X, y = make_regression(n_samples=200, n_features=20, n_informative=5, noise=10, random_state=0)

ridge = Ridge(alpha=1.0).fit(X, y)
lasso = Lasso(alpha=1.0).fit(X, y)
print('ridge non-zero coefs', int(np.sum(np.abs(ridge.coef_) > 1e-6)))
print('lasso non-zero coefs', int(np.sum(np.abs(lasso.coef_) > 1e-6)))
```

**Yaad rakho:** Regularise karne se pehle features scale karo, warna penalty usi column ko sazaa deta hai jiski units chhoti hain.

**Aam galti:** Test set par `alpha` tune karna — use sirf train par cross-validation se chuno.

Practice: `examples/04_elastic_net.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Choosing alpha with cross-validation

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

Practice: `examples/05_choosing_alpha_with_cross_validation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. The scaling requirement

### Aasaan Bhasha

Data parallelism model ki copies banata hai aur batch baant deta hai; model parallelism model ko baantta hai jab wo ek device par na aaye. Profiling ke baad hi scale karo — 'humein aur GPUs chahiye' wali zyadatar problems asal me dheema data loader hoti hain.

### Chhota code

```python
# Effective batch = per_device_batch * n_devices * grad_accum_steps
per_device, devices, accum = 8, 4, 4
print('effective batch size', per_device * devices * accum)
print('\\nGradient accumulation gives a large effective batch on small memory:')
print('  for i, batch in enumerate(loader):')
print('      loss = model(batch).loss / accum')
print('      loss.backward()')
print('      if (i + 1) % accum == 0:')
print('          opt.step(); opt.zero_grad()')
```

**Yaad rakho:** Pehle profile karo. GPU 30% utilisation par matlab bottleneck data pipeline hai, GPU nahi.

**Aam galti:** Batch scale karte waqt learning rate galat scale karna — bade batch ko aam taur par bada LR chahiye.

Practice: `examples/06_the_scaling_requirement.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Coefficient paths

### Aasaan Bhasha

ML code ko baaki code jaise tests chahiye, plus data tests: schema, ranges, null rates, class balance. Har known failure mode ke liye ek behavioural test jodo — ek test jo pichhli baar ka outage pakad leta, wo 90% coverage se zyada keemti hai.

### Chhota code

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

**Yaad rakho:** Data contract test karo, sirf function nahi — kharab data kharab code se zyada models todta hai.

**Aam galti:** Sirf happy path test karna, jisse poora-null column chupchap constant model train kar deta hai.

Practice: `examples/07_coefficient_paths.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Regularisation for logistic regression

### Aasaan Bhasha

Logistic regression linear score ko sigmoid se dabaa kar probability banata hai. Coefficients log-odds hain: +0.7 matlab odds lagbhag double. Jahan decision regulator ko samjhana pade, wahan aaj bhi yahi default hai.

### Chhota code

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

**Yaad rakho:** Sigmoid ka input clip karo — bade negative number ka `exp` overflow hokar NaN de deta hai.

**Aam galti:** Raw output ko calibrated probability maan lena bina kabhi calibration curve dekhe.

Practice: `examples/08_regularisation_for_logistic_regression.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Sparse models for interpretability

### Aasaan Bhasha

Agar aap decision samjha nahi sakte, to aap use defend bhi nahi kar sakte — aur credit, hiring aur healthcare me ye legally zaroori hai. Permutation importance model-agnostic aur imaandaar hai. SHAP per-prediction attributions deta hai theoretical base ke saath par sach me compute maangta hai.

### Chhota code

```python
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

X, y = load_breast_cancer(return_X_y=True)
names = load_breast_cancer().feature_names
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0)
m = RandomForestClassifier(n_estimators=200, random_state=0, n_jobs=-1).fit(Xtr, ytr)

imp = permutation_importance(m, Xte, yte, n_repeats=10, random_state=0)
for i in np.argsort(-imp.importances_mean)[:5]:
    print(f'{names[i]:<28} {imp.importances_mean[i]:.4f}')
```

**Yaad rakho:** TEST set par permutation importance batati hai ki generalise karne ke liye model kis par tik raha hai.

**Aam galti:** Importance ko causation ki tarah pesh karna — model ne correlation dhoonda hai, bas.

Practice: `examples/09_sparse_models_for_interpretability.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Comparing all four on one dataset

### Aasaan Bhasha

Aaj ka idea — **Comparing all four on one dataset** — Regularised linear models ke theme ke andar aata hai. Ise trivia nahi, ek tool ki tarah padho: ye kaam kya karta hai, aapke data ke baare me kya maan kar chalta hai, aur wo maanyata jhooth nikle to kya tootta hai?

### Chhota code

```python
# Explore: Comparing all four on one dataset
print("practice: Comparing all four on one dataset")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Yaad rakho:** `Comparing all four on one dataset` use karne se pehle ek assumption likho jo ye aapke data ke baare me maanta hai.

**Aam galti:** `Comparing all four on one dataset` ko tutorial se copy-paste kar lena bina jaane ki wo kya maanta hai aur kab fail hota hai.

Practice: `examples/10_comparing_all_four_on_one_dataset.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 47 ke baad aapko ye aana chahiye

- **Why unregularised models overfit wide data** ko bina notes dekhe kisi dost ko samjha sakna.
- **Ridge regression** ko bina notes dekhe kisi dost ko samjha sakna.
- **Lasso and automatic feature selection** ko bina notes dekhe kisi dost ko samjha sakna.
- **Elastic net** ko bina notes dekhe kisi dost ko samjha sakna.
- **Choosing alpha with cross-validation** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
