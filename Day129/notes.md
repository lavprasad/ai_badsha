# Day 129 — Fine-tuning encoder models

Today's goal: work through **Fine-tuning encoder models** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Hugging Face transformers basics |
| 2 | AutoTokenizer and AutoModel |
| 3 | Adding a classification head |
| 4 | Dataset formatting and collation |
| 5 | Trainer API vs manual loop |
| 6 | Learning rates for fine-tuning |
| 7 | Freezing layers |
| 8 | Evaluating on a held-out set |
| 9 | Overfitting on small text datasets |
| 10 | A ticket classifier walkthrough |

---

## 1. Hugging Face transformers basics

Hyperparameters are the settings you choose, not learn. Grid search is exhaustive and wasteful; random search finds good regions faster in high dimensions; Bayesian search learns from previous trials. Always search inside cross-validation.

```python
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
import numpy as np

X, y = load_breast_cancer(return_X_y=True)
space = {
    'n_estimators': [100, 300, 600],
    'max_depth': [None, 4, 8, 16],
    'min_samples_leaf': [1, 2, 4, 8],
}
search = RandomizedSearchCV(
    RandomForestClassifier(random_state=0, n_jobs=-1),
    space, n_iter=12, cv=5, random_state=0,
).fit(X, y)
print(search.best_params_, round(search.best_score_, 4))
```

**Remember:** Fix the random seed and log every trial, or you cannot reproduce your own best model.

**Common mistake:** Tuning 40 hyperparameters on 400 rows — you are now fitting the validation set.

Practice: open `examples/01_hugging_face_transformers_basics.py`, predict the output, change one line, predict again.

## 2. AutoTokenizer and AutoModel

Hyperparameters are the settings you choose, not learn. Grid search is exhaustive and wasteful; random search finds good regions faster in high dimensions; Bayesian search learns from previous trials. Always search inside cross-validation.

```python
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
import numpy as np

X, y = load_breast_cancer(return_X_y=True)
space = {
    'n_estimators': [100, 300, 600],
    'max_depth': [None, 4, 8, 16],
    'min_samples_leaf': [1, 2, 4, 8],
}
search = RandomizedSearchCV(
    RandomForestClassifier(random_state=0, n_jobs=-1),
    space, n_iter=12, cv=5, random_state=0,
).fit(X, y)
print(search.best_params_, round(search.best_score_, 4))
```

**Remember:** Fix the random seed and log every trial, or you cannot reproduce your own best model.

**Common mistake:** Tuning 40 hyperparameters on 400 rows — you are now fitting the validation set.

Practice: open `examples/02_autotokenizer_and_automodel.py`, predict the output, change one line, predict again.

## 3. Adding a classification head

Hyperparameters are the settings you choose, not learn. Grid search is exhaustive and wasteful; random search finds good regions faster in high dimensions; Bayesian search learns from previous trials. Always search inside cross-validation.

```python
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
import numpy as np

X, y = load_breast_cancer(return_X_y=True)
space = {
    'n_estimators': [100, 300, 600],
    'max_depth': [None, 4, 8, 16],
    'min_samples_leaf': [1, 2, 4, 8],
}
search = RandomizedSearchCV(
    RandomForestClassifier(random_state=0, n_jobs=-1),
    space, n_iter=12, cv=5, random_state=0,
).fit(X, y)
print(search.best_params_, round(search.best_score_, 4))
```

**Remember:** Fix the random seed and log every trial, or you cannot reproduce your own best model.

**Common mistake:** Tuning 40 hyperparameters on 400 rows — you are now fitting the validation set.

Practice: open `examples/03_adding_a_classification_head.py`, predict the output, change one line, predict again.

## 4. Dataset formatting and collation

Hyperparameters are the settings you choose, not learn. Grid search is exhaustive and wasteful; random search finds good regions faster in high dimensions; Bayesian search learns from previous trials. Always search inside cross-validation.

```python
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
import numpy as np

X, y = load_breast_cancer(return_X_y=True)
space = {
    'n_estimators': [100, 300, 600],
    'max_depth': [None, 4, 8, 16],
    'min_samples_leaf': [1, 2, 4, 8],
}
search = RandomizedSearchCV(
    RandomForestClassifier(random_state=0, n_jobs=-1),
    space, n_iter=12, cv=5, random_state=0,
).fit(X, y)
print(search.best_params_, round(search.best_score_, 4))
```

**Remember:** Fix the random seed and log every trial, or you cannot reproduce your own best model.

**Common mistake:** Tuning 40 hyperparameters on 400 rows — you are now fitting the validation set.

Practice: open `examples/04_dataset_formatting_and_collation.py`, predict the output, change one line, predict again.

## 5. Trainer API vs manual loop

Hyperparameters are the settings you choose, not learn. Grid search is exhaustive and wasteful; random search finds good regions faster in high dimensions; Bayesian search learns from previous trials. Always search inside cross-validation.

```python
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
import numpy as np

X, y = load_breast_cancer(return_X_y=True)
space = {
    'n_estimators': [100, 300, 600],
    'max_depth': [None, 4, 8, 16],
    'min_samples_leaf': [1, 2, 4, 8],
}
search = RandomizedSearchCV(
    RandomForestClassifier(random_state=0, n_jobs=-1),
    space, n_iter=12, cv=5, random_state=0,
).fit(X, y)
print(search.best_params_, round(search.best_score_, 4))
```

