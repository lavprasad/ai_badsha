# Day 23 — Descriptive statistics

Today's goal: work through **descriptive statistics** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Mean, median and mode |
| 2 | Variance and standard deviation |
| 3 | Quantiles, percentiles and IQR |
| 4 | Skewness and kurtosis |
| 5 | Covariance and correlation |
| 6 | Correlation is not causation |
| 7 | Robust statistics and outliers |
| 8 | Standardisation and z-scores |
| 9 | Simpson's paradox |
| 10 | Summarising a dataset honestly |

---

## 1. Mean, median and mode

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

## 2. Variance and standard deviation

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

## 3. Quantiles, percentiles and IQR

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

## 4. Skewness and kurtosis

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

## 5. Covariance and correlation

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

## 6. Correlation is not causation

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

## 7. Robust statistics and outliers

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

## 8. Standardisation and z-scores

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

## 9. Simpson's paradox

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

## 10. Summarising a dataset honestly

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

---

## What you should be able to do after Day 23

- Explain **Mean, median and mode** to someone else without notes.
- Explain **Variance and standard deviation** to someone else without notes.
- Explain **Quantiles, percentiles and IQR** to someone else without notes.
- Explain **Skewness and kurtosis** to someone else without notes.
- Explain **Covariance and correlation** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
