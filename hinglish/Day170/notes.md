# Day 170 — Code-focused AI

Aaj ka goal: **Code-focused AI** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Code as a modality |
| 2 | Code completion models |
| 3 | Repository-level context |
| 4 | Test generation |
| 5 | Code review assistance |
| 6 | Refactoring with LLMs |
| 7 | Execution feedback loops |
| 8 | Security of generated code |
| 9 | Evaluating code correctness |
| 10 | Building a code assistant workflow |

---

## 1. Code as a modality

### Aasaan Bhasha

Code me wo cheez hai jo text me nahi: ek oracle. Aap use chala sakte ho. Kisi bhi code-generating loop ko output compile, test aur lint karna chahiye aur failures wapas feed karni chahiye — yahi ek loop zyadatar quality gap band kar deta hai. Generated code ko asli credentials ke saath chalne se pehle injected dependencies aur unsafe calls ke liye review karo.

### Chhota code

```python
def generate_until_passing(generate, run_tests, max_attempts=3):
    feedback = None
    for attempt in range(1, max_attempts + 1):
        code = generate(feedback)
        ok, output = run_tests(code)
        print(f'attempt {attempt}: {"PASS" if ok else "FAIL"} — {output}')
        if ok:
            return code
        feedback = output          # the failure IS the next prompt
    return None

state = {'n': 0}
def fake_gen(fb):
    state['n'] += 1
    return f'version{state["n"]}'
def fake_tests(code):
    return (code == 'version2', 'assertion failed on empty input' if code != 'version2' else 'all green')

print('final:', generate_until_passing(fake_gen, fake_tests))
```

**Yaad rakho:** Test failure ka text seedha context me wapas do — wo aapke paas ka sabse high-signal prompt hai.

**Aam galti:** Aisa generated code accept kar lena jo aisa package import karta hai jiska astitva kisi ne verify nahi kiya (asli supply-chain vector).

Practice: `examples/01_code_as_a_modality.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Code completion models

### Aasaan Bhasha

Code me wo cheez hai jo text me nahi: ek oracle. Aap use chala sakte ho. Kisi bhi code-generating loop ko output compile, test aur lint karna chahiye aur failures wapas feed karni chahiye — yahi ek loop zyadatar quality gap band kar deta hai. Generated code ko asli credentials ke saath chalne se pehle injected dependencies aur unsafe calls ke liye review karo.

### Chhota code

```python
def generate_until_passing(generate, run_tests, max_attempts=3):
    feedback = None
    for attempt in range(1, max_attempts + 1):
        code = generate(feedback)
        ok, output = run_tests(code)
        print(f'attempt {attempt}: {"PASS" if ok else "FAIL"} — {output}')
        if ok:
            return code
        feedback = output          # the failure IS the next prompt
    return None

state = {'n': 0}
def fake_gen(fb):
    state['n'] += 1
    return f'version{state["n"]}'
def fake_tests(code):
    return (code == 'version2', 'assertion failed on empty input' if code != 'version2' else 'all green')

print('final:', generate_until_passing(fake_gen, fake_tests))
```

**Yaad rakho:** Test failure ka text seedha context me wapas do — wo aapke paas ka sabse high-signal prompt hai.

**Aam galti:** Aisa generated code accept kar lena jo aisa package import karta hai jiska astitva kisi ne verify nahi kiya (asli supply-chain vector).

Practice: `examples/02_code_completion_models.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Repository-level context

### Aasaan Bhasha

Code me wo cheez hai jo text me nahi: ek oracle. Aap use chala sakte ho. Kisi bhi code-generating loop ko output compile, test aur lint karna chahiye aur failures wapas feed karni chahiye — yahi ek loop zyadatar quality gap band kar deta hai. Generated code ko asli credentials ke saath chalne se pehle injected dependencies aur unsafe calls ke liye review karo.

### Chhota code

```python
def generate_until_passing(generate, run_tests, max_attempts=3):
    feedback = None
    for attempt in range(1, max_attempts + 1):
        code = generate(feedback)
        ok, output = run_tests(code)
        print(f'attempt {attempt}: {"PASS" if ok else "FAIL"} — {output}')
        if ok:
            return code
        feedback = output          # the failure IS the next prompt
    return None

state = {'n': 0}
def fake_gen(fb):
    state['n'] += 1
    return f'version{state["n"]}'
def fake_tests(code):
    return (code == 'version2', 'assertion failed on empty input' if code != 'version2' else 'all green')

print('final:', generate_until_passing(fake_gen, fake_tests))
```

**Yaad rakho:** Test failure ka text seedha context me wapas do — wo aapke paas ka sabse high-signal prompt hai.

