# Day 130 — Pretraining language models

Today's goal: work through **Pretraining language models** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | The next-token objective at scale |
| 2 | Data collection and filtering |
| 3 | Deduplication and quality scoring |
| 4 | Tokeniser training |
| 5 | Compute budget and scaling laws |
| 6 | Chinchilla-optimal data ratios |
| 7 | Training instabilities |
| 8 | Evaluation during pretraining |
| 9 | Cost realities |
| 10 | Why almost nobody should pretrain |

---

## 1. The next-token objective at scale

Pretraining is one absurdly simple objective at enormous scale: predict the next token. Everything else — grammar, facts, reasoning traces, style — falls out of doing that well over trillions of tokens. Scaling laws say loss falls predictably with model size, data and compute together.

```python
from collections import defaultdict, Counter
import random

text = 'the cat sat on the mat the cat ate the rat'.split()
model = defaultdict(Counter)
for a, b in zip(text, text[1:]):
    model[a][b] += 1

random.seed(0)
word, out = 'the', ['the']
for _ in range(6):
    nxt = model[word].most_common(1)[0][0] if model[word] else 'the'
    out.append(nxt)
    word = nxt
print(' '.join(out))   # a 2-gram LM: same objective, 10 orders of magnitude smaller
```

**Remember:** A bigger model trained on too little data is a waste — compute, parameters and tokens scale together.

**Common mistake:** Believing a base model will follow instructions; that behaviour comes from the tuning stages after.

## 2. Data collection and filtering

Pretraining is one absurdly simple objective at enormous scale: predict the next token. Everything else — grammar, facts, reasoning traces, style — falls out of doing that well over trillions of tokens. Scaling laws say loss falls predictably with model size, data and compute together.

```python
from collections import defaultdict, Counter
import random

text = 'the cat sat on the mat the cat ate the rat'.split()
model = defaultdict(Counter)
for a, b in zip(text, text[1:]):
    model[a][b] += 1

random.seed(0)
word, out = 'the', ['the']
for _ in range(6):
    nxt = model[word].most_common(1)[0][0] if model[word] else 'the'
    out.append(nxt)
    word = nxt
print(' '.join(out))   # a 2-gram LM: same objective, 10 orders of magnitude smaller
```

**Remember:** A bigger model trained on too little data is a waste — compute, parameters and tokens scale together.

**Common mistake:** Believing a base model will follow instructions; that behaviour comes from the tuning stages after.

## 3. Deduplication and quality scoring

Pretraining is one absurdly simple objective at enormous scale: predict the next token. Everything else — grammar, facts, reasoning traces, style — falls out of doing that well over trillions of tokens. Scaling laws say loss falls predictably with model size, data and compute together.

```python
from collections import defaultdict, Counter
import random

text = 'the cat sat on the mat the cat ate the rat'.split()
model = defaultdict(Counter)
for a, b in zip(text, text[1:]):
    model[a][b] += 1

random.seed(0)
word, out = 'the', ['the']
for _ in range(6):
    nxt = model[word].most_common(1)[0][0] if model[word] else 'the'
    out.append(nxt)
    word = nxt
print(' '.join(out))   # a 2-gram LM: same objective, 10 orders of magnitude smaller
```

**Remember:** A bigger model trained on too little data is a waste — compute, parameters and tokens scale together.

**Common mistake:** Believing a base model will follow instructions; that behaviour comes from the tuning stages after.

## 4. Tokeniser training

Models see token IDs, not text. Byte-pair encoding merges frequent character pairs so common words are one token and rare words split into pieces. Tokens are why you are billed per token, why context limits are in tokens, and why models are bad at counting letters.

```python
from collections import Counter

def bpe_merges(words, n_merges=3):
    corpus = {' '.join(w) + ' </w>': c for w, c in words.items()}
    for _ in range(n_merges):
        pairs = Counter()
        for word, freq in corpus.items():
            syms = word.split()
            for a, b in zip(syms, syms[1:]):
                pairs[(a, b)] += freq
        if not pairs:
            break
        best = max(pairs, key=pairs.get)
        merged = ''.join(best)
        corpus = {w.replace(' '.join(best), merged): c for w, c in corpus.items()}
        print('merged', best, '->', merged)
    return corpus

bpe_merges({'low': 5, 'lower': 2, 'newest': 6, 'widest': 3})
```

**Remember:** Roughly 1 token ~ 4 characters of English; other languages cost far more tokens per word.

**Common mistake:** Estimating cost or context usage in words instead of tokens and overflowing the window in production.

## 5. Compute budget and scaling laws

Pretraining is one absurdly simple objective at enormous scale: predict the next token. Everything else — grammar, facts, reasoning traces, style — falls out of doing that well over trillions of tokens. Scaling laws say loss falls predictably with model size, data and compute together.

```python
from collections import defaultdict, Counter
import random

text = 'the cat sat on the mat the cat ate the rat'.split()
model = defaultdict(Counter)
for a, b in zip(text, text[1:]):
    model[a][b] += 1

random.seed(0)
word, out = 'the', ['the']
for _ in range(6):
    nxt = model[word].most_common(1)[0][0] if model[word] else 'the'
    out.append(nxt)
    word = nxt
print(' '.join(out))   # a 2-gram LM: same objective, 10 orders of magnitude smaller
```

