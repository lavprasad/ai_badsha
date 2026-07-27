# Day 137 — Summarisation and extraction

Today's goal: work through **summarisation and extraction** — ten concepts, ten runnable examples, five questions.

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

For documents larger than the context window, summarise in a tree: chunk, summarise each, then summarise the summaries. Detail is lost at every level, so keep the things that must survive (numbers, names, decisions) as structured extraction alongside the prose.

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

**Remember:** Extract facts structurally and summarise prose separately — summarisation loses numbers first.

**Common mistake:** Judging summary quality by ROUGE, which rewards word overlap and ignores whether it is true.

## 2. Chunking long documents

RAG grounds answers in your documents: chunk, embed, store, retrieve the top-k for the question, and put them in the prompt. Retrieval quality is the whole ballgame — a perfect model answering from the wrong three chunks is still wrong.

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

**Remember:** Always show the source of each retrieved chunk in the answer so users can verify it.

**Common mistake:** Chunking blindly at 1000 characters and cutting tables and code blocks in half.

## 3. Map-reduce summarisation

For documents larger than the context window, summarise in a tree: chunk, summarise each, then summarise the summaries. Detail is lost at every level, so keep the things that must survive (numbers, names, decisions) as structured extraction alongside the prose.

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

**Remember:** Extract facts structurally and summarise prose separately — summarisation loses numbers first.

**Common mistake:** Judging summary quality by ROUGE, which rewards word overlap and ignores whether it is true.

## 4. Refine chains

For documents larger than the context window, summarise in a tree: chunk, summarise each, then summarise the summaries. Detail is lost at every level, so keep the things that must survive (numbers, names, decisions) as structured extraction alongside the prose.

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

**Remember:** Extract facts structurally and summarise prose separately — summarisation loses numbers first.

**Common mistake:** Judging summary quality by ROUGE, which rewards word overlap and ignores whether it is true.

## 5. Structured extraction with schemas

For documents larger than the context window, summarise in a tree: chunk, summarise each, then summarise the summaries. Detail is lost at every level, so keep the things that must survive (numbers, names, decisions) as structured extraction alongside the prose.

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

**Remember:** Extract facts structurally and summarise prose separately — summarisation loses numbers first.

**Common mistake:** Judging summary quality by ROUGE, which rewards word overlap and ignores whether it is true.

## 6. Handling documents beyond context

For documents larger than the context window, summarise in a tree: chunk, summarise each, then summarise the summaries. Detail is lost at every level, so keep the things that must survive (numbers, names, decisions) as structured extraction alongside the prose.

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

**Remember:** Extract facts structurally and summarise prose separately — summarisation loses numbers first.

**Common mistake:** Judging summary quality by ROUGE, which rewards word overlap and ignores whether it is true.

## 7. Evaluating summaries

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

## 8. ROUGE and its limits

For documents larger than the context window, summarise in a tree: chunk, summarise each, then summarise the summaries. Detail is lost at every level, so keep the things that must survive (numbers, names, decisions) as structured extraction alongside the prose.

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

**Remember:** Extract facts structurally and summarise prose separately — summarisation loses numbers first.

**Common mistake:** Judging summary quality by ROUGE, which rewards word overlap and ignores whether it is true.

## 9. Human evaluation rubrics

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

## 10. A meeting-notes summariser

For documents larger than the context window, summarise in a tree: chunk, summarise each, then summarise the summaries. Detail is lost at every level, so keep the things that must survive (numbers, names, decisions) as structured extraction alongside the prose.

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

**Remember:** Extract facts structurally and summarise prose separately — summarisation loses numbers first.

**Common mistake:** Judging summary quality by ROUGE, which rewards word overlap and ignores whether it is true.

---

## What you should be able to do after Day 137

- Explain **Extractive vs abstractive summarisation** to someone else without notes.
- Explain **Chunking long documents** to someone else without notes.
- Explain **Map-reduce summarisation** to someone else without notes.
- Explain **Refine chains** to someone else without notes.
- Explain **Structured extraction with schemas** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
