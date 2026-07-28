# Day 133 — Inference and decoding

Aaj ka goal: **Inference and decoding** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

### Aasaan Bhasha

Generation ek loop hai: distribution predict karo, token chuno, jodo, dohrao. Greedy deterministic aur repetitive hai; sampling variety wala aur risky. Stop sequences aur max_tokens aapke circuit breakers hain — inke bina ek loop tab tak chal sakta hai jab tak aapka budget khatm na ho jaaye.

### Chhota code

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

**Yaad rakho:** max_tokens aur stop sequences hamesha set karo. Yahi bug aur bill ke beech ka farq hai.

**Aam galti:** Retry loop par max_tokens unbounded chhod dena aur raat bhar me mahine ka budget jala dena.

Practice: `examples/01_autoregressive_generation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Greedy decoding

### Aasaan Bhasha

Generation ek loop hai: distribution predict karo, token chuno, jodo, dohrao. Greedy deterministic aur repetitive hai; sampling variety wala aur risky. Stop sequences aur max_tokens aapke circuit breakers hain — inke bina ek loop tab tak chal sakta hai jab tak aapka budget khatm na ho jaaye.

### Chhota code

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

**Yaad rakho:** max_tokens aur stop sequences hamesha set karo. Yahi bug aur bill ke beech ka farq hai.

**Aam galti:** Retry loop par max_tokens unbounded chhod dena aur raat bhar me mahine ka budget jala dena.

Practice: `examples/02_greedy_decoding.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Temperature

### Aasaan Bhasha

Temperature 0 lagbhag deterministic hai aur extraction ke liye sahi; zyada values creative kaam ke liye variety deti hain. Top-p sabse chhota set rakhta hai jo probability mass ka p cover kare. Cost per token in aur out hai, isliye prompt chhota karna sabse sasta optimisation hai.

### Chhota code

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

**Yaad rakho:** Jise aap parse karoge uske liye temperature 0 use karo; randomness prose ke liye bachaao.

**Aam galti:** Temperature 1 par extraction chala kar hafte bhar 'random' JSON failures debug karna.

Practice: `examples/03_temperature.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Top-k sampling

### Aasaan Bhasha

Distribution batati hai kaunsi values likely hain. Measurement noise ke liye Gaussian, haan/na ke liye Bernoulli, per-interval counts ke liye Poisson. Sahi distribution chunna hi apna loss function chunna hai: Gaussian likelihood se MSE aata hai, Bernoulli se cross-entropy.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
normal = rng.normal(loc=0, scale=1, size=10_000)
coin = rng.binomial(n=1, p=0.3, size=10_000)

print('normal mean/std', round(normal.mean(), 3), round(normal.std(), 3))
print('coin heads rate ', coin.mean())
```

**Yaad rakho:** Jab result dobara banana ho to RNG hamesha seed karo (`default_rng(0)`).

**Aam galti:** Skewed, bounded ya count data par Gaussian maan lena aur phir residuals dekh kar hairan hona.

Practice: `examples/04_top_k_sampling.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Top-p nucleus sampling

### Aasaan Bhasha

Distribution batati hai kaunsi values likely hain. Measurement noise ke liye Gaussian, haan/na ke liye Bernoulli, per-interval counts ke liye Poisson. Sahi distribution chunna hi apna loss function chunna hai: Gaussian likelihood se MSE aata hai, Bernoulli se cross-entropy.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
normal = rng.normal(loc=0, scale=1, size=10_000)
coin = rng.binomial(n=1, p=0.3, size=10_000)

print('normal mean/std', round(normal.mean(), 3), round(normal.std(), 3))
print('coin heads rate ', coin.mean())
```

**Yaad rakho:** Jab result dobara banana ho to RNG hamesha seed karo (`default_rng(0)`).

**Aam galti:** Skewed, bounded ya count data par Gaussian maan lena aur phir residuals dekh kar hairan hona.

