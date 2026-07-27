# Day 121 — Tokenisation

Today's goal: work through **tokenisation** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Why models need tokens, not words |
| 2 | Word-level tokenisation and OOV |
| 3 | Character-level trade-offs |
| 4 | Byte-pair encoding |
| 5 | WordPiece and SentencePiece |
| 6 | Vocabulary size decisions |
| 7 | Special tokens: BOS, EOS, PAD, UNK |
| 8 | Token counts and cost estimation |
| 9 | Tokenisation across languages |
| 10 | Implementing BPE merges by hand |

---

## 1. Why models need tokens, not words

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

## 2. Word-level tokenisation and OOV

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

## 3. Character-level trade-offs

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

## 4. Byte-pair encoding

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

## 5. WordPiece and SentencePiece

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

## 6. Vocabulary size decisions

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

## 7. Special tokens: BOS, EOS, PAD, UNK

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

## 8. Token counts and cost estimation

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

## 9. Tokenisation across languages

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

## 10. Implementing BPE merges by hand

A DataFrame is a table with labelled columns and an index. Most real ML work is 80% reshaping tables: load, clean, group, join, aggregate. Learn `groupby` and `merge` well and you can answer most data questions without writing loops.

```python
import pandas as pd

df = pd.DataFrame({
    'city': ['pune', 'pune', 'delhi', 'delhi'],
    'sales': [10, 20, 5, 7],
})
print(df.groupby('city')['sales'].sum())

lookup = pd.DataFrame({'city': ['pune', 'delhi'], 'zone': ['west', 'north']})
print(df.merge(lookup, on='city', how='left'))
```

**Remember:** Always check `df.shape` before and after a merge — a silent row explosion means duplicate keys.

**Common mistake:** Chained assignment (`df[df.a > 1]['b'] = 0`) that writes to a copy and changes nothing.

---

## What you should be able to do after Day 121

- Explain **Why models need tokens, not words** to someone else without notes.
- Explain **Word-level tokenisation and OOV** to someone else without notes.
- Explain **Character-level trade-offs** to someone else without notes.
- Explain **Byte-pair encoding** to someone else without notes.
- Explain **WordPiece and SentencePiece** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