**Aam galti:** Aisa generated code accept kar lena jo aisa package import karta hai jiska astitva kisi ne verify nahi kiya (asli supply-chain vector).

Practice: `examples/03_repository_level_context.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Test generation

### Aasaan Bhasha

Code me wo cheez hai jo text me nahi: ek oracle. Aap use chala sakte ho. Kisi bhi code-generating loop ko output compile, test aur lint karna chahiye aur failures wapas feed karni chahiye — yahi ek loop zyadatar quality gap band kar deta hai. Generated code ko asli credentials ke saath chalne se pehle injected dependencies aur unsafe calls ke liye review karo.

### Chhota code

```python
def generate_until_passing(generate, run_tests, max_attempts=3):
    feedback = None
    for attempt in range(1, max_attempts + 1):
        code = generate(feedback)
        ok, output = run_tests(code)
        print(f'attempt {attempt}: {"PASS" if ok else "FAIL"} — {output}')
        if ok:
            return code
        feedback = output          # the failure IS the next prompt
    return None

state = {'n': 0}
def fake_gen(fb):
    state['n'] += 1
    return f'version{state["n"]}'
def fake_tests(code):
    return (code == 'version2', 'assertion failed on empty input' if code != 'version2' else 'all green')

print('final:', generate_until_passing(fake_gen, fake_tests))
```

**Yaad rakho:** Test failure ka text seedha context me wapas do — wo aapke paas ka sabse high-signal prompt hai.

**Aam galti:** Aisa generated code accept kar lena jo aisa package import karta hai jiska astitva kisi ne verify nahi kiya (asli supply-chain vector).

Practice: `examples/04_test_generation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Code review assistance

### Aasaan Bhasha

Code me wo cheez hai jo text me nahi: ek oracle. Aap use chala sakte ho. Kisi bhi code-generating loop ko output compile, test aur lint karna chahiye aur failures wapas feed karni chahiye — yahi ek loop zyadatar quality gap band kar deta hai. Generated code ko asli credentials ke saath chalne se pehle injected dependencies aur unsafe calls ke liye review karo.

### Chhota code

```python
def generate_until_passing(generate, run_tests, max_attempts=3):
    feedback = None
    for attempt in range(1, max_attempts + 1):
        code = generate(feedback)
        ok, output = run_tests(code)
        print(f'attempt {attempt}: {"PASS" if ok else "FAIL"} — {output}')
        if ok:
            return code
        feedback = output          # the failure IS the next prompt
    return None

state = {'n': 0}
def fake_gen(fb):
    state['n'] += 1
    return f'version{state["n"]}'
def fake_tests(code):
    return (code == 'version2', 'assertion failed on empty input' if code != 'version2' else 'all green')

print('final:', generate_until_passing(fake_gen, fake_tests))
```

**Yaad rakho:** Test failure ka text seedha context me wapas do — wo aapke paas ka sabse high-signal prompt hai.

**Aam galti:** Aisa generated code accept kar lena jo aisa package import karta hai jiska astitva kisi ne verify nahi kiya (asli supply-chain vector).

Practice: `examples/05_code_review_assistance.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Refactoring with LLMs

### Aasaan Bhasha

Code me wo cheez hai jo text me nahi: ek oracle. Aap use chala sakte ho. Kisi bhi code-generating loop ko output compile, test aur lint karna chahiye aur failures wapas feed karni chahiye — yahi ek loop zyadatar quality gap band kar deta hai. Generated code ko asli credentials ke saath chalne se pehle injected dependencies aur unsafe calls ke liye review karo.

### Chhota code

```python
def generate_until_passing(generate, run_tests, max_attempts=3):
    feedback = None
    for attempt in range(1, max_attempts + 1):
        code = generate(feedback)
        ok, output = run_tests(code)
        print(f'attempt {attempt}: {"PASS" if ok else "FAIL"} — {output}')
        if ok:
            return code
        feedback = output          # the failure IS the next prompt
    return None

state = {'n': 0}
def fake_gen(fb):
    state['n'] += 1
    return f'version{state["n"]}'
def fake_tests(code):
    return (code == 'version2', 'assertion failed on empty input' if code != 'version2' else 'all green')

print('final:', generate_until_passing(fake_gen, fake_tests))
```

**Yaad rakho:** Test failure ka text seedha context me wapas do — wo aapke paas ka sabse high-signal prompt hai.

**Aam galti:** Aisa generated code accept kar lena jo aisa package import karta hai jiska astitva kisi ne verify nahi kiya (asli supply-chain vector).

Practice: `examples/06_refactoring_with_llms.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Execution feedback loops

