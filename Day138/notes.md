# Day 138 — Conversational systems

Today's goal: work through **Conversational systems** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Turns, roles and system prompts |
| 2 | Conversation state and memory |
| 3 | Context window management |
| 4 | Summarising older turns |
| 5 | Persona and tone control |
| 6 | Handling out-of-scope requests |
| 7 | Escalation to a human |
| 8 | Multi-turn evaluation |
| 9 | Latency perception and streaming |
| 10 | Building a grounded support bot |

---

## 1. Turns, roles and system prompts

A prompt is a program written in English. Be specific about role, task, format and constraints. Few-shot examples teach format better than any description. Asking for reasoning steps helps on multi-step problems and wastes tokens on simple lookups.

```python
prompt = '''You are a support triage assistant.

Classify the ticket into exactly one of: BILLING, BUG, FEATURE, OTHER.
Return JSON only: {"label": ..., "confidence": 0.0-1.0}

Examples:
Ticket: "charged twice this month" -> {"label": "BILLING", "confidence": 0.95}
Ticket: "app crashes on upload"    -> {"label": "BUG", "confidence": 0.92}

Ticket: "can you add dark mode?"
'''
print(prompt)
print('Structure: role -> task -> allowed outputs -> format -> examples -> input.')
```

**Remember:** Put the output format last and show it as an example — models copy the nearest pattern.

**Common mistake:** Writing a vague prompt, getting vague output, and blaming the model.

Practice: open `examples/01_turns_roles_and_system_prompts.py`, predict the output, change one line, predict again.

## 2. Conversation state and memory

Context is not memory. Context is what fits in this request; memory is what you deliberately store and retrieve. Design the schema explicitly — what is stored, how it expires, how conflicts resolve — or you get an assistant that confidently repeats something the user corrected last month.

```python
import time

class Memory:
    def __init__(self, ttl_days=90):
        self.items, self.ttl = [], ttl_days * 86400

    def add(self, key, value, ts):
        self.items = [i for i in self.items if i['key'] != key]   # newest wins
        self.items.append({'key': key, 'value': value, 'ts': ts})

    def recall(self, now):
        return [i for i in self.items if now - i['ts'] < self.ttl]

m = Memory(ttl_days=30)
m.add('preferred_name', 'Sam', ts=0)
m.add('preferred_name', 'Samir', ts=100)      # correction replaces, not appends
print(m.recall(now=200))
print(m.recall(now=30 * 86400 + 200))          # expired
```

**Remember:** A correction must overwrite, not coexist. Two contradictory memories will both get retrieved.

**Common mistake:** Appending every stated fact to a vector store forever, so stale and corrected facts compete at retrieval.

Practice: open `examples/02_conversation_state_and_memory.py`, predict the output, change one line, predict again.

## 3. Context window management

Temperature 0 is near-deterministic and right for extraction; higher values add diversity for creative work. Top-p keeps the smallest set of tokens covering p of the probability mass. Cost is per token in and out, so trimming the prompt is the cheapest optimisation there is.

```python
import numpy as np

def sample(logits, temperature=1.0, top_p=0.9, seed=0):
    z = np.array(logits) / max(temperature, 1e-6)
    p = np.exp(z - z.max())
    p /= p.sum()
    order = np.argsort(-p)
    keep = order[:max(1, int(np.searchsorted(np.cumsum(p[order]), top_p) + 1))]
    p2 = p[keep] / p[keep].sum()
    return int(np.random.default_rng(seed).choice(keep, p=p2))

logits = [3.0, 2.0, 1.0, 0.5]
print('greedy-ish (T=0.1):', sample(logits, temperature=0.1))
print('creative  (T=1.5):', sample(logits, temperature=1.5, seed=3))
```

**Remember:** Use temperature 0 for anything you will parse; save randomness for prose.

**Common mistake:** Running extraction at temperature 1 and debugging 'random' JSON failures for a week.

Practice: open `examples/03_context_window_management.py`, predict the output, change one line, predict again.

## 4. Summarising older turns

Context is not memory. Context is what fits in this request; memory is what you deliberately store and retrieve. Design the schema explicitly — what is stored, how it expires, how conflicts resolve — or you get an assistant that confidently repeats something the user corrected last month.

```python
import time

class Memory:
    def __init__(self, ttl_days=90):
        self.items, self.ttl = [], ttl_days * 86400

    def add(self, key, value, ts):
        self.items = [i for i in self.items if i['key'] != key]   # newest wins
        self.items.append({'key': key, 'value': value, 'ts': ts})

    def recall(self, now):
        return [i for i in self.items if now - i['ts'] < self.ttl]

m = Memory(ttl_days=30)
m.add('preferred_name', 'Sam', ts=0)
m.add('preferred_name', 'Samir', ts=100)      # correction replaces, not appends
print(m.recall(now=200))
print(m.recall(now=30 * 86400 + 200))          # expired
```

**Remember:** A correction must overwrite, not coexist. Two contradictory memories will both get retrieved.