**Remember:** Fix the random seed and log every trial, or you cannot reproduce your own best model.

**Common mistake:** Tuning 40 hyperparameters on 400 rows — you are now fitting the validation set.

Practice: open `examples/05_trainer_api_vs_manual_loop.py`, predict the output, change one line, predict again.

## 6. Learning rates for fine-tuning

Gradient descent repeatedly steps against the gradient. Full-batch is stable but slow; stochastic is noisy but escapes shallow traps; mini-batch is the practical middle. The learning rate is the single most important knob you will ever turn.

```python
import numpy as np

rng = np.random.default_rng(0)
X = rng.normal(size=(1000, 3))
true_w = np.array([1.0, -2.0, 0.5])
y = X @ true_w + rng.normal(scale=0.1, size=1000)

w, lr, batch = np.zeros(3), 0.1, 32
for epoch in range(20):
    idx = rng.permutation(len(X))
    for start in range(0, len(X), batch):
        b = idx[start:start + batch]
        grad = 2 * X[b].T @ (X[b] @ w - y[b]) / len(b)
        w -= lr * grad
print('learned', np.round(w, 3), 'target', true_w)
```

**Remember:** Shuffle every epoch, otherwise the model learns the order of your file.

**Common mistake:** Leaving the learning rate fixed forever instead of decaying it once the loss plateaus.

Practice: open `examples/06_learning_rates_for_fine_tuning.py`, predict the output, change one line, predict again.

## 7. Freezing layers

Hyperparameters are the settings you choose, not learn. Grid search is exhaustive and wasteful; random search finds good regions faster in high dimensions; Bayesian search learns from previous trials. Always search inside cross-validation.

```python
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
import numpy as np

X, y = load_breast_cancer(return_X_y=True)
space = {
    'n_estimators': [100, 300, 600],
    'max_depth': [None, 4, 8, 16],
    'min_samples_leaf': [1, 2, 4, 8],
}
search = RandomizedSearchCV(
    RandomForestClassifier(random_state=0, n_jobs=-1),
    space, n_iter=12, cv=5, random_state=0,
).fit(X, y)
print(search.best_params_, round(search.best_score_, 4))
```

**Remember:** Fix the random seed and log every trial, or you cannot reproduce your own best model.

**Common mistake:** Tuning 40 hyperparameters on 400 rows — you are now fitting the validation set.

Practice: open `examples/07_freezing_layers.py`, predict the output, change one line, predict again.

## 8. Evaluating on a held-out set

Hyperparameters are the settings you choose, not learn. Grid search is exhaustive and wasteful; random search finds good regions faster in high dimensions; Bayesian search learns from previous trials. Always search inside cross-validation.

```python
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
import numpy as np

X, y = load_breast_cancer(return_X_y=True)
space = {
    'n_estimators': [100, 300, 600],
    'max_depth': [None, 4, 8, 16],
    'min_samples_leaf': [1, 2, 4, 8],
}
search = RandomizedSearchCV(
    RandomForestClassifier(random_state=0, n_jobs=-1),
    space, n_iter=12, cv=5, random_state=0,
).fit(X, y)
print(search.best_params_, round(search.best_score_, 4))
```

**Remember:** Fix the random seed and log every trial, or you cannot reproduce your own best model.

**Common mistake:** Tuning 40 hyperparameters on 400 rows — you are now fitting the validation set.

Practice: open `examples/08_evaluating_on_a_held_out_set.py`, predict the output, change one line, predict again.

## 9. Overfitting on small text datasets

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

Practice: open `examples/09_overfitting_on_small_text_datasets.py`, predict the output, change one line, predict again.

## 10. A ticket classifier walkthrough

Hyperparameters are the settings you choose, not learn. Grid search is exhaustive and wasteful; random search finds good regions faster in high dimensions; Bayesian search learns from previous trials. Always search inside cross-validation.

```python
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
import numpy as np

X, y = load_breast_cancer(return_X_y=True)
space = {
    'n_estimators': [100, 300, 600],
    'max_depth': [None, 4, 8, 16],
    'min_samples_leaf': [1, 2, 4, 8],
}
search = RandomizedSearchCV(
    RandomForestClassifier(random_state=0, n_jobs=-1),
    space, n_iter=12, cv=5, random_state=0,
).fit(X, y)
print(search.best_params_, round(search.best_score_, 4))
```

**Remember:** Fix the random seed and log every trial, or you cannot reproduce your own best model.

**Common mistake:** Tuning 40 hyperparameters on 400 rows — you are now fitting the validation set.

Practice: open `examples/10_a_ticket_classifier_walkthrough.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 129

- Explain **Hugging Face transformers basics** to someone else without notes.
- Explain **AutoTokenizer and AutoModel** to someone else without notes.
- Explain **Adding a classification head** to someone else without notes.
- Explain **Dataset formatting and collation** to someone else without notes.
- Explain **Trainer API vs manual loop** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
