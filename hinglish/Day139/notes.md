# Day 139 — Multilingual and Indic NLP

Aaj ka goal: **Multilingual and Indic NLP** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

Practice: `examples/01_tokenisation_cost_across_scripts.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Multilingual model families

### Aasaan Bhasha

Tokenisers zyadatar English par train hote hain, isliye wahi vaakya Hindi ya Tamil me teen se paanch guna zyada tokens le sakta hai — matlab zyada paisa, kam context aur kharab quality. Kuch bhi price ya size karne se pehle apne asli users ki bhasha ka token cost check karo.

### Chhota code

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

**Yaad rakho:** Per request tokens apne users ki asli bhasha me naapo, English me nahi.

**Aam galti:** English samples se context window aur budget tay karna, phir aisi script me launch karna jo 4x mehngi hai.

Practice: `examples/02_multilingual_model_families.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Cross-lingual transfer

### Aasaan Bhasha

Tokenisers zyadatar English par train hote hain, isliye wahi vaakya Hindi ya Tamil me teen se paanch guna zyada tokens le sakta hai — matlab zyada paisa, kam context aur kharab quality. Kuch bhi price ya size karne se pehle apne asli users ki bhasha ka token cost check karo.

### Chhota code

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

**Yaad rakho:** Per request tokens apne users ki asli bhasha me naapo, English me nahi.

**Aam galti:** English samples se context window aur budget tay karna, phir aisi script me launch karna jo 4x mehngi hai.

Practice: `examples/03_cross_lingual_transfer.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Translation quality evaluation

### Aasaan Bhasha

Vibes prompt change se nahi bachte. Asli inputs ka chhota golden set banao expected outputs ke saath, har change par chalao, aur score track karo. Open-ended quality ke liye LLM judge use karo, par pehle judge ko human ratings se calibrate karo.

### Chhota code

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

**Yaad rakho:** Aapke chune hue 50 asli examples 5000 synthetic examples se behtar hain jinhe kisi ne check hi nahi kiya.

**Aam galti:** Shukravaar ko bina eval ke prompt badalna aur somvaar ko customers se pata chalna.

Practice: `examples/04_translation_quality_evaluation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Code-mixed Hinglish text

### Aasaan Bhasha

Tokenisers zyadatar English par train hote hain, isliye wahi vaakya Hindi ya Tamil me teen se paanch guna zyada tokens le sakta hai — matlab zyada paisa, kam context aur kharab quality. Kuch bhi price ya size karne se pehle apne asli users ki bhasha ka token cost check karo.

### Chhota code

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

**Yaad rakho:** Per request tokens apne users ki asli bhasha me naapo, English me nahi.

**Aam galti:** English samples se context window aur budget tay karna, phir aisi script me launch karna jo 4x mehngi hai.

Practice: `examples/05_code_mixed_hinglish_text.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Transliteration

### Aasaan Bhasha

Tokenisers zyadatar English par train hote hain, isliye wahi vaakya Hindi ya Tamil me teen se paanch guna zyada tokens le sakta hai — matlab zyada paisa, kam context aur kharab quality. Kuch bhi price ya size karne se pehle apne asli users ki bhasha ka token cost check karo.

### Chhota code

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

**Yaad rakho:** Per request tokens apne users ki asli bhasha me naapo, English me nahi.

**Aam galti:** English samples se context window aur budget tay karna, phir aisi script me launch karna jo 4x mehngi hai.

Practice: `examples/06_transliteration.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Low-resource language strategies

### Aasaan Bhasha

Tokenisers zyadatar English par train hote hain, isliye wahi vaakya Hindi ya Tamil me teen se paanch guna zyada tokens le sakta hai — matlab zyada paisa, kam context aur kharab quality. Kuch bhi price ya size karne se pehle apne asli users ki bhasha ka token cost check karo.

### Chhota code

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

**Yaad rakho:** Per request tokens apne users ki asli bhasha me naapo, English me nahi.

**Aam galti:** English samples se context window aur budget tay karna, phir aisi script me launch karna jo 4x mehngi hai.

Practice: `examples/07_low_resource_language_strategies.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Dataset scarcity workarounds

### Aasaan Bhasha

ML code ko baaki code jaise tests chahiye, plus data tests: schema, ranges, null rates, class balance. Har known failure mode ke liye ek behavioural test jodo — ek test jo pichhli baar ka outage pakad leta, wo 90% coverage se zyada keemti hai.

### Chhota code

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

**Yaad rakho:** Data contract test karo, sirf function nahi — kharab data kharab code se zyada models todta hai.

**Aam galti:** Sirf happy path test karna, jisse poora-null column chupchap constant model train kar deta hai.

Practice: `examples/08_dataset_scarcity_workarounds.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Evaluation in non-English languages

### Aasaan Bhasha

Vibes prompt change se nahi bachte. Asli inputs ka chhota golden set banao expected outputs ke saath, har change par chalao, aur score track karo. Open-ended quality ke liye LLM judge use karo, par pehle judge ko human ratings se calibrate karo.

### Chhota code

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

**Yaad rakho:** Aapke chune hue 50 asli examples 5000 synthetic examples se behtar hain jinhe kisi ne check hi nahi kiya.

**Aam galti:** Shukravaar ko bina eval ke prompt badalna aur somvaar ko customers se pata chalna.

Practice: `examples/09_evaluation_in_non_english_languages.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Building for Indian language users

### Aasaan Bhasha

Projects wahi jagah hain jahan seekha hua chipakta hai. Pehle ek patli end-to-end slice banao — data load, kuch bewakoof train, evaluate, ek prediction serve — phir ek-ek layer sudharo. Pehle din chalne wala baseline us perfect model se behtar hai jo kabhi ship hi nahi hota.

### Chhota code

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

**Yaad rakho:** Hyperparameters tune karne me ek din lagane se pehle galat predictions dekhne me ek ghanta lagao.

**Aam galti:** Chhe hafte feature engineering karna bina kisi baseline ke jo sabit kare ki kisi cheez se fayda hua.

Practice: `examples/10_building_for_indian_language_users.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 139 ke baad aapko ye aana chahiye

- **Tokenisation cost across scripts** ko bina notes dekhe kisi dost ko samjha sakna.
- **Multilingual model families** ko bina notes dekhe kisi dost ko samjha sakna.
- **Cross-lingual transfer** ko bina notes dekhe kisi dost ko samjha sakna.
- **Translation quality evaluation** ko bina notes dekhe kisi dost ko samjha sakna.
- **Code-mixed Hinglish text** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
