# Day 49 — Regression metrics and residuals

Today's goal: work through **regression metrics and residuals** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | MAE and its interpretation |
| 2 | MSE and RMSE |
| 3 | R-squared and adjusted R-squared |
| 4 | MAPE and its zero problem |
| 5 | Choosing a metric from the cost of error |
| 6 | Baseline: predicting the mean |
| 7 | Residual analysis |
| 8 | Error distribution by segment |
| 9 | Prediction intervals |
| 10 | Reporting results without overclaiming |

---

## 1. MAE and its interpretation

Linear regression fits a straight line by minimising squared error. It is the honest baseline for every regression problem: fast, interpretable, and the thing your fancy model must beat before it earns its complexity.

```python
import numpy as np

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 1))
y = 3.0 * X[:, 0] + 2.0 + rng.normal(scale=0.5, size=200)

Xb = np.c_[np.ones(len(X)), X]                 # add bias column
w = np.linalg.lstsq(Xb, y, rcond=None)[0]      # solves the normal equations safely
print(f'intercept {w[0]:.3f}  slope {w[1]:.3f}')

resid = y - Xb @ w
print('residual mean (should be ~0):', round(float(resid.mean()), 6))
```

**Remember:** Plot residuals against predictions — any visible pattern means the linear form is wrong.

**Common mistake:** Reporting R² on training data and calling it model performance.

## 2. MSE and RMSE

Linear regression fits a straight line by minimising squared error. It is the honest baseline for every regression problem: fast, interpretable, and the thing your fancy model must beat before it earns its complexity.

```python
import numpy as np

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 1))
y = 3.0 * X[:, 0] + 2.0 + rng.normal(scale=0.5, size=200)

Xb = np.c_[np.ones(len(X)), X]                 # add bias column
w = np.linalg.lstsq(Xb, y, rcond=None)[0]      # solves the normal equations safely
print(f'intercept {w[0]:.3f}  slope {w[1]:.3f}')

resid = y - Xb @ w
print('residual mean (should be ~0):', round(float(resid.mean()), 6))
```

**Remember:** Plot residuals against predictions — any visible pattern means the linear form is wrong.

**Common mistake:** Reporting R² on training data and calling it model performance.

## 3. R-squared and adjusted R-squared

Linear regression fits a straight line by minimising squared error. It is the honest baseline for every regression problem: fast, interpretable, and the thing your fancy model must beat before it earns its complexity.

```python
import numpy as np

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 1))
y = 3.0 * X[:, 0] + 2.0 + rng.normal(scale=0.5, size=200)

Xb = np.c_[np.ones(len(X)), X]                 # add bias column
w = np.linalg.lstsq(Xb, y, rcond=None)[0]      # solves the normal equations safely
print(f'intercept {w[0]:.3f}  slope {w[1]:.3f}')

resid = y - Xb @ w
print('residual mean (should be ~0):', round(float(resid.mean()), 6))
```

**Remember:** Plot residuals against predictions — any visible pattern means the linear form is wrong.

**Common mistake:** Reporting R² on training data and calling it model performance.

## 4. MAPE and its zero problem

Linear regression fits a straight line by minimising squared error. It is the honest baseline for every regression problem: fast, interpretable, and the thing your fancy model must beat before it earns its complexity.

```python
import numpy as np

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 1))
y = 3.0 * X[:, 0] + 2.0 + rng.normal(scale=0.5, size=200)

Xb = np.c_[np.ones(len(X)), X]                 # add bias column
w = np.linalg.lstsq(Xb, y, rcond=None)[0]      # solves the normal equations safely
print(f'intercept {w[0]:.3f}  slope {w[1]:.3f}')

resid = y - Xb @ w
print('residual mean (should be ~0):', round(float(resid.mean()), 6))
```

**Remember:** Plot residuals against predictions — any visible pattern means the linear form is wrong.

**Common mistake:** Reporting R² on training data and calling it model performance.

## 5. Choosing a metric from the cost of error

Linear regression fits a straight line by minimising squared error. It is the honest baseline for every regression problem: fast, interpretable, and the thing your fancy model must beat before it earns its complexity.

```python
import numpy as np

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 1))
y = 3.0 * X[:, 0] + 2.0 + rng.normal(scale=0.5, size=200)

Xb = np.c_[np.ones(len(X)), X]                 # add bias column
w = np.linalg.lstsq(Xb, y, rcond=None)[0]      # solves the normal equations safely
print(f'intercept {w[0]:.3f}  slope {w[1]:.3f}')

resid = y - Xb @ w
print('residual mean (should be ~0):', round(float(resid.mean()), 6))
```

**Remember:** Plot residuals against predictions — any visible pattern means the linear form is wrong.

