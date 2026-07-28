# Day 142 — Model evaluation for LLMs

Aaj ka goal: **Model evaluation for LLMs** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Why standard benchmarks mislead |
| 2 | Building a golden dataset |
| 3 | Task-specific automatic metrics |
| 4 | Exact match and structured checks |
| 5 | LLM-as-judge |
| 6 | Calibrating a judge against humans |
| 7 | Pairwise comparison and Elo |
| 8 | Regression testing prompts |
| 9 | Evaluating latency and cost too |
| 10 | An eval harness you run on every change |

---

## 1. Why standard benchmarks mislead

### Aasaan Bhasha

Vibes prompt change se nahi bachte. Asli inputs ka chhota golden set banao expected outputs ke saath, har change par chalao, aur score track karo. Open-ended quality ke liye LLM judge use karo, par pehle judge ko human ratings se calibrate karo.

### Chhota code

```python
GOLDEN = [
    {'input': 'charged twice', 'expect': 'BILLING'},
    {'input': 'crashes on upload', 'expect': 'BUG'},
    {'input': 'please add dark mode', 'expect': 'FEATURE'},
]

def classify(text):                      # stand-in for the real model call
    t = text.lower()
    if 'charg' in t or 'bill' in t:
        return 'BILLING'
    if 'crash' in t or 'error' in t:
        return 'BUG'
    return 'FEATURE'

hits = sum(classify(c['input']) == c['expect'] for c in GOLDEN)
print(f'eval score {hits}/{len(GOLDEN)}')
assert hits == len(GOLDEN), 'regression: fix before shipping'
```

**Yaad rakho:** Aapke chune hue 50 asli examples 5000 synthetic examples se behtar hain jinhe kisi ne check hi nahi kiya.

**Aam galti:** Shukravaar ko bina eval ke prompt badalna aur somvaar ko customers se pata chalna.

Practice: `examples/01_why_standard_benchmarks_mislead.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Building a golden dataset

### Aasaan Bhasha

Vibes prompt change se nahi bachte. Asli inputs ka chhota golden set banao expected outputs ke saath, har change par chalao, aur score track karo. Open-ended quality ke liye LLM judge use karo, par pehle judge ko human ratings se calibrate karo.

### Chhota code

```python
GOLDEN = [
    {'input': 'charged twice', 'expect': 'BILLING'},
    {'input': 'crashes on upload', 'expect': 'BUG'},
    {'input': 'please add dark mode', 'expect': 'FEATURE'},
]

def classify(text):                      # stand-in for the real model call
    t = text.lower()
    if 'charg' in t or 'bill' in t:
        return 'BILLING'
    if 'crash' in t or 'error' in t:
        return 'BUG'
    return 'FEATURE'

hits = sum(classify(c['input']) == c['expect'] for c in GOLDEN)
print(f'eval score {hits}/{len(GOLDEN)}')
assert hits == len(GOLDEN), 'regression: fix before shipping'
```

**Yaad rakho:** Aapke chune hue 50 asli examples 5000 synthetic examples se behtar hain jinhe kisi ne check hi nahi kiya.

**Aam galti:** Shukravaar ko bina eval ke prompt badalna aur somvaar ko customers se pata chalna.

Practice: `examples/02_building_a_golden_dataset.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Task-specific automatic metrics

### Aasaan Bhasha

Vibes prompt change se nahi bachte. Asli inputs ka chhota golden set banao expected outputs ke saath, har change par chalao, aur score track karo. Open-ended quality ke liye LLM judge use karo, par pehle judge ko human ratings se calibrate karo.

### Chhota code

```python
GOLDEN = [
    {'input': 'charged twice', 'expect': 'BILLING'},
    {'input': 'crashes on upload', 'expect': 'BUG'},
    {'input': 'please add dark mode', 'expect': 'FEATURE'},
]

def classify(text):                      # stand-in for the real model call
    t = text.lower()
    if 'charg' in t or 'bill' in t:
        return 'BILLING'
    if 'crash' in t or 'error' in t:
        return 'BUG'
    return 'FEATURE'

hits = sum(classify(c['input']) == c['expect'] for c in GOLDEN)
print(f'eval score {hits}/{len(GOLDEN)}')
assert hits == len(GOLDEN), 'regression: fix before shipping'
```

**Yaad rakho:** Aapke chune hue 50 asli examples 5000 synthetic examples se behtar hain jinhe kisi ne check hi nahi kiya.

**Aam galti:** Shukravaar ko bina eval ke prompt badalna aur somvaar ko customers se pata chalna.

