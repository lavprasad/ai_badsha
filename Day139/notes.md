# Day 139 — Multilingual and Indic NLP

Today's goal: work through **multilingual and indic nlp** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Tokenisation cost across scripts |
| 2 | Multilingual model families |
| 3 | Cross-lingual transfer |
| 4 | Translation quality evaluation |
| 5 | Code-mixed Hinglish text |
| 6 | Transliteration |
| 7 | Low-resource language strategies |
| 8 | Dataset scarcity workarounds |
| 9 | Evaluation in non-English languages |
| 10 | Building for Indian language users |

---

## 1. Tokenisation cost across scripts

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

## 2. Multilingual model families

Tokenisers are trained mostly on English, so the same sentence in Hindi or Tamil can cost three to five times more tokens — which means more money, less context and worse quality. Check the token cost of your actual users' language before you price or size anything.

```python
def rough_tokens(text, chars_per_token):
    return round(len(text) / chars_per_token)

samples = [
    ('english', 'Please refund my order from last week.', 4.0),
    ('hinglish', 'Mera last week ka order refund kar do please.', 3.5),
    ('devanagari', 'कृपया मेरा पिछले सप्ताह का ऑर्डर वापस करें।', 1.5),
]
for name, text, cpt in samples:
    print(f'{name:<12} {len(text):>3} chars -> ~{rough_tokens(text, cpt):>3} tokens')
print('\nSame meaning, very different bills and context usage.')
```

**Remember:** Measure tokens per request in your users' actual language, not in English.

**Common mistake:** Sizing a context window and a budget from English samples, then launching in a script that costs 4x.

## 3. Cross-lingual transfer

Tokenisers are trained mostly on English, so the same sentence in Hindi or Tamil can cost three to five times more tokens — which means more money, less context and worse quality. Check the token cost of your actual users' language before you price or size anything.

```python
def rough_tokens(text, chars_per_token):
    return round(len(text) / chars_per_token)

samples = [
    ('english', 'Please refund my order from last week.', 4.0),
    ('hinglish', 'Mera last week ka order refund kar do please.', 3.5),
    ('devanagari', 'कृपया मेरा पिछले सप्ताह का ऑर्डर वापस करें।', 1.5),
]
for name, text, cpt in samples:
    print(f'{name:<12} {len(text):>3} chars -> ~{rough_tokens(text, cpt):>3} tokens')
print('\nSame meaning, very different bills and context usage.')
```

**Remember:** Measure tokens per request in your users' actual language, not in English.

**Common mistake:** Sizing a context window and a budget from English samples, then launching in a script that costs 4x.

## 4. Translation quality evaluation

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

## 5. Code-mixed Hinglish text

Tokenisers are trained mostly on English, so the same sentence in Hindi or Tamil can cost three to five times more tokens — which means more money, less context and worse quality. Check the token cost of your actual users' language before you price or size anything.

```python
def rough_tokens(text, chars_per_token):
    return round(len(text) / chars_per_token)

samples = [
    ('english', 'Please refund my order from last week.', 4.0),
    ('hinglish', 'Mera last week ka order refund kar do please.', 3.5),
    ('devanagari', 'कृपया मेरा पिछले सप्ताह का ऑर्डर वापस करें।', 1.5),
]
for name, text, cpt in samples:
    print(f'{name:<12} {len(text):>3} chars -> ~{rough_tokens(text, cpt):>3} tokens')
print('\nSame meaning, very different bills and context usage.')
```

**Remember:** Measure tokens per request in your users' actual language, not in English.

**Common mistake:** Sizing a context window and a budget from English samples, then launching in a script that costs 4x.

## 6. Transliteration

Tokenisers are trained mostly on English, so the same sentence in Hindi or Tamil can cost three to five times more tokens — which means more money, less context and worse quality. Check the token cost of your actual users' language before you price or size anything.

```python
def rough_tokens(text, chars_per_token):
    return round(len(text) / chars_per_token)

samples = [
    ('english', 'Please refund my order from last week.', 4.0),
    ('hinglish', 'Mera last week ka order refund kar do please.', 3.5),
    ('devanagari', 'कृपया मेरा पिछले सप्ताह का ऑर्डर वापस करें।', 1.5),
]
for name, text, cpt in samples:
    print(f'{name:<12} {len(text):>3} chars -> ~{rough_tokens(text, cpt):>3} tokens')
print('\nSame meaning, very different bills and context usage.')
```

**Remember:** Measure tokens per request in your users' actual language, not in English.

**Common mistake:** Sizing a context window and a budget from English samples, then launching in a script that costs 4x.

## 7. Low-resource language strategies

Tokenisers are trained mostly on English, so the same sentence in Hindi or Tamil can cost three to five times more tokens — which means more money, less context and worse quality. Check the token cost of your actual users' language before you price or size anything.

```python
def rough_tokens(text, chars_per_token):
    return round(len(text) / chars_per_token)

samples = [
    ('english', 'Please refund my order from last week.', 4.0),
    ('hinglish', 'Mera last week ka order refund kar do please.', 3.5),
    ('devanagari', 'कृपया मेरा पिछले सप्ताह का ऑर्डर वापस करें।', 1.5),
]
for name, text, cpt in samples:
    print(f'{name:<12} {len(text):>3} chars -> ~{rough_tokens(text, cpt):>3} tokens')
print('\nSame meaning, very different bills and context usage.')
```

**Remember:** Measure tokens per request in your users' actual language, not in English.

**Common mistake:** Sizing a context window and a budget from English samples, then launching in a script that costs 4x.

## 8. Dataset scarcity workarounds

ML code needs the same tests as any code, plus data tests: schema, ranges, null rates, class balance. Add one behavioural test per known failure mode — a test that would have caught last quarter's outage is worth more than 90% coverage.

```python
import numpy as np

def preprocess(x):
    x = np.asarray(x, dtype=float)
    if np.isnan(x).any():
        raise ValueError('NaN in input')
    return (x - x.mean()) / (x.std() + 1e-8)

def test_preprocess():
    out = preprocess([1.0, 2.0, 3.0])
    assert abs(float(out.mean())) < 1e-6, 'should be zero-centred'
    assert abs(float(out.std()) - 1.0) < 1e-6, 'should be unit variance'
    try:
        preprocess([1.0, float('nan')])
    except ValueError:
        pass
    else:
        raise AssertionError('NaN should have raised')
    print('ok')

test_preprocess()
```

**Remember:** Test the data contract, not just the function — bad data breaks more models than bad code.

**Common mistake:** Testing only the happy path, so an all-null column silently trains a constant model.

## 9. Evaluation in non-English languages

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

## 10. Building for Indian language users

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

---

## What you should be able to do after Day 139

- Explain **Tokenisation cost across scripts** to someone else without notes.
- Explain **Multilingual model families** to someone else without notes.
- Explain **Cross-lingual transfer** to someone else without notes.
- Explain **Translation quality evaluation** to someone else without notes.
- Explain **Code-mixed Hinglish text** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
