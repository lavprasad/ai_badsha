# Day 37 — Exploratory data analysis

Today's goal: work through **Exploratory data analysis** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | First five questions of any dataset |
| 2 | Shape, dtypes, memory |
| 3 | Univariate distributions |
| 4 | Bivariate relationships with the target |
| 5 | Correlation matrices and their limits |
| 6 | Segment analysis by group |
| 7 | Time trends in the data |
| 8 | Finding data-entry errors |
| 9 | Documenting surprises as you go |
| 10 | Turning EDA into modelling hypotheses |

---

## 1. First five questions of any dataset

LoRA freezes the base weights and trains two small low-rank matrices whose product is added to each target layer. You update ~0.1% of the parameters, the checkpoint is megabytes not gigabytes, and you can swap adapters per customer. QLoRA adds 4-bit base weights so a 7B model fits on one consumer GPU.

```python
import numpy as np

d, r = 512, 8                      # full dim vs LoRA rank
rng = np.random.default_rng(0)
W = rng.normal(size=(d, d)) * 0.02  # frozen base weight
A = rng.normal(size=(d, r)) * 0.01  # trainable
B = np.zeros((r, d))                # trainable, starts at zero -> no change at step 0

delta = A @ B
print('base params   ', W.size)
print('lora params   ', A.size + B.size, f'({100 * (A.size + B.size) / W.size:.1f}%)')
print('effective W = W + A@B, shape', (W + delta).shape)
```

**Remember:** Initialise B to zeros so the adapted model starts exactly equal to the base model.

**Common mistake:** Setting rank far too high — you lose the efficiency and gain the overfitting.

Practice: open `examples/01_first_five_questions_of_any_dataset.py`, predict the output, change one line, predict again.

## 2. Shape, dtypes, memory

NumPy stores numbers in one contiguous typed block and runs loops in C. Vectorised code (whole-array operations) is often 50-100x faster than a Python `for` loop and reads closer to the maths. Broadcasting stretches smaller shapes to match without copying data.

```python
import numpy as np

a = np.arange(6).reshape(2, 3)
print(a.shape, a.dtype)

b = np.array([10, 20, 30])       # shape (3,)
print(a + b)                     # broadcast over rows

print(a.sum(axis=0))             # column sums
print(a.sum(axis=1))             # row sums
```

**Remember:** `axis=0` collapses rows (down the columns); `axis=1` collapses columns (across a row).

**Common mistake:** Looping over array elements in Python instead of using a vectorised operation.

Practice: open `examples/02_shape_dtypes_memory.py`, predict the output, change one line, predict again.

## 3. Univariate distributions

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

Practice: open `examples/03_univariate_distributions.py`, predict the output, change one line, predict again.

## 4. Bivariate relationships with the target

LoRA freezes the base weights and trains two small low-rank matrices whose product is added to each target layer. You update ~0.1% of the parameters, the checkpoint is megabytes not gigabytes, and you can swap adapters per customer. QLoRA adds 4-bit base weights so a 7B model fits on one consumer GPU.

```python
import numpy as np

d, r = 512, 8                      # full dim vs LoRA rank
rng = np.random.default_rng(0)
W = rng.normal(size=(d, d)) * 0.02  # frozen base weight
A = rng.normal(size=(d, r)) * 0.01  # trainable
B = np.zeros((r, d))                # trainable, starts at zero -> no change at step 0

delta = A @ B
print('base params   ', W.size)
print('lora params   ', A.size + B.size, f'({100 * (A.size + B.size) / W.size:.1f}%)')
print('effective W = W + A@B, shape', (W + delta).shape)
```

**Remember:** Initialise B to zeros so the adapted model starts exactly equal to the base model.

**Common mistake:** Setting rank far too high — you lose the efficiency and gain the overfitting.

Practice: open `examples/04_bivariate_relationships_with_the_target.py`, predict the output, change one line, predict again.

## 5. Correlation matrices and their limits

LoRA freezes the base weights and trains two small low-rank matrices whose product is added to each target layer. You update ~0.1% of the parameters, the checkpoint is megabytes not gigabytes, and you can swap adapters per customer. QLoRA adds 4-bit base weights so a 7B model fits on one consumer GPU.

```python
import numpy as np

d, r = 512, 8                      # full dim vs LoRA rank
rng = np.random.default_rng(0)
W = rng.normal(size=(d, d)) * 0.02  # frozen base weight
A = rng.normal(size=(d, r)) * 0.01  # trainable
B = np.zeros((r, d))                # trainable, starts at zero -> no change at step 0

delta = A @ B
print('base params   ', W.size)
print('lora params   ', A.size + B.size, f'({100 * (A.size + B.size) / W.size:.1f}%)')
print('effective W = W + A@B, shape', (W + delta).shape)
```

**Remember:** Initialise B to zeros so the adapted model starts exactly equal to the base model.

**Common mistake:** Setting rank far too high — you lose the efficiency and gain the overfitting.

Practice: open `examples/05_correlation_matrices_and_their_limits.py`, predict the output, change one line, predict again.

## 6. Segment analysis by group

LoRA freezes the base weights and trains two small low-rank matrices whose product is added to each target layer. You update ~0.1% of the parameters, the checkpoint is megabytes not gigabytes, and you can swap adapters per customer. QLoRA adds 4-bit base weights so a 7B model fits on one consumer GPU.

