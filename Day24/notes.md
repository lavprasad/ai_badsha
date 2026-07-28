# Day 24 — Inferential statistics

Today's goal: work through **Inferential statistics** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Population vs sample |
| 2 | Sampling distributions and standard error |
| 3 | Confidence intervals |
| 4 | Null and alternative hypotheses |
| 5 | p-values and what they are not |
| 6 | t-test and chi-square test |
| 7 | Type I and Type II errors |
| 8 | Statistical power and sample size |
| 9 | Multiple comparisons and correction |
| 10 | Bootstrapping without formulas |

---

## 1. Population vs sample

You measure a sample and want to claim something about a population. Type I error is crying wolf; Type II is missing a real effect. Power is your chance of detecting a real effect of a given size — decide it before collecting data, or you will run an experiment that could never have succeeded.

```python
import numpy as np

rng = np.random.default_rng(0)
a = rng.normal(10.0, 2.0, 60)
b = rng.normal(11.0, 2.0, 60)

# Welch t-statistic, no scipy needed
se = np.sqrt(a.var(ddof=1) / len(a) + b.var(ddof=1) / len(b))
t = (b.mean() - a.mean()) / se
print(f'mean diff {b.mean() - a.mean():.3f}  t = {t:.2f}')
print('|t| > 2 is roughly the 5% threshold at these sample sizes')

# Twenty independent tests at 5%: expect one false positive by chance alone
print('expected false positives in 20 tests:', 20 * 0.05)
```

**Remember:** Testing 20 hypotheses at p<0.05 gives you one false positive on average. Correct for it.

**Common mistake:** Slicing the data 15 ways after the fact and reporting the one slice that reached significance.

Practice: open `examples/01_population_vs_sample.py`, predict the output, change one line, predict again.

## 2. Sampling distributions and standard error

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

Practice: open `examples/02_sampling_distributions_and_standard_erro.py`, predict the output, change one line, predict again.

## 3. Confidence intervals

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

Practice: open `examples/03_confidence_intervals.py`, predict the output, change one line, predict again.

## 4. Null and alternative hypotheses

You measure a sample and want to claim something about a population. Type I error is crying wolf; Type II is missing a real effect. Power is your chance of detecting a real effect of a given size — decide it before collecting data, or you will run an experiment that could never have succeeded.

```python
import numpy as np

rng = np.random.default_rng(0)
a = rng.normal(10.0, 2.0, 60)
b = rng.normal(11.0, 2.0, 60)

# Welch t-statistic, no scipy needed
se = np.sqrt(a.var(ddof=1) / len(a) + b.var(ddof=1) / len(b))
t = (b.mean() - a.mean()) / se
print(f'mean diff {b.mean() - a.mean():.3f}  t = {t:.2f}')
print('|t| > 2 is roughly the 5% threshold at these sample sizes')

# Twenty independent tests at 5%: expect one false positive by chance alone
print('expected false positives in 20 tests:', 20 * 0.05)
```

**Remember:** Testing 20 hypotheses at p<0.05 gives you one false positive on average. Correct for it.

**Common mistake:** Slicing the data 15 ways after the fact and reporting the one slice that reached significance.

Practice: open `examples/04_null_and_alternative_hypotheses.py`, predict the output, change one line, predict again.

## 5. p-values and what they are not

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

Practice: open `examples/05_p_values_and_what_they_are_not.py`, predict the output, change one line, predict again.

## 6. t-test and chi-square test

You measure a sample and want to claim something about a population. Type I error is crying wolf; Type II is missing a real effect. Power is your chance of detecting a real effect of a given size — decide it before collecting data, or you will run an experiment that could never have succeeded.

```python
import numpy as np

rng = np.random.default_rng(0)
a = rng.normal(10.0, 2.0, 60)
b = rng.normal(11.0, 2.0, 60)

# Welch t-statistic, no scipy needed
se = np.sqrt(a.var(ddof=1) / len(a) + b.var(ddof=1) / len(b))
t = (b.mean() - a.mean()) / se
print(f'mean diff {b.mean() - a.mean():.3f}  t = {t:.2f}')
print('|t| > 2 is roughly the 5% threshold at these sample sizes')

# Twenty independent tests at 5%: expect one false positive by chance alone
print('expected false positives in 20 tests:', 20 * 0.05)
```

**Remember:** Testing 20 hypotheses at p<0.05 gives you one false positive on average. Correct for it.

**Common mistake:** Slicing the data 15 ways after the fact and reporting the one slice that reached significance.

Practice: open `examples/06_t_test_and_chi_square_test.py`, predict the output, change one line, predict again.

## 7. Type I and Type II errors

