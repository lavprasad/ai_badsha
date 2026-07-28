# Day 72 — Debugging a model that will not learn

Today's goal: work through **Debugging a model that will not learn** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Check the data before the model |
| 2 | Verify labels and their alignment |
| 3 | Overfit a tiny subset deliberately |
| 4 | Check for constant or leaky features |
| 5 | Inspect the loss curve |
| 6 | Compare against the dummy baseline |
| 7 | Look at the worst predictions by hand |
| 8 | Check the split for contamination |
| 9 | Simplify until it works, then rebuild |
| 10 | A systematic debugging checklist |

---

## 1. Check the data before the model

Debug in a fixed order, cheapest test first. Can the model overfit 20 rows to zero loss? If not, the bug is in the data or the wiring, not the capacity. Is the loss at step zero what random guessing predicts? If not, the labels or the output layer are wrong.

```python
import numpy as np

def sanity_report(X, y, n_classes):
    print('shapes        ', X.shape, y.shape)
    print('nan in X      ', bool(np.isnan(X).any()))
    const = [i for i in range(X.shape[1]) if np.std(X[:, i]) == 0]
    print('constant cols ', const)
    counts = np.bincount(y, minlength=n_classes)
    print('class counts  ', counts)
    print('expected loss at init ~', round(float(np.log(n_classes)), 4))

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 5)); X[:, 2] = 1.0     # planted constant column
sanity_report(X, rng.integers(0, 3, 200), 3)
```

**Remember:** Expected cross-entropy at initialisation is ln(n_classes). A different value means a wiring bug.

**Common mistake:** Tuning hyperparameters for two days on a pipeline whose labels were misaligned by one row.

Practice: open `examples/01_check_the_data_before_the_model.py`, predict the output, change one line, predict again.

## 2. Verify labels and their alignment

After supervised tuning, models are aligned to human preference. RLHF trains a reward model on human comparisons, then optimises against it with PPO. DPO skips the reward model and optimises preference pairs directly — simpler, cheaper, and now the common choice.

```python
import numpy as np

# DPO intuition: raise logprob of the chosen reply relative to the rejected one,
# while a KL term keeps you near the reference model.
policy = {'chosen': -2.0, 'rejected': -2.5}     # log-probs under the trained model
ref = {'chosen': -2.4, 'rejected': -2.3}        # log-probs under the frozen reference
beta = 0.1

margin = beta * ((policy['chosen'] - ref['chosen']) - (policy['rejected'] - ref['rejected']))
loss = -np.log(1 / (1 + np.exp(-margin)))
print(f'margin {margin:.4f}  dpo loss {loss:.4f}')
```

**Remember:** Alignment optimises a proxy for what humans want; the proxy can always be gamed.

**Common mistake:** Over-optimising the reward model until outputs are sycophantic and useless — classic reward hacking.

Practice: open `examples/02_verify_labels_and_their_alignment.py`, predict the output, change one line, predict again.

## 3. Overfit a tiny subset deliberately

Debug in a fixed order, cheapest test first. Can the model overfit 20 rows to zero loss? If not, the bug is in the data or the wiring, not the capacity. Is the loss at step zero what random guessing predicts? If not, the labels or the output layer are wrong.

```python
import numpy as np

def sanity_report(X, y, n_classes):
    print('shapes        ', X.shape, y.shape)
    print('nan in X      ', bool(np.isnan(X).any()))
    const = [i for i in range(X.shape[1]) if np.std(X[:, i]) == 0]
    print('constant cols ', const)
    counts = np.bincount(y, minlength=n_classes)
    print('class counts  ', counts)
    print('expected loss at init ~', round(float(np.log(n_classes)), 4))

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 5)); X[:, 2] = 1.0     # planted constant column
sanity_report(X, rng.integers(0, 3, 200), 3)
```

**Remember:** Expected cross-entropy at initialisation is ln(n_classes). A different value means a wiring bug.

**Common mistake:** Tuning hyperparameters for two days on a pipeline whose labels were misaligned by one row.

