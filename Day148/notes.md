# Day 148 — LLM APIs in code

Today's goal: work through **LLM APIs in code** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Anatomy of a chat completion request |
| 2 | System prompts and message roles |
| 3 | max_tokens and stop conditions |
| 4 | Streaming responses |
| 5 | Retries, timeouts and backoff |
| 6 | Rate limits and concurrency |
| 7 | Cost tracking per request |
| 8 | Prompt caching for stable prefixes |
| 9 | Structured outputs and tool schemas |
| 10 | A resilient API client wrapper |

---

## 1. Anatomy of a chat completion request

Any network call to a model will eventually time out, get rate-limited, or return malformed output. A production client needs timeouts, bounded retries with exponential backoff and jitter, a concurrency cap, and per-request cost logging. Write it once and reuse it everywhere.

```python
import random, time

def with_retries(call, attempts=4, base=0.5, timeout_s=30):
    last = None
    for i in range(attempts):
        try:
            return call(timeout=timeout_s)
        except Exception as e:                     # narrow this to your client's errors
            last = e
            if i == attempts - 1:
                break
            sleep = base * (2 ** i) + random.random() * 0.1   # backoff + jitter
            print(f'attempt {i + 1} failed ({e}); retrying in {sleep:.2f}s')
            time.sleep(min(sleep, 0.01))          # shortened for the demo
    raise RuntimeError(f'all {attempts} attempts failed') from last

calls = {'n': 0}
def flaky(timeout):
    calls['n'] += 1
    if calls['n'] < 3:
        raise TimeoutError('upstream slow')
    return 'ok'

print(with_retries(flaky))
```

**Remember:** Jitter matters: without it, every client retries at the same instant and re-creates the outage.

**Common mistake:** Infinite retries on a 400-class error that will never succeed, hammering the API and your budget.

## 2. System prompts and message roles

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

## 3. max_tokens and stop conditions

Generation is a loop: predict a distribution, pick a token, append, repeat. Greedy is deterministic and repetitive; sampling is varied and riskier. Stop sequences and max_tokens are your circuit breakers — without them a loop can run until it exhausts your budget.

```python
import numpy as np

def generate(next_dist, max_tokens=20, stop=('.',), greedy=True, seed=0):
    rng = np.random.default_rng(seed)
    out = []
    for _ in range(max_tokens):
        tokens, probs = next_dist(out)
        tok = tokens[int(np.argmax(probs))] if greedy else rng.choice(tokens, p=probs)
        out.append(tok)
        if tok in stop:
            break
    return ''.join(out)

vocab = list('abc.')
dist = lambda hist: (vocab, np.array([0.4, 0.3, 0.2, 0.1]))
print('greedy :', generate(dist))
print('sampled:', generate(dist, greedy=False))
```

**Remember:** Always set max_tokens and stop sequences. They are the difference between a bug and a bill.

**Common mistake:** Leaving max_tokens unbounded on a retry loop and burning a month's budget overnight.

## 4. Streaming responses

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

## 5. Retries, timeouts and backoff

Any network call to a model will eventually time out, get rate-limited, or return malformed output. A production client needs timeouts, bounded retries with exponential backoff and jitter, a concurrency cap, and per-request cost logging. Write it once and reuse it everywhere.

```python
import random, time

def with_retries(call, attempts=4, base=0.5, timeout_s=30):
    last = None
    for i in range(attempts):
        try:
            return call(timeout=timeout_s)
        except Exception as e:                     # narrow this to your client's errors
            last = e
            if i == attempts - 1:
                break
            sleep = base * (2 ** i) + random.random() * 0.1   # backoff + jitter
            print(f'attempt {i + 1} failed ({e}); retrying in {sleep:.2f}s')
            time.sleep(min(sleep, 0.01))          # shortened for the demo
    raise RuntimeError(f'all {attempts} attempts failed') from last

calls = {'n': 0}
def flaky(timeout):
    calls['n'] += 1
    if calls['n'] < 3:
        raise TimeoutError('upstream slow')
    return 'ok'

print(with_retries(flaky))
```

**Remember:** Jitter matters: without it, every client retries at the same instant and re-creates the outage.

**Common mistake:** Infinite retries on a 400-class error that will never succeed, hammering the API and your budget.

## 6. Rate limits and concurrency

Any network call to a model will eventually time out, get rate-limited, or return malformed output. A production client needs timeouts, bounded retries with exponential backoff and jitter, a concurrency cap, and per-request cost logging. Write it once and reuse it everywhere.

```python
import random, time

def with_retries(call, attempts=4, base=0.5, timeout_s=30):
    last = None
    for i in range(attempts):
        try:
            return call(timeout=timeout_s)
        except Exception as e:                     # narrow this to your client's errors
            last = e
            if i == attempts - 1:
                break
            sleep = base * (2 ** i) + random.random() * 0.1   # backoff + jitter
            print(f'attempt {i + 1} failed ({e}); retrying in {sleep:.2f}s')
            time.sleep(min(sleep, 0.01))          # shortened for the demo
    raise RuntimeError(f'all {attempts} attempts failed') from last

calls = {'n': 0}
def flaky(timeout):
    calls['n'] += 1
    if calls['n'] < 3:
        raise TimeoutError('upstream slow')
    return 'ok'

print(with_retries(flaky))
```

