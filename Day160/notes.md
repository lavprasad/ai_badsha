# Day 160 — Model Context Protocol and integrations

Today's goal: work through **model context protocol and integrations** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Why a protocol for tools |
| 2 | MCP servers and clients |
| 3 | Resources, tools and prompts |
| 4 | Local vs remote servers |
| 5 | Authentication in integrations |
| 6 | Building a small MCP server |
| 7 | Security review of a third-party server |
| 8 | Versioning tool contracts |
| 9 | Debugging protocol issues |
| 10 | Integrations as the real product surface |

---

## 1. Why a protocol for tools

A tool protocol standardises how a model discovers and calls capabilities, so one integration works across clients. The security question is the important one: a third-party server sees whatever context you send it and can return text that steers your agent. Review it like you would a dependency with network and disk access.

```python
REVIEW = [
    'What data does this server receive on each call?',
    'Where does it run — my machine, my VPC, or a vendor?',
    'What credentials does it hold, and with what scope?',
    'Can its responses inject instructions into my agent loop?',
    'Is it pinned to a version, or does it auto-update?',
    'What is logged, where, and for how long?',
]
for i, q in enumerate(REVIEW, 1):
    print(f'{i}. {q}')
```

**Remember:** A tool server's response is untrusted input to your agent. Delimit it and never let it grant permissions.

**Common mistake:** Installing a convenient community server with broad credentials and no review of what it sends upstream.

## 2. MCP servers and clients

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

## 3. Resources, tools and prompts

A tool protocol standardises how a model discovers and calls capabilities, so one integration works across clients. The security question is the important one: a third-party server sees whatever context you send it and can return text that steers your agent. Review it like you would a dependency with network and disk access.

```python
REVIEW = [
    'What data does this server receive on each call?',
    'Where does it run — my machine, my VPC, or a vendor?',
    'What credentials does it hold, and with what scope?',
    'Can its responses inject instructions into my agent loop?',
    'Is it pinned to a version, or does it auto-update?',
    'What is logged, where, and for how long?',
]
for i, q in enumerate(REVIEW, 1):
    print(f'{i}. {q}')
```

**Remember:** A tool server's response is untrusted input to your agent. Delimit it and never let it grant permissions.

**Common mistake:** Installing a convenient community server with broad credentials and no review of what it sends upstream.

## 4. Local vs remote servers

A tool protocol standardises how a model discovers and calls capabilities, so one integration works across clients. The security question is the important one: a third-party server sees whatever context you send it and can return text that steers your agent. Review it like you would a dependency with network and disk access.

```python
REVIEW = [
    'What data does this server receive on each call?',
    'Where does it run — my machine, my VPC, or a vendor?',
    'What credentials does it hold, and with what scope?',
    'Can its responses inject instructions into my agent loop?',
    'Is it pinned to a version, or does it auto-update?',
    'What is logged, where, and for how long?',
]
for i, q in enumerate(REVIEW, 1):
    print(f'{i}. {q}')
```

**Remember:** A tool server's response is untrusted input to your agent. Delimit it and never let it grant permissions.

**Common mistake:** Installing a convenient community server with broad credentials and no review of what it sends upstream.

## 5. Authentication in integrations

A tool protocol standardises how a model discovers and calls capabilities, so one integration works across clients. The security question is the important one: a third-party server sees whatever context you send it and can return text that steers your agent. Review it like you would a dependency with network and disk access.

```python
REVIEW = [
    'What data does this server receive on each call?',
    'Where does it run — my machine, my VPC, or a vendor?',
    'What credentials does it hold, and with what scope?',
    'Can its responses inject instructions into my agent loop?',
    'Is it pinned to a version, or does it auto-update?',
    'What is logged, where, and for how long?',
]
for i, q in enumerate(REVIEW, 1):
    print(f'{i}. {q}')
```

**Remember:** A tool server's response is untrusted input to your agent. Delimit it and never let it grant permissions.

