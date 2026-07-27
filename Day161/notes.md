# Day 161 — Memory for AI applications

Today's goal: work through **memory for ai applications** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Short-term context vs long-term memory |
| 2 | Conversation summarisation |
| 3 | Fact extraction and storage |
| 4 | Vector memory and its failure modes |
| 5 | Structured memory in a database |
| 6 | Recency, relevance and importance scoring |
| 7 | Forgetting and expiry |
| 8 | Privacy and user control over memory |
| 9 | Memory conflicts and contradictions |
| 10 | Designing a memory schema |

---

## 1. Short-term context vs long-term memory

Context is not memory. Context is what fits in this request; memory is what you deliberately store and retrieve. Design the schema explicitly — what is stored, how it expires, how conflicts resolve — or you get an assistant that confidently repeats something the user corrected last month.

```python
import time

class Memory:
    def __init__(self, ttl_days=90):
        self.items, self.ttl = [], ttl_days * 86400

    def add(self, key, value, ts):
        self.items = [i for i in self.items if i['key'] != key]   # newest wins
        self.items.append({'key': key, 'value': value, 'ts': ts})

    def recall(self, now):
        return [i for i in self.items if now - i['ts'] < self.ttl]

m = Memory(ttl_days=30)
m.add('preferred_name', 'Sam', ts=0)
m.add('preferred_name', 'Samir', ts=100)      # correction replaces, not appends
print(m.recall(now=200))
print(m.recall(now=30 * 86400 + 200))          # expired
```

**Remember:** A correction must overwrite, not coexist. Two contradictory memories will both get retrieved.

**Common mistake:** Appending every stated fact to a vector store forever, so stale and corrected facts compete at retrieval.

## 2. Conversation summarisation

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

## 3. Fact extraction and storage

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

## 4. Vector memory and its failure modes

A vector is a list of numbers with a direction and length. The dot product measures alignment: large and positive when two vectors point the same way, zero when perpendicular. Cosine similarity is the dot product with length divided out, which is why it compares embeddings of different magnitudes fairly.

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 4.0, 6.0])

print('dot   ', a @ b)
print('norm  ', np.linalg.norm(a))
cos = (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))
print('cosine', cos)   # 1.0 -> same direction
```

**Remember:** Cosine similarity ignores magnitude; Euclidean distance does not. Pick the one that matches your question.

**Common mistake:** Comparing raw embeddings with Euclidean distance when only direction carries meaning.

## 5. Structured memory in a database

Today's idea — **Structured memory in a database** — sits inside the theme of Memory for AI applications. Read it as a tool, not trivia: what job does it do, what does it assume about your data, and what breaks when that assumption is false?

```python
# Explore: Structured memory in a database
print("practice: Structured memory in a database")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Remember:** State one assumption `Structured memory in a database` makes about your data before you use it.

**Common mistake:** Copy-pasting `Structured memory in a database` from a tutorial without knowing what it assumes or when it fails.

## 6. Recency, relevance and importance scoring

Context is not memory. Context is what fits in this request; memory is what you deliberately store and retrieve. Design the schema explicitly — what is stored, how it expires, how conflicts resolve — or you get an assistant that confidently repeats something the user corrected last month.

```python
import time

class Memory:
    def __init__(self, ttl_days=90):
        self.items, self.ttl = [], ttl_days * 86400

    def add(self, key, value, ts):
        self.items = [i for i in self.items if i['key'] != key]   # newest wins
        self.items.append({'key': key, 'value': value, 'ts': ts})

    def recall(self, now):
        return [i for i in self.items if now - i['ts'] < self.ttl]

m = Memory(ttl_days=30)
m.add('preferred_name', 'Sam', ts=0)
m.add('preferred_name', 'Samir', ts=100)      # correction replaces, not appends
print(m.recall(now=200))
print(m.recall(now=30 * 86400 + 200))          # expired
```

**Remember:** A correction must overwrite, not coexist. Two contradictory memories will both get retrieved.

**Common mistake:** Appending every stated fact to a vector store forever, so stale and corrected facts compete at retrieval.

## 7. Forgetting and expiry

Context is not memory. Context is what fits in this request; memory is what you deliberately store and retrieve. Design the schema explicitly — what is stored, how it expires, how conflicts resolve — or you get an assistant that confidently repeats something the user corrected last month.

