# Day 85 — PyTorch data pipeline

Today's goal: work through **PyTorch data pipeline** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Dataset and __getitem__ |
| 2 | DataLoader, batching and shuffling |
| 3 | num_workers and prefetching |
| 4 | Custom collate functions |
| 5 | Transforms and augmentation |
| 6 | Handling variable-length inputs |
| 7 | Weighted samplers for imbalance |
| 8 | Reproducible shuffling with seeds |
| 9 | Profiling a slow data loader |
| 10 | Building a Dataset for your own files |

---

## 1. Dataset and __getitem__

A Pipeline chains preprocessing and the model into one object that fits and predicts as a unit. This is the single best defence against leakage, and it means deployment ships one artefact instead of six loose steps you must remember to repeat.

```python
import numpy as np, pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression

df = pd.DataFrame({'age': [25, np.nan, 40, 33], 'city': ['pune', 'delhi', 'pune', 'delhi']})
y = [0, 1, 0, 1]

pre = ColumnTransformer([
    ('num', Pipeline([('imp', SimpleImputer(strategy='median')), ('sc', StandardScaler())]), ['age']),
    ('cat', OneHotEncoder(handle_unknown='ignore'), ['city']),
])
model = Pipeline([('pre', pre), ('clf', LogisticRegression())]).fit(df, y)
print(model.predict(df))
```

**Remember:** `handle_unknown='ignore'` stops production crashing on a category you never saw in training.

**Common mistake:** Preprocessing in a notebook and then forgetting one step when writing the serving code.

Practice: open `examples/01_dataset_and_getitem.py`, predict the output, change one line, predict again.

## 2. DataLoader, batching and shuffling

A Pipeline chains preprocessing and the model into one object that fits and predicts as a unit. This is the single best defence against leakage, and it means deployment ships one artefact instead of six loose steps you must remember to repeat.

```python
import numpy as np, pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression

df = pd.DataFrame({'age': [25, np.nan, 40, 33], 'city': ['pune', 'delhi', 'pune', 'delhi']})
y = [0, 1, 0, 1]

pre = ColumnTransformer([
    ('num', Pipeline([('imp', SimpleImputer(strategy='median')), ('sc', StandardScaler())]), ['age']),
    ('cat', OneHotEncoder(handle_unknown='ignore'), ['city']),
])
model = Pipeline([('pre', pre), ('clf', LogisticRegression())]).fit(df, y)
print(model.predict(df))
```

**Remember:** `handle_unknown='ignore'` stops production crashing on a category you never saw in training.

**Common mistake:** Preprocessing in a notebook and then forgetting one step when writing the serving code.

Practice: open `examples/02_dataloader_batching_and_shuffling.py`, predict the output, change one line, predict again.

## 3. num_workers and prefetching

A Pipeline chains preprocessing and the model into one object that fits and predicts as a unit. This is the single best defence against leakage, and it means deployment ships one artefact instead of six loose steps you must remember to repeat.

```python
import numpy as np, pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression

df = pd.DataFrame({'age': [25, np.nan, 40, 33], 'city': ['pune', 'delhi', 'pune', 'delhi']})
y = [0, 1, 0, 1]

pre = ColumnTransformer([
    ('num', Pipeline([('imp', SimpleImputer(strategy='median')), ('sc', StandardScaler())]), ['age']),
    ('cat', OneHotEncoder(handle_unknown='ignore'), ['city']),
])
model = Pipeline([('pre', pre), ('clf', LogisticRegression())]).fit(df, y)
print(model.predict(df))
```

**Remember:** `handle_unknown='ignore'` stops production crashing on a category you never saw in training.

**Common mistake:** Preprocessing in a notebook and then forgetting one step when writing the serving code.

Practice: open `examples/03_num_workers_and_prefetching.py`, predict the output, change one line, predict again.

## 4. Custom collate functions

