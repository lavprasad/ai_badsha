# Day 40 — Encoding and scaling

Today's goal: work through **Encoding and scaling** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | One-hot encoding |
| 2 | Ordinal encoding when order is real |
| 3 | Target encoding and its leakage risk |
| 4 | Hashing trick for high cardinality |
| 5 | Handling unseen categories at inference |
| 6 | StandardScaler vs MinMaxScaler |
| 7 | RobustScaler for outlier-heavy data |
| 8 | Log and power transforms |
| 9 | Which models need scaling and which do not |
| 10 | Fitting transforms on train only |

---

## 1. One-hot encoding

Models need numbers. One-hot is safe for low-cardinality nominal categories. Label/ordinal encoding invents a false order unless the order is real (small < medium < large). Target encoding is powerful and leaks badly unless you fit it inside cross-validation folds.

```python
import pandas as pd

df = pd.DataFrame({'size': ['small', 'large', 'medium'], 'city': ['pune', 'delhi', 'pune']})

order = {'small': 0, 'medium': 1, 'large': 2}     # real order -> ordinal is fine
df['size_ord'] = df['size'].map(order)

print(pd.get_dummies(df[['city']], prefix='city', dtype=int))
print(df)
```

**Remember:** Handle unseen categories at inference time — decide up front whether they map to 'other' or raise.

**Common mistake:** One-hot encoding a 50,000-value ID column and blowing up memory for zero signal.

Practice: open `examples/01_one_hot_encoding.py`, predict the output, change one line, predict again.

## 2. Ordinal encoding when order is real

Models need numbers. One-hot is safe for low-cardinality nominal categories. Label/ordinal encoding invents a false order unless the order is real (small < medium < large). Target encoding is powerful and leaks badly unless you fit it inside cross-validation folds.

```python
import pandas as pd

df = pd.DataFrame({'size': ['small', 'large', 'medium'], 'city': ['pune', 'delhi', 'pune']})

order = {'small': 0, 'medium': 1, 'large': 2}     # real order -> ordinal is fine
df['size_ord'] = df['size'].map(order)

print(pd.get_dummies(df[['city']], prefix='city', dtype=int))
print(df)
```

**Remember:** Handle unseen categories at inference time — decide up front whether they map to 'other' or raise.

**Common mistake:** One-hot encoding a 50,000-value ID column and blowing up memory for zero signal.

Practice: open `examples/02_ordinal_encoding_when_order_is_real.py`, predict the output, change one line, predict again.

## 3. Target encoding and its leakage risk

Models need numbers. One-hot is safe for low-cardinality nominal categories. Label/ordinal encoding invents a false order unless the order is real (small < medium < large). Target encoding is powerful and leaks badly unless you fit it inside cross-validation folds.

```python
import pandas as pd

df = pd.DataFrame({'size': ['small', 'large', 'medium'], 'city': ['pune', 'delhi', 'pune']})

order = {'small': 0, 'medium': 1, 'large': 2}     # real order -> ordinal is fine
df['size_ord'] = df['size'].map(order)

print(pd.get_dummies(df[['city']], prefix='city', dtype=int))
print(df)
```

**Remember:** Handle unseen categories at inference time — decide up front whether they map to 'other' or raise.

**Common mistake:** One-hot encoding a 50,000-value ID column and blowing up memory for zero signal.

Practice: open `examples/03_target_encoding_and_its_leakage_risk.py`, predict the output, change one line, predict again.

## 4. Hashing trick for high cardinality

Data parallelism replicates the model and splits the batch; model parallelism splits the model when it will not fit on one device. Scale only after profiling — most 'we need more GPUs' problems are actually a slow data loader.

```python
# Effective batch = per_device_batch * n_devices * grad_accum_steps
per_device, devices, accum = 8, 4, 4
print('effective batch size', per_device * devices * accum)
print('\\nGradient accumulation gives a large effective batch on small memory:')
print('  for i, batch in enumerate(loader):')
print('      loss = model(batch).loss / accum')
print('      loss.backward()')
print('      if (i + 1) % accum == 0:')
print('          opt.step(); opt.zero_grad()')
```

**Remember:** Profile first. GPU at 30% utilisation means the bottleneck is the data pipeline, not the GPU.

**Common mistake:** Scaling the learning rate wrongly when you scale the batch — a larger batch usually needs a larger LR.

Practice: open `examples/04_hashing_trick_for_high_cardinality.py`, predict the output, change one line, predict again.

## 5. Handling unseen categories at inference

Data parallelism replicates the model and splits the batch; model parallelism splits the model when it will not fit on one device. Scale only after profiling — most 'we need more GPUs' problems are actually a slow data loader.

