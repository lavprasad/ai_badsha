# Day 158 — Agents: tools and capabilities

Aaj ka goal: **Agents: tools and capabilities** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Designing a good tool interface |
| 2 | Read-only vs mutating tools |
| 3 | Search and retrieval tools |
| 4 | Code execution sandboxes |
| 5 | File system access controls |
| 6 | API calling tools |
| 7 | Database query tools with allowlists |
| 8 | Human approval gates |
| 9 | Tool descriptions as prompts |
| 10 | Testing tools independently |

---

## 1. Designing a good tool interface

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

Practice: `examples/01_designing_a_good_tool_interface.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Read-only vs mutating tools

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

Practice: `examples/02_read_only_vs_mutating_tools.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Search and retrieval tools

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

Practice: `examples/03_search_and_retrieval_tools.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Code execution sandboxes

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

Practice: `examples/04_code_execution_sandboxes.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. File system access controls

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

Practice: `examples/05_file_system_access_controls.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. API calling tools

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

Practice: `examples/06_api_calling_tools.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Database query tools with allowlists

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

Practice: `examples/07_database_query_tools_with_allowlists.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Human approval gates

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

Practice: `examples/08_human_approval_gates.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Tool descriptions as prompts

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

Practice: `examples/09_tool_descriptions_as_prompts.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Testing tools independently

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

Practice: `examples/10_testing_tools_independently.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 158 ke baad aapko ye aana chahiye

- **Designing a good tool interface** ko bina notes dekhe kisi dost ko samjha sakna.
- **Read-only vs mutating tools** ko bina notes dekhe kisi dost ko samjha sakna.
- **Search and retrieval tools** ko bina notes dekhe kisi dost ko samjha sakna.
- **Code execution sandboxes** ko bina notes dekhe kisi dost ko samjha sakna.
- **File system access controls** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