**Common mistake:** Appending every stated fact to a vector store forever, so stale and corrected facts compete at retrieval.

Practice: open `examples/04_summarising_older_turns.py`, predict the output, change one line, predict again.

## 5. Persona and tone control

Context is not memory. Context is what fits in this request; memory is what you deliberately store and retrieve. Design the schema explicitly — what is stored, how it expires, how conflicts resolve — or you get an assistant that confidently repeats something the user corrected last month.

```python
import time

class Memory:
    def __init__(self, ttl_days=90):
        self.items, self.ttl = [], ttl_days * 86400

    def add(self, key, value, ts):
        self.items = [i for i in self.items if i['key'] != key]   # newest wins
        self.items.append({'key': key, 'value': value, 'ts': ts})

    def recall(self, now):
        return [i for i in self.items if now - i['ts'] < self.ttl]

m = Memory(ttl_days=30)
m.add('preferred_name', 'Sam', ts=0)
m.add('preferred_name', 'Samir', ts=100)      # correction replaces, not appends
print(m.recall(now=200))
print(m.recall(now=30 * 86400 + 200))          # expired
```

**Remember:** A correction must overwrite, not coexist. Two contradictory memories will both get retrieved.

**Common mistake:** Appending every stated fact to a vector store forever, so stale and corrected facts compete at retrieval.

Practice: open `examples/05_persona_and_tone_control.py`, predict the output, change one line, predict again.

## 6. Handling out-of-scope requests

Default arguments are evaluated once, at function definition time. A mutable default (list, dict, set) is therefore shared by every call — a bug that shows up as 'my function remembers the last call'. Use `None` and build the real default inside.

```python
def bad(item, bucket=[]):        # created ONCE
    bucket.append(item)
    return bucket

def good(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket

print(bad(1), bad(2))     # [1] [1, 2]  <- leaked
print(good(1), good(2))   # [1] [2]     <- correct
```

**Remember:** Default arguments must be immutable. `None` plus a check is the standard fix.

**Common mistake:** A `def f(x, cache={})` that silently accumulates state across every call in the process.

Practice: open `examples/06_handling_out_of_scope_requests.py`, predict the output, change one line, predict again.

## 7. Escalation to a human

Context is not memory. Context is what fits in this request; memory is what you deliberately store and retrieve. Design the schema explicitly — what is stored, how it expires, how conflicts resolve — or you get an assistant that confidently repeats something the user corrected last month.

```python
import time

class Memory:
    def __init__(self, ttl_days=90):
        self.items, self.ttl = [], ttl_days * 86400

    def add(self, key, value, ts):
        self.items = [i for i in self.items if i['key'] != key]   # newest wins
        self.items.append({'key': key, 'value': value, 'ts': ts})

    def recall(self, now):
        return [i for i in self.items if now - i['ts'] < self.ttl]

m = Memory(ttl_days=30)
m.add('preferred_name', 'Sam', ts=0)
m.add('preferred_name', 'Samir', ts=100)      # correction replaces, not appends
print(m.recall(now=200))
print(m.recall(now=30 * 86400 + 200))          # expired
```

**Remember:** A correction must overwrite, not coexist. Two contradictory memories will both get retrieved.

**Common mistake:** Appending every stated fact to a vector store forever, so stale and corrected facts compete at retrieval.

Practice: open `examples/07_escalation_to_a_human.py`, predict the output, change one line, predict again.

## 8. Multi-turn evaluation

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

Practice: open `examples/08_multi_turn_evaluation.py`, predict the output, change one line, predict again.

## 9. Latency perception and streaming

Data parallelism replicates the model and splits the batch; model parallelism splits the model when it will not fit on one device. Scale only after profiling — most 'we need more GPUs' problems are actually a slow data loader.

```python
# Effective batch = per_device_batch * n_devices * grad_accum_steps
per_device, devices, accum = 8, 4, 4
print('effective batch size', per_device * devices * accum)
print('\\nGradient accumulation gives a large effective batch on small memory:')
print('  for i, batch in enumerate(loader):')
print('      loss = model(batch).loss / accum')
print('      loss.backward()')
print('      if (i + 1) % accum == 0:')
print('          opt.step(); opt.zero_grad()')
```

**Remember:** Profile first. GPU at 30% utilisation means the bottleneck is the data pipeline, not the GPU.

**Common mistake:** Scaling the learning rate wrongly when you scale the batch — a larger batch usually needs a larger LR.

Practice: open `examples/09_latency_perception_and_streaming.py`, predict the output, change one line, predict again.

## 10. Building a grounded support bot

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

Practice: open `examples/10_building_a_grounded_support_bot.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 138

- Explain **Turns, roles and system prompts** to someone else without notes.
- Explain **Conversation state and memory** to someone else without notes.
- Explain **Context window management** to someone else without notes.
- Explain **Summarising older turns** to someone else without notes.
- Explain **Persona and tone control** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
