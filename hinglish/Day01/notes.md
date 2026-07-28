# Day 01 — Setting up your AI workbench

Aaj ka goal: **Setting up your AI workbench** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

### Aasaan Bhasha

Python AI me isliye nahi jeeta ki wo tez hai, balki isliye ki tez hisse (NumPy, PyTorch) andar se C aur CUDA hain, upar se aisi bhasha me lipte hue jisme aap soch sakte ho. Aapka pehla kaam ek chalta hua, alag environment banana hai aur ye aadat daalna ki aap sach me kaunsa interpreter chala rahe ho — zyadatar 'meri machine par to chalta hai' wale bugs wahin se shuru hote hain.

### Chhota code

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

**Yaad rakho:** Ye file pehle din chalao aur jab bhi kuch rahasyamay toote — 'kaunsa Python?' ka jawab turant mil jaata hai.

**Aam galti:** Ek Python se package install karna aur doosre se import karna, phir package ko dosh dena.

Practice: `examples/01_why_python_owns_ai.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Installing Python and checking the version

### Aasaan Bhasha

Python AI me isliye nahi jeeta ki wo tez hai, balki isliye ki tez hisse (NumPy, PyTorch) andar se C aur CUDA hain, upar se aisi bhasha me lipte hue jisme aap soch sakte ho. Aapka pehla kaam ek chalta hua, alag environment banana hai aur ye aadat daalna ki aap sach me kaunsa interpreter chala rahe ho — zyadatar 'meri machine par to chalta hai' wale bugs wahin se shuru hote hain.

### Chhota code

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

**Yaad rakho:** Ye file pehle din chalao aur jab bhi kuch rahasyamay toote — 'kaunsa Python?' ka jawab turant mil jaata hai.

**Aam galti:** Ek Python se package install karna aur doosre se import karna, phir package ko dosh dena.

Practice: `examples/02_installing_python_and_checking_the_versi.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Virtual environments with venv

### Aasaan Bhasha

Virtual environment ek project ke liye Python ki private copy hai. Iske bina do projects ek hi library version ke liye ladte hain. Ek baar banao, activate karo, usi me install karo, aur exact versions freeze kar do taaki koi aur aapka result dobara bana sake.

### Chhota code

```python
# python -m venv .venv
# .venv\\Scripts\\activate      (Windows)
# source .venv/bin/activate     (macOS/Linux)
# pip install numpy pandas scikit-learn
# pip freeze > requirements.txt
import sys
print(sys.executable)  # proves which Python you are actually using
```

**Yaad rakho:** Agar `pip install` chala par import fail ho raha hai, to aapne kisi doosre interpreter me install kiya hai.

**Aam galti:** Globally install karna, phir sochna ki colleague ki machine par alag result kyun aa raha hai.

Practice: `examples/03_virtual_environments_with_venv.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. pip install and requirements.txt

### Aasaan Bhasha

`pip install X` aaj ka sabse naya compatible version uthaata hai, jo wo nahi hai jo aapke colleague ko pichhle mahine mila tha. `requirements.txt` me exact versions pin karo taaki result dobara ban sake. Install hamesha activated virtual environment me karo, globally kabhi nahi.

### Chhota code

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

**Yaad rakho:** `numpy>=1.26` ek khwaahish hai; `numpy==1.26.4` ek vaada hai. Jise dobara banana ho use exactly pin karo.

**Aam galti:** Requirements file ke bina code commit karna, jisse koi bhi wo environment dobara nahi bana sakta jisne aapke numbers diye the.

Practice: `examples/04_pip_install_and_requirements_txt.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Choosing an editor: VS Code basics

### Aasaan Bhasha

Koi bhi editor chalta hai, par chaar cheezein asli waqt bachati hain: jump-to-definition, integrated debugger, interpreter selector, aur inline type errors. Debugger khaaskar seekho — shape mismatch me step karna bees `print` statements se hamesha behtar hai.

### Chhota code

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

**Yaad rakho:** `breakpoint()` built-in hai. Value dekhne ke liye ab kabhi print statements jodne ki zaroorat nahi.