Practice: `examples/03_task_specific_automatic_metrics.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Exact match and structured checks

### Aasaan Bhasha

Vibes prompt change se nahi bachte. Asli inputs ka chhota golden set banao expected outputs ke saath, har change par chalao, aur score track karo. Open-ended quality ke liye LLM judge use karo, par pehle judge ko human ratings se calibrate karo.

### Chhota code

```python
GOLDEN = [
    {'input': 'charged twice', 'expect': 'BILLING'},
    {'input': 'crashes on upload', 'expect': 'BUG'},
    {'input': 'please add dark mode', 'expect': 'FEATURE'},
]

def classify(text):                      # stand-in for the real model call
    t = text.lower()
    if 'charg' in t or 'bill' in t:
        return 'BILLING'
    if 'crash' in t or 'error' in t:
        return 'BUG'
    return 'FEATURE'

hits = sum(classify(c['input']) == c['expect'] for c in GOLDEN)
print(f'eval score {hits}/{len(GOLDEN)}')
assert hits == len(GOLDEN), 'regression: fix before shipping'
```

**Yaad rakho:** Aapke chune hue 50 asli examples 5000 synthetic examples se behtar hain jinhe kisi ne check hi nahi kiya.

**Aam galti:** Shukravaar ko bina eval ke prompt badalna aur somvaar ko customers se pata chalna.

Practice: `examples/04_exact_match_and_structured_checks.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. LLM-as-judge

### Aasaan Bhasha

Vibes prompt change se nahi bachte. Asli inputs ka chhota golden set banao expected outputs ke saath, har change par chalao, aur score track karo. Open-ended quality ke liye LLM judge use karo, par pehle judge ko human ratings se calibrate karo.

### Chhota code

```python
GOLDEN = [
    {'input': 'charged twice', 'expect': 'BILLING'},
    {'input': 'crashes on upload', 'expect': 'BUG'},
    {'input': 'please add dark mode', 'expect': 'FEATURE'},
]

def classify(text):                      # stand-in for the real model call
    t = text.lower()
    if 'charg' in t or 'bill' in t:
        return 'BILLING'
    if 'crash' in t or 'error' in t:
        return 'BUG'
    return 'FEATURE'

hits = sum(classify(c['input']) == c['expect'] for c in GOLDEN)
print(f'eval score {hits}/{len(GOLDEN)}')
assert hits == len(GOLDEN), 'regression: fix before shipping'
```

**Yaad rakho:** Aapke chune hue 50 asli examples 5000 synthetic examples se behtar hain jinhe kisi ne check hi nahi kiya.

**Aam galti:** Shukravaar ko bina eval ke prompt badalna aur somvaar ko customers se pata chalna.

Practice: `examples/05_llm_as_judge.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Calibrating a judge against humans

### Aasaan Bhasha

Vibes prompt change se nahi bachte. Asli inputs ka chhota golden set banao expected outputs ke saath, har change par chalao, aur score track karo. Open-ended quality ke liye LLM judge use karo, par pehle judge ko human ratings se calibrate karo.

### Chhota code

```python
GOLDEN = [
    {'input': 'charged twice', 'expect': 'BILLING'},
    {'input': 'crashes on upload', 'expect': 'BUG'},
    {'input': 'please add dark mode', 'expect': 'FEATURE'},
]

def classify(text):                      # stand-in for the real model call
    t = text.lower()
    if 'charg' in t or 'bill' in t:
        return 'BILLING'
    if 'crash' in t or 'error' in t:
        return 'BUG'
    return 'FEATURE'

hits = sum(classify(c['input']) == c['expect'] for c in GOLDEN)
print(f'eval score {hits}/{len(GOLDEN)}')
assert hits == len(GOLDEN), 'regression: fix before shipping'
```

**Yaad rakho:** Aapke chune hue 50 asli examples 5000 synthetic examples se behtar hain jinhe kisi ne check hi nahi kiya.

**Aam galti:** Shukravaar ko bina eval ke prompt badalna aur somvaar ko customers se pata chalna.

Practice: `examples/06_calibrating_a_judge_against_humans.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Pairwise comparison and Elo

### Aasaan Bhasha

Vibes prompt change se nahi bachte. Asli inputs ka chhota golden set banao expected outputs ke saath, har change par chalao, aur score track karo. Open-ended quality ke liye LLM judge use karo, par pehle judge ko human ratings se calibrate karo.

### Chhota code

```python
GOLDEN = [
    {'input': 'charged twice', 'expect': 'BILLING'},
    {'input': 'crashes on upload', 'expect': 'BUG'},
    {'input': 'please add dark mode', 'expect': 'FEATURE'},
]

def classify(text):                      # stand-in for the real model call
    t = text.lower()
    if 'charg' in t or 'bill' in t:
        return 'BILLING'
    if 'crash' in t or 'error' in t:
        return 'BUG'
    return 'FEATURE'

hits = sum(classify(c['input']) == c['expect'] for c in GOLDEN)
print(f'eval score {hits}/{len(GOLDEN)}')
assert hits == len(GOLDEN), 'regression: fix before shipping'
```

