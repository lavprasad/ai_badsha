# Day 01 — Setting up your AI workbench

Today's goal: work through **setting up your ai workbench** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Why Python owns AI |
| 2 | Installing Python and checking the version |
| 3 | Virtual environments with venv |
| 4 | pip install and requirements.txt |
| 5 | Choosing an editor: VS Code basics |
| 6 | Jupyter notebooks vs .py scripts |
| 7 | Google Colab and free GPUs |
| 8 | Reading a traceback without panic |
| 9 | Your first script: hello, model |
| 10 | How to use this 200-day course |

---

## 1. Why Python owns AI

Python won AI not because it is fast but because the fast parts (NumPy, PyTorch) are C and CUDA underneath, wrapped in a language you can think in. Your first job is a working, isolated environment and the habit of checking which interpreter you are actually running — most 'it works on my machine' bugs start there.

```python
import sys, platform

print('python  ', sys.version.split()[0])
print('binary  ', sys.executable)      # WHICH python is this?
print('platform', platform.system(), platform.machine())

for mod in ('numpy', 'pandas', 'sklearn', 'torch'):
    try:
        m = __import__(mod)
        print(f'{mod:<8} {getattr(m, "__version__", "?")}')
    except ImportError:
        print(f'{mod:<8} not installed')
```

**Remember:** Run this file on day one and whenever anything mysterious breaks — it answers 'which Python?' instantly.

**Common mistake:** Installing a package with one Python and importing it with another, then blaming the package.

## 2. Installing Python and checking the version

Python won AI not because it is fast but because the fast parts (NumPy, PyTorch) are C and CUDA underneath, wrapped in a language you can think in. Your first job is a working, isolated environment and the habit of checking which interpreter you are actually running — most 'it works on my machine' bugs start there.

```python
import sys, platform

print('python  ', sys.version.split()[0])
print('binary  ', sys.executable)      # WHICH python is this?
print('platform', platform.system(), platform.machine())

for mod in ('numpy', 'pandas', 'sklearn', 'torch'):
    try:
        m = __import__(mod)
        print(f'{mod:<8} {getattr(m, "__version__", "?")}')
    except ImportError:
        print(f'{mod:<8} not installed')
```

**Remember:** Run this file on day one and whenever anything mysterious breaks — it answers 'which Python?' instantly.

**Common mistake:** Installing a package with one Python and importing it with another, then blaming the package.

## 3. Virtual environments with venv

A virtual environment is a private copy of Python for one project. Without it, two projects fight over the same library versions. Create it once, activate it, install into it, and freeze the exact versions so someone else can reproduce your run.

```python
# python -m venv .venv
# .venv\\Scripts\\activate      (Windows)
# source .venv/bin/activate     (macOS/Linux)
# pip install numpy pandas scikit-learn
# pip freeze > requirements.txt
import sys
print(sys.executable)  # proves which Python you are actually using
```

**Remember:** If `pip install` worked but the import fails, you installed into a different interpreter.

**Common mistake:** Installing globally, then wondering why a colleague's machine gets different results.

## 4. pip install and requirements.txt

`pip install X` grabs the newest compatible version today, which is not the version your colleague got last month. Pin exact versions in `requirements.txt` so a result is reproducible. Install into an activated virtual environment, never globally.

```python
import subprocess, sys

# What is actually installed, in requirements.txt format:
out = subprocess.run([sys.executable, '-m', 'pip', 'freeze'],
                     capture_output=True, text=True).stdout
lines = [l for l in out.splitlines() if l and not l.startswith('-e')]
print(f'{len(lines)} pinned packages, first 5:')
for l in lines[:5]:
    print(' ', l)
print('\nSave with:  pip freeze > requirements.txt')
print('Restore with: pip install -r requirements.txt')
```

**Remember:** `numpy>=1.26` is a wish; `numpy==1.26.4` is a promise. Pin exactly for anything you must reproduce.

**Common mistake:** Committing code without the requirements file, so nobody can rebuild the environment that produced your numbers.

## 5. Choosing an editor: VS Code basics

Any editor works, but four features save real time: jump-to-definition, an integrated debugger, an interpreter selector, and inline type errors. Learn the debugger specifically — stepping through a shape mismatch beats twenty `print` statements every time.

