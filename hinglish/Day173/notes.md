# Day 173 — Multi-agent and orchestration

Aaj ka goal: **Multi-agent and orchestration** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | When one agent is not enough |
| 2 | Orchestrator and worker patterns |
| 3 | Parallel fan-out and synthesis |
| 4 | Specialised agent roles |
| 5 | Shared state and handoffs |
| 6 | Cost multiplication risk |
| 7 | Debugging multi-agent runs |
| 8 | Deterministic orchestration code |
| 9 | Evaluating a multi-agent system |
| 10 | Simplifying back to one agent |

---

## 1. When one agent is not enough

### Aasaan Bhasha

Agent ek loop hai: model tool chunta hai, aapka code use chalata hai, result wapas context me jaata hai, aur ye dohraata hai jab tak kaam poora na ho. Taakat tools se aati hai, prompt se nahi. Iterations cap karo, har step log karo, aur kisi bhi irreversible cheez se pehle confirmation maango.

### Chhota code

```python
def calculator(expr):
    return eval(expr, {'__builtins__': {}}, {})   # locked-down namespace only

TOOLS = {'calc': calculator}

def agent_loop(plan, max_steps=5):
    """`plan` stands in for the model's tool choices."""
    history = []
    for step, (tool, arg) in enumerate(plan[:max_steps], 1):
        result = TOOLS[tool](arg)
        history.append((step, tool, arg, result))
        print(f'step {step}: {tool}({arg!r}) -> {result}')
    return history

agent_loop([('calc', '2 + 2'), ('calc', '(2 + 2) * 10')])
```

**Yaad rakho:** Loop hamesha bounded rakho. Bina limit ka agent paisa jalata hai aur fail hone ke naye tareeke dhoondh leta hai.

**Aam galti:** Agent ko shell tool dena bina allowlist aur bina confirmation step ke.

Practice: `examples/01_when_one_agent_is_not_enough.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Orchestrator and worker patterns

### Aasaan Bhasha

Agent ek loop hai: model tool chunta hai, aapka code use chalata hai, result wapas context me jaata hai, aur ye dohraata hai jab tak kaam poora na ho. Taakat tools se aati hai, prompt se nahi. Iterations cap karo, har step log karo, aur kisi bhi irreversible cheez se pehle confirmation maango.

### Chhota code

```python
def calculator(expr):
    return eval(expr, {'__builtins__': {}}, {})   # locked-down namespace only

TOOLS = {'calc': calculator}

def agent_loop(plan, max_steps=5):
    """`plan` stands in for the model's tool choices."""
    history = []
    for step, (tool, arg) in enumerate(plan[:max_steps], 1):
        result = TOOLS[tool](arg)
        history.append((step, tool, arg, result))
        print(f'step {step}: {tool}({arg!r}) -> {result}')
    return history

agent_loop([('calc', '2 + 2'), ('calc', '(2 + 2) * 10')])
```

**Yaad rakho:** Loop hamesha bounded rakho. Bina limit ka agent paisa jalata hai aur fail hone ke naye tareeke dhoondh leta hai.

**Aam galti:** Agent ko shell tool dena bina allowlist aur bina confirmation step ke.

Practice: `examples/02_orchestrator_and_worker_patterns.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Parallel fan-out and synthesis

### Aasaan Bhasha

Agent ek loop hai: model tool chunta hai, aapka code use chalata hai, result wapas context me jaata hai, aur ye dohraata hai jab tak kaam poora na ho. Taakat tools se aati hai, prompt se nahi. Iterations cap karo, har step log karo, aur kisi bhi irreversible cheez se pehle confirmation maango.

### Chhota code

```python
def calculator(expr):
    return eval(expr, {'__builtins__': {}}, {})   # locked-down namespace only

TOOLS = {'calc': calculator}

def agent_loop(plan, max_steps=5):
    """`plan` stands in for the model's tool choices."""
    history = []
    for step, (tool, arg) in enumerate(plan[:max_steps], 1):
        result = TOOLS[tool](arg)
        history.append((step, tool, arg, result))
        print(f'step {step}: {tool}({arg!r}) -> {result}')
    return history

agent_loop([('calc', '2 + 2'), ('calc', '(2 + 2) * 10')])
```

**Yaad rakho:** Loop hamesha bounded rakho. Bina limit ka agent paisa jalata hai aur fail hone ke naye tareeke dhoondh leta hai.

**Aam galti:** Agent ko shell tool dena bina allowlist aur bina confirmation step ke.