```python
import numpy as np

d, r = 512, 8                      # full dim vs LoRA rank
rng = np.random.default_rng(0)
W = rng.normal(size=(d, d)) * 0.02  # frozen base weight
A = rng.normal(size=(d, r)) * 0.01  # trainable
B = np.zeros((r, d))                # trainable, starts at zero -> no change at step 0

delta = A @ B
print('base params   ', W.size)
print('lora params   ', A.size + B.size, f'({100 * (A.size + B.size) / W.size:.1f}%)')
print('effective W = W + A@B, shape', (W + delta).shape)
```

**Remember:** Initialise B to zeros so the adapted model starts exactly equal to the base model.

**Common mistake:** Setting rank far too high — you lose the efficiency and gain the overfitting.

Practice: open `examples/06_segment_analysis_by_group.py`, predict the output, change one line, predict again.

## 7. Time trends in the data

LoRA freezes the base weights and trains two small low-rank matrices whose product is added to each target layer. You update ~0.1% of the parameters, the checkpoint is megabytes not gigabytes, and you can swap adapters per customer. QLoRA adds 4-bit base weights so a 7B model fits on one consumer GPU.

```python
import numpy as np

d, r = 512, 8                      # full dim vs LoRA rank
rng = np.random.default_rng(0)
W = rng.normal(size=(d, d)) * 0.02  # frozen base weight
A = rng.normal(size=(d, r)) * 0.01  # trainable
B = np.zeros((r, d))                # trainable, starts at zero -> no change at step 0

delta = A @ B
print('base params   ', W.size)
print('lora params   ', A.size + B.size, f'({100 * (A.size + B.size) / W.size:.1f}%)')
print('effective W = W + A@B, shape', (W + delta).shape)
```

**Remember:** Initialise B to zeros so the adapted model starts exactly equal to the base model.

**Common mistake:** Setting rank far too high — you lose the efficiency and gain the overfitting.

Practice: open `examples/07_time_trends_in_the_data.py`, predict the output, change one line, predict again.

## 8. Finding data-entry errors

LoRA freezes the base weights and trains two small low-rank matrices whose product is added to each target layer. You update ~0.1% of the parameters, the checkpoint is megabytes not gigabytes, and you can swap adapters per customer. QLoRA adds 4-bit base weights so a 7B model fits on one consumer GPU.

```python
import numpy as np

d, r = 512, 8                      # full dim vs LoRA rank
rng = np.random.default_rng(0)
W = rng.normal(size=(d, d)) * 0.02  # frozen base weight
A = rng.normal(size=(d, r)) * 0.01  # trainable
B = np.zeros((r, d))                # trainable, starts at zero -> no change at step 0

delta = A @ B
print('base params   ', W.size)
print('lora params   ', A.size + B.size, f'({100 * (A.size + B.size) / W.size:.1f}%)')
print('effective W = W + A@B, shape', (W + delta).shape)
```

**Remember:** Initialise B to zeros so the adapted model starts exactly equal to the base model.

**Common mistake:** Setting rank far too high — you lose the efficiency and gain the overfitting.

Practice: open `examples/08_finding_data_entry_errors.py`, predict the output, change one line, predict again.

## 9. Documenting surprises as you go

LoRA freezes the base weights and trains two small low-rank matrices whose product is added to each target layer. You update ~0.1% of the parameters, the checkpoint is megabytes not gigabytes, and you can swap adapters per customer. QLoRA adds 4-bit base weights so a 7B model fits on one consumer GPU.

```python
import numpy as np

d, r = 512, 8                      # full dim vs LoRA rank
rng = np.random.default_rng(0)
W = rng.normal(size=(d, d)) * 0.02  # frozen base weight
A = rng.normal(size=(d, r)) * 0.01  # trainable
B = np.zeros((r, d))                # trainable, starts at zero -> no change at step 0

delta = A @ B
print('base params   ', W.size)
print('lora params   ', A.size + B.size, f'({100 * (A.size + B.size) / W.size:.1f}%)')
print('effective W = W + A@B, shape', (W + delta).shape)
```

**Remember:** Initialise B to zeros so the adapted model starts exactly equal to the base model.

**Common mistake:** Setting rank far too high — you lose the efficiency and gain the overfitting.

Practice: open `examples/09_documenting_surprises_as_you_go.py`, predict the output, change one line, predict again.

## 10. Turning EDA into modelling hypotheses

LoRA freezes the base weights and trains two small low-rank matrices whose product is added to each target layer. You update ~0.1% of the parameters, the checkpoint is megabytes not gigabytes, and you can swap adapters per customer. QLoRA adds 4-bit base weights so a 7B model fits on one consumer GPU.

```python
import numpy as np

d, r = 512, 8                      # full dim vs LoRA rank
rng = np.random.default_rng(0)
W = rng.normal(size=(d, d)) * 0.02  # frozen base weight
A = rng.normal(size=(d, r)) * 0.01  # trainable
B = np.zeros((r, d))                # trainable, starts at zero -> no change at step 0

delta = A @ B
print('base params   ', W.size)
print('lora params   ', A.size + B.size, f'({100 * (A.size + B.size) / W.size:.1f}%)')
print('effective W = W + A@B, shape', (W + delta).shape)
```

**Remember:** Initialise B to zeros so the adapted model starts exactly equal to the base model.

**Common mistake:** Setting rank far too high — you lose the efficiency and gain the overfitting.

Practice: open `examples/10_turning_eda_into_modelling_hypotheses.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 37

- Explain **First five questions of any dataset** to someone else without notes.
- Explain **Shape, dtypes, memory** to someone else without notes.
- Explain **Univariate distributions** to someone else without notes.
- Explain **Bivariate relationships with the target** to someone else without notes.
- Explain **Correlation matrices and their limits** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
