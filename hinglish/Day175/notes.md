# Day 175 — From notebook to software

Aaj ka goal: **From notebook to software** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

### Aasaan Bhasha

Notebooks cells ke beech state rakhte hain — exploring ke liye badhiya, reproducibility ke liye bekaar. Notebook ko scratchpad samjho; jab logic pakka ho jaaye to use `.py` module me daal do jise aap import aur test kar sako.

### Chhota code

```python
# In a notebook, cell order != execution order.
# Restart & Run All before you trust any result.
import pandas as pd
df = pd.DataFrame({'x': [1, 2, 3]})
df.head()
```

**Yaad rakho:** 'Restart kernel and run all' hi ek imaandaar test hai ki notebook sach me chalta hai.

**Aam galti:** Aisa notebook dena jiska result das minute pehle delete ki gayi cell par depend karta hai.

Practice: `examples/01_why_notebooks_do_not_ship.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Project structure for ML repos

### Aasaan Bhasha

Notebooks cells ke beech state rakhte hain — exploring ke liye badhiya, reproducibility ke liye bekaar. Notebook ko scratchpad samjho; jab logic pakka ho jaaye to use `.py` module me daal do jise aap import aur test kar sako.

### Chhota code

```python
# In a notebook, cell order != execution order.
# Restart & Run All before you trust any result.
import pandas as pd
df = pd.DataFrame({'x': [1, 2, 3]})
df.head()
```

**Yaad rakho:** 'Restart kernel and run all' hi ek imaandaar test hai ki notebook sach me chalta hai.

**Aam galti:** Aisa notebook dena jiska result das minute pehle delete ki gayi cell par depend karta hai.

Practice: `examples/02_project_structure_for_ml_repos.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Configuration files over hard-coded values

### Aasaan Bhasha

Notebooks cells ke beech state rakhte hain — exploring ke liye badhiya, reproducibility ke liye bekaar. Notebook ko scratchpad samjho; jab logic pakka ho jaaye to use `.py` module me daal do jise aap import aur test kar sako.

### Chhota code

```python
# In a notebook, cell order != execution order.
# Restart & Run All before you trust any result.
import pandas as pd
df = pd.DataFrame({'x': [1, 2, 3]})
df.head()
```

**Yaad rakho:** 'Restart kernel and run all' hi ek imaandaar test hai ki notebook sach me chalta hai.

**Aam galti:** Aisa notebook dena jiska result das minute pehle delete ki gayi cell par depend karta hai.

Practice: `examples/03_configuration_files_over_hard_coded_valu.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Separating data, training and serving code

### Aasaan Bhasha

Notebooks cells ke beech state rakhte hain — exploring ke liye badhiya, reproducibility ke liye bekaar. Notebook ko scratchpad samjho; jab logic pakka ho jaaye to use `.py` module me daal do jise aap import aur test kar sako.

### Chhota code

```python
# In a notebook, cell order != execution order.
# Restart & Run All before you trust any result.
import pandas as pd
df = pd.DataFrame({'x': [1, 2, 3]})
df.head()
```

**Yaad rakho:** 'Restart kernel and run all' hi ek imaandaar test hai ki notebook sach me chalta hai.

**Aam galti:** Aisa notebook dena jiska result das minute pehle delete ki gayi cell par depend karta hai.

Practice: `examples/04_separating_data_training_and_serving_cod.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Logging instead of print

### Aasaan Bhasha

Notebooks cells ke beech state rakhte hain — exploring ke liye badhiya, reproducibility ke liye bekaar. Notebook ko scratchpad samjho; jab logic pakka ho jaaye to use `.py` module me daal do jise aap import aur test kar sako.

### Chhota code

```python
# In a notebook, cell order != execution order.
# Restart & Run All before you trust any result.
import pandas as pd
df = pd.DataFrame({'x': [1, 2, 3]})
df.head()
```

**Yaad rakho:** 'Restart kernel and run all' hi ek imaandaar test hai ki notebook sach me chalta hai.

**Aam galti:** Aisa notebook dena jiska result das minute pehle delete ki gayi cell par depend karta hai.

