# Day 52 — Decision trees

Today's goal: work through **decision trees** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Splitting to increase purity |
| 2 | Gini impurity vs entropy |
| 3 | Information gain |
| 4 | Recursive partitioning |
| 5 | Depth, leaf size and pruning |
| 6 | Handling categorical and missing values |
| 7 | Regression trees |
| 8 | Reading a tree as rules |
| 9 | Instability of single trees |
| 10 | Visualising and exporting a tree |

---

## 1. Splitting to increase purity

A tree asks yes/no questions, splitting to make each side purer. It needs no scaling, handles mixed types, and reads like a flowchart. Left unconstrained it memorises the training set perfectly, so depth and leaf-size limits are mandatory.

```python
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
tree = DecisionTreeClassifier(max_depth=3, min_samples_leaf=5, random_state=0).fit(X, y)
print(export_text(tree, feature_names=load_iris().feature_names))
```

**Remember:** A single unpruned tree is almost always worse than a small forest — but it is readable, which sometimes wins.

**Common mistake:** Trusting a deep tree's feature importances; they are unstable and biased toward high-cardinality columns.

## 2. Gini impurity vs entropy

Entropy measures surprise: a fair coin has 1 bit, a two-headed coin has 0. Cross-entropy measures how surprised your model is by the truth — which is why it is the loss for classifiers and language models. Perplexity is just exp(cross-entropy), read as 'effective number of choices'.

```python
import numpy as np

def cross_entropy(p_true, p_pred, eps=1e-12):
    p_pred = np.clip(p_pred, eps, 1 - eps)
    return -np.sum(p_true * np.log(p_pred))

truth = np.array([0, 1, 0])              # class 1 is correct
confident = np.array([0.05, 0.90, 0.05])
unsure = np.array([0.33, 0.34, 0.33])
print('confident loss', round(cross_entropy(truth, confident), 3))
print('unsure loss   ', round(cross_entropy(truth, unsure), 3))
print('perplexity    ', round(float(np.exp(cross_entropy(truth, unsure))), 3))
```

**Remember:** Clip probabilities before `log` — `log(0)` is `-inf` and poisons the whole batch.

**Common mistake:** Applying softmax twice (once in the model, once in the loss) and getting flat, untrainable gradients.

## 3. Information gain

A tree asks yes/no questions, splitting to make each side purer. It needs no scaling, handles mixed types, and reads like a flowchart. Left unconstrained it memorises the training set perfectly, so depth and leaf-size limits are mandatory.

```python
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
tree = DecisionTreeClassifier(max_depth=3, min_samples_leaf=5, random_state=0).fit(X, y)
print(export_text(tree, feature_names=load_iris().feature_names))
```

**Remember:** A single unpruned tree is almost always worse than a small forest — but it is readable, which sometimes wins.

**Common mistake:** Trusting a deep tree's feature importances; they are unstable and biased toward high-cardinality columns.

## 4. Recursive partitioning

A tree asks yes/no questions, splitting to make each side purer. It needs no scaling, handles mixed types, and reads like a flowchart. Left unconstrained it memorises the training set perfectly, so depth and leaf-size limits are mandatory.

```python
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
tree = DecisionTreeClassifier(max_depth=3, min_samples_leaf=5, random_state=0).fit(X, y)
print(export_text(tree, feature_names=load_iris().feature_names))
```

**Remember:** A single unpruned tree is almost always worse than a small forest — but it is readable, which sometimes wins.

**Common mistake:** Trusting a deep tree's feature importances; they are unstable and biased toward high-cardinality columns.

## 5. Depth, leaf size and pruning

A tree asks yes/no questions, splitting to make each side purer. It needs no scaling, handles mixed types, and reads like a flowchart. Left unconstrained it memorises the training set perfectly, so depth and leaf-size limits are mandatory.

```python
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
tree = DecisionTreeClassifier(max_depth=3, min_samples_leaf=5, random_state=0).fit(X, y)
print(export_text(tree, feature_names=load_iris().feature_names))
```