**Remember:** A bigger model trained on too little data is a waste — compute, parameters and tokens scale together.

**Common mistake:** Believing a base model will follow instructions; that behaviour comes from the tuning stages after.

## 6. Chinchilla-optimal data ratios

Pretraining is one absurdly simple objective at enormous scale: predict the next token. Everything else — grammar, facts, reasoning traces, style — falls out of doing that well over trillions of tokens. Scaling laws say loss falls predictably with model size, data and compute together.

```python
from collections import defaultdict, Counter
import random

text = 'the cat sat on the mat the cat ate the rat'.split()
model = defaultdict(Counter)
for a, b in zip(text, text[1:]):
    model[a][b] += 1

random.seed(0)
word, out = 'the', ['the']
for _ in range(6):
    nxt = model[word].most_common(1)[0][0] if model[word] else 'the'
    out.append(nxt)
    word = nxt
print(' '.join(out))   # a 2-gram LM: same objective, 10 orders of magnitude smaller
```

**Remember:** A bigger model trained on too little data is a waste — compute, parameters and tokens scale together.

**Common mistake:** Believing a base model will follow instructions; that behaviour comes from the tuning stages after.

## 7. Training instabilities

Pretraining is one absurdly simple objective at enormous scale: predict the next token. Everything else — grammar, facts, reasoning traces, style — falls out of doing that well over trillions of tokens. Scaling laws say loss falls predictably with model size, data and compute together.

```python
from collections import defaultdict, Counter
import random

text = 'the cat sat on the mat the cat ate the rat'.split()
model = defaultdict(Counter)
for a, b in zip(text, text[1:]):
    model[a][b] += 1

random.seed(0)
word, out = 'the', ['the']
for _ in range(6):
    nxt = model[word].most_common(1)[0][0] if model[word] else 'the'
    out.append(nxt)
    word = nxt
print(' '.join(out))   # a 2-gram LM: same objective, 10 orders of magnitude smaller
```

**Remember:** A bigger model trained on too little data is a waste — compute, parameters and tokens scale together.

**Common mistake:** Believing a base model will follow instructions; that behaviour comes from the tuning stages after.

## 8. Evaluation during pretraining

Pretraining is one absurdly simple objective at enormous scale: predict the next token. Everything else — grammar, facts, reasoning traces, style — falls out of doing that well over trillions of tokens. Scaling laws say loss falls predictably with model size, data and compute together.

```python
from collections import defaultdict, Counter
import random

text = 'the cat sat on the mat the cat ate the rat'.split()
model = defaultdict(Counter)
for a, b in zip(text, text[1:]):
    model[a][b] += 1

random.seed(0)
word, out = 'the', ['the']
for _ in range(6):
    nxt = model[word].most_common(1)[0][0] if model[word] else 'the'
    out.append(nxt)
    word = nxt
print(' '.join(out))   # a 2-gram LM: same objective, 10 orders of magnitude smaller
```

**Remember:** A bigger model trained on too little data is a waste — compute, parameters and tokens scale together.

**Common mistake:** Believing a base model will follow instructions; that behaviour comes from the tuning stages after.

## 9. Cost realities

Pretraining is one absurdly simple objective at enormous scale: predict the next token. Everything else — grammar, facts, reasoning traces, style — falls out of doing that well over trillions of tokens. Scaling laws say loss falls predictably with model size, data and compute together.

```python
from collections import defaultdict, Counter
import random

text = 'the cat sat on the mat the cat ate the rat'.split()
model = defaultdict(Counter)
for a, b in zip(text, text[1:]):
    model[a][b] += 1

random.seed(0)
word, out = 'the', ['the']
for _ in range(6):
    nxt = model[word].most_common(1)[0][0] if model[word] else 'the'
    out.append(nxt)
    word = nxt
print(' '.join(out))   # a 2-gram LM: same objective, 10 orders of magnitude smaller
```

**Remember:** A bigger model trained on too little data is a waste — compute, parameters and tokens scale together.

**Common mistake:** Believing a base model will follow instructions; that behaviour comes from the tuning stages after.

## 10. Why almost nobody should pretrain

Pretraining is one absurdly simple objective at enormous scale: predict the next token. Everything else — grammar, facts, reasoning traces, style — falls out of doing that well over trillions of tokens. Scaling laws say loss falls predictably with model size, data and compute together.

```python
from collections import defaultdict, Counter
import random

text = 'the cat sat on the mat the cat ate the rat'.split()
model = defaultdict(Counter)
for a, b in zip(text, text[1:]):
    model[a][b] += 1

random.seed(0)
word, out = 'the', ['the']
for _ in range(6):
    nxt = model[word].most_common(1)[0][0] if model[word] else 'the'
    out.append(nxt)
    word = nxt
print(' '.join(out))   # a 2-gram LM: same objective, 10 orders of magnitude smaller
```

**Remember:** A bigger model trained on too little data is a waste — compute, parameters and tokens scale together.

**Common mistake:** Believing a base model will follow instructions; that behaviour comes from the tuning stages after.

---

## What you should be able to do after Day 130

- Explain **The next-token objective at scale** to someone else without notes.
- Explain **Data collection and filtering** to someone else without notes.
- Explain **Deduplication and quality scoring** to someone else without notes.
- Explain **Tokeniser training** to someone else without notes.
- Explain **Compute budget and scaling laws** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
