# Day 83 — Regularisation in deep nets

Today's goal: work through **Regularisation in deep nets** — ten concepts, ten runnable examples, five questions.

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

Underfitting is high bias: the model is too simple and is wrong everywhere, including on training data. Overfitting is high variance: it memorised the training set and falls apart on new data. The gap between train and validation score tells you which one you have.

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

**Remember:** Train 1.00 / test 0.70 is overfitting. Train 0.70 / test 0.69 is underfitting. Fix the right one.

**Common mistake:** Adding capacity to fix a gap that was caused by too little data or a leak, not by too little capacity.

Practice: open `examples/01_overfitting_in_high_capacity_models.py`, predict the output, change one line, predict again.

## 2. Weight decay

Regularisation penalises large weights so the model prefers simpler explanations. L2 (ridge) shrinks everything smoothly; L1 (lasso) drives some weights exactly to zero and thereby selects features. Elastic net mixes both.

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

**Remember:** Scale features before regularising, or the penalty punishes whichever column happens to use small units.

**Common mistake:** Tuning `alpha` on the test set — pick it with cross-validation on train only.

Practice: open `examples/02_weight_decay.py`, predict the output, change one line, predict again.

## 3. Dropout

Regularisation penalises large weights so the model prefers simpler explanations. L2 (ridge) shrinks everything smoothly; L1 (lasso) drives some weights exactly to zero and thereby selects features. Elastic net mixes both.

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

**Remember:** Scale features before regularising, or the penalty punishes whichever column happens to use small units.

**Common mistake:** Tuning `alpha` on the test set — pick it with cross-validation on train only.

Practice: open `examples/03_dropout.py`, predict the output, change one line, predict again.

## 4. Inverted dropout at inference

Regularisation penalises large weights so the model prefers simpler explanations. L2 (ridge) shrinks everything smoothly; L1 (lasso) drives some weights exactly to zero and thereby selects features. Elastic net mixes both.

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

**Remember:** Scale features before regularising, or the penalty punishes whichever column happens to use small units.

**Common mistake:** Tuning `alpha` on the test set — pick it with cross-validation on train only.

Practice: open `examples/04_inverted_dropout_at_inference.py`, predict the output, change one line, predict again.

## 5. Early stopping

Regularisation penalises large weights so the model prefers simpler explanations. L2 (ridge) shrinks everything smoothly; L1 (lasso) drives some weights exactly to zero and thereby selects features. Elastic net mixes both.

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

**Remember:** Scale features before regularising, or the penalty punishes whichever column happens to use small units.

**Common mistake:** Tuning `alpha` on the test set — pick it with cross-validation on train only.

Practice: open `examples/05_early_stopping.py`, predict the output, change one line, predict again.

## 6. Data augmentation as regularisation

Regularisation penalises large weights so the model prefers simpler explanations. L2 (ridge) shrinks everything smoothly; L1 (lasso) drives some weights exactly to zero and thereby selects features. Elastic net mixes both.

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

**Remember:** Scale features before regularising, or the penalty punishes whichever column happens to use small units.

**Common mistake:** Tuning `alpha` on the test set — pick it with cross-validation on train only.

Practice: open `examples/06_data_augmentation_as_regularisation.py`, predict the output, change one line, predict again.

## 7. Label smoothing

Regularisation penalises large weights so the model prefers simpler explanations. L2 (ridge) shrinks everything smoothly; L1 (lasso) drives some weights exactly to zero and thereby selects features. Elastic net mixes both.

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

**Remember:** Scale features before regularising, or the penalty punishes whichever column happens to use small units.

**Common mistake:** Tuning `alpha` on the test set — pick it with cross-validation on train only.

Practice: open `examples/07_label_smoothing.py`, predict the output, change one line, predict again.

## 8. Mixup and CutMix

Regularisation penalises large weights so the model prefers simpler explanations. L2 (ridge) shrinks everything smoothly; L1 (lasso) drives some weights exactly to zero and thereby selects features. Elastic net mixes both.

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

**Remember:** Scale features before regularising, or the penalty punishes whichever column happens to use small units.

**Common mistake:** Tuning `alpha` on the test set — pick it with cross-validation on train only.

Practice: open `examples/08_mixup_and_cutmix.py`, predict the output, change one line, predict again.

## 9. Ensembling and snapshot ensembles

Regularisation penalises large weights so the model prefers simpler explanations. L2 (ridge) shrinks everything smoothly; L1 (lasso) drives some weights exactly to zero and thereby selects features. Elastic net mixes both.

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

**Remember:** Scale features before regularising, or the penalty punishes whichever column happens to use small units.

**Common mistake:** Tuning `alpha` on the test set — pick it with cross-validation on train only.

Practice: open `examples/09_ensembling_and_snapshot_ensembles.py`, predict the output, change one line, predict again.

## 10. Choosing regularisation by symptom

Regularisation penalises large weights so the model prefers simpler explanations. L2 (ridge) shrinks everything smoothly; L1 (lasso) drives some weights exactly to zero and thereby selects features. Elastic net mixes both.

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

**Remember:** Scale features before regularising, or the penalty punishes whichever column happens to use small units.

**Common mistake:** Tuning `alpha` on the test set — pick it with cross-validation on train only.

Practice: open `examples/10_choosing_regularisation_by_symptom.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 83

- Explain **Overfitting in high-capacity models** to someone else without notes.
- Explain **Weight decay** to someone else without notes.
- Explain **Dropout** to someone else without notes.
- Explain **Inverted dropout at inference** to someone else without notes.
- Explain **Early stopping** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