Practice: open `examples/03_overfit_a_tiny_subset_deliberately.py`, predict the output, change one line, predict again.

## 4. Check for constant or leaky features

Debug in a fixed order, cheapest test first. Can the model overfit 20 rows to zero loss? If not, the bug is in the data or the wiring, not the capacity. Is the loss at step zero what random guessing predicts? If not, the labels or the output layer are wrong.

```python
import numpy as np

def sanity_report(X, y, n_classes):
    print('shapes        ', X.shape, y.shape)
    print('nan in X      ', bool(np.isnan(X).any()))
    const = [i for i in range(X.shape[1]) if np.std(X[:, i]) == 0]
    print('constant cols ', const)
    counts = np.bincount(y, minlength=n_classes)
    print('class counts  ', counts)
    print('expected loss at init ~', round(float(np.log(n_classes)), 4))

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 5)); X[:, 2] = 1.0     # planted constant column
sanity_report(X, rng.integers(0, 3, 200), 3)
```

**Remember:** Expected cross-entropy at initialisation is ln(n_classes). A different value means a wiring bug.

**Common mistake:** Tuning hyperparameters for two days on a pipeline whose labels were misaligned by one row.

Practice: open `examples/04_check_for_constant_or_leaky_features.py`, predict the output, change one line, predict again.

## 5. Inspect the loss curve

Debug in a fixed order, cheapest test first. Can the model overfit 20 rows to zero loss? If not, the bug is in the data or the wiring, not the capacity. Is the loss at step zero what random guessing predicts? If not, the labels or the output layer are wrong.

```python
import numpy as np

def sanity_report(X, y, n_classes):
    print('shapes        ', X.shape, y.shape)
    print('nan in X      ', bool(np.isnan(X).any()))
    const = [i for i in range(X.shape[1]) if np.std(X[:, i]) == 0]
    print('constant cols ', const)
    counts = np.bincount(y, minlength=n_classes)
    print('class counts  ', counts)
    print('expected loss at init ~', round(float(np.log(n_classes)), 4))

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 5)); X[:, 2] = 1.0     # planted constant column
sanity_report(X, rng.integers(0, 3, 200), 3)
```

**Remember:** Expected cross-entropy at initialisation is ln(n_classes). A different value means a wiring bug.

**Common mistake:** Tuning hyperparameters for two days on a pipeline whose labels were misaligned by one row.

Practice: open `examples/05_inspect_the_loss_curve.py`, predict the output, change one line, predict again.

## 6. Compare against the dummy baseline

Every scikit-learn model has the same three methods, which means swapping algorithms is a one-line change. Start every problem with `DummyClassifier` — if your real model cannot beat 'always predict the majority class' by a clear margin, something is wrong with the data, not the model.

```python
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, stratify=y, random_state=0)

baseline = DummyClassifier(strategy='most_frequent').fit(Xtr, ytr)
model = RandomForestClassifier(n_estimators=200, random_state=0).fit(Xtr, ytr)
print(f'dummy {baseline.score(Xte, yte):.3f}   model {model.score(Xte, yte):.3f}')
```

**Remember:** Report your model's score next to the dummy's. A number alone means nothing.

**Common mistake:** Celebrating 92% accuracy on data where 91% of rows are one class.

Practice: open `examples/06_compare_against_the_dummy_baseline.py`, predict the output, change one line, predict again.

## 7. Look at the worst predictions by hand

Debug in a fixed order, cheapest test first. Can the model overfit 20 rows to zero loss? If not, the bug is in the data or the wiring, not the capacity. Is the loss at step zero what random guessing predicts? If not, the labels or the output layer are wrong.

```python
import numpy as np

def sanity_report(X, y, n_classes):
    print('shapes        ', X.shape, y.shape)
    print('nan in X      ', bool(np.isnan(X).any()))
    const = [i for i in range(X.shape[1]) if np.std(X[:, i]) == 0]
    print('constant cols ', const)
    counts = np.bincount(y, minlength=n_classes)
    print('class counts  ', counts)
    print('expected loss at init ~', round(float(np.log(n_classes)), 4))

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 5)); X[:, 2] = 1.0     # planted constant column
sanity_report(X, rng.integers(0, 3, 200), 3)
```