**Yaad rakho:** Aapke chune hue 50 asli examples 5000 synthetic examples se behtar hain jinhe kisi ne check hi nahi kiya.

**Aam galti:** Shukravaar ko bina eval ke prompt badalna aur somvaar ko customers se pata chalna.

Practice: `examples/07_pairwise_comparison_and_elo.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Regression testing prompts

### Aasaan Bhasha

Vibes prompt change se nahi bachte. Asli inputs ka chhota golden set banao expected outputs ke saath, har change par chalao, aur score track karo. Open-ended quality ke liye LLM judge use karo, par pehle judge ko human ratings se calibrate karo.

### Chhota code

```python
GOLDEN = [
    {'input': 'charged twice', 'expect': 'BILLING'},
    {'input': 'crashes on upload', 'expect': 'BUG'},
    {'input': 'please add dark mode', 'expect': 'FEATURE'},
]

def classify(text):                      # stand-in for the real model call
    t = text.lower()
    if 'charg' in t or 'bill' in t:
        return 'BILLING'
    if 'crash' in t or 'error' in t:
        return 'BUG'
    return 'FEATURE'

hits = sum(classify(c['input']) == c['expect'] for c in GOLDEN)
print(f'eval score {hits}/{len(GOLDEN)}')
assert hits == len(GOLDEN), 'regression: fix before shipping'
```

**Yaad rakho:** Aapke chune hue 50 asli examples 5000 synthetic examples se behtar hain jinhe kisi ne check hi nahi kiya.

**Aam galti:** Shukravaar ko bina eval ke prompt badalna aur somvaar ko customers se pata chalna.

Practice: `examples/08_regression_testing_prompts.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Evaluating latency and cost too

### Aasaan Bhasha

Vibes prompt change se nahi bachte. Asli inputs ka chhota golden set banao expected outputs ke saath, har change par chalao, aur score track karo. Open-ended quality ke liye LLM judge use karo, par pehle judge ko human ratings se calibrate karo.

### Chhota code

```python
GOLDEN = [
    {'input': 'charged twice', 'expect': 'BILLING'},
    {'input': 'crashes on upload', 'expect': 'BUG'},
    {'input': 'please add dark mode', 'expect': 'FEATURE'},
]

def classify(text):                      # stand-in for the real model call
    t = text.lower()
    if 'charg' in t or 'bill' in t:
        return 'BILLING'
    if 'crash' in t or 'error' in t:
        return 'BUG'
    return 'FEATURE'

hits = sum(classify(c['input']) == c['expect'] for c in GOLDEN)
print(f'eval score {hits}/{len(GOLDEN)}')
assert hits == len(GOLDEN), 'regression: fix before shipping'
```

**Yaad rakho:** Aapke chune hue 50 asli examples 5000 synthetic examples se behtar hain jinhe kisi ne check hi nahi kiya.

**Aam galti:** Shukravaar ko bina eval ke prompt badalna aur somvaar ko customers se pata chalna.

Practice: `examples/09_evaluating_latency_and_cost_too.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. An eval harness you run on every change

### Aasaan Bhasha

Vibes prompt change se nahi bachte. Asli inputs ka chhota golden set banao expected outputs ke saath, har change par chalao, aur score track karo. Open-ended quality ke liye LLM judge use karo, par pehle judge ko human ratings se calibrate karo.

### Chhota code

```python
GOLDEN = [
    {'input': 'charged twice', 'expect': 'BILLING'},
    {'input': 'crashes on upload', 'expect': 'BUG'},
    {'input': 'please add dark mode', 'expect': 'FEATURE'},
]

def classify(text):                      # stand-in for the real model call
    t = text.lower()
    if 'charg' in t or 'bill' in t:
        return 'BILLING'
    if 'crash' in t or 'error' in t:
        return 'BUG'
    return 'FEATURE'

hits = sum(classify(c['input']) == c['expect'] for c in GOLDEN)
print(f'eval score {hits}/{len(GOLDEN)}')
assert hits == len(GOLDEN), 'regression: fix before shipping'
```

**Yaad rakho:** Aapke chune hue 50 asli examples 5000 synthetic examples se behtar hain jinhe kisi ne check hi nahi kiya.

**Aam galti:** Shukravaar ko bina eval ke prompt badalna aur somvaar ko customers se pata chalna.

Practice: `examples/10_an_eval_harness_you_run_on_every_change.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 142 ke baad aapko ye aana chahiye

- **Why standard benchmarks mislead** ko bina notes dekhe kisi dost ko samjha sakna.
- **Building a golden dataset** ko bina notes dekhe kisi dost ko samjha sakna.
- **Task-specific automatic metrics** ko bina notes dekhe kisi dost ko samjha sakna.
- **Exact match and structured checks** ko bina notes dekhe kisi dost ko samjha sakna.
- **LLM-as-judge** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
