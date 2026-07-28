# Day 170 — Code-focused AI

Today's goal: work through **Code-focused AI** — ten concepts, ten runnable examples, five questions.

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

Code has something text does not: an oracle. You can run it. Any code-generating loop should compile, test and lint the output and feed failures back — that single loop closes most of the quality gap. Review generated code for injected dependencies and unsafe calls before it ever runs with real credentials.

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

**Remember:** Feed the test failure text straight back as context — it is the highest-signal prompt you have.

**Common mistake:** Accepting generated code that imports a package name nobody verified exists (a real supply-chain vector).

Practice: open `examples/01_code_as_a_modality.py`, predict the output, change one line, predict again.

## 2. Code completion models

Code has something text does not: an oracle. You can run it. Any code-generating loop should compile, test and lint the output and feed failures back — that single loop closes most of the quality gap. Review generated code for injected dependencies and unsafe calls before it ever runs with real credentials.

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

**Remember:** Feed the test failure text straight back as context — it is the highest-signal prompt you have.

**Common mistake:** Accepting generated code that imports a package name nobody verified exists (a real supply-chain vector).

Practice: open `examples/02_code_completion_models.py`, predict the output, change one line, predict again.

## 3. Repository-level context

Code has something text does not: an oracle. You can run it. Any code-generating loop should compile, test and lint the output and feed failures back — that single loop closes most of the quality gap. Review generated code for injected dependencies and unsafe calls before it ever runs with real credentials.

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

**Remember:** Feed the test failure text straight back as context — it is the highest-signal prompt you have.

**Common mistake:** Accepting generated code that imports a package name nobody verified exists (a real supply-chain vector).

Practice: open `examples/03_repository_level_context.py`, predict the output, change one line, predict again.

## 4. Test generation

Code has something text does not: an oracle. You can run it. Any code-generating loop should compile, test and lint the output and feed failures back — that single loop closes most of the quality gap. Review generated code for injected dependencies and unsafe calls before it ever runs with real credentials.

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

**Remember:** Feed the test failure text straight back as context — it is the highest-signal prompt you have.

**Common mistake:** Accepting generated code that imports a package name nobody verified exists (a real supply-chain vector).

Practice: open `examples/04_test_generation.py`, predict the output, change one line, predict again.

## 5. Code review assistance

Code has something text does not: an oracle. You can run it. Any code-generating loop should compile, test and lint the output and feed failures back — that single loop closes most of the quality gap. Review generated code for injected dependencies and unsafe calls before it ever runs with real credentials.

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

**Remember:** Feed the test failure text straight back as context — it is the highest-signal prompt you have.

**Common mistake:** Accepting generated code that imports a package name nobody verified exists (a real supply-chain vector).

Practice: open `examples/05_code_review_assistance.py`, predict the output, change one line, predict again.

## 6. Refactoring with LLMs

Code has something text does not: an oracle. You can run it. Any code-generating loop should compile, test and lint the output and feed failures back — that single loop closes most of the quality gap. Review generated code for injected dependencies and unsafe calls before it ever runs with real credentials.

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

**Remember:** Feed the test failure text straight back as context — it is the highest-signal prompt you have.

**Common mistake:** Accepting generated code that imports a package name nobody verified exists (a real supply-chain vector).

Practice: open `examples/06_refactoring_with_llms.py`, predict the output, change one line, predict again.

## 7. Execution feedback loops

Code has something text does not: an oracle. You can run it. Any code-generating loop should compile, test and lint the output and feed failures back — that single loop closes most of the quality gap. Review generated code for injected dependencies and unsafe calls before it ever runs with real credentials.

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

**Remember:** Feed the test failure text straight back as context — it is the highest-signal prompt you have.

**Common mistake:** Accepting generated code that imports a package name nobody verified exists (a real supply-chain vector).

Practice: open `examples/07_execution_feedback_loops.py`, predict the output, change one line, predict again.

## 8. Security of generated code

Code has something text does not: an oracle. You can run it. Any code-generating loop should compile, test and lint the output and feed failures back — that single loop closes most of the quality gap. Review generated code for injected dependencies and unsafe calls before it ever runs with real credentials.

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

**Remember:** Feed the test failure text straight back as context — it is the highest-signal prompt you have.

**Common mistake:** Accepting generated code that imports a package name nobody verified exists (a real supply-chain vector).

Practice: open `examples/08_security_of_generated_code.py`, predict the output, change one line, predict again.

## 9. Evaluating code correctness

Vibes do not survive a prompt change. Build a small golden set of real inputs with expected outputs, run it on every change, and track the score. Use an LLM judge for open-ended quality, but calibrate the judge against human ratings first.

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

**Remember:** 50 real examples you curated beat 5000 synthetic ones nobody checked.

**Common mistake:** Changing the prompt on Friday with no eval and finding out from customers on Monday.

Practice: open `examples/09_evaluating_code_correctness.py`, predict the output, change one line, predict again.

## 10. Building a code assistant workflow

Projects are where the learning sticks. Build a thin end-to-end slice first — load data, train something dumb, evaluate, serve one prediction — then improve one layer at a time. A working baseline on day one beats a perfect model that never ships.

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

**Remember:** Spend an hour looking at wrong predictions before you spend a day tuning hyperparameters.

**Common mistake:** Six weeks of feature engineering with no baseline to prove any of it helped.

Practice: open `examples/10_building_a_code_assistant_workflow.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 170

- Explain **Code as a modality** to someone else without notes.
- Explain **Code completion models** to someone else without notes.
- Explain **Repository-level context** to someone else without notes.
- Explain **Test generation** to someone else without notes.
- Explain **Code review assistance** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