**Common mistake:** Reporting R² on training data and calling it model performance.

## 6. Baseline: predicting the mean

The mean is pulled around by outliers; the median is not. Report both, plus a spread measure. When mean and median disagree sharply, the distribution is skewed and averages are lying to you.

```python
import numpy as np

salaries = np.array([30, 32, 35, 33, 31, 900])   # one founder
print('mean  ', salaries.mean())     # 176.8 — misleading
print('median', np.median(salaries)) # 32.5  — honest
print('p95   ', np.percentile(salaries, 95))

q1, q3 = np.percentile(salaries, [25, 75])
iqr = q3 - q1
print('outliers', salaries[(salaries < q1 - 1.5 * iqr) | (salaries > q3 + 1.5 * iqr)])
```

**Remember:** Quote median + IQR for skewed data, mean + std only for roughly symmetric data.

**Common mistake:** Removing 'outliers' automatically when they are the exact events you were hired to predict.

## 7. Residual analysis

Linear regression fits a straight line by minimising squared error. It is the honest baseline for every regression problem: fast, interpretable, and the thing your fancy model must beat before it earns its complexity.

```python
import numpy as np

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 1))
y = 3.0 * X[:, 0] + 2.0 + rng.normal(scale=0.5, size=200)

Xb = np.c_[np.ones(len(X)), X]                 # add bias column
w = np.linalg.lstsq(Xb, y, rcond=None)[0]      # solves the normal equations safely
print(f'intercept {w[0]:.3f}  slope {w[1]:.3f}')

resid = y - Xb @ w
print('residual mean (should be ~0):', round(float(resid.mean()), 6))
```

**Remember:** Plot residuals against predictions — any visible pattern means the linear form is wrong.

**Common mistake:** Reporting R² on training data and calling it model performance.

## 8. Error distribution by segment

A distribution says which values are likely. Gaussian for measurement noise, Bernoulli for yes/no, Poisson for counts per interval. Choosing the right one is choosing your loss function: Gaussian likelihood gives MSE, Bernoulli gives cross-entropy.

```python
import numpy as np

rng = np.random.default_rng(0)
normal = rng.normal(loc=0, scale=1, size=10_000)
coin = rng.binomial(n=1, p=0.3, size=10_000)

print('normal mean/std', round(normal.mean(), 3), round(normal.std(), 3))
print('coin heads rate ', coin.mean())
```

**Remember:** Always seed your RNG (`default_rng(0)`) when you want a result someone else can reproduce.

**Common mistake:** Assuming Gaussian for skewed, bounded, or count data and then being surprised by the residuals.

## 9. Prediction intervals

Linear regression fits a straight line by minimising squared error. It is the honest baseline for every regression problem: fast, interpretable, and the thing your fancy model must beat before it earns its complexity.

```python
import numpy as np

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 1))
y = 3.0 * X[:, 0] + 2.0 + rng.normal(scale=0.5, size=200)

Xb = np.c_[np.ones(len(X)), X]                 # add bias column
w = np.linalg.lstsq(Xb, y, rcond=None)[0]      # solves the normal equations safely
print(f'intercept {w[0]:.3f}  slope {w[1]:.3f}')

resid = y - Xb @ w
print('residual mean (should be ~0):', round(float(resid.mean()), 6))
```

**Remember:** Plot residuals against predictions — any visible pattern means the linear form is wrong.

**Common mistake:** Reporting R² on training data and calling it model performance.

## 10. Reporting results without overclaiming

Linear regression fits a straight line by minimising squared error. It is the honest baseline for every regression problem: fast, interpretable, and the thing your fancy model must beat before it earns its complexity.

```python
import numpy as np

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 1))
y = 3.0 * X[:, 0] + 2.0 + rng.normal(scale=0.5, size=200)

Xb = np.c_[np.ones(len(X)), X]                 # add bias column
w = np.linalg.lstsq(Xb, y, rcond=None)[0]      # solves the normal equations safely
print(f'intercept {w[0]:.3f}  slope {w[1]:.3f}')

resid = y - Xb @ w
print('residual mean (should be ~0):', round(float(resid.mean()), 6))
```

**Remember:** Plot residuals against predictions — any visible pattern means the linear form is wrong.

**Common mistake:** Reporting R² on training data and calling it model performance.

---

## What you should be able to do after Day 49

- Explain **MAE and its interpretation** to someone else without notes.
- Explain **MSE and RMSE** to someone else without notes.
- Explain **R-squared and adjusted R-squared** to someone else without notes.
- Explain **MAPE and its zero problem** to someone else without notes.
- Explain **Choosing a metric from the cost of error** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