A Pipeline chains preprocessing and the model into one object that fits and predicts as a unit. This is the single best defence against leakage, and it means deployment ships one artefact instead of six loose steps you must remember to repeat.

```python
import numpy as np, pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression

df = pd.DataFrame({'age': [25, np.nan, 40, 33], 'city': ['pune', 'delhi', 'pune', 'delhi']})
y = [0, 1, 0, 1]

pre = ColumnTransformer([
    ('num', Pipeline([('imp', SimpleImputer(strategy='median')), ('sc', StandardScaler())]), ['age']),
    ('cat', OneHotEncoder(handle_unknown='ignore'), ['city']),
])
model = Pipeline([('pre', pre), ('clf', LogisticRegression())]).fit(df, y)
print(model.predict(df))
```

**Remember:** `handle_unknown='ignore'` stops production crashing on a category you never saw in training.

**Common mistake:** Preprocessing in a notebook and then forgetting one step when writing the serving code.

Practice: open `examples/04_custom_collate_functions.py`, predict the output, change one line, predict again.

## 5. Transforms and augmentation

A Pipeline chains preprocessing and the model into one object that fits and predicts as a unit. This is the single best defence against leakage, and it means deployment ships one artefact instead of six loose steps you must remember to repeat.

```python
import numpy as np, pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression

df = pd.DataFrame({'age': [25, np.nan, 40, 33], 'city': ['pune', 'delhi', 'pune', 'delhi']})
y = [0, 1, 0, 1]

pre = ColumnTransformer([
    ('num', Pipeline([('imp', SimpleImputer(strategy='median')), ('sc', StandardScaler())]), ['age']),
    ('cat', OneHotEncoder(handle_unknown='ignore'), ['city']),
])
model = Pipeline([('pre', pre), ('clf', LogisticRegression())]).fit(df, y)
print(model.predict(df))
```

**Remember:** `handle_unknown='ignore'` stops production crashing on a category you never saw in training.

**Common mistake:** Preprocessing in a notebook and then forgetting one step when writing the serving code.

Practice: open `examples/05_transforms_and_augmentation.py`, predict the output, change one line, predict again.

## 6. Handling variable-length inputs

A Pipeline chains preprocessing and the model into one object that fits and predicts as a unit. This is the single best defence against leakage, and it means deployment ships one artefact instead of six loose steps you must remember to repeat.

```python
import numpy as np, pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression

df = pd.DataFrame({'age': [25, np.nan, 40, 33], 'city': ['pune', 'delhi', 'pune', 'delhi']})
y = [0, 1, 0, 1]

pre = ColumnTransformer([
    ('num', Pipeline([('imp', SimpleImputer(strategy='median')), ('sc', StandardScaler())]), ['age']),
    ('cat', OneHotEncoder(handle_unknown='ignore'), ['city']),
])
model = Pipeline([('pre', pre), ('clf', LogisticRegression())]).fit(df, y)
print(model.predict(df))
```

**Remember:** `handle_unknown='ignore'` stops production crashing on a category you never saw in training.

**Common mistake:** Preprocessing in a notebook and then forgetting one step when writing the serving code.

Practice: open `examples/06_handling_variable_length_inputs.py`, predict the output, change one line, predict again.

## 7. Weighted samplers for imbalance

A Pipeline chains preprocessing and the model into one object that fits and predicts as a unit. This is the single best defence against leakage, and it means deployment ships one artefact instead of six loose steps you must remember to repeat.

```python
import numpy as np, pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression

df = pd.DataFrame({'age': [25, np.nan, 40, 33], 'city': ['pune', 'delhi', 'pune', 'delhi']})
y = [0, 1, 0, 1]

pre = ColumnTransformer([
    ('num', Pipeline([('imp', SimpleImputer(strategy='median')), ('sc', StandardScaler())]), ['age']),
    ('cat', OneHotEncoder(handle_unknown='ignore'), ['city']),
])
model = Pipeline([('pre', pre), ('clf', LogisticRegression())]).fit(df, y)
print(model.predict(df))
```