```python
import time

class Memory:
    def __init__(self, ttl_days=90):
        self.items, self.ttl = [], ttl_days * 86400

    def add(self, key, value, ts):
        self.items = [i for i in self.items if i['key'] != key]   # newest wins
        self.items.append({'key': key, 'value': value, 'ts': ts})

    def recall(self, now):
        return [i for i in self.items if now - i['ts'] < self.ttl]

m = Memory(ttl_days=30)
m.add('preferred_name', 'Sam', ts=0)
m.add('preferred_name', 'Samir', ts=100)      # correction replaces, not appends
print(m.recall(now=200))
print(m.recall(now=30 * 86400 + 200))          # expired
```

**Remember:** A correction must overwrite, not coexist. Two contradictory memories will both get retrieved.

**Common mistake:** Appending every stated fact to a vector store forever, so stale and corrected facts compete at retrieval.

## 8. Privacy and user control over memory

Models learn the bias in their training data and then apply it at scale with a veneer of objectivity. Measure error rates per group, not just overall. Fairness definitions genuinely conflict with each other — you must choose one explicitly and document why.

```python
import numpy as np
import pandas as pd

df = pd.DataFrame({
    'group': ['a'] * 100 + ['b'] * 100,
    'y':     [1] * 50 + [0] * 50 + [1] * 50 + [0] * 50,
    'pred':  [1] * 45 + [0] * 55 + [1] * 30 + [0] * 70,
})
for g, sub in df.groupby('group'):
    tpr = ((sub.pred == 1) & (sub.y == 1)).sum() / max((sub.y == 1).sum(), 1)
    rate = (sub.pred == 1).mean()
    print(f'group {g}: selection rate {rate:.2f}  recall {tpr:.2f}')
print('Large gaps here are the finding — investigate before shipping.')
```

**Remember:** Dropping the sensitive attribute does not remove bias; proxies (pincode, name) carry it right back in.

**Common mistake:** Auditing fairness once at launch and never again as the data drifts.

## 9. Memory conflicts and contradictions

Context is not memory. Context is what fits in this request; memory is what you deliberately store and retrieve. Design the schema explicitly — what is stored, how it expires, how conflicts resolve — or you get an assistant that confidently repeats something the user corrected last month.

```python
import time

class Memory:
    def __init__(self, ttl_days=90):
        self.items, self.ttl = [], ttl_days * 86400

    def add(self, key, value, ts):
        self.items = [i for i in self.items if i['key'] != key]   # newest wins
        self.items.append({'key': key, 'value': value, 'ts': ts})

    def recall(self, now):
        return [i for i in self.items if now - i['ts'] < self.ttl]

m = Memory(ttl_days=30)
m.add('preferred_name', 'Sam', ts=0)
m.add('preferred_name', 'Samir', ts=100)      # correction replaces, not appends
print(m.recall(now=200))
print(m.recall(now=30 * 86400 + 200))          # expired
```

**Remember:** A correction must overwrite, not coexist. Two contradictory memories will both get retrieved.

**Common mistake:** Appending every stated fact to a vector store forever, so stale and corrected facts compete at retrieval.

## 10. Designing a memory schema

Context is not memory. Context is what fits in this request; memory is what you deliberately store and retrieve. Design the schema explicitly — what is stored, how it expires, how conflicts resolve — or you get an assistant that confidently repeats something the user corrected last month.

```python
import time

class Memory:
    def __init__(self, ttl_days=90):
        self.items, self.ttl = [], ttl_days * 86400

    def add(self, key, value, ts):
        self.items = [i for i in self.items if i['key'] != key]   # newest wins
        self.items.append({'key': key, 'value': value, 'ts': ts})

    def recall(self, now):
        return [i for i in self.items if now - i['ts'] < self.ttl]

m = Memory(ttl_days=30)
m.add('preferred_name', 'Sam', ts=0)
m.add('preferred_name', 'Samir', ts=100)      # correction replaces, not appends
print(m.recall(now=200))
print(m.recall(now=30 * 86400 + 200))          # expired
```

**Remember:** A correction must overwrite, not coexist. Two contradictory memories will both get retrieved.

**Common mistake:** Appending every stated fact to a vector store forever, so stale and corrected facts compete at retrieval.

---

## What you should be able to do after Day 161

- Explain **Short-term context vs long-term memory** to someone else without notes.
- Explain **Conversation summarisation** to someone else without notes.
- Explain **Fact extraction and storage** to someone else without notes.
- Explain **Vector memory and its failure modes** to someone else without notes.
- Explain **Structured memory in a database** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
