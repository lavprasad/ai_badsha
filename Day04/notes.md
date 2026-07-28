# Day 04 — Files, JSON and the filesystem

Today's goal: work through **Files, JSON and the filesystem** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Reading and writing text files |
| 2 | Context managers and with |
| 3 | CSV files with the csv module |
| 4 | JSON serialisation and parsing |
| 5 | pathlib for portable paths |
| 6 | Encoding: UTF-8 and why it bites |
| 7 | Working with large files line by line |
| 8 | Compressed files: gzip and zip |
| 9 | Environment variables and secrets |
| 10 | A tiny dataset downloader script |

---

## 1. Reading and writing text files

`with open(...)` closes the file even if the body raises — that is what a context manager is for. Iterate a file object line by line and Python never loads the whole thing into memory, which is how you process a 40 GB log on a laptop.

```python
from pathlib import Path

p = Path('demo.txt')
with p.open('w', encoding='utf-8') as fh:
    for i in range(5):
        fh.write(f'row {i}\n')

total = 0
with p.open(encoding='utf-8') as fh:
    for line in fh:              # streams; never holds the whole file
        total += 1
print('lines:', total)
p.unlink()
```

**Remember:** Always pass `encoding='utf-8'` explicitly — the platform default differs on Windows.

**Common mistake:** `fh.read().split('\n')` on a huge file, which loads it all into RAM and then dies.

## 2. Context managers and with

`with open(...)` closes the file even if the body raises — that is what a context manager is for. Iterate a file object line by line and Python never loads the whole thing into memory, which is how you process a 40 GB log on a laptop.

```python
from pathlib import Path

p = Path('demo.txt')
with p.open('w', encoding='utf-8') as fh:
    for i in range(5):
        fh.write(f'row {i}\n')

total = 0
with p.open(encoding='utf-8') as fh:
    for line in fh:              # streams; never holds the whole file
        total += 1
print('lines:', total)
p.unlink()
```

**Remember:** Always pass `encoding='utf-8'` explicitly — the platform default differs on Windows.

**Common mistake:** `fh.read().split('\n')` on a huge file, which loads it all into RAM and then dies.

## 3. CSV files with the csv module

A DataFrame is a table with labelled columns and an index. Most real ML work is 80% reshaping tables: load, clean, group, join, aggregate. Learn `groupby` and `merge` well and you can answer most data questions without writing loops.

```python
import pandas as pd

df = pd.DataFrame({
    'city': ['pune', 'pune', 'delhi', 'delhi'],
    'sales': [10, 20, 5, 7],
})
print(df.groupby('city')['sales'].sum())

lookup = pd.DataFrame({'city': ['pune', 'delhi'], 'zone': ['west', 'north']})
print(df.merge(lookup, on='city', how='left'))
```

**Remember:** Always check `df.shape` before and after a merge — a silent row explosion means duplicate keys.

**Common mistake:** Chained assignment (`df[df.a > 1]['b'] = 0`) that writes to a copy and changes nothing.

## 4. JSON serialisation and parsing

Save the whole pipeline, not just the estimator. Also save the library versions and the training data hash — a pickle from a different scikit-learn version may load and give subtly different numbers, which is worse than failing.

```python
import joblib, sklearn, json
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
model = LogisticRegression(max_iter=500).fit(X, y)
joblib.dump(model, 'model.joblib')
json.dump({'sklearn': sklearn.__version__, 'features': X.shape[1]}, open('model_meta.json', 'w'))

loaded = joblib.load('model.joblib')
print('reloaded score', round(loaded.score(X, y), 4))
```

**Remember:** Never unpickle a model file you did not produce — pickle executes arbitrary code on load.

**Common mistake:** Shipping a pickle with no version metadata and discovering the drift six months later.

## 5. pathlib for portable paths

JSON is the lingua franca between your code, APIs and model outputs. `pathlib` makes paths work identically on Windows and Linux. Secrets belong in environment variables, never in the source file — because the source file ends up in git, and git is forever.

```python
import json, os
from pathlib import Path

config = {'model': 'small', 'epochs': 3, 'tags': ['demo']}
p = Path('config.json')
p.write_text(json.dumps(config, indent=2), encoding='utf-8')
print(json.loads(p.read_text(encoding='utf-8')))
p.unlink()

api_key = os.environ.get('MY_API_KEY')
print('key loaded from env:', bool(api_key))   # never print the key itself
```

