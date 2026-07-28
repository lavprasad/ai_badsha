# Day 62 — Feature importance and model explanation

Today's goal: work through **Feature importance and model explanation** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Global vs local explanation |
| 2 | Coefficients in linear models |
| 3 | Impurity importance and its bias |
| 4 | Permutation importance |
| 5 | Partial dependence plots |
| 6 | Individual conditional expectation |
| 7 | SHAP values |
| 8 | LIME |
| 9 | Explaining to a non-technical stakeholder |
| 10 | Explanation is not causation |

---

## 1. Global vs local explanation

If you cannot explain a decision, you cannot defend it — and in credit, hiring and healthcare you are legally required to. Permutation importance is model-agnostic and honest. SHAP gives per-prediction attributions with a solid theoretical basis but costs real compute.

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

**Remember:** Permutation importance on the TEST set answers 'what does this model rely on to generalise'.

**Common mistake:** Presenting importance as causation — the model found correlation, nothing more.

Practice: open `examples/01_global_vs_local_explanation.py`, predict the output, change one line, predict again.

## 2. Coefficients in linear models

If you cannot explain a decision, you cannot defend it — and in credit, hiring and healthcare you are legally required to. Permutation importance is model-agnostic and honest. SHAP gives per-prediction attributions with a solid theoretical basis but costs real compute.

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

**Remember:** Permutation importance on the TEST set answers 'what does this model rely on to generalise'.

**Common mistake:** Presenting importance as causation — the model found correlation, nothing more.

Practice: open `examples/02_coefficients_in_linear_models.py`, predict the output, change one line, predict again.

## 3. Impurity importance and its bias

If you cannot explain a decision, you cannot defend it — and in credit, hiring and healthcare you are legally required to. Permutation importance is model-agnostic and honest. SHAP gives per-prediction attributions with a solid theoretical basis but costs real compute.

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

**Remember:** Permutation importance on the TEST set answers 'what does this model rely on to generalise'.

**Common mistake:** Presenting importance as causation — the model found correlation, nothing more.

Practice: open `examples/03_impurity_importance_and_its_bias.py`, predict the output, change one line, predict again.

## 4. Permutation importance

If you cannot explain a decision, you cannot defend it — and in credit, hiring and healthcare you are legally required to. Permutation importance is model-agnostic and honest. SHAP gives per-prediction attributions with a solid theoretical basis but costs real compute.

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

**Remember:** Permutation importance on the TEST set answers 'what does this model rely on to generalise'.

**Common mistake:** Presenting importance as causation — the model found correlation, nothing more.

Practice: open `examples/04_permutation_importance.py`, predict the output, change one line, predict again.

## 5. Partial dependence plots

Plot before you model. A histogram exposes skew and outliers, a scatter exposes non-linearity, and a line of residuals exposes a model that is systematically wrong. Five minutes of plotting saves hours of confused tuning.

```python
import matplotlib
matplotlib.use('Agg')          # headless-safe for scripts/CI
import matplotlib.pyplot as plt
import numpy as np

x = np.random.default_rng(0).normal(size=500)
fig, ax = plt.subplots()
ax.hist(x, bins=30)
ax.set_title('sample distribution')
fig.savefig('hist.png', dpi=120)
print('wrote hist.png')
```

**Remember:** Label the axes. An unlabelled plot is a decoration, not evidence.

**Common mistake:** Judging a model by its accuracy number alone without ever looking at the data.

Practice: open `examples/05_partial_dependence_plots.py`, predict the output, change one line, predict again.

## 6. Individual conditional expectation

If you cannot explain a decision, you cannot defend it — and in credit, hiring and healthcare you are legally required to. Permutation importance is model-agnostic and honest. SHAP gives per-prediction attributions with a solid theoretical basis but costs real compute.

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

**Remember:** Permutation importance on the TEST set answers 'what does this model rely on to generalise'.

**Common mistake:** Presenting importance as causation — the model found correlation, nothing more.

Practice: open `examples/06_individual_conditional_expectation.py`, predict the output, change one line, predict again.

## 7. SHAP values

If you cannot explain a decision, you cannot defend it — and in credit, hiring and healthcare you are legally required to. Permutation importance is model-agnostic and honest. SHAP gives per-prediction attributions with a solid theoretical basis but costs real compute.

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

**Remember:** Permutation importance on the TEST set answers 'what does this model rely on to generalise'.

**Common mistake:** Presenting importance as causation — the model found correlation, nothing more.

Practice: open `examples/07_shap_values.py`, predict the output, change one line, predict again.

## 8. LIME

If you cannot explain a decision, you cannot defend it — and in credit, hiring and healthcare you are legally required to. Permutation importance is model-agnostic and honest. SHAP gives per-prediction attributions with a solid theoretical basis but costs real compute.

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

**Remember:** Permutation importance on the TEST set answers 'what does this model rely on to generalise'.

**Common mistake:** Presenting importance as causation — the model found correlation, nothing more.

Practice: open `examples/08_lime.py`, predict the output, change one line, predict again.

## 9. Explaining to a non-technical stakeholder

If you cannot explain a decision, you cannot defend it — and in credit, hiring and healthcare you are legally required to. Permutation importance is model-agnostic and honest. SHAP gives per-prediction attributions with a solid theoretical basis but costs real compute.

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

**Remember:** Permutation importance on the TEST set answers 'what does this model rely on to generalise'.

**Common mistake:** Presenting importance as causation — the model found correlation, nothing more.

Practice: open `examples/09_explaining_to_a_non_technical_stakeholde.py`, predict the output, change one line, predict again.

## 10. Explanation is not causation

If you cannot explain a decision, you cannot defend it — and in credit, hiring and healthcare you are legally required to. Permutation importance is model-agnostic and honest. SHAP gives per-prediction attributions with a solid theoretical basis but costs real compute.

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

**Remember:** Permutation importance on the TEST set answers 'what does this model rely on to generalise'.

**Common mistake:** Presenting importance as causation — the model found correlation, nothing more.

Practice: open `examples/10_explanation_is_not_causation.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 62

- Explain **Global vs local explanation** to someone else without notes.
- Explain **Coefficients in linear models** to someone else without notes.
- Explain **Impurity importance and its bias** to someone else without notes.
- Explain **Permutation importance** to someone else without notes.
- Explain **Partial dependence plots** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
