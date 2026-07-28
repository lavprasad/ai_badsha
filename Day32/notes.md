# Day 32 — Logistic regression, mathematically

Today's goal: work through **Logistic regression, mathematically** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | From linear score to probability |
| 2 | The sigmoid and the logit |
| 3 | Odds and log-odds interpretation |
| 4 | Maximum likelihood for Bernoulli data |
| 5 | Deriving the cross-entropy loss |
| 6 | The gradient of logistic loss |
| 7 | Decision boundaries |
| 8 | Multiclass with softmax |
| 9 | Regularised logistic regression |
| 10 | Implementing it from scratch |

---

## 1. From linear score to probability

Bayes' rule updates a belief with evidence: posterior = likelihood x prior / evidence. The most common mistake in applied ML is ignoring the prior — a 99%-accurate test for a 1-in-10000 disease still gives mostly false positives.

```python
prior = 1 / 10_000          # base rate of the disease
sensitivity = 0.99          # P(positive | sick)
false_positive = 0.01       # P(positive | healthy)

evidence = sensitivity * prior + false_positive * (1 - prior)
posterior = sensitivity * prior / evidence
print(f'P(sick | positive) = {posterior:.4f}')   # ~0.0098
```

**Remember:** Rare events make precision collapse no matter how good the classifier looks on accuracy.

**Common mistake:** Reporting accuracy on an imbalanced problem where predicting 'no' always scores 99%.

Practice: open `examples/01_from_linear_score_to_probability.py`, predict the output, change one line, predict again.

## 2. The sigmoid and the logit

Logistic regression squashes a linear score through a sigmoid to get a probability. The coefficients are log-odds: +0.7 means the odds roughly double per unit. It stays the default for anything where you must explain the decision to a regulator.

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

**Remember:** Clip the sigmoid input — `exp` of a large negative number overflows and returns NaN.

**Common mistake:** Reading the raw output as a calibrated probability without ever checking a calibration curve.

Practice: open `examples/02_the_sigmoid_and_the_logit.py`, predict the output, change one line, predict again.

## 3. Odds and log-odds interpretation

Logistic regression squashes a linear score through a sigmoid to get a probability. The coefficients are log-odds: +0.7 means the odds roughly double per unit. It stays the default for anything where you must explain the decision to a regulator.

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

**Remember:** Clip the sigmoid input — `exp` of a large negative number overflows and returns NaN.

**Common mistake:** Reading the raw output as a calibrated probability without ever checking a calibration curve.

Practice: open `examples/03_odds_and_log_odds_interpretation.py`, predict the output, change one line, predict again.

## 4. Maximum likelihood for Bernoulli data

Bayes' rule updates a belief with evidence: posterior = likelihood x prior / evidence. The most common mistake in applied ML is ignoring the prior — a 99%-accurate test for a 1-in-10000 disease still gives mostly false positives.

```python
prior = 1 / 10_000          # base rate of the disease
sensitivity = 0.99          # P(positive | sick)
false_positive = 0.01       # P(positive | healthy)

evidence = sensitivity * prior + false_positive * (1 - prior)
posterior = sensitivity * prior / evidence
print(f'P(sick | positive) = {posterior:.4f}')   # ~0.0098
```

**Remember:** Rare events make precision collapse no matter how good the classifier looks on accuracy.

**Common mistake:** Reporting accuracy on an imbalanced problem where predicting 'no' always scores 99%.

Practice: open `examples/04_maximum_likelihood_for_bernoulli_data.py`, predict the output, change one line, predict again.

## 5. Deriving the cross-entropy loss

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

Practice: open `examples/05_deriving_the_cross_entropy_loss.py`, predict the output, change one line, predict again.

## 6. The gradient of logistic loss

The derivative answers: if I nudge this input a little, how much does the output move? The gradient is that answer for every input at once, so it points uphill. Training walks downhill by stepping against the gradient. The chain rule is what lets you propagate that answer through a stack of layers.

```python
import numpy as np

def f(x):
    return x ** 2 + 3 * x

def numeric_grad(fn, x, h=1e-6):
    return (fn(x + h) - fn(x - h)) / (2 * h)

x = 2.0
print('numeric  ', numeric_grad(f, x))
print('analytic ', 2 * x + 3)   # should match to ~1e-6
```

**Remember:** A central difference `(f(x+h)-f(x-h))/2h` is the cheapest way to check a hand-written gradient.

**Common mistake:** Trusting a derivation you never gradient-checked; a sign error trains slowly instead of failing loudly.

Practice: open `examples/06_the_gradient_of_logistic_loss.py`, predict the output, change one line, predict again.

## 7. Decision boundaries

Logistic regression squashes a linear score through a sigmoid to get a probability. The coefficients are log-odds: +0.7 means the odds roughly double per unit. It stays the default for anything where you must explain the decision to a regulator.

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

**Remember:** Clip the sigmoid input — `exp` of a large negative number overflows and returns NaN.

**Common mistake:** Reading the raw output as a calibrated probability without ever checking a calibration curve.

Practice: open `examples/07_decision_boundaries.py`, predict the output, change one line, predict again.

## 8. Multiclass with softmax

Logistic regression squashes a linear score through a sigmoid to get a probability. The coefficients are log-odds: +0.7 means the odds roughly double per unit. It stays the default for anything where you must explain the decision to a regulator.

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

**Remember:** Clip the sigmoid input — `exp` of a large negative number overflows and returns NaN.

**Common mistake:** Reading the raw output as a calibrated probability without ever checking a calibration curve.

Practice: open `examples/08_multiclass_with_softmax.py`, predict the output, change one line, predict again.

## 9. Regularised logistic regression

Logistic regression squashes a linear score through a sigmoid to get a probability. The coefficients are log-odds: +0.7 means the odds roughly double per unit. It stays the default for anything where you must explain the decision to a regulator.

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

**Remember:** Clip the sigmoid input — `exp` of a large negative number overflows and returns NaN.

**Common mistake:** Reading the raw output as a calibrated probability without ever checking a calibration curve.

Practice: open `examples/09_regularised_logistic_regression.py`, predict the output, change one line, predict again.

## 10. Implementing it from scratch

Logistic regression squashes a linear score through a sigmoid to get a probability. The coefficients are log-odds: +0.7 means the odds roughly double per unit. It stays the default for anything where you must explain the decision to a regulator.

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

**Remember:** Clip the sigmoid input — `exp` of a large negative number overflows and returns NaN.

**Common mistake:** Reading the raw output as a calibrated probability without ever checking a calibration curve.

Practice: open `examples/10_implementing_it_from_scratch.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 32

- Explain **From linear score to probability** to someone else without notes.
- Explain **The sigmoid and the logit** to someone else without notes.
- Explain **Odds and log-odds interpretation** to someone else without notes.
- Explain **Maximum likelihood for Bernoulli data** to someone else without notes.
- Explain **Deriving the cross-entropy loss** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