**Remember:** Use `Path` division (`root / 'data' / 'x.csv'`) instead of string concatenation with slashes.

**Common mistake:** Committing an API key, then 'removing' it in a later commit where it still lives in history.

## 6. Encoding: UTF-8 and why it bites

Today's idea — **Encoding: UTF-8 and why it bites** — sits inside the theme of Files, JSON and the filesystem. Read it as a tool, not trivia: what job does it do, what does it assume about your data, and what breaks when that assumption is false?

```python
# Explore: Encoding: UTF-8 and why it bites
print("practice: Encoding: UTF-8 and why it bites")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Remember:** State one assumption `Encoding: UTF-8 and why it bites` makes about your data before you use it.

**Common mistake:** Copy-pasting `Encoding: UTF-8 and why it bites` from a tutorial without knowing what it assumes or when it fails.

## 7. Working with large files line by line

`with open(...)` closes the file even if the body raises — that is what a context manager is for. Iterate a file object line by line and Python never loads the whole thing into memory, which is how you process a 40 GB log on a laptop.

```python
from pathlib import Path

p = Path('demo.txt')
with p.open('w', encoding='utf-8') as fh:
    for i in range(5):
        fh.write(f'row {i}\n')

total = 0
with p.open(encoding='utf-8') as fh:
    for line in fh:              # streams; never holds the whole file
        total += 1
print('lines:', total)
p.unlink()
```

**Remember:** Always pass `encoding='utf-8'` explicitly — the platform default differs on Windows.

**Common mistake:** `fh.read().split('\n')` on a huge file, which loads it all into RAM and then dies.

## 8. Compressed files: gzip and zip

`with open(...)` closes the file even if the body raises — that is what a context manager is for. Iterate a file object line by line and Python never loads the whole thing into memory, which is how you process a 40 GB log on a laptop.

```python
from pathlib import Path

p = Path('demo.txt')
with p.open('w', encoding='utf-8') as fh:
    for i in range(5):
        fh.write(f'row {i}\n')

total = 0
with p.open(encoding='utf-8') as fh:
    for line in fh:              # streams; never holds the whole file
        total += 1
print('lines:', total)
p.unlink()
```

**Remember:** Always pass `encoding='utf-8'` explicitly — the platform default differs on Windows.

**Common mistake:** `fh.read().split('\n')` on a huge file, which loads it all into RAM and then dies.

## 9. Environment variables and secrets

JSON is the lingua franca between your code, APIs and model outputs. `pathlib` makes paths work identically on Windows and Linux. Secrets belong in environment variables, never in the source file — because the source file ends up in git, and git is forever.

```python
import json, os
from pathlib import Path

config = {'model': 'small', 'epochs': 3, 'tags': ['demo']}
p = Path('config.json')
p.write_text(json.dumps(config, indent=2), encoding='utf-8')
print(json.loads(p.read_text(encoding='utf-8')))
p.unlink()

api_key = os.environ.get('MY_API_KEY')
print('key loaded from env:', bool(api_key))   # never print the key itself
```

**Remember:** Use `Path` division (`root / 'data' / 'x.csv'`) instead of string concatenation with slashes.

**Common mistake:** Committing an API key, then 'removing' it in a later commit where it still lives in history.

## 10. A tiny dataset downloader script

JSON is the lingua franca between your code, APIs and model outputs. `pathlib` makes paths work identically on Windows and Linux. Secrets belong in environment variables, never in the source file — because the source file ends up in git, and git is forever.

```python
import json, os
from pathlib import Path

config = {'model': 'small', 'epochs': 3, 'tags': ['demo']}
p = Path('config.json')
p.write_text(json.dumps(config, indent=2), encoding='utf-8')
print(json.loads(p.read_text(encoding='utf-8')))
p.unlink()

api_key = os.environ.get('MY_API_KEY')
print('key loaded from env:', bool(api_key))   # never print the key itself
```

**Remember:** Use `Path` division (`root / 'data' / 'x.csv'`) instead of string concatenation with slashes.

**Common mistake:** Committing an API key, then 'removing' it in a later commit where it still lives in history.

---

## What you should be able to do after Day 04

- Explain **Reading and writing text files** to someone else without notes.
- Explain **Context managers and with** to someone else without notes.
- Explain **CSV files with the csv module** to someone else without notes.
- Explain **JSON serialisation and parsing** to someone else without notes.
- Explain **pathlib for portable paths** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
