# Day 46 — Linear regression in practice

Today's goal: work through **linear regression in practice** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | When a straight line is the right model |
| 2 | Fitting with scikit-learn |
| 3 | Interpreting coefficients and units |
| 4 | Residual plots and what they reveal |
| 5 | Heteroscedasticity |
| 6 | Polynomial regression |
| 7 | Multicollinearity in real data |
| 8 | Robust regression for outliers |
| 9 | Predicting with confidence intervals |
| 10 | House-price regression walkthrough |

---

## 1. When a straight line is the right model

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

## 2. Fitting with scikit-learn

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

## 3. Interpreting coefficients and units

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

## 4. Residual plots and what they reveal

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

## 5. Heteroscedasticity

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

## 6. Polynomial regression

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

## 7. Multicollinearity in real data

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

## 8. Robust regression for outliers

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

## 9. Predicting with confidence intervals

A p-value is P(data this extreme | nothing is going on). It is not the probability your idea is right. A confidence interval is more useful because it shows effect size and uncertainty together — a 'significant' 0.1% lift may not be worth shipping.

```python
import numpy as np

rng = np.random.default_rng(0)
control = rng.normal(10.0, 2.0, 500)
variant = rng.normal(10.3, 2.0, 500)

diff = variant.mean() - control.mean()
se = np.sqrt(control.var(ddof=1) / 500 + variant.var(ddof=1) / 500)
print(f'lift {diff:.3f}  95% CI [{diff - 1.96 * se:.3f}, {diff + 1.96 * se:.3f}]')
```

**Remember:** Decide the sample size and the metric BEFORE looking at the data.

**Common mistake:** Peeking daily and stopping the test the moment p < 0.05 — that inflates false positives badly.

## 10. House-price regression walkthrough

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

## What you should be able to do after Day 46

- Explain **When a straight line is the right model** to someone else without notes.
- Explain **Fitting with scikit-learn** to someone else without notes.
- Explain **Interpreting coefficients and units** to someone else without notes.
- Explain **Residual plots and what they reveal** to someone else without notes.
- Explain **Heteroscedasticity** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
