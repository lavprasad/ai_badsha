# Day 159 — Agents: planning and reliability

Today's goal: work through **Agents: planning and reliability** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Explicit planning steps |
| 2 | Replanning after failure |
| 3 | Subagents and delegation |
| 4 | Parallel tool calls |
| 5 | Context management across long runs |
| 6 | Cost control and budgets |
| 7 | Detecting loops and stalls |
| 8 | Checkpointing long tasks |
| 9 | Determinism where it matters |
| 10 | Evaluating agent trajectories |

---

## 1. Explicit planning steps

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

## 2. Replanning after failure

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

## 3. Subagents and delegation

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

## 4. Parallel tool calls

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

## 5. Context management across long runs

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

## 6. Cost control and budgets

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

## 7. Detecting loops and stalls

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

## 8. Checkpointing long tasks

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

## 9. Determinism where it matters

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

## 10. Evaluating agent trajectories

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

## What you should be able to do after Day 159

- Explain **Explicit planning steps** to someone else without notes.
- Explain **Replanning after failure** to someone else without notes.
- Explain **Subagents and delegation** to someone else without notes.
- Explain **Parallel tool calls** to someone else without notes.
- Explain **Context management across long runs** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