Practice: `examples/05_logging_instead_of_print.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Command-line entry points

### Aasaan Bhasha

Notebooks cells ke beech state rakhte hain — exploring ke liye badhiya, reproducibility ke liye bekaar. Notebook ko scratchpad samjho; jab logic pakka ho jaaye to use `.py` module me daal do jise aap import aur test kar sako.

### Chhota code

```python
# In a notebook, cell order != execution order.
# Restart & Run All before you trust any result.
import pandas as pd
df = pd.DataFrame({'x': [1, 2, 3]})
df.head()
```

**Yaad rakho:** 'Restart kernel and run all' hi ek imaandaar test hai ki notebook sach me chalta hai.

**Aam galti:** Aisa notebook dena jiska result das minute pehle delete ki gayi cell par depend karta hai.

Practice: `examples/06_command_line_entry_points.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Packaging with pyproject.toml

### Aasaan Bhasha

Notebooks cells ke beech state rakhte hain — exploring ke liye badhiya, reproducibility ke liye bekaar. Notebook ko scratchpad samjho; jab logic pakka ho jaaye to use `.py` module me daal do jise aap import aur test kar sako.

### Chhota code

```python
# In a notebook, cell order != execution order.
# Restart & Run All before you trust any result.
import pandas as pd
df = pd.DataFrame({'x': [1, 2, 3]})
df.head()
```

**Yaad rakho:** 'Restart kernel and run all' hi ek imaandaar test hai ki notebook sach me chalta hai.

**Aam galti:** Aisa notebook dena jiska result das minute pehle delete ki gayi cell par depend karta hai.

Practice: `examples/07_packaging_with_pyproject_toml.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Dependency pinning

### Aasaan Bhasha

Notebooks cells ke beech state rakhte hain — exploring ke liye badhiya, reproducibility ke liye bekaar. Notebook ko scratchpad samjho; jab logic pakka ho jaaye to use `.py` module me daal do jise aap import aur test kar sako.

### Chhota code

```python
# In a notebook, cell order != execution order.
# Restart & Run All before you trust any result.
import pandas as pd
df = pd.DataFrame({'x': [1, 2, 3]})
df.head()
```

**Yaad rakho:** 'Restart kernel and run all' hi ek imaandaar test hai ki notebook sach me chalta hai.

**Aam galti:** Aisa notebook dena jiska result das minute pehle delete ki gayi cell par depend karta hai.

Practice: `examples/08_dependency_pinning.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Making the whole run one command

### Aasaan Bhasha

Notebooks cells ke beech state rakhte hain — exploring ke liye badhiya, reproducibility ke liye bekaar. Notebook ko scratchpad samjho; jab logic pakka ho jaaye to use `.py` module me daal do jise aap import aur test kar sako.

### Chhota code

```python
# In a notebook, cell order != execution order.
# Restart & Run All before you trust any result.
import pandas as pd
df = pd.DataFrame({'x': [1, 2, 3]})
df.head()
```

**Yaad rakho:** 'Restart kernel and run all' hi ek imaandaar test hai ki notebook sach me chalta hai.

**Aam galti:** Aisa notebook dena jiska result das minute pehle delete ki gayi cell par depend karta hai.

Practice: `examples/09_making_the_whole_run_one_command.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Refactoring a notebook into modules

### Aasaan Bhasha

Notebooks cells ke beech state rakhte hain — exploring ke liye badhiya, reproducibility ke liye bekaar. Notebook ko scratchpad samjho; jab logic pakka ho jaaye to use `.py` module me daal do jise aap import aur test kar sako.

### Chhota code

```python
# In a notebook, cell order != execution order.
# Restart & Run All before you trust any result.
import pandas as pd
df = pd.DataFrame({'x': [1, 2, 3]})
df.head()
```

**Yaad rakho:** 'Restart kernel and run all' hi ek imaandaar test hai ki notebook sach me chalta hai.

**Aam galti:** Aisa notebook dena jiska result das minute pehle delete ki gayi cell par depend karta hai.

Practice: `examples/10_refactoring_a_notebook_into_modules.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 175 ke baad aapko ye aana chahiye

- **Why notebooks do not ship** ko bina notes dekhe kisi dost ko samjha sakna.
- **Project structure for ML repos** ko bina notes dekhe kisi dost ko samjha sakna.
- **Configuration files over hard-coded values** ko bina notes dekhe kisi dost ko samjha sakna.
- **Separating data, training and serving code** ko bina notes dekhe kisi dost ko samjha sakna.
- **Logging instead of print** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