**Remember:** A single unpruned tree is almost always worse than a small forest — but it is readable, which sometimes wins.

**Common mistake:** Trusting a deep tree's feature importances; they are unstable and biased toward high-cardinality columns.

## 6. Handling categorical and missing values

Missing data is information, not just noise. Before filling anything, ask *why* it is missing: a sensor that fails only under load is not missing at random. Then choose: drop rows, drop the column, fill with a statistic, or add an explicit 'was missing' indicator column.

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'age': [25, np.nan, 40, np.nan]})
print(df.isna().sum())

df['age_missing'] = df['age'].isna().astype(int)   # keep the signal
df['age'] = df['age'].fillna(df['age'].median())    # then fill
print(df)
```

**Remember:** Compute the fill statistic on the TRAIN split only, then apply it to test.

**Common mistake:** Filling with the mean computed over the full dataset — that leaks test information into training.

## 7. Regression trees

A tree asks yes/no questions, splitting to make each side purer. It needs no scaling, handles mixed types, and reads like a flowchart. Left unconstrained it memorises the training set perfectly, so depth and leaf-size limits are mandatory.

```python
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
tree = DecisionTreeClassifier(max_depth=3, min_samples_leaf=5, random_state=0).fit(X, y)
print(export_text(tree, feature_names=load_iris().feature_names))
```

**Remember:** A single unpruned tree is almost always worse than a small forest — but it is readable, which sometimes wins.

**Common mistake:** Trusting a deep tree's feature importances; they are unstable and biased toward high-cardinality columns.

## 8. Reading a tree as rules

A tree asks yes/no questions, splitting to make each side purer. It needs no scaling, handles mixed types, and reads like a flowchart. Left unconstrained it memorises the training set perfectly, so depth and leaf-size limits are mandatory.

```python
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
tree = DecisionTreeClassifier(max_depth=3, min_samples_leaf=5, random_state=0).fit(X, y)
print(export_text(tree, feature_names=load_iris().feature_names))
```

**Remember:** A single unpruned tree is almost always worse than a small forest — but it is readable, which sometimes wins.

**Common mistake:** Trusting a deep tree's feature importances; they are unstable and biased toward high-cardinality columns.

## 9. Instability of single trees

A tree asks yes/no questions, splitting to make each side purer. It needs no scaling, handles mixed types, and reads like a flowchart. Left unconstrained it memorises the training set perfectly, so depth and leaf-size limits are mandatory.

```python
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
tree = DecisionTreeClassifier(max_depth=3, min_samples_leaf=5, random_state=0).fit(X, y)
print(export_text(tree, feature_names=load_iris().feature_names))
```

**Remember:** A single unpruned tree is almost always worse than a small forest — but it is readable, which sometimes wins.

**Common mistake:** Trusting a deep tree's feature importances; they are unstable and biased toward high-cardinality columns.

## 10. Visualising and exporting a tree

A tree asks yes/no questions, splitting to make each side purer. It needs no scaling, handles mixed types, and reads like a flowchart. Left unconstrained it memorises the training set perfectly, so depth and leaf-size limits are mandatory.

```python
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
tree = DecisionTreeClassifier(max_depth=3, min_samples_leaf=5, random_state=0).fit(X, y)
print(export_text(tree, feature_names=load_iris().feature_names))
```

**Remember:** A single unpruned tree is almost always worse than a small forest — but it is readable, which sometimes wins.

**Common mistake:** Trusting a deep tree's feature importances; they are unstable and biased toward high-cardinality columns.

---

## What you should be able to do after Day 52

- Explain **Splitting to increase purity** to someone else without notes.
- Explain **Gini impurity vs entropy** to someone else without notes.
- Explain **Information gain** to someone else without notes.
- Explain **Recursive partitioning** to someone else without notes.
- Explain **Depth, leaf size and pruning** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