```python
# Effective batch = per_device_batch * n_devices * grad_accum_steps
per_device, devices, accum = 8, 4, 4
print('effective batch size', per_device * devices * accum)
print('\\nGradient accumulation gives a large effective batch on small memory:')
print('  for i, batch in enumerate(loader):')
print('      loss = model(batch).loss / accum')
print('      loss.backward()')
print('      if (i + 1) % accum == 0:')
print('          opt.step(); opt.zero_grad()')
```

**Remember:** Profile first. GPU at 30% utilisation means the bottleneck is the data pipeline, not the GPU.

**Common mistake:** Scaling the learning rate wrongly when you scale the batch — a larger batch usually needs a larger LR.

Practice: open `examples/05_handling_unseen_categories_at_inference.py`, predict the output, change one line, predict again.

## 6. StandardScaler vs MinMaxScaler

Distance and gradient-based models care about units: a salary column in rupees will dominate an age column purely by magnitude. Standardise (mean 0, std 1) for most models; min-max scale when you need a bounded [0,1] range. Tree models do not care.

```python
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
pipe = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
print('cv accuracy', cross_val_score(pipe, X, y, cv=5).mean().round(4))
```

**Remember:** Put the scaler INSIDE a Pipeline so cross-validation refits it per fold and cannot leak.

**Common mistake:** Calling `fit_transform` on the full dataset before splitting — classic, silent, score-inflating leak.

Practice: open `examples/06_standardscaler_vs_minmaxscaler.py`, predict the output, change one line, predict again.

## 7. RobustScaler for outlier-heavy data

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

Practice: open `examples/07_robustscaler_for_outlier_heavy_data.py`, predict the output, change one line, predict again.

## 8. Log and power transforms

Data parallelism replicates the model and splits the batch; model parallelism splits the model when it will not fit on one device. Scale only after profiling — most 'we need more GPUs' problems are actually a slow data loader.

```python
# Effective batch = per_device_batch * n_devices * grad_accum_steps
per_device, devices, accum = 8, 4, 4
print('effective batch size', per_device * devices * accum)
print('\\nGradient accumulation gives a large effective batch on small memory:')
print('  for i, batch in enumerate(loader):')
print('      loss = model(batch).loss / accum')
print('      loss.backward()')
print('      if (i + 1) % accum == 0:')
print('          opt.step(); opt.zero_grad()')
```

**Remember:** Profile first. GPU at 30% utilisation means the bottleneck is the data pipeline, not the GPU.

**Common mistake:** Scaling the learning rate wrongly when you scale the batch — a larger batch usually needs a larger LR.

Practice: open `examples/08_log_and_power_transforms.py`, predict the output, change one line, predict again.

## 9. Which models need scaling and which do not

Data parallelism replicates the model and splits the batch; model parallelism splits the model when it will not fit on one device. Scale only after profiling — most 'we need more GPUs' problems are actually a slow data loader.

```python
# Effective batch = per_device_batch * n_devices * grad_accum_steps
per_device, devices, accum = 8, 4, 4
print('effective batch size', per_device * devices * accum)
print('\\nGradient accumulation gives a large effective batch on small memory:')
print('  for i, batch in enumerate(loader):')
print('      loss = model(batch).loss / accum')
print('      loss.backward()')
print('      if (i + 1) % accum == 0:')
print('          opt.step(); opt.zero_grad()')
```

**Remember:** Profile first. GPU at 30% utilisation means the bottleneck is the data pipeline, not the GPU.

**Common mistake:** Scaling the learning rate wrongly when you scale the batch — a larger batch usually needs a larger LR.

Practice: open `examples/09_which_models_need_scaling_and_which_do_n.py`, predict the output, change one line, predict again.

## 10. Fitting transforms on train only

Data parallelism replicates the model and splits the batch; model parallelism splits the model when it will not fit on one device. Scale only after profiling — most 'we need more GPUs' problems are actually a slow data loader.

```python
# Effective batch = per_device_batch * n_devices * grad_accum_steps
per_device, devices, accum = 8, 4, 4
print('effective batch size', per_device * devices * accum)
print('\\nGradient accumulation gives a large effective batch on small memory:')
print('  for i, batch in enumerate(loader):')
print('      loss = model(batch).loss / accum')
print('      loss.backward()')
print('      if (i + 1) % accum == 0:')
print('          opt.step(); opt.zero_grad()')
```

**Remember:** Profile first. GPU at 30% utilisation means the bottleneck is the data pipeline, not the GPU.

**Common mistake:** Scaling the learning rate wrongly when you scale the batch — a larger batch usually needs a larger LR.

Practice: open `examples/10_fitting_transforms_on_train_only.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 40

- Explain **One-hot encoding** to someone else without notes.
- Explain **Ordinal encoding when order is real** to someone else without notes.
- Explain **Target encoding and its leakage risk** to someone else without notes.
- Explain **Hashing trick for high cardinality** to someone else without notes.
- Explain **Handling unseen categories at inference** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