**Remember:** `handle_unknown='ignore'` stops production crashing on a category you never saw in training.

**Common mistake:** Preprocessing in a notebook and then forgetting one step when writing the serving code.

Practice: open `examples/07_weighted_samplers_for_imbalance.py`, predict the output, change one line, predict again.

## 8. Reproducible shuffling with seeds

A Pipeline chains preprocessing and the model into one object that fits and predicts as a unit. This is the single best defence against leakage, and it means deployment ships one artefact instead of six loose steps you must remember to repeat.

```python
import numpy as np, pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression

df = pd.DataFrame({'age': [25, np.nan, 40, 33], 'city': ['pune', 'delhi', 'pune', 'delhi']})
y = [0, 1, 0, 1]

pre = ColumnTransformer([
    ('num', Pipeline([('imp', SimpleImputer(strategy='median')), ('sc', StandardScaler())]), ['age']),
    ('cat', OneHotEncoder(handle_unknown='ignore'), ['city']),
])
model = Pipeline([('pre', pre), ('clf', LogisticRegression())]).fit(df, y)
print(model.predict(df))
```

**Remember:** `handle_unknown='ignore'` stops production crashing on a category you never saw in training.

**Common mistake:** Preprocessing in a notebook and then forgetting one step when writing the serving code.

Practice: open `examples/08_reproducible_shuffling_with_seeds.py`, predict the output, change one line, predict again.

## 9. Profiling a slow data loader

A Pipeline chains preprocessing and the model into one object that fits and predicts as a unit. This is the single best defence against leakage, and it means deployment ships one artefact instead of six loose steps you must remember to repeat.

```python
import numpy as np, pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression

df = pd.DataFrame({'age': [25, np.nan, 40, 33], 'city': ['pune', 'delhi', 'pune', 'delhi']})
y = [0, 1, 0, 1]

pre = ColumnTransformer([
    ('num', Pipeline([('imp', SimpleImputer(strategy='median')), ('sc', StandardScaler())]), ['age']),
    ('cat', OneHotEncoder(handle_unknown='ignore'), ['city']),
])
model = Pipeline([('pre', pre), ('clf', LogisticRegression())]).fit(df, y)
print(model.predict(df))
```

**Remember:** `handle_unknown='ignore'` stops production crashing on a category you never saw in training.

**Common mistake:** Preprocessing in a notebook and then forgetting one step when writing the serving code.

Practice: open `examples/09_profiling_a_slow_data_loader.py`, predict the output, change one line, predict again.

## 10. Building a Dataset for your own files

A Pipeline chains preprocessing and the model into one object that fits and predicts as a unit. This is the single best defence against leakage, and it means deployment ships one artefact instead of six loose steps you must remember to repeat.

```python
import numpy as np, pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression

df = pd.DataFrame({'age': [25, np.nan, 40, 33], 'city': ['pune', 'delhi', 'pune', 'delhi']})
y = [0, 1, 0, 1]

pre = ColumnTransformer([
    ('num', Pipeline([('imp', SimpleImputer(strategy='median')), ('sc', StandardScaler())]), ['age']),
    ('cat', OneHotEncoder(handle_unknown='ignore'), ['city']),
])
model = Pipeline([('pre', pre), ('clf', LogisticRegression())]).fit(df, y)
print(model.predict(df))
```

**Remember:** `handle_unknown='ignore'` stops production crashing on a category you never saw in training.

**Common mistake:** Preprocessing in a notebook and then forgetting one step when writing the serving code.

Practice: open `examples/10_building_a_dataset_for_your_own_files.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 85

- Explain **Dataset and __getitem__** to someone else without notes.
- Explain **DataLoader, batching and shuffling** to someone else without notes.
- Explain **num_workers and prefetching** to someone else without notes.
- Explain **Custom collate functions** to someone else without notes.
- Explain **Transforms and augmentation** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