**Common mistake:** Installing a convenient community server with broad credentials and no review of what it sends upstream.

## 6. Building a small MCP server

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

## 7. Security review of a third-party server

A tool protocol standardises how a model discovers and calls capabilities, so one integration works across clients. The security question is the important one: a third-party server sees whatever context you send it and can return text that steers your agent. Review it like you would a dependency with network and disk access.

```python
REVIEW = [
    'What data does this server receive on each call?',
    'Where does it run — my machine, my VPC, or a vendor?',
    'What credentials does it hold, and with what scope?',
    'Can its responses inject instructions into my agent loop?',
    'Is it pinned to a version, or does it auto-update?',
    'What is logged, where, and for how long?',
]
for i, q in enumerate(REVIEW, 1):
    print(f'{i}. {q}')
```

**Remember:** A tool server's response is untrusted input to your agent. Delimit it and never let it grant permissions.

**Common mistake:** Installing a convenient community server with broad credentials and no review of what it sends upstream.

## 8. Versioning tool contracts

An experiment you cannot reproduce is an anecdote. Track for every run: code commit, data version, hyperparameters, metrics and the artefact. Six months later, 'which run produced the model in production' must have an answer.

```python
import json, hashlib, subprocess

def run_record(params, metrics, data_path=None):
    try:
        commit = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'], text=True).strip()
    except Exception:
        commit = 'unknown'
    return {
        'commit': commit,
        'params': params,
        'metrics': metrics,
        'data_sha': hashlib.sha256((data_path or 'none').encode()).hexdigest()[:12],
    }

print(json.dumps(run_record({'lr': 0.01, 'depth': 6}, {'auc': 0.912}, 'data/train.csv'), indent=2))
```

**Remember:** Log the data version alongside the code version — data changes silently, code changes loudly.

**Common mistake:** Naming files `model_final_v2_REAL_use_this.pkl` instead of using a registry.

## 9. Debugging protocol issues

A tool protocol standardises how a model discovers and calls capabilities, so one integration works across clients. The security question is the important one: a third-party server sees whatever context you send it and can return text that steers your agent. Review it like you would a dependency with network and disk access.

```python
REVIEW = [
    'What data does this server receive on each call?',
    'Where does it run — my machine, my VPC, or a vendor?',
    'What credentials does it hold, and with what scope?',
    'Can its responses inject instructions into my agent loop?',
    'Is it pinned to a version, or does it auto-update?',
    'What is logged, where, and for how long?',
]
for i, q in enumerate(REVIEW, 1):
    print(f'{i}. {q}')
```

**Remember:** A tool server's response is untrusted input to your agent. Delimit it and never let it grant permissions.

**Common mistake:** Installing a convenient community server with broad credentials and no review of what it sends upstream.

## 10. Integrations as the real product surface

A tool protocol standardises how a model discovers and calls capabilities, so one integration works across clients. The security question is the important one: a third-party server sees whatever context you send it and can return text that steers your agent. Review it like you would a dependency with network and disk access.

```python
REVIEW = [
    'What data does this server receive on each call?',
    'Where does it run — my machine, my VPC, or a vendor?',
    'What credentials does it hold, and with what scope?',
    'Can its responses inject instructions into my agent loop?',
    'Is it pinned to a version, or does it auto-update?',
    'What is logged, where, and for how long?',
]
for i, q in enumerate(REVIEW, 1):
    print(f'{i}. {q}')
```

**Remember:** A tool server's response is untrusted input to your agent. Delimit it and never let it grant permissions.

**Common mistake:** Installing a convenient community server with broad credentials and no review of what it sends upstream.

---

## What you should be able to do after Day 160

- Explain **Why a protocol for tools** to someone else without notes.
- Explain **MCP servers and clients** to someone else without notes.
- Explain **Resources, tools and prompts** to someone else without notes.
- Explain **Local vs remote servers** to someone else without notes.
- Explain **Authentication in integrations** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
