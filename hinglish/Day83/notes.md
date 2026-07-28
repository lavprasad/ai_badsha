# Day 83 — Regularisation in deep nets

Aaj ka goal: **Regularisation in deep nets** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Overfitting in high-capacity models |
| 2 | Weight decay |
| 3 | Dropout |
| 4 | Inverted dropout at inference |
| 5 | Early stopping |
| 6 | Data augmentation as regularisation |
| 7 | Label smoothing |
| 8 | Mixup and CutMix |
| 9 | Ensembling and snapshot ensembles |
| 10 | Choosing regularisation by symptom |

---

## 1. Overfitting in high-capacity models

### Aasaan Bhasha

Underfitting matlab high bias: model itna simple hai ki har jagah galat hai, training data par bhi. Overfitting matlab high variance: usne training set ratt liya aur naye data par bikhar jaata hai. Train aur validation score ka farq batata hai aapke paas kaunsa wala hai.

### Chhota code

```python
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=800, n_informative=5, random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0)

for depth in (1, 3, 8, None):
    m = DecisionTreeClassifier(max_depth=depth, random_state=0).fit(Xtr, ytr)
    print(f'depth={str(depth):>4}  train={m.score(Xtr, ytr):.3f}  test={m.score(Xte, yte):.3f}')
```

**Yaad rakho:** Train 1.00 / test 0.70 overfitting hai. Train 0.70 / test 0.69 underfitting hai. Sahi wale ko theek karo.

**Aam galti:** Capacity badha kar aisa gap theek karna jo asal me kam data ya leak se aaya tha.

Practice: `examples/01_overfitting_in_high_capacity_models.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Weight decay

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

Practice: `examples/02_weight_decay.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Dropout

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

Practice: `examples/03_dropout.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Inverted dropout at inference

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

Practice: `examples/04_inverted_dropout_at_inference.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Early stopping

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

Practice: `examples/05_early_stopping.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Data augmentation as regularisation

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

Practice: `examples/06_data_augmentation_as_regularisation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Label smoothing

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

Practice: `examples/07_label_smoothing.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Mixup and CutMix

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

Practice: `examples/08_mixup_and_cutmix.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Ensembling and snapshot ensembles

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

Practice: `examples/09_ensembling_and_snapshot_ensembles.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Choosing regularisation by symptom

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

Practice: `examples/10_choosing_regularisation_by_symptom.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 83 ke baad aapko ye aana chahiye

- **Overfitting in high-capacity models** ko bina notes dekhe kisi dost ko samjha sakna.
- **Weight decay** ko bina notes dekhe kisi dost ko samjha sakna.
- **Dropout** ko bina notes dekhe kisi dost ko samjha sakna.
- **Inverted dropout at inference** ko bina notes dekhe kisi dost ko samjha sakna.
- **Early stopping** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
