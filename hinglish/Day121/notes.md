# Day 121 — Tokenisation

Aaj ka goal: **Tokenisation** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

### Aasaan Bhasha

Models text nahi, token IDs dekhte hain. Byte-pair encoding aksar aane wale character pairs ko jod deta hai taaki common words ek token banein aur rare words tukdon me toote. Tokens hi wajah hain ki bill per-token hai, context limits tokens me hain, aur models letters ginne me kamzor hain.

### Chhota code

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

**Yaad rakho:** Lagbhag 1 token ~ 4 English characters; doosri bhashaon me per word tokens kahin zyada lagte hain.

**Aam galti:** Cost ya context ka andaaza words me lagana, tokens me nahi, aur production me window overflow kar dena.

Practice: `examples/01_why_models_need_tokens_not_words.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Word-level tokenisation and OOV

### Aasaan Bhasha

Models text nahi, token IDs dekhte hain. Byte-pair encoding aksar aane wale character pairs ko jod deta hai taaki common words ek token banein aur rare words tukdon me toote. Tokens hi wajah hain ki bill per-token hai, context limits tokens me hain, aur models letters ginne me kamzor hain.

### Chhota code

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

**Yaad rakho:** Lagbhag 1 token ~ 4 English characters; doosri bhashaon me per word tokens kahin zyada lagte hain.

**Aam galti:** Cost ya context ka andaaza words me lagana, tokens me nahi, aur production me window overflow kar dena.

Practice: `examples/02_word_level_tokenisation_and_oov.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Character-level trade-offs

### Aasaan Bhasha

Models text nahi, token IDs dekhte hain. Byte-pair encoding aksar aane wale character pairs ko jod deta hai taaki common words ek token banein aur rare words tukdon me toote. Tokens hi wajah hain ki bill per-token hai, context limits tokens me hain, aur models letters ginne me kamzor hain.

### Chhota code

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

**Yaad rakho:** Lagbhag 1 token ~ 4 English characters; doosri bhashaon me per word tokens kahin zyada lagte hain.

**Aam galti:** Cost ya context ka andaaza words me lagana, tokens me nahi, aur production me window overflow kar dena.

Practice: `examples/03_character_level_trade_offs.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Byte-pair encoding

### Aasaan Bhasha

Models text nahi, token IDs dekhte hain. Byte-pair encoding aksar aane wale character pairs ko jod deta hai taaki common words ek token banein aur rare words tukdon me toote. Tokens hi wajah hain ki bill per-token hai, context limits tokens me hain, aur models letters ginne me kamzor hain.

### Chhota code

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

**Yaad rakho:** Lagbhag 1 token ~ 4 English characters; doosri bhashaon me per word tokens kahin zyada lagte hain.

**Aam galti:** Cost ya context ka andaaza words me lagana, tokens me nahi, aur production me window overflow kar dena.

Practice: `examples/04_byte_pair_encoding.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. WordPiece and SentencePiece

### Aasaan Bhasha

Models text nahi, token IDs dekhte hain. Byte-pair encoding aksar aane wale character pairs ko jod deta hai taaki common words ek token banein aur rare words tukdon me toote. Tokens hi wajah hain ki bill per-token hai, context limits tokens me hain, aur models letters ginne me kamzor hain.

### Chhota code

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

**Yaad rakho:** Lagbhag 1 token ~ 4 English characters; doosri bhashaon me per word tokens kahin zyada lagte hain.

**Aam galti:** Cost ya context ka andaaza words me lagana, tokens me nahi, aur production me window overflow kar dena.

Practice: `examples/05_wordpiece_and_sentencepiece.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Vocabulary size decisions

### Aasaan Bhasha

Models text nahi, token IDs dekhte hain. Byte-pair encoding aksar aane wale character pairs ko jod deta hai taaki common words ek token banein aur rare words tukdon me toote. Tokens hi wajah hain ki bill per-token hai, context limits tokens me hain, aur models letters ginne me kamzor hain.

### Chhota code

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

**Yaad rakho:** Lagbhag 1 token ~ 4 English characters; doosri bhashaon me per word tokens kahin zyada lagte hain.

**Aam galti:** Cost ya context ka andaaza words me lagana, tokens me nahi, aur production me window overflow kar dena.

Practice: `examples/06_vocabulary_size_decisions.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Special tokens: BOS, EOS, PAD, UNK

### Aasaan Bhasha

Models text nahi, token IDs dekhte hain. Byte-pair encoding aksar aane wale character pairs ko jod deta hai taaki common words ek token banein aur rare words tukdon me toote. Tokens hi wajah hain ki bill per-token hai, context limits tokens me hain, aur models letters ginne me kamzor hain.

### Chhota code

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

**Yaad rakho:** Lagbhag 1 token ~ 4 English characters; doosri bhashaon me per word tokens kahin zyada lagte hain.

**Aam galti:** Cost ya context ka andaaza words me lagana, tokens me nahi, aur production me window overflow kar dena.

Practice: `examples/07_special_tokens_bos_eos_pad_unk.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Token counts and cost estimation

### Aasaan Bhasha

Models text nahi, token IDs dekhte hain. Byte-pair encoding aksar aane wale character pairs ko jod deta hai taaki common words ek token banein aur rare words tukdon me toote. Tokens hi wajah hain ki bill per-token hai, context limits tokens me hain, aur models letters ginne me kamzor hain.

### Chhota code

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

**Yaad rakho:** Lagbhag 1 token ~ 4 English characters; doosri bhashaon me per word tokens kahin zyada lagte hain.

**Aam galti:** Cost ya context ka andaaza words me lagana, tokens me nahi, aur production me window overflow kar dena.

Practice: `examples/08_token_counts_and_cost_estimation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Tokenisation across languages

### Aasaan Bhasha

Models text nahi, token IDs dekhte hain. Byte-pair encoding aksar aane wale character pairs ko jod deta hai taaki common words ek token banein aur rare words tukdon me toote. Tokens hi wajah hain ki bill per-token hai, context limits tokens me hain, aur models letters ginne me kamzor hain.

### Chhota code

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

**Yaad rakho:** Lagbhag 1 token ~ 4 English characters; doosri bhashaon me per word tokens kahin zyada lagte hain.

**Aam galti:** Cost ya context ka andaaza words me lagana, tokens me nahi, aur production me window overflow kar dena.

Practice: `examples/09_tokenisation_across_languages.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Implementing BPE merges by hand

### Aasaan Bhasha

DataFrame ek table hai jisme labelled columns aur ek index hota hai. Asli ML ka 80% kaam tables ko reshape karna hi hai: load, clean, group, join, aggregate. `groupby` aur `merge` acche se seekh lo to zyadatar data sawaal bina loop likhe hal ho jaate hain.

### Chhota code

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

**Yaad rakho:** Merge se pehle aur baad me `df.shape` zaroor check karo — chupke se rows badhna matlab duplicate keys.

**Aam galti:** Chained assignment (`df[df.a > 1]['b'] = 0`) jo copy par likhta hai aur kuch nahi badalta.

Practice: `examples/10_implementing_bpe_merges_by_hand.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 121 ke baad aapko ye aana chahiye

- **Why models need tokens, not words** ko bina notes dekhe kisi dost ko samjha sakna.
- **Word-level tokenisation and OOV** ko bina notes dekhe kisi dost ko samjha sakna.
- **Character-level trade-offs** ko bina notes dekhe kisi dost ko samjha sakna.
- **Byte-pair encoding** ko bina notes dekhe kisi dost ko samjha sakna.
- **WordPiece and SentencePiece** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