Practice: `examples/03_parallel_fan_out_and_synthesis.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Specialised agent roles

### Aasaan Bhasha

Agent ek loop hai: model tool chunta hai, aapka code use chalata hai, result wapas context me jaata hai, aur ye dohraata hai jab tak kaam poora na ho. Taakat tools se aati hai, prompt se nahi. Iterations cap karo, har step log karo, aur kisi bhi irreversible cheez se pehle confirmation maango.

### Chhota code

```python
def calculator(expr):
    return eval(expr, {'__builtins__': {}}, {})   # locked-down namespace only

TOOLS = {'calc': calculator}

def agent_loop(plan, max_steps=5):
    """`plan` stands in for the model's tool choices."""
    history = []
    for step, (tool, arg) in enumerate(plan[:max_steps], 1):
        result = TOOLS[tool](arg)
        history.append((step, tool, arg, result))
        print(f'step {step}: {tool}({arg!r}) -> {result}')
    return history

agent_loop([('calc', '2 + 2'), ('calc', '(2 + 2) * 10')])
```

**Yaad rakho:** Loop hamesha bounded rakho. Bina limit ka agent paisa jalata hai aur fail hone ke naye tareeke dhoondh leta hai.

**Aam galti:** Agent ko shell tool dena bina allowlist aur bina confirmation step ke.

Practice: `examples/04_specialised_agent_roles.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Shared state and handoffs

### Aasaan Bhasha

Agent ek loop hai: model tool chunta hai, aapka code use chalata hai, result wapas context me jaata hai, aur ye dohraata hai jab tak kaam poora na ho. Taakat tools se aati hai, prompt se nahi. Iterations cap karo, har step log karo, aur kisi bhi irreversible cheez se pehle confirmation maango.

### Chhota code

```python
def calculator(expr):
    return eval(expr, {'__builtins__': {}}, {})   # locked-down namespace only

TOOLS = {'calc': calculator}

def agent_loop(plan, max_steps=5):
    """`plan` stands in for the model's tool choices."""
    history = []
    for step, (tool, arg) in enumerate(plan[:max_steps], 1):
        result = TOOLS[tool](arg)
        history.append((step, tool, arg, result))
        print(f'step {step}: {tool}({arg!r}) -> {result}')
    return history

agent_loop([('calc', '2 + 2'), ('calc', '(2 + 2) * 10')])
```

**Yaad rakho:** Loop hamesha bounded rakho. Bina limit ka agent paisa jalata hai aur fail hone ke naye tareeke dhoondh leta hai.

**Aam galti:** Agent ko shell tool dena bina allowlist aur bina confirmation step ke.

Practice: `examples/05_shared_state_and_handoffs.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Cost multiplication risk

### Aasaan Bhasha

Agent ek loop hai: model tool chunta hai, aapka code use chalata hai, result wapas context me jaata hai, aur ye dohraata hai jab tak kaam poora na ho. Taakat tools se aati hai, prompt se nahi. Iterations cap karo, har step log karo, aur kisi bhi irreversible cheez se pehle confirmation maango.

### Chhota code

```python
def calculator(expr):
    return eval(expr, {'__builtins__': {}}, {})   # locked-down namespace only

TOOLS = {'calc': calculator}

def agent_loop(plan, max_steps=5):
    """`plan` stands in for the model's tool choices."""
    history = []
    for step, (tool, arg) in enumerate(plan[:max_steps], 1):
        result = TOOLS[tool](arg)
        history.append((step, tool, arg, result))
        print(f'step {step}: {tool}({arg!r}) -> {result}')
    return history

agent_loop([('calc', '2 + 2'), ('calc', '(2 + 2) * 10')])
```

**Yaad rakho:** Loop hamesha bounded rakho. Bina limit ka agent paisa jalata hai aur fail hone ke naye tareeke dhoondh leta hai.

**Aam galti:** Agent ko shell tool dena bina allowlist aur bina confirmation step ke.

Practice: `examples/06_cost_multiplication_risk.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Debugging multi-agent runs

### Aasaan Bhasha

Agent ek loop hai: model tool chunta hai, aapka code use chalata hai, result wapas context me jaata hai, aur ye dohraata hai jab tak kaam poora na ho. Taakat tools se aati hai, prompt se nahi. Iterations cap karo, har step log karo, aur kisi bhi irreversible cheez se pehle confirmation maango.

### Chhota code

```python
def calculator(expr):
    return eval(expr, {'__builtins__': {}}, {})   # locked-down namespace only

TOOLS = {'calc': calculator}

def agent_loop(plan, max_steps=5):
    """`plan` stands in for the model's tool choices."""
    history = []
    for step, (tool, arg) in enumerate(plan[:max_steps], 1):
        result = TOOLS[tool](arg)
        history.append((step, tool, arg, result))
        print(f'step {step}: {tool}({arg!r}) -> {result}')
    return history

agent_loop([('calc', '2 + 2'), ('calc', '(2 + 2) * 10')])
```

