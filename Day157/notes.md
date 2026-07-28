# Day 157 — Agents: the loop

Today's goal: work through **Agents: the loop** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | What makes something an agent |
| 2 | The observe-decide-act loop |
| 3 | Tool definitions and schemas |
| 4 | Tool result formatting |
| 5 | Iteration limits |
| 6 | Termination conditions |
| 7 | State between steps |
| 8 | Error handling inside the loop |
| 9 | Logging every step for debugging |
| 10 | Building a two-tool agent from scratch |

---

## 1. What makes something an agent

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

## 2. The observe-decide-act loop

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

## 3. Tool definitions and schemas

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

## 4. Tool result formatting

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

## 5. Iteration limits

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

## 6. Termination conditions

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

## 7. State between steps

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

## 8. Error handling inside the loop

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

## 9. Logging every step for debugging

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

## 10. Building a two-tool agent from scratch

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

---

## What you should be able to do after Day 157

- Explain **What makes something an agent** to someone else without notes.
- Explain **The observe-decide-act loop** to someone else without notes.
- Explain **Tool definitions and schemas** to someone else without notes.
- Explain **Tool result formatting** to someone else without notes.
- Explain **Iteration limits** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