You measure a sample and want to claim something about a population. Type I error is crying wolf; Type II is missing a real effect. Power is your chance of detecting a real effect of a given size — decide it before collecting data, or you will run an experiment that could never have succeeded.

```python
import numpy as np

rng = np.random.default_rng(0)
a = rng.normal(10.0, 2.0, 60)
b = rng.normal(11.0, 2.0, 60)

# Welch t-statistic, no scipy needed
se = np.sqrt(a.var(ddof=1) / len(a) + b.var(ddof=1) / len(b))
t = (b.mean() - a.mean()) / se
print(f'mean diff {b.mean() - a.mean():.3f}  t = {t:.2f}')
print('|t| > 2 is roughly the 5% threshold at these sample sizes')

# Twenty independent tests at 5%: expect one false positive by chance alone
print('expected false positives in 20 tests:', 20 * 0.05)
```

**Remember:** Testing 20 hypotheses at p<0.05 gives you one false positive on average. Correct for it.

**Common mistake:** Slicing the data 15 ways after the fact and reporting the one slice that reached significance.

Practice: open `examples/07_type_i_and_type_ii_errors.py`, predict the output, change one line, predict again.

## 8. Statistical power and sample size

You measure a sample and want to claim something about a population. Type I error is crying wolf; Type II is missing a real effect. Power is your chance of detecting a real effect of a given size — decide it before collecting data, or you will run an experiment that could never have succeeded.

```python
import numpy as np

rng = np.random.default_rng(0)
a = rng.normal(10.0, 2.0, 60)
b = rng.normal(11.0, 2.0, 60)

# Welch t-statistic, no scipy needed
se = np.sqrt(a.var(ddof=1) / len(a) + b.var(ddof=1) / len(b))
t = (b.mean() - a.mean()) / se
print(f'mean diff {b.mean() - a.mean():.3f}  t = {t:.2f}')
print('|t| > 2 is roughly the 5% threshold at these sample sizes')

# Twenty independent tests at 5%: expect one false positive by chance alone
print('expected false positives in 20 tests:', 20 * 0.05)
```

**Remember:** Testing 20 hypotheses at p<0.05 gives you one false positive on average. Correct for it.

**Common mistake:** Slicing the data 15 ways after the fact and reporting the one slice that reached significance.

Practice: open `examples/08_statistical_power_and_sample_size.py`, predict the output, change one line, predict again.

## 9. Multiple comparisons and correction

You measure a sample and want to claim something about a population. Type I error is crying wolf; Type II is missing a real effect. Power is your chance of detecting a real effect of a given size — decide it before collecting data, or you will run an experiment that could never have succeeded.

```python
import numpy as np

rng = np.random.default_rng(0)
a = rng.normal(10.0, 2.0, 60)
b = rng.normal(11.0, 2.0, 60)

# Welch t-statistic, no scipy needed
se = np.sqrt(a.var(ddof=1) / len(a) + b.var(ddof=1) / len(b))
t = (b.mean() - a.mean()) / se
print(f'mean diff {b.mean() - a.mean():.3f}  t = {t:.2f}')
print('|t| > 2 is roughly the 5% threshold at these sample sizes')

# Twenty independent tests at 5%: expect one false positive by chance alone
print('expected false positives in 20 tests:', 20 * 0.05)
```

**Remember:** Testing 20 hypotheses at p<0.05 gives you one false positive on average. Correct for it.

**Common mistake:** Slicing the data 15 ways after the fact and reporting the one slice that reached significance.

Practice: open `examples/09_multiple_comparisons_and_correction.py`, predict the output, change one line, predict again.

## 10. Bootstrapping without formulas

Bagging trains many trees on bootstrap samples with random feature subsets, then averages. Averaging cancels the variance that makes single trees erratic. Random forests are the best default for tabular data when you want something that works with almost no tuning.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score

X, y = load_breast_cancer(return_X_y=True)
rf = RandomForestClassifier(n_estimators=300, min_samples_leaf=2, n_jobs=-1, random_state=0)
print('cv accuracy', cross_val_score(rf, X, y, cv=5).mean().round(4))

rf.fit(X, y)
top = sorted(zip(load_breast_cancer().feature_names, rf.feature_importances_), key=lambda t: -t[1])[:5]
print('top features', [(n, round(v, 3)) for n, v in top])
```

**Remember:** More trees never overfit — they only cost time. Depth and leaf size are the knobs that control fit.

**Common mistake:** Using impurity-based importances for business decisions instead of permutation importance.

Practice: open `examples/10_bootstrapping_without_formulas.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 24

- Explain **Population vs sample** to someone else without notes.
- Explain **Sampling distributions and standard error** to someone else without notes.
- Explain **Confidence intervals** to someone else without notes.
- Explain **Null and alternative hypotheses** to someone else without notes.
- Explain **p-values and what they are not** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