### Aasaan Bhasha

Code me wo cheez hai jo text me nahi: ek oracle. Aap use chala sakte ho. Kisi bhi code-generating loop ko output compile, test aur lint karna chahiye aur failures wapas feed karni chahiye — yahi ek loop zyadatar quality gap band kar deta hai. Generated code ko asli credentials ke saath chalne se pehle injected dependencies aur unsafe calls ke liye review karo.

### Chhota code

```python
def generate_until_passing(generate, run_tests, max_attempts=3):
    feedback = None
    for attempt in range(1, max_attempts + 1):
        code = generate(feedback)
        ok, output = run_tests(code)
        print(f'attempt {attempt}: {"PASS" if ok else "FAIL"} — {output}')
        if ok:
            return code
        feedback = output          # the failure IS the next prompt
    return None

state = {'n': 0}
def fake_gen(fb):
    state['n'] += 1
    return f'version{state["n"]}'
def fake_tests(code):
    return (code == 'version2', 'assertion failed on empty input' if code != 'version2' else 'all green')

print('final:', generate_until_passing(fake_gen, fake_tests))
```

**Yaad rakho:** Test failure ka text seedha context me wapas do — wo aapke paas ka sabse high-signal prompt hai.

**Aam galti:** Aisa generated code accept kar lena jo aisa package import karta hai jiska astitva kisi ne verify nahi kiya (asli supply-chain vector).

Practice: `examples/07_execution_feedback_loops.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Security of generated code

### Aasaan Bhasha

Code me wo cheez hai jo text me nahi: ek oracle. Aap use chala sakte ho. Kisi bhi code-generating loop ko output compile, test aur lint karna chahiye aur failures wapas feed karni chahiye — yahi ek loop zyadatar quality gap band kar deta hai. Generated code ko asli credentials ke saath chalne se pehle injected dependencies aur unsafe calls ke liye review karo.

### Chhota code

```python
def generate_until_passing(generate, run_tests, max_attempts=3):
    feedback = None
    for attempt in range(1, max_attempts + 1):
        code = generate(feedback)
        ok, output = run_tests(code)
        print(f'attempt {attempt}: {"PASS" if ok else "FAIL"} — {output}')
        if ok:
            return code
        feedback = output          # the failure IS the next prompt
    return None

state = {'n': 0}
def fake_gen(fb):
    state['n'] += 1
    return f'version{state["n"]}'
def fake_tests(code):
    return (code == 'version2', 'assertion failed on empty input' if code != 'version2' else 'all green')

print('final:', generate_until_passing(fake_gen, fake_tests))
```

**Yaad rakho:** Test failure ka text seedha context me wapas do — wo aapke paas ka sabse high-signal prompt hai.

**Aam galti:** Aisa generated code accept kar lena jo aisa package import karta hai jiska astitva kisi ne verify nahi kiya (asli supply-chain vector).

Practice: `examples/08_security_of_generated_code.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Evaluating code correctness

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

Practice: `examples/09_evaluating_code_correctness.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Building a code assistant workflow

### Aasaan Bhasha

Projects wahi jagah hain jahan seekha hua chipakta hai. Pehle ek patli end-to-end slice banao — data load, kuch bewakoof train, evaluate, ek prediction serve — phir ek-ek layer sudharo. Pehle din chalne wala baseline us perfect model se behtar hai jo kabhi ship hi nahi hota.

### Chhota code

```python
STEPS = [
    '1. Define the decision the model supports and the metric that measures it',
    '2. Get the data; write the loader; assert the schema',
    '3. Dumb baseline (mean / majority class) -> this is the bar',
    '4. Simple model + honest validation split',
    '5. Error analysis: look at 30 wrong predictions by hand',
    '6. Improve the biggest error bucket, not the leaderboard',
    '7. Serve it, log inputs and outputs, monitor drift',
]
for s in STEPS:
    print(s)
```

**Yaad rakho:** Hyperparameters tune karne me ek din lagane se pehle galat predictions dekhne me ek ghanta lagao.

**Aam galti:** Chhe hafte feature engineering karna bina kisi baseline ke jo sabit kare ki kisi cheez se fayda hua.

Practice: `examples/10_building_a_code_assistant_workflow.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 170 ke baad aapko ye aana chahiye

- **Code as a modality** ko bina notes dekhe kisi dost ko samjha sakna.
- **Code completion models** ko bina notes dekhe kisi dost ko samjha sakna.
- **Repository-level context** ko bina notes dekhe kisi dost ko samjha sakna.
- **Test generation** ko bina notes dekhe kisi dost ko samjha sakna.
- **Code review assistance** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