**Aam galti:** Nested pipeline ko print statements se debug karna jinhe aap phir hataana bhool jaate ho.

Practice: `examples/05_choosing_an_editor_vs_code_basics.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Jupyter notebooks vs .py scripts

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

Practice: `examples/06_jupyter_notebooks_vs_py_scripts.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Google Colab and free GPUs

### Aasaan Bhasha

Colab browser me muft GPU deta hai, jo deep learning shuru karne ki sabse badi rukaawat hata deta hai. Pech ye hai ki machine aarzi hai: kuch ghante idle rehne par gayab ho jaati hai aur aapki files bhi le jaati hai. Har baar Drive mount karo ya checkpoints kisi permanent jagah save karo.

### Chhota code

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

**Yaad rakho:** Jo /content ke bahar save nahi hai wo runtime recycle hote hi khatam. Har epoch checkpoint karo.

**Aam galti:** Colab me chaar ghante bina checkpointing train karna aur ek disconnect me sab kho dena.

Practice: `examples/07_google_colab_and_free_gpus.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Reading a traceback without panic

### Aasaan Bhasha

Exceptions happy path ko failure handling se alag karte hain. Sabse sankeern exception pakdo jisse aap sach me ubhar sakte ho, baaki ko upar jaane do — khaali `except:` wahi bug chhupata hai jise dekhna sabse zaroori tha. Tracebacks neeche se upar padho: aakhri line batati hai kya toota, upar ki lines batati hain aap wahan pahuche kaise.

### Chhota code

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

**Yaad rakho:** `raise ... from e` asli wajah traceback me rakhta hai. Use kabhi nigalo mat.

**Aam galti:** Poore pipeline ke aas-paas `except: pass`, jo crash ko chupchap galat output me badal deta hai.

Practice: `examples/08_reading_a_traceback_without_panic.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Your first script: hello, model

### Aasaan Bhasha

Python AI me isliye nahi jeeta ki wo tez hai, balki isliye ki tez hisse (NumPy, PyTorch) andar se C aur CUDA hain, upar se aisi bhasha me lipte hue jisme aap soch sakte ho. Aapka pehla kaam ek chalta hua, alag environment banana hai aur ye aadat daalna ki aap sach me kaunsa interpreter chala rahe ho — zyadatar 'meri machine par to chalta hai' wale bugs wahin se shuru hote hain.

### Chhota code

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

**Yaad rakho:** Ye file pehle din chalao aur jab bhi kuch rahasyamay toote — 'kaunsa Python?' ka jawab turant mil jaata hai.

**Aam galti:** Ek Python se package install karna aur doosre se import karna, phir package ko dosh dena.

Practice: `examples/09_your_first_script_hello_model.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. How to use this 200-day course

### Aasaan Bhasha

Python AI me isliye nahi jeeta ki wo tez hai, balki isliye ki tez hisse (NumPy, PyTorch) andar se C aur CUDA hain, upar se aisi bhasha me lipte hue jisme aap soch sakte ho. Aapka pehla kaam ek chalta hua, alag environment banana hai aur ye aadat daalna ki aap sach me kaunsa interpreter chala rahe ho — zyadatar 'meri machine par to chalta hai' wale bugs wahin se shuru hote hain.

### Chhota code

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

**Yaad rakho:** Ye file pehle din chalao aur jab bhi kuch rahasyamay toote — 'kaunsa Python?' ka jawab turant mil jaata hai.

**Aam galti:** Ek Python se package install karna aur doosre se import karna, phir package ko dosh dena.

Practice: `examples/10_how_to_use_this_200_day_course.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 01 ke baad aapko ye aana chahiye

- **Why Python owns AI** ko bina notes dekhe kisi dost ko samjha sakna.
- **Installing Python and checking the version** ko bina notes dekhe kisi dost ko samjha sakna.
- **Virtual environments with venv** ko bina notes dekhe kisi dost ko samjha sakna.
- **pip install and requirements.txt** ko bina notes dekhe kisi dost ko samjha sakna.
- **Choosing an editor: VS Code basics** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