**Remember:** Expected cross-entropy at initialisation is ln(n_classes). A different value means a wiring bug.

**Common mistake:** Tuning hyperparameters for two days on a pipeline whose labels were misaligned by one row.

Practice: open `examples/07_look_at_the_worst_predictions_by_hand.py`, predict the output, change one line, predict again.

## 8. Check the split for contamination

Debug in a fixed order, cheapest test first. Can the model overfit 20 rows to zero loss? If not, the bug is in the data or the wiring, not the capacity. Is the loss at step zero what random guessing predicts? If not, the labels or the output layer are wrong.

```python
import numpy as np

def sanity_report(X, y, n_classes):
    print('shapes        ', X.shape, y.shape)
    print('nan in X      ', bool(np.isnan(X).any()))
    const = [i for i in range(X.shape[1]) if np.std(X[:, i]) == 0]
    print('constant cols ', const)
    counts = np.bincount(y, minlength=n_classes)
    print('class counts  ', counts)
    print('expected loss at init ~', round(float(np.log(n_classes)), 4))

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 5)); X[:, 2] = 1.0     # planted constant column
sanity_report(X, rng.integers(0, 3, 200), 3)
```

**Remember:** Expected cross-entropy at initialisation is ln(n_classes). A different value means a wiring bug.

**Common mistake:** Tuning hyperparameters for two days on a pipeline whose labels were misaligned by one row.

Practice: open `examples/08_check_the_split_for_contamination.py`, predict the output, change one line, predict again.

## 9. Simplify until it works, then rebuild

Projects are where the learning sticks. Build a thin end-to-end slice first — load data, train something dumb, evaluate, serve one prediction — then improve one layer at a time. A working baseline on day one beats a perfect model that never ships.

```python
STEPS = [
    '1. Define the decision the model supports and the metric that measures it',
    '2. Get the data; write the loader; assert the schema',
    '3. Dumb baseline (mean / majority class) -> this is the bar',
    '4. Simple model + honest validation split',
    '5. Error analysis: look at 30 wrong predictions by hand',
    '6. Improve the biggest error bucket, not the leaderboard',
    '7. Serve it, log inputs and outputs, monitor drift',
]
for s in STEPS:
    print(s)
```

**Remember:** Spend an hour looking at wrong predictions before you spend a day tuning hyperparameters.

**Common mistake:** Six weeks of feature engineering with no baseline to prove any of it helped.

Practice: open `examples/09_simplify_until_it_works_then_rebuild.py`, predict the output, change one line, predict again.

## 10. A systematic debugging checklist

Debug in a fixed order, cheapest test first. Can the model overfit 20 rows to zero loss? If not, the bug is in the data or the wiring, not the capacity. Is the loss at step zero what random guessing predicts? If not, the labels or the output layer are wrong.

```python
import numpy as np

def sanity_report(X, y, n_classes):
    print('shapes        ', X.shape, y.shape)
    print('nan in X      ', bool(np.isnan(X).any()))
    const = [i for i in range(X.shape[1]) if np.std(X[:, i]) == 0]
    print('constant cols ', const)
    counts = np.bincount(y, minlength=n_classes)
    print('class counts  ', counts)
    print('expected loss at init ~', round(float(np.log(n_classes)), 4))

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 5)); X[:, 2] = 1.0     # planted constant column
sanity_report(X, rng.integers(0, 3, 200), 3)
```

**Remember:** Expected cross-entropy at initialisation is ln(n_classes). A different value means a wiring bug.

**Common mistake:** Tuning hyperparameters for two days on a pipeline whose labels were misaligned by one row.

Practice: open `examples/10_a_systematic_debugging_checklist.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 72

- Explain **Check the data before the model** to someone else without notes.
- Explain **Verify labels and their alignment** to someone else without notes.
- Explain **Overfit a tiny subset deliberately** to someone else without notes.
- Explain **Check for constant or leaky features** to someone else without notes.
- Explain **Inspect the loss curve** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
