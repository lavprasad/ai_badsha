# Day 12 — Statistical plotting and EDA visuals

Today's goal: work through **Statistical plotting and EDA visuals** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | seaborn on top of matplotlib |
| 2 | Distribution plots: hist, kde, box, violin |
| 3 | Pairplots and correlation heatmaps |
| 4 | Categorical comparisons |
| 5 | Scatter with hue and size encoding |
| 6 | Faceting by a grouping variable |
| 7 | Spotting skew and outliers visually |
| 8 | Detecting non-linearity |
| 9 | Chart types that mislead |
| 10 | Building a one-page EDA report |

---

## 1. seaborn on top of matplotlib

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

Practice: open `examples/01_seaborn_on_top_of_matplotlib.py`, predict the output, change one line, predict again.

## 2. Distribution plots: hist, kde, box, violin

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

Practice: open `examples/02_distribution_plots_hist_kde_box_violin.py`, predict the output, change one line, predict again.

## 3. Pairplots and correlation heatmaps

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

Practice: open `examples/03_pairplots_and_correlation_heatmaps.py`, predict the output, change one line, predict again.

## 4. Categorical comparisons

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

Practice: open `examples/04_categorical_comparisons.py`, predict the output, change one line, predict again.

## 5. Scatter with hue and size encoding

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

Practice: open `examples/05_scatter_with_hue_and_size_encoding.py`, predict the output, change one line, predict again.

## 6. Faceting by a grouping variable

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

Practice: open `examples/06_faceting_by_a_grouping_variable.py`, predict the output, change one line, predict again.

## 7. Spotting skew and outliers visually

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

Practice: open `examples/07_spotting_skew_and_outliers_visually.py`, predict the output, change one line, predict again.

## 8. Detecting non-linearity

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

Practice: open `examples/08_detecting_non_linearity.py`, predict the output, change one line, predict again.

## 9. Chart types that mislead

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

Practice: open `examples/09_chart_types_that_mislead.py`, predict the output, change one line, predict again.

## 10. Building a one-page EDA report

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

Practice: open `examples/10_building_a_one_page_eda_report.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 12

- Explain **seaborn on top of matplotlib** to someone else without notes.
- Explain **Distribution plots: hist, kde, box, violin** to someone else without notes.
- Explain **Pairplots and correlation heatmaps** to someone else without notes.
- Explain **Categorical comparisons** to someone else without notes.
- Explain **Scatter with hue and size encoding** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
