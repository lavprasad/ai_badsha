# Day 133 — Inference and decoding

Today's goal: work through **Inference and decoding** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Autoregressive generation |
| 2 | Greedy decoding |
| 3 | Temperature |
| 4 | Top-k sampling |
| 5 | Top-p nucleus sampling |
| 6 | Repetition penalties |
| 7 | Beam search for constrained tasks |
| 8 | Stop sequences |
| 9 | Streaming tokens to the user |
| 10 | Choosing decoding settings per task |

---

## 1. Autoregressive generation

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

## 2. Greedy decoding

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

## 3. Temperature

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

## 4. Top-k sampling

A distribution says which values are likely. Gaussian for measurement noise, Bernoulli for yes/no, Poisson for counts per interval. Choosing the right one is choosing your loss function: Gaussian likelihood gives MSE, Bernoulli gives cross-entropy.

```python
import numpy as np

rng = np.random.default_rng(0)
normal = rng.normal(loc=0, scale=1, size=10_000)
coin = rng.binomial(n=1, p=0.3, size=10_000)

print('normal mean/std', round(normal.mean(), 3), round(normal.std(), 3))
print('coin heads rate ', coin.mean())
```

**Remember:** Always seed your RNG (`default_rng(0)`) when you want a result someone else can reproduce.

**Common mistake:** Assuming Gaussian for skewed, bounded, or count data and then being surprised by the residuals.

## 5. Top-p nucleus sampling

A distribution says which values are likely. Gaussian for measurement noise, Bernoulli for yes/no, Poisson for counts per interval. Choosing the right one is choosing your loss function: Gaussian likelihood gives MSE, Bernoulli gives cross-entropy.

```python
import numpy as np

rng = np.random.default_rng(0)
normal = rng.normal(loc=0, scale=1, size=10_000)
coin = rng.binomial(n=1, p=0.3, size=10_000)

print('normal mean/std', round(normal.mean(), 3), round(normal.std(), 3))
print('coin heads rate ', coin.mean())
```

**Remember:** Always seed your RNG (`default_rng(0)`) when you want a result someone else can reproduce.

**Common mistake:** Assuming Gaussian for skewed, bounded, or count data and then being surprised by the residuals.

## 6. Repetition penalties

Today's idea — **Repetition penalties** — sits inside the theme of Inference and decoding. Read it as a tool, not trivia: what job does it do, what does it assume about your data, and what breaks when that assumption is false?

```python
# Explore: Repetition penalties
print("practice: Repetition penalties")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Remember:** State one assumption `Repetition penalties` makes about your data before you use it.

**Common mistake:** Copy-pasting `Repetition penalties` from a tutorial without knowing what it assumes or when it fails.

## 7. Beam search for constrained tasks

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

## 8. Stop sequences

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

## 9. Streaming tokens to the user

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

## 10. Choosing decoding settings per task

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

---

## What you should be able to do after Day 133

- Explain **Autoregressive generation** to someone else without notes.
- Explain **Greedy decoding** to someone else without notes.
- Explain **Temperature** to someone else without notes.
- Explain **Top-k sampling** to someone else without notes.
- Explain **Top-p nucleus sampling** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