**Remember:** Jitter matters: without it, every client retries at the same instant and re-creates the outage.

**Common mistake:** Infinite retries on a 400-class error that will never succeed, hammering the API and your budget.

## 7. Cost tracking per request

Any network call to a model will eventually time out, get rate-limited, or return malformed output. A production client needs timeouts, bounded retries with exponential backoff and jitter, a concurrency cap, and per-request cost logging. Write it once and reuse it everywhere.

```python
import random, time

def with_retries(call, attempts=4, base=0.5, timeout_s=30):
    last = None
    for i in range(attempts):
        try:
            return call(timeout=timeout_s)
        except Exception as e:                     # narrow this to your client's errors
            last = e
            if i == attempts - 1:
                break
            sleep = base * (2 ** i) + random.random() * 0.1   # backoff + jitter
            print(f'attempt {i + 1} failed ({e}); retrying in {sleep:.2f}s')
            time.sleep(min(sleep, 0.01))          # shortened for the demo
    raise RuntimeError(f'all {attempts} attempts failed') from last

calls = {'n': 0}
def flaky(timeout):
    calls['n'] += 1
    if calls['n'] < 3:
        raise TimeoutError('upstream slow')
    return 'ok'

print(with_retries(flaky))
```

**Remember:** Jitter matters: without it, every client retries at the same instant and re-creates the outage.

**Common mistake:** Infinite retries on a 400-class error that will never succeed, hammering the API and your budget.

## 8. Prompt caching for stable prefixes

The Messages API takes a system prompt plus alternating user/assistant turns and returns content blocks. Put stable content (long instructions, retrieved corpora) at the front and mark it cacheable — cache hits cut both latency and cost sharply. Stream when a human is waiting.

```python
# pip install anthropic ; export ANTHROPIC_API_KEY=...
# import anthropic
# client = anthropic.Anthropic()
# resp = client.messages.create(
#     model='claude-sonnet-5',
#     max_tokens=1024,
#     system=[{'type': 'text', 'text': LONG_STABLE_INSTRUCTIONS,
#              'cache_control': {'type': 'ephemeral'}}],
#     messages=[{'role': 'user', 'content': 'Summarise the attached policy.'}],
# )
# print(resp.content[0].text)
print('Stable prefix first + cache_control -> cheaper, faster repeat calls.')
```

**Remember:** Never hard-code an API key. Read it from the environment and keep it out of git.

**Common mistake:** Rebuilding the prompt in a different order each call, so nothing ever hits the cache.

## 9. Structured outputs and tool schemas

Free text is hard to parse; ask for JSON against a schema instead. Tool/function calling formalises this: you describe callable functions, the model returns a structured call, your code executes it and returns the result. Always validate before you act on the output.

```python
import json

TOOL = {
    'name': 'get_weather',
    'description': 'Current weather for a city',
    'input_schema': {
        'type': 'object',
        'properties': {'city': {'type': 'string'}, 'unit': {'type': 'string', 'enum': ['c', 'f']}},
        'required': ['city'],
    },
}

model_output = '{"city": "Pune", "unit": "c"}'
try:
    args = json.loads(model_output)
    assert 'city' in args, 'missing required field: city'
    print('validated call ->', TOOL['name'], args)
except (json.JSONDecodeError, AssertionError) as e:
    print('reject and retry:', e)
```

**Remember:** Validate every model-produced payload against the schema before it reaches your database.

**Common mistake:** Passing model output straight into `eval`, a shell command, or an SQL string.

## 10. A resilient API client wrapper

Any network call to a model will eventually time out, get rate-limited, or return malformed output. A production client needs timeouts, bounded retries with exponential backoff and jitter, a concurrency cap, and per-request cost logging. Write it once and reuse it everywhere.

```python
import random, time

def with_retries(call, attempts=4, base=0.5, timeout_s=30):
    last = None
    for i in range(attempts):
        try:
            return call(timeout=timeout_s)
        except Exception as e:                     # narrow this to your client's errors
            last = e
            if i == attempts - 1:
                break
            sleep = base * (2 ** i) + random.random() * 0.1   # backoff + jitter
            print(f'attempt {i + 1} failed ({e}); retrying in {sleep:.2f}s')
            time.sleep(min(sleep, 0.01))          # shortened for the demo
    raise RuntimeError(f'all {attempts} attempts failed') from last

calls = {'n': 0}
def flaky(timeout):
    calls['n'] += 1
    if calls['n'] < 3:
        raise TimeoutError('upstream slow')
    return 'ok'

print(with_retries(flaky))
```

**Remember:** Jitter matters: without it, every client retries at the same instant and re-creates the outage.

**Common mistake:** Infinite retries on a 400-class error that will never succeed, hammering the API and your budget.

---

## What you should be able to do after Day 148

- Explain **Anatomy of a chat completion request** to someone else without notes.
- Explain **System prompts and message roles** to someone else without notes.
- Explain **max_tokens and stop conditions** to someone else without notes.
- Explain **Streaming responses** to someone else without notes.
- Explain **Retries, timeouts and backoff** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
