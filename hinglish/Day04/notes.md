# Day 04 — Files, JSON and the filesystem

Aaj ka goal: **Files, JSON and the filesystem** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

### Aasaan Bhasha

`with open(...)` file band kar deta hai chahe body me exception aa jaaye — context manager isi ke liye hai. File object par line-by-line ghumo aur Python poori file memory me kabhi nahi laata, isi tarah laptop par 40 GB ka log process hota hai.

### Chhota code

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

**Yaad rakho:** Hamesha `encoding='utf-8'` explicitly do — Windows par platform default alag hota hai.

**Aam galti:** Badi file par `fh.read().split('\n')`, jo sab RAM me laa kar mar jaata hai.

Practice: `examples/01_reading_and_writing_text_files.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Context managers and with

### Aasaan Bhasha

`with open(...)` file band kar deta hai chahe body me exception aa jaaye — context manager isi ke liye hai. File object par line-by-line ghumo aur Python poori file memory me kabhi nahi laata, isi tarah laptop par 40 GB ka log process hota hai.

### Chhota code

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

**Yaad rakho:** Hamesha `encoding='utf-8'` explicitly do — Windows par platform default alag hota hai.

**Aam galti:** Badi file par `fh.read().split('\n')`, jo sab RAM me laa kar mar jaata hai.

Practice: `examples/02_context_managers_and_with.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. CSV files with the csv module

### Aasaan Bhasha

DataFrame ek table hai jisme labelled columns aur ek index hota hai. Asli ML ka 80% kaam tables ko reshape karna hi hai: load, clean, group, join, aggregate. `groupby` aur `merge` acche se seekh lo to zyadatar data sawaal bina loop likhe hal ho jaate hain.

### Chhota code

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

**Yaad rakho:** Merge se pehle aur baad me `df.shape` zaroor check karo — chupke se rows badhna matlab duplicate keys.

**Aam galti:** Chained assignment (`df[df.a > 1]['b'] = 0`) jo copy par likhta hai aur kuch nahi badalta.

Practice: `examples/03_csv_files_with_the_csv_module.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. JSON serialisation and parsing

### Aasaan Bhasha

Poori pipeline save karo, sirf estimator nahi. Library versions aur training data ka hash bhi save karo — alag scikit-learn version ka pickle load to ho jaayega par thoda alag numbers de sakta hai, jo fail hone se bhi bura hai.

### Chhota code

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

**Yaad rakho:** Aisi model file kabhi unpickle mat karo jo aapne nahi banayi — pickle load par arbitrary code chalata hai.

**Aam galti:** Bina version metadata ke pickle ship karna aur chhe mahine baad drift pata chalna.

Practice: `examples/04_json_serialisation_and_parsing.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. pathlib for portable paths

### Aasaan Bhasha

JSON aapke code, APIs aur model outputs ke beech ki aam bhasha hai. `pathlib` paths ko Windows aur Linux dono par ek jaisa chalata hai. Secrets environment variables me rakho, source file me kabhi nahi — kyunki source file git me pahuchti hai, aur git hamesha ke liye yaad rakhta hai.

### Chhota code

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

**Yaad rakho:** Slashes wali string joduai ke bajaye `Path` division (`root / 'data' / 'x.csv'`) use karo.

**Aam galti:** API key commit karna, phir baad ke commit me 'hata dena' jabki wo history me abhi bhi zinda hai.

Practice: `examples/05_pathlib_for_portable_paths.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Encoding: UTF-8 and why it bites

### Aasaan Bhasha

Aaj ka idea — **Encoding: UTF-8 and why it bites** — Files, JSON and the filesystem ke theme ke andar aata hai. Ise trivia nahi, ek tool ki tarah padho: ye kaam kya karta hai, aapke data ke baare me kya maan kar chalta hai, aur wo maanyata jhooth nikle to kya tootta hai?

### Chhota code

```python
# Explore: Encoding: UTF-8 and why it bites
print("practice: Encoding: UTF-8 and why it bites")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Yaad rakho:** `Encoding: UTF-8 and why it bites` use karne se pehle ek assumption likho jo ye aapke data ke baare me maanta hai.

**Aam galti:** `Encoding: UTF-8 and why it bites` ko tutorial se copy-paste kar lena bina jaane ki wo kya maanta hai aur kab fail hota hai.

Practice: `examples/06_encoding_utf_8_and_why_it_bites.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Working with large files line by line

### Aasaan Bhasha

`with open(...)` file band kar deta hai chahe body me exception aa jaaye — context manager isi ke liye hai. File object par line-by-line ghumo aur Python poori file memory me kabhi nahi laata, isi tarah laptop par 40 GB ka log process hota hai.

### Chhota code

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

**Yaad rakho:** Hamesha `encoding='utf-8'` explicitly do — Windows par platform default alag hota hai.

**Aam galti:** Badi file par `fh.read().split('\n')`, jo sab RAM me laa kar mar jaata hai.

Practice: `examples/07_working_with_large_files_line_by_line.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Compressed files: gzip and zip

### Aasaan Bhasha

`with open(...)` file band kar deta hai chahe body me exception aa jaaye — context manager isi ke liye hai. File object par line-by-line ghumo aur Python poori file memory me kabhi nahi laata, isi tarah laptop par 40 GB ka log process hota hai.

### Chhota code

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

**Yaad rakho:** Hamesha `encoding='utf-8'` explicitly do — Windows par platform default alag hota hai.

**Aam galti:** Badi file par `fh.read().split('\n')`, jo sab RAM me laa kar mar jaata hai.

Practice: `examples/08_compressed_files_gzip_and_zip.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Environment variables and secrets

### Aasaan Bhasha

JSON aapke code, APIs aur model outputs ke beech ki aam bhasha hai. `pathlib` paths ko Windows aur Linux dono par ek jaisa chalata hai. Secrets environment variables me rakho, source file me kabhi nahi — kyunki source file git me pahuchti hai, aur git hamesha ke liye yaad rakhta hai.

### Chhota code

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

**Yaad rakho:** Slashes wali string joduai ke bajaye `Path` division (`root / 'data' / 'x.csv'`) use karo.

**Aam galti:** API key commit karna, phir baad ke commit me 'hata dena' jabki wo history me abhi bhi zinda hai.

Practice: `examples/09_environment_variables_and_secrets.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. A tiny dataset downloader script

### Aasaan Bhasha

JSON aapke code, APIs aur model outputs ke beech ki aam bhasha hai. `pathlib` paths ko Windows aur Linux dono par ek jaisa chalata hai. Secrets environment variables me rakho, source file me kabhi nahi — kyunki source file git me pahuchti hai, aur git hamesha ke liye yaad rakhta hai.

### Chhota code

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

**Yaad rakho:** Slashes wali string joduai ke bajaye `Path` division (`root / 'data' / 'x.csv'`) use karo.

**Aam galti:** API key commit karna, phir baad ke commit me 'hata dena' jabki wo history me abhi bhi zinda hai.

Practice: `examples/10_a_tiny_dataset_downloader_script.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 04 ke baad aapko ye aana chahiye

- **Reading and writing text files** ko bina notes dekhe kisi dost ko samjha sakna.
- **Context managers and with** ko bina notes dekhe kisi dost ko samjha sakna.
- **CSV files with the csv module** ko bina notes dekhe kisi dost ko samjha sakna.
- **JSON serialisation and parsing** ko bina notes dekhe kisi dost ko samjha sakna.
- **pathlib for portable paths** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