```python
# The debugger you already have, no editor required:
def normalise(values):
    total = sum(values)
    # breakpoint()      # <- uncomment: drops you into an interactive prompt here
    return [v / total for v in values]

print(normalise([1, 2, 3]))
print('''
At a breakpoint:  n = next line   s = step into   c = continue
                  p expr = print   l = list source  q = quit
''')
```

**Remember:** `breakpoint()` is built in. You never need to add print statements to inspect a value again.

**Common mistake:** Debugging a nested pipeline with print statements you then forget to remove.

## 6. Jupyter notebooks vs .py scripts

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

## 7. Google Colab and free GPUs

Colab gives you a free GPU in a browser, which removes the biggest barrier to starting deep learning. The catch is that the machine is temporary: it disappears after a few hours of idleness and takes your files with it. Mount Drive or save checkpoints to somewhere permanent, every time.

```python
import os

def on_colab():
    return 'COLAB_GPU' in os.environ or os.path.exists('/content')

print('running on Colab:', on_colab())
print('''
Colab survival rules:
  1. Save checkpoints to Drive, not /content — /content is wiped.
  2. Re-run the pip install cell after every reconnect.
  3. Check the GPU you were given: !nvidia-smi
  4. Long jobs get disconnected. Checkpoint every epoch.
''')
```

**Remember:** Anything not saved outside /content is gone when the runtime recycles. Checkpoint every epoch.

**Common mistake:** Training for four hours in Colab with no checkpointing and losing everything to a disconnect.

## 8. Reading a traceback without panic

Exceptions separate the happy path from failure handling. Catch the narrowest exception you can actually recover from, and let the rest propagate — a bare `except:` hides the bug you most needed to see. Read tracebacks bottom-up: the last line is what broke, the lines above are how you got there.

```python
class DataContractError(ValueError):
    """Raised when input data violates the agreed schema."""

def load_age(raw):
    try:
        age = int(raw)
    except (TypeError, ValueError) as e:
        raise DataContractError(f'age must be an integer, got {raw!r}') from e
    if not 0 <= age <= 130:
        raise DataContractError(f'age out of range: {age}')
    return age

for value in ('42', 'abc', '999'):
    try:
        print(load_age(value))
    except DataContractError as e:
        print('rejected:', e)
```

**Remember:** `raise ... from e` keeps the original cause in the traceback. Never swallow it.

**Common mistake:** `except: pass` around a whole pipeline, turning a crash into silently wrong output.

## 9. Your first script: hello, model

Python won AI not because it is fast but because the fast parts (NumPy, PyTorch) are C and CUDA underneath, wrapped in a language you can think in. Your first job is a working, isolated environment and the habit of checking which interpreter you are actually running — most 'it works on my machine' bugs start there.

```python
import sys, platform

print('python  ', sys.version.split()[0])
print('binary  ', sys.executable)      # WHICH python is this?
print('platform', platform.system(), platform.machine())

for mod in ('numpy', 'pandas', 'sklearn', 'torch'):
    try:
        m = __import__(mod)
        print(f'{mod:<8} {getattr(m, "__version__", "?")}')
    except ImportError:
        print(f'{mod:<8} not installed')
```

**Remember:** Run this file on day one and whenever anything mysterious breaks — it answers 'which Python?' instantly.

**Common mistake:** Installing a package with one Python and importing it with another, then blaming the package.

## 10. How to use this 200-day course

Python won AI not because it is fast but because the fast parts (NumPy, PyTorch) are C and CUDA underneath, wrapped in a language you can think in. Your first job is a working, isolated environment and the habit of checking which interpreter you are actually running — most 'it works on my machine' bugs start there.

```python
import sys, platform

print('python  ', sys.version.split()[0])
print('binary  ', sys.executable)      # WHICH python is this?
print('platform', platform.system(), platform.machine())

for mod in ('numpy', 'pandas', 'sklearn', 'torch'):
    try:
        m = __import__(mod)
        print(f'{mod:<8} {getattr(m, "__version__", "?")}')
    except ImportError:
        print(f'{mod:<8} not installed')
```

**Remember:** Run this file on day one and whenever anything mysterious breaks — it answers 'which Python?' instantly.

**Common mistake:** Installing a package with one Python and importing it with another, then blaming the package.

---

## What you should be able to do after Day 01

- Explain **Why Python owns AI** to someone else without notes.
- Explain **Installing Python and checking the version** to someone else without notes.
- Explain **Virtual environments with venv** to someone else without notes.
- Explain **pip install and requirements.txt** to someone else without notes.
- Explain **Choosing an editor: VS Code basics** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