**Yaad rakho:** Loop hamesha bounded rakho. Bina limit ka agent paisa jalata hai aur fail hone ke naye tareeke dhoondh leta hai.

**Aam galti:** Agent ko shell tool dena bina allowlist aur bina confirmation step ke.

Practice: `examples/07_debugging_multi_agent_runs.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Deterministic orchestration code

### Aasaan Bhasha

Agent ek loop hai: model tool chunta hai, aapka code use chalata hai, result wapas context me jaata hai, aur ye dohraata hai jab tak kaam poora na ho. Taakat tools se aati hai, prompt se nahi. Iterations cap karo, har step log karo, aur kisi bhi irreversible cheez se pehle confirmation maango.

### Chhota code

```python
def calculator(expr):
    return eval(expr, {'__builtins__': {}}, {})   # locked-down namespace only

TOOLS = {'calc': calculator}

def agent_loop(plan, max_steps=5):
    """`plan` stands in for the model's tool choices."""
    history = []
    for step, (tool, arg) in enumerate(plan[:max_steps], 1):
        result = TOOLS[tool](arg)
        history.append((step, tool, arg, result))
        print(f'step {step}: {tool}({arg!r}) -> {result}')
    return history

agent_loop([('calc', '2 + 2'), ('calc', '(2 + 2) * 10')])
```

**Yaad rakho:** Loop hamesha bounded rakho. Bina limit ka agent paisa jalata hai aur fail hone ke naye tareeke dhoondh leta hai.

**Aam galti:** Agent ko shell tool dena bina allowlist aur bina confirmation step ke.

Practice: `examples/08_deterministic_orchestration_code.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Evaluating a multi-agent system

### Aasaan Bhasha

Agent ek loop hai: model tool chunta hai, aapka code use chalata hai, result wapas context me jaata hai, aur ye dohraata hai jab tak kaam poora na ho. Taakat tools se aati hai, prompt se nahi. Iterations cap karo, har step log karo, aur kisi bhi irreversible cheez se pehle confirmation maango.

### Chhota code

```python
def calculator(expr):
    return eval(expr, {'__builtins__': {}}, {})   # locked-down namespace only

TOOLS = {'calc': calculator}

def agent_loop(plan, max_steps=5):
    """`plan` stands in for the model's tool choices."""
    history = []
    for step, (tool, arg) in enumerate(plan[:max_steps], 1):
        result = TOOLS[tool](arg)
        history.append((step, tool, arg, result))
        print(f'step {step}: {tool}({arg!r}) -> {result}')
    return history

agent_loop([('calc', '2 + 2'), ('calc', '(2 + 2) * 10')])
```

**Yaad rakho:** Loop hamesha bounded rakho. Bina limit ka agent paisa jalata hai aur fail hone ke naye tareeke dhoondh leta hai.

**Aam galti:** Agent ko shell tool dena bina allowlist aur bina confirmation step ke.

Practice: `examples/09_evaluating_a_multi_agent_system.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Simplifying back to one agent

### Aasaan Bhasha

Agent ek loop hai: model tool chunta hai, aapka code use chalata hai, result wapas context me jaata hai, aur ye dohraata hai jab tak kaam poora na ho. Taakat tools se aati hai, prompt se nahi. Iterations cap karo, har step log karo, aur kisi bhi irreversible cheez se pehle confirmation maango.

### Chhota code

```python
def calculator(expr):
    return eval(expr, {'__builtins__': {}}, {})   # locked-down namespace only

TOOLS = {'calc': calculator}

def agent_loop(plan, max_steps=5):
    """`plan` stands in for the model's tool choices."""
    history = []
    for step, (tool, arg) in enumerate(plan[:max_steps], 1):
        result = TOOLS[tool](arg)
        history.append((step, tool, arg, result))
        print(f'step {step}: {tool}({arg!r}) -> {result}')
    return history

agent_loop([('calc', '2 + 2'), ('calc', '(2 + 2) * 10')])
```

**Yaad rakho:** Loop hamesha bounded rakho. Bina limit ka agent paisa jalata hai aur fail hone ke naye tareeke dhoondh leta hai.

**Aam galti:** Agent ko shell tool dena bina allowlist aur bina confirmation step ke.

Practice: `examples/10_simplifying_back_to_one_agent.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 173 ke baad aapko ye aana chahiye

- **When one agent is not enough** ko bina notes dekhe kisi dost ko samjha sakna.
- **Orchestrator and worker patterns** ko bina notes dekhe kisi dost ko samjha sakna.
- **Parallel fan-out and synthesis** ko bina notes dekhe kisi dost ko samjha sakna.
- **Specialised agent roles** ko bina notes dekhe kisi dost ko samjha sakna.
- **Shared state and handoffs** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