Practice: `examples/05_top_p_nucleus_sampling.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Repetition penalties

### Aasaan Bhasha

Aaj ka idea — **Repetition penalties** — Inference and decoding ke theme ke andar aata hai. Ise trivia nahi, ek tool ki tarah padho: ye kaam kya karta hai, aapke data ke baare me kya maan kar chalta hai, aur wo maanyata jhooth nikle to kya tootta hai?

### Chhota code

```python
# Explore: Repetition penalties
print("practice: Repetition penalties")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Yaad rakho:** `Repetition penalties` use karne se pehle ek assumption likho jo ye aapke data ke baare me maanta hai.

**Aam galti:** `Repetition penalties` ko tutorial se copy-paste kar lena bina jaane ki wo kya maanta hai aur kab fail hota hai.

Practice: `examples/06_repetition_penalties.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Beam search for constrained tasks

### Aasaan Bhasha

Generation ek loop hai: distribution predict karo, token chuno, jodo, dohrao. Greedy deterministic aur repetitive hai; sampling variety wala aur risky. Stop sequences aur max_tokens aapke circuit breakers hain — inke bina ek loop tab tak chal sakta hai jab tak aapka budget khatm na ho jaaye.

### Chhota code

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

**Yaad rakho:** max_tokens aur stop sequences hamesha set karo. Yahi bug aur bill ke beech ka farq hai.

**Aam galti:** Retry loop par max_tokens unbounded chhod dena aur raat bhar me mahine ka budget jala dena.

Practice: `examples/07_beam_search_for_constrained_tasks.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Stop sequences

### Aasaan Bhasha

Generation ek loop hai: distribution predict karo, token chuno, jodo, dohrao. Greedy deterministic aur repetitive hai; sampling variety wala aur risky. Stop sequences aur max_tokens aapke circuit breakers hain — inke bina ek loop tab tak chal sakta hai jab tak aapka budget khatm na ho jaaye.

### Chhota code

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

**Yaad rakho:** max_tokens aur stop sequences hamesha set karo. Yahi bug aur bill ke beech ka farq hai.

**Aam galti:** Retry loop par max_tokens unbounded chhod dena aur raat bhar me mahine ka budget jala dena.

Practice: `examples/08_stop_sequences.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Streaming tokens to the user

### Aasaan Bhasha

Generation ek loop hai: distribution predict karo, token chuno, jodo, dohrao. Greedy deterministic aur repetitive hai; sampling variety wala aur risky. Stop sequences aur max_tokens aapke circuit breakers hain — inke bina ek loop tab tak chal sakta hai jab tak aapka budget khatm na ho jaaye.

### Chhota code

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

**Yaad rakho:** max_tokens aur stop sequences hamesha set karo. Yahi bug aur bill ke beech ka farq hai.

**Aam galti:** Retry loop par max_tokens unbounded chhod dena aur raat bhar me mahine ka budget jala dena.

Practice: `examples/09_streaming_tokens_to_the_user.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Choosing decoding settings per task

### Aasaan Bhasha

Generation ek loop hai: distribution predict karo, token chuno, jodo, dohrao. Greedy deterministic aur repetitive hai; sampling variety wala aur risky. Stop sequences aur max_tokens aapke circuit breakers hain — inke bina ek loop tab tak chal sakta hai jab tak aapka budget khatm na ho jaaye.

### Chhota code

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

**Yaad rakho:** max_tokens aur stop sequences hamesha set karo. Yahi bug aur bill ke beech ka farq hai.

**Aam galti:** Retry loop par max_tokens unbounded chhod dena aur raat bhar me mahine ka budget jala dena.

Practice: `examples/10_choosing_decoding_settings_per_task.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 133 ke baad aapko ye aana chahiye

- **Autoregressive generation** ko bina notes dekhe kisi dost ko samjha sakna.
- **Greedy decoding** ko bina notes dekhe kisi dost ko samjha sakna.
- **Temperature** ko bina notes dekhe kisi dost ko samjha sakna.
- **Top-k sampling** ko bina notes dekhe kisi dost ko samjha sakna.
- **Top-p nucleus sampling** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
