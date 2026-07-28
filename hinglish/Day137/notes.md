# Day 137 — Summarisation and extraction

Aaj ka goal: **Summarisation and extraction** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Extractive vs abstractive summarisation |
| 2 | Chunking long documents |
| 3 | Map-reduce summarisation |
| 4 | Refine chains |
| 5 | Structured extraction with schemas |
| 6 | Handling documents beyond context |
| 7 | Evaluating summaries |
| 8 | ROUGE and its limits |
| 9 | Human evaluation rubrics |
| 10 | A meeting-notes summariser |

---

## 1. Extractive vs abstractive summarisation

### Aasaan Bhasha

Context window se badi documents ke liye tree me summarise karo: chunk karo, har ek ka summary banao, phir summaries ka summary. Har level par detail khoti hai, isliye jo cheezein bachni hi chahiye (numbers, naam, decisions) unhe prose ke saath structured extraction me alag rakho.

### Chhota code

```python
def map_reduce_summarize(chunks, summarize, combine_at=4):
    level = [summarize(c) for c in chunks]
    rounds = 1
    while len(level) > 1:
        level = [summarize(' '.join(level[i:i + combine_at]))
                 for i in range(0, len(level), combine_at)]
        rounds += 1
    return level[0], rounds

fake = lambda t: t[:40]
docs = [f'section {i} content ' * 5 for i in range(9)]
summary, rounds = map_reduce_summarize(docs, fake)
print(f'{len(docs)} chunks -> {rounds} rounds -> {summary!r}')
```

**Yaad rakho:** Facts structurally extract karo aur prose alag se summarise karo — summarisation sabse pehle numbers khoti hai.

**Aam galti:** Summary ki quality ROUGE se aankna, jo word overlap ko inaam deta hai aur sach hone ki parwah nahi karta.

Practice: `examples/01_extractive_vs_abstractive_summarisation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Chunking long documents

### Aasaan Bhasha

RAG jawaabon ko aapke documents me jodta hai: chunk karo, embed karo, store karo, sawaal ke liye top-k retrieve karo, aur prompt me daal do. Retrieval ki quality hi poora khel hai — galat teen chunks se perfect model ka jawab bhi galat hi rahega.

### Chhota code

```python
import numpy as np

docs = [
    'Refunds are processed within 5 business days.',
    'Our office is in Pune, open 9am to 6pm.',
    'Enterprise plans include a dedicated support engineer.',
]

def fake_embed(text):                       # stand-in for a real embedding model
    rng = np.random.default_rng(abs(hash(text)) % (2 ** 32))
    v = rng.normal(size=32)
    return v / np.linalg.norm(v)

index = np.array([fake_embed(d) for d in docs])
q = fake_embed('how long do refunds take')
top = int(np.argmax(index @ q))
print('retrieved:', docs[top])
print('\\nReal pipeline: chunk 300-800 tokens with overlap -> embed -> ANN index -> rerank -> prompt.')
```

**Yaad rakho:** Jawab me har retrieved chunk ka source dikhao taaki users use verify kar sakein.

**Aam galti:** Aankh band karke 1000 characters par chunk karna aur tables aur code blocks ko beech se kaat dena.

Practice: `examples/02_chunking_long_documents.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Map-reduce summarisation

### Aasaan Bhasha

Context window se badi documents ke liye tree me summarise karo: chunk karo, har ek ka summary banao, phir summaries ka summary. Har level par detail khoti hai, isliye jo cheezein bachni hi chahiye (numbers, naam, decisions) unhe prose ke saath structured extraction me alag rakho.

### Chhota code

```python
def map_reduce_summarize(chunks, summarize, combine_at=4):
    level = [summarize(c) for c in chunks]
    rounds = 1
    while len(level) > 1:
        level = [summarize(' '.join(level[i:i + combine_at]))
                 for i in range(0, len(level), combine_at)]
        rounds += 1
    return level[0], rounds

fake = lambda t: t[:40]
docs = [f'section {i} content ' * 5 for i in range(9)]
summary, rounds = map_reduce_summarize(docs, fake)
print(f'{len(docs)} chunks -> {rounds} rounds -> {summary!r}')
```

**Yaad rakho:** Facts structurally extract karo aur prose alag se summarise karo — summarisation sabse pehle numbers khoti hai.

**Aam galti:** Summary ki quality ROUGE se aankna, jo word overlap ko inaam deta hai aur sach hone ki parwah nahi karta.

Practice: `examples/03_map_reduce_summarisation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Refine chains

### Aasaan Bhasha

Context window se badi documents ke liye tree me summarise karo: chunk karo, har ek ka summary banao, phir summaries ka summary. Har level par detail khoti hai, isliye jo cheezein bachni hi chahiye (numbers, naam, decisions) unhe prose ke saath structured extraction me alag rakho.

### Chhota code

```python
def map_reduce_summarize(chunks, summarize, combine_at=4):
    level = [summarize(c) for c in chunks]
    rounds = 1
    while len(level) > 1:
        level = [summarize(' '.join(level[i:i + combine_at]))
                 for i in range(0, len(level), combine_at)]
        rounds += 1
    return level[0], rounds

fake = lambda t: t[:40]
docs = [f'section {i} content ' * 5 for i in range(9)]
summary, rounds = map_reduce_summarize(docs, fake)
print(f'{len(docs)} chunks -> {rounds} rounds -> {summary!r}')
```

**Yaad rakho:** Facts structurally extract karo aur prose alag se summarise karo — summarisation sabse pehle numbers khoti hai.

**Aam galti:** Summary ki quality ROUGE se aankna, jo word overlap ko inaam deta hai aur sach hone ki parwah nahi karta.

Practice: `examples/04_refine_chains.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Structured extraction with schemas

