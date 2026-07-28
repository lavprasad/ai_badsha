# Day 175 — From notebook to software

Today's goal: work through **From notebook to software** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Why notebooks do not ship |
| 2 | Project structure for ML repos |
| 3 | Configuration files over hard-coded values |
| 4 | Separating data, training and serving code |
| 5 | Logging instead of print |
| 6 | Command-line entry points |
| 7 | Packaging with pyproject.toml |
| 8 | Dependency pinning |
| 9 | Making the whole run one command |
| 10 | Refactoring a notebook into modules |

---

## 1. Why notebooks do not ship

Notebooks keep state between cells, which is great for exploring and terrible for reproducibility. Treat the notebook as a scratchpad; once logic settles, move it into a `.py` module you can import and test.

```python
# In a notebook, cell order != execution order.
# Restart & Run All before you trust any result.
import pandas as pd
df = pd.DataFrame({'x': [1, 2, 3]})
df.head()
```

**Remember:** 'Restart kernel and run all' is the only honest test that a notebook works.

**Common mistake:** Shipping a notebook whose results depend on a deleted cell you ran ten minutes ago.

Practice: open `examples/01_why_notebooks_do_not_ship.py`, predict the output, change one line, predict again.

## 2. Project structure for ML repos

Notebooks keep state between cells, which is great for exploring and terrible for reproducibility. Treat the notebook as a scratchpad; once logic settles, move it into a `.py` module you can import and test.

```python
# In a notebook, cell order != execution order.
# Restart & Run All before you trust any result.
import pandas as pd
df = pd.DataFrame({'x': [1, 2, 3]})
df.head()
```

**Remember:** 'Restart kernel and run all' is the only honest test that a notebook works.

**Common mistake:** Shipping a notebook whose results depend on a deleted cell you ran ten minutes ago.

Practice: open `examples/02_project_structure_for_ml_repos.py`, predict the output, change one line, predict again.

## 3. Configuration files over hard-coded values

Notebooks keep state between cells, which is great for exploring and terrible for reproducibility. Treat the notebook as a scratchpad; once logic settles, move it into a `.py` module you can import and test.

```python
# In a notebook, cell order != execution order.
# Restart & Run All before you trust any result.
import pandas as pd
df = pd.DataFrame({'x': [1, 2, 3]})
df.head()
```

**Remember:** 'Restart kernel and run all' is the only honest test that a notebook works.

**Common mistake:** Shipping a notebook whose results depend on a deleted cell you ran ten minutes ago.

Practice: open `examples/03_configuration_files_over_hard_coded_valu.py`, predict the output, change one line, predict again.

## 4. Separating data, training and serving code

Notebooks keep state between cells, which is great for exploring and terrible for reproducibility. Treat the notebook as a scratchpad; once logic settles, move it into a `.py` module you can import and test.

```python
# In a notebook, cell order != execution order.
# Restart & Run All before you trust any result.
import pandas as pd
df = pd.DataFrame({'x': [1, 2, 3]})
df.head()
```

**Remember:** 'Restart kernel and run all' is the only honest test that a notebook works.

**Common mistake:** Shipping a notebook whose results depend on a deleted cell you ran ten minutes ago.

Practice: open `examples/04_separating_data_training_and_serving_cod.py`, predict the output, change one line, predict again.

## 5. Logging instead of print

Notebooks keep state between cells, which is great for exploring and terrible for reproducibility. Treat the notebook as a scratchpad; once logic settles, move it into a `.py` module you can import and test.

```python
# In a notebook, cell order != execution order.
# Restart & Run All before you trust any result.
import pandas as pd
df = pd.DataFrame({'x': [1, 2, 3]})
df.head()
```

**Remember:** 'Restart kernel and run all' is the only honest test that a notebook works.

**Common mistake:** Shipping a notebook whose results depend on a deleted cell you ran ten minutes ago.

Practice: open `examples/05_logging_instead_of_print.py`, predict the output, change one line, predict again.

## 6. Command-line entry points

Notebooks keep state between cells, which is great for exploring and terrible for reproducibility. Treat the notebook as a scratchpad; once logic settles, move it into a `.py` module you can import and test.

```python
# In a notebook, cell order != execution order.
# Restart & Run All before you trust any result.
import pandas as pd
df = pd.DataFrame({'x': [1, 2, 3]})
df.head()
```

**Remember:** 'Restart kernel and run all' is the only honest test that a notebook works.

**Common mistake:** Shipping a notebook whose results depend on a deleted cell you ran ten minutes ago.

Practice: open `examples/06_command_line_entry_points.py`, predict the output, change one line, predict again.

## 7. Packaging with pyproject.toml

Notebooks keep state between cells, which is great for exploring and terrible for reproducibility. Treat the notebook as a scratchpad; once logic settles, move it into a `.py` module you can import and test.

```python
# In a notebook, cell order != execution order.
# Restart & Run All before you trust any result.
import pandas as pd
df = pd.DataFrame({'x': [1, 2, 3]})
df.head()
```

**Remember:** 'Restart kernel and run all' is the only honest test that a notebook works.

**Common mistake:** Shipping a notebook whose results depend on a deleted cell you ran ten minutes ago.

Practice: open `examples/07_packaging_with_pyproject_toml.py`, predict the output, change one line, predict again.

## 8. Dependency pinning

Notebooks keep state between cells, which is great for exploring and terrible for reproducibility. Treat the notebook as a scratchpad; once logic settles, move it into a `.py` module you can import and test.

```python
# In a notebook, cell order != execution order.
# Restart & Run All before you trust any result.
import pandas as pd
df = pd.DataFrame({'x': [1, 2, 3]})
df.head()
```

**Remember:** 'Restart kernel and run all' is the only honest test that a notebook works.

**Common mistake:** Shipping a notebook whose results depend on a deleted cell you ran ten minutes ago.

Practice: open `examples/08_dependency_pinning.py`, predict the output, change one line, predict again.

## 9. Making the whole run one command

Notebooks keep state between cells, which is great for exploring and terrible for reproducibility. Treat the notebook as a scratchpad; once logic settles, move it into a `.py` module you can import and test.

```python
# In a notebook, cell order != execution order.
# Restart & Run All before you trust any result.
import pandas as pd
df = pd.DataFrame({'x': [1, 2, 3]})
df.head()
```

**Remember:** 'Restart kernel and run all' is the only honest test that a notebook works.

**Common mistake:** Shipping a notebook whose results depend on a deleted cell you ran ten minutes ago.

Practice: open `examples/09_making_the_whole_run_one_command.py`, predict the output, change one line, predict again.

## 10. Refactoring a notebook into modules

Notebooks keep state between cells, which is great for exploring and terrible for reproducibility. Treat the notebook as a scratchpad; once logic settles, move it into a `.py` module you can import and test.

```python
# In a notebook, cell order != execution order.
# Restart & Run All before you trust any result.
import pandas as pd
df = pd.DataFrame({'x': [1, 2, 3]})
df.head()
```

**Remember:** 'Restart kernel and run all' is the only honest test that a notebook works.

**Common mistake:** Shipping a notebook whose results depend on a deleted cell you ran ten minutes ago.

Practice: open `examples/10_refactoring_a_notebook_into_modules.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 175

- Explain **Why notebooks do not ship** to someone else without notes.
- Explain **Project structure for ML repos** to someone else without notes.
- Explain **Configuration files over hard-coded values** to someone else without notes.
- Explain **Separating data, training and serving code** to someone else without notes.
- Explain **Logging instead of print** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
