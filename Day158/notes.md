# Day 158 — Agents: tools and capabilities

Today's goal: work through **Agents: tools and capabilities** — ten concepts, ten runnable examples, five questions.

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

An agent is a loop: the model picks a tool, your code runs it, the result goes back into context, repeat until done. Power comes from the tools, not the prompt. Cap the iterations, log every step, and require confirmation before anything irreversible.

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

**Remember:** Always bound the loop. An unbounded agent burns money and finds creative ways to fail.

**Common mistake:** Giving an agent a shell tool with no allowlist and no confirmation step.

Practice: open `examples/01_designing_a_good_tool_interface.py`, predict the output, change one line, predict again.

## 2. Read-only vs mutating tools

An agent is a loop: the model picks a tool, your code runs it, the result goes back into context, repeat until done. Power comes from the tools, not the prompt. Cap the iterations, log every step, and require confirmation before anything irreversible.

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

**Remember:** Always bound the loop. An unbounded agent burns money and finds creative ways to fail.

**Common mistake:** Giving an agent a shell tool with no allowlist and no confirmation step.

Practice: open `examples/02_read_only_vs_mutating_tools.py`, predict the output, change one line, predict again.

## 3. Search and retrieval tools

An agent is a loop: the model picks a tool, your code runs it, the result goes back into context, repeat until done. Power comes from the tools, not the prompt. Cap the iterations, log every step, and require confirmation before anything irreversible.

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

**Remember:** Always bound the loop. An unbounded agent burns money and finds creative ways to fail.

**Common mistake:** Giving an agent a shell tool with no allowlist and no confirmation step.

Practice: open `examples/03_search_and_retrieval_tools.py`, predict the output, change one line, predict again.

## 4. Code execution sandboxes

An agent is a loop: the model picks a tool, your code runs it, the result goes back into context, repeat until done. Power comes from the tools, not the prompt. Cap the iterations, log every step, and require confirmation before anything irreversible.

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

**Remember:** Always bound the loop. An unbounded agent burns money and finds creative ways to fail.

**Common mistake:** Giving an agent a shell tool with no allowlist and no confirmation step.

Practice: open `examples/04_code_execution_sandboxes.py`, predict the output, change one line, predict again.

## 5. File system access controls

An agent is a loop: the model picks a tool, your code runs it, the result goes back into context, repeat until done. Power comes from the tools, not the prompt. Cap the iterations, log every step, and require confirmation before anything irreversible.

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

**Remember:** Always bound the loop. An unbounded agent burns money and finds creative ways to fail.

**Common mistake:** Giving an agent a shell tool with no allowlist and no confirmation step.

Practice: open `examples/05_file_system_access_controls.py`, predict the output, change one line, predict again.

## 6. API calling tools

An agent is a loop: the model picks a tool, your code runs it, the result goes back into context, repeat until done. Power comes from the tools, not the prompt. Cap the iterations, log every step, and require confirmation before anything irreversible.

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

**Remember:** Always bound the loop. An unbounded agent burns money and finds creative ways to fail.

**Common mistake:** Giving an agent a shell tool with no allowlist and no confirmation step.

Practice: open `examples/06_api_calling_tools.py`, predict the output, change one line, predict again.

## 7. Database query tools with allowlists

An agent is a loop: the model picks a tool, your code runs it, the result goes back into context, repeat until done. Power comes from the tools, not the prompt. Cap the iterations, log every step, and require confirmation before anything irreversible.

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

**Remember:** Always bound the loop. An unbounded agent burns money and finds creative ways to fail.

**Common mistake:** Giving an agent a shell tool with no allowlist and no confirmation step.

Practice: open `examples/07_database_query_tools_with_allowlists.py`, predict the output, change one line, predict again.

## 8. Human approval gates

An agent is a loop: the model picks a tool, your code runs it, the result goes back into context, repeat until done. Power comes from the tools, not the prompt. Cap the iterations, log every step, and require confirmation before anything irreversible.

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

**Remember:** Always bound the loop. An unbounded agent burns money and finds creative ways to fail.

**Common mistake:** Giving an agent a shell tool with no allowlist and no confirmation step.

Practice: open `examples/08_human_approval_gates.py`, predict the output, change one line, predict again.

## 9. Tool descriptions as prompts

An agent is a loop: the model picks a tool, your code runs it, the result goes back into context, repeat until done. Power comes from the tools, not the prompt. Cap the iterations, log every step, and require confirmation before anything irreversible.

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

**Remember:** Always bound the loop. An unbounded agent burns money and finds creative ways to fail.

**Common mistake:** Giving an agent a shell tool with no allowlist and no confirmation step.

Practice: open `examples/09_tool_descriptions_as_prompts.py`, predict the output, change one line, predict again.

## 10. Testing tools independently

An agent is a loop: the model picks a tool, your code runs it, the result goes back into context, repeat until done. Power comes from the tools, not the prompt. Cap the iterations, log every step, and require confirmation before anything irreversible.

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

**Remember:** Always bound the loop. An unbounded agent burns money and finds creative ways to fail.

**Common mistake:** Giving an agent a shell tool with no allowlist and no confirmation step.

Practice: open `examples/10_testing_tools_independently.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 158

- Explain **Designing a good tool interface** to someone else without notes.
- Explain **Read-only vs mutating tools** to someone else without notes.
- Explain **Search and retrieval tools** to someone else without notes.
- Explain **Code execution sandboxes** to someone else without notes.
- Explain **File system access controls** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