### Aasaan Bhasha

Context window se badi documents ke liye tree me summarise karo: chunk karo, har ek ka summary banao, phir summaries ka summary. Har level par detail khoti hai, isliye jo cheezein bachni hi chahiye (numbers, naam, decisions) unhe prose ke saath structured extraction me alag rakho.

### Chhota code

```python
def map_reduce_summarize(chunks, summarize, combine_at=4):
    level = [summarize(c) for c in chunks]
    rounds = 1
    while len(level) > 1:
        level = [summarize(' '.join(level[i:i + combine_at]))
                 for i in range(0, len(level), combine_at)]
        rounds += 1
    return level[0], rounds

fake = lambda t: t[:40]
docs = [f'section {i} content ' * 5 for i in range(9)]
summary, rounds = map_reduce_summarize(docs, fake)
print(f'{len(docs)} chunks -> {rounds} rounds -> {summary!r}')
```

**Yaad rakho:** Facts structurally extract karo aur prose alag se summarise karo — summarisation sabse pehle numbers khoti hai.

**Aam galti:** Summary ki quality ROUGE se aankna, jo word overlap ko inaam deta hai aur sach hone ki parwah nahi karta.

Practice: `examples/05_structured_extraction_with_schemas.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Handling documents beyond context

### Aasaan Bhasha

Context window se badi documents ke liye tree me summarise karo: chunk karo, har ek ka summary banao, phir summaries ka summary. Har level par detail khoti hai, isliye jo cheezein bachni hi chahiye (numbers, naam, decisions) unhe prose ke saath structured extraction me alag rakho.

### Chhota code

```python
def map_reduce_summarize(chunks, summarize, combine_at=4):
    level = [summarize(c) for c in chunks]
    rounds = 1
    while len(level) > 1:
        level = [summarize(' '.join(level[i:i + combine_at]))
                 for i in range(0, len(level), combine_at)]
        rounds += 1
    return level[0], rounds

fake = lambda t: t[:40]
docs = [f'section {i} content ' * 5 for i in range(9)]
summary, rounds = map_reduce_summarize(docs, fake)
print(f'{len(docs)} chunks -> {rounds} rounds -> {summary!r}')
```

**Yaad rakho:** Facts structurally extract karo aur prose alag se summarise karo — summarisation sabse pehle numbers khoti hai.

**Aam galti:** Summary ki quality ROUGE se aankna, jo word overlap ko inaam deta hai aur sach hone ki parwah nahi karta.

Practice: `examples/06_handling_documents_beyond_context.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Evaluating summaries

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

Practice: `examples/07_evaluating_summaries.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. ROUGE and its limits

### Aasaan Bhasha

Context window se badi documents ke liye tree me summarise karo: chunk karo, har ek ka summary banao, phir summaries ka summary. Har level par detail khoti hai, isliye jo cheezein bachni hi chahiye (numbers, naam, decisions) unhe prose ke saath structured extraction me alag rakho.

### Chhota code

```python
def map_reduce_summarize(chunks, summarize, combine_at=4):
    level = [summarize(c) for c in chunks]
    rounds = 1
    while len(level) > 1:
        level = [summarize(' '.join(level[i:i + combine_at]))
                 for i in range(0, len(level), combine_at)]
        rounds += 1
    return level[0], rounds

fake = lambda t: t[:40]
docs = [f'section {i} content ' * 5 for i in range(9)]
summary, rounds = map_reduce_summarize(docs, fake)
print(f'{len(docs)} chunks -> {rounds} rounds -> {summary!r}')
```

**Yaad rakho:** Facts structurally extract karo aur prose alag se summarise karo — summarisation sabse pehle numbers khoti hai.

**Aam galti:** Summary ki quality ROUGE se aankna, jo word overlap ko inaam deta hai aur sach hone ki parwah nahi karta.

Practice: `examples/08_rouge_and_its_limits.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Human evaluation rubrics

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

Practice: `examples/09_human_evaluation_rubrics.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. A meeting-notes summariser

### Aasaan Bhasha

Context window se badi documents ke liye tree me summarise karo: chunk karo, har ek ka summary banao, phir summaries ka summary. Har level par detail khoti hai, isliye jo cheezein bachni hi chahiye (numbers, naam, decisions) unhe prose ke saath structured extraction me alag rakho.

### Chhota code

```python
def map_reduce_summarize(chunks, summarize, combine_at=4):
    level = [summarize(c) for c in chunks]
    rounds = 1
    while len(level) > 1:
        level = [summarize(' '.join(level[i:i + combine_at]))
                 for i in range(0, len(level), combine_at)]
        rounds += 1
    return level[0], rounds

fake = lambda t: t[:40]
docs = [f'section {i} content ' * 5 for i in range(9)]
summary, rounds = map_reduce_summarize(docs, fake)
print(f'{len(docs)} chunks -> {rounds} rounds -> {summary!r}')
```

**Yaad rakho:** Facts structurally extract karo aur prose alag se summarise karo — summarisation sabse pehle numbers khoti hai.

**Aam galti:** Summary ki quality ROUGE se aankna, jo word overlap ko inaam deta hai aur sach hone ki parwah nahi karta.

Practice: `examples/10_a_meeting_notes_summariser.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 137 ke baad aapko ye aana chahiye

- **Extractive vs abstractive summarisation** ko bina notes dekhe kisi dost ko samjha sakna.
- **Chunking long documents** ko bina notes dekhe kisi dost ko samjha sakna.
- **Map-reduce summarisation** ko bina notes dekhe kisi dost ko samjha sakna.
- **Refine chains** ko bina notes dekhe kisi dost ko samjha sakna.
- **Structured extraction with schemas** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
