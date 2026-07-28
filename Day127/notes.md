# Day 127 — Positional information

Today's goal: work through **Positional information** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Why attention is order-blind |
| 2 | Sinusoidal positional encoding |
| 3 | Learned positional embeddings |
| 4 | Relative position encodings |
| 5 | RoPE rotary embeddings |
| 6 | ALiBi |
| 7 | Context length extension methods |
| 8 | Position and long-context failure |
| 9 | Lost in the middle effect |
| 10 | Choosing an encoding scheme |

---

## 1. Why attention is order-blind

Attention lets every token look at every other token and decide what matters. Each token emits a query, a key and a value; the query-key dot products become weights over the values. Multiple heads let the model attend to several relationships at once.

```python
import numpy as np

def softmax(z):
    z = z - z.max(axis=-1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=-1, keepdims=True)

rng = np.random.default_rng(0)
seq, d = 4, 8
Q, K, V = (rng.normal(size=(seq, d)) for _ in range(3))

scores = Q @ K.T / np.sqrt(d)             # scale keeps softmax out of saturation
mask = np.triu(np.ones((seq, seq)), k=1) * -1e9   # causal: no peeking ahead
weights = softmax(scores + mask)
print(weights.round(3))
print('output shape', (weights @ V).shape)
```

**Remember:** The 1/sqrt(d) scale is not cosmetic — without it softmax saturates and gradients die.

**Common mistake:** Omitting the causal mask in a decoder, so the model trivially cheats by reading the next token.

## 2. Sinusoidal positional encoding

A transformer block is attention + feed-forward, each wrapped in a residual connection and a LayerNorm. Attention alone is order-blind, so positions are injected explicitly. Encoder-only (BERT) is for understanding, decoder-only (GPT) for generation, encoder-decoder (T5) for translation-shaped tasks.

```python
import numpy as np

def positional_encoding(seq_len, d_model):
    pos = np.arange(seq_len)[:, None]
    i = np.arange(d_model)[None, :]
    angle = pos / np.power(10_000, (2 * (i // 2)) / d_model)
    pe = np.zeros((seq_len, d_model))
    pe[:, 0::2] = np.sin(angle[:, 0::2])
    pe[:, 1::2] = np.cos(angle[:, 1::2])
    return pe

pe = positional_encoding(6, 8)
print(pe.round(2))
print('shape', pe.shape)
```

**Remember:** Block = LayerNorm -> Attention -> add residual -> LayerNorm -> MLP -> add residual. Memorise it.

**Common mistake:** Assuming a bigger context window is free — attention cost grows with the square of sequence length.

## 3. Learned positional embeddings

An embedding maps text to a dense vector where nearby means similar in meaning. Unlike keyword search, 'car trouble' matches 'engine won't start'. Every RAG system is embeddings plus nearest-neighbour lookup.

```python
import numpy as np

# Toy 3-D 'embeddings' to show the mechanics
vecs = {
    'king':  np.array([0.9, 0.8, 0.1]),
    'queen': np.array([0.9, 0.1, 0.8]),
    'man':   np.array([0.4, 0.9, 0.1]),
    'woman': np.array([0.4, 0.1, 0.9]),
}

def cos(a, b):
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))

analogy = vecs['king'] - vecs['man'] + vecs['woman']
best = max(vecs, key=lambda w: cos(analogy, vecs[w]) if w != 'king' else -1)
print('king - man + woman ~', best)
```

**Remember:** Normalise embeddings, then cosine similarity is just a dot product — much faster at scale.

**Common mistake:** Mixing vectors from two different embedding models in one index; the spaces are unrelated.

## 4. Relative position encodings

Long context is not the same as long attention. Models reliably use the beginning and end of a long prompt and get vaguer in the middle. Put the instruction and the most important evidence at the edges, and do not assume a 200k window means 200k of usable attention.

```python
def arrange_prompt(instruction, chunks, question):
    """Most relevant chunks at the edges, weakest in the middle."""
    ranked = sorted(chunks, key=lambda c: -c['score'])
    head = ranked[0::2]           # strongest alternate to the front
    tail = ranked[1::2][::-1]     # rest to the back
    body = '\n'.join(c['text'] for c in head + tail)
    return f'{instruction}\n\n{body}\n\nQuestion: {question}'

chunks = [{'text': f'chunk{i}', 'score': s} for i, s in enumerate([0.9, 0.4, 0.8, 0.2])]
print(arrange_prompt('Answer only from the context.', chunks, 'refund window?'))
```

**Remember:** Order matters. Best evidence first and last; filler in the middle is where attention thins out.

**Common mistake:** Stuffing 100 retrieved chunks in retrieval order and assuming the model reads them all equally.

## 5. RoPE rotary embeddings

An embedding maps text to a dense vector where nearby means similar in meaning. Unlike keyword search, 'car trouble' matches 'engine won't start'. Every RAG system is embeddings plus nearest-neighbour lookup.

```python
import numpy as np

# Toy 3-D 'embeddings' to show the mechanics
vecs = {
    'king':  np.array([0.9, 0.8, 0.1]),
    'queen': np.array([0.9, 0.1, 0.8]),
    'man':   np.array([0.4, 0.9, 0.1]),
    'woman': np.array([0.4, 0.1, 0.9]),
}

def cos(a, b):
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))

analogy = vecs['king'] - vecs['man'] + vecs['woman']
best = max(vecs, key=lambda w: cos(analogy, vecs[w]) if w != 'king' else -1)
print('king - man + woman ~', best)
```

**Remember:** Normalise embeddings, then cosine similarity is just a dot product — much faster at scale.

**Common mistake:** Mixing vectors from two different embedding models in one index; the spaces are unrelated.

## 6. ALiBi

Long context is not the same as long attention. Models reliably use the beginning and end of a long prompt and get vaguer in the middle. Put the instruction and the most important evidence at the edges, and do not assume a 200k window means 200k of usable attention.

```python
def arrange_prompt(instruction, chunks, question):
    """Most relevant chunks at the edges, weakest in the middle."""
    ranked = sorted(chunks, key=lambda c: -c['score'])
    head = ranked[0::2]           # strongest alternate to the front
    tail = ranked[1::2][::-1]     # rest to the back
    body = '\n'.join(c['text'] for c in head + tail)
    return f'{instruction}\n\n{body}\n\nQuestion: {question}'

chunks = [{'text': f'chunk{i}', 'score': s} for i, s in enumerate([0.9, 0.4, 0.8, 0.2])]
print(arrange_prompt('Answer only from the context.', chunks, 'refund window?'))
```

**Remember:** Order matters. Best evidence first and last; filler in the middle is where attention thins out.

**Common mistake:** Stuffing 100 retrieved chunks in retrieval order and assuming the model reads them all equally.

## 7. Context length extension methods

Long context is not the same as long attention. Models reliably use the beginning and end of a long prompt and get vaguer in the middle. Put the instruction and the most important evidence at the edges, and do not assume a 200k window means 200k of usable attention.

```python
def arrange_prompt(instruction, chunks, question):
    """Most relevant chunks at the edges, weakest in the middle."""
    ranked = sorted(chunks, key=lambda c: -c['score'])
    head = ranked[0::2]           # strongest alternate to the front
    tail = ranked[1::2][::-1]     # rest to the back
    body = '\n'.join(c['text'] for c in head + tail)
    return f'{instruction}\n\n{body}\n\nQuestion: {question}'

chunks = [{'text': f'chunk{i}', 'score': s} for i, s in enumerate([0.9, 0.4, 0.8, 0.2])]
print(arrange_prompt('Answer only from the context.', chunks, 'refund window?'))
```

**Remember:** Order matters. Best evidence first and last; filler in the middle is where attention thins out.

**Common mistake:** Stuffing 100 retrieved chunks in retrieval order and assuming the model reads them all equally.

## 8. Position and long-context failure

Long context is not the same as long attention. Models reliably use the beginning and end of a long prompt and get vaguer in the middle. Put the instruction and the most important evidence at the edges, and do not assume a 200k window means 200k of usable attention.

```python
def arrange_prompt(instruction, chunks, question):
    """Most relevant chunks at the edges, weakest in the middle."""
    ranked = sorted(chunks, key=lambda c: -c['score'])
    head = ranked[0::2]           # strongest alternate to the front
    tail = ranked[1::2][::-1]     # rest to the back
    body = '\n'.join(c['text'] for c in head + tail)
    return f'{instruction}\n\n{body}\n\nQuestion: {question}'

chunks = [{'text': f'chunk{i}', 'score': s} for i, s in enumerate([0.9, 0.4, 0.8, 0.2])]
print(arrange_prompt('Answer only from the context.', chunks, 'refund window?'))
```

**Remember:** Order matters. Best evidence first and last; filler in the middle is where attention thins out.

**Common mistake:** Stuffing 100 retrieved chunks in retrieval order and assuming the model reads them all equally.

## 9. Lost in the middle effect

Long context is not the same as long attention. Models reliably use the beginning and end of a long prompt and get vaguer in the middle. Put the instruction and the most important evidence at the edges, and do not assume a 200k window means 200k of usable attention.

```python
def arrange_prompt(instruction, chunks, question):
    """Most relevant chunks at the edges, weakest in the middle."""
    ranked = sorted(chunks, key=lambda c: -c['score'])
    head = ranked[0::2]           # strongest alternate to the front
    tail = ranked[1::2][::-1]     # rest to the back
    body = '\n'.join(c['text'] for c in head + tail)
    return f'{instruction}\n\n{body}\n\nQuestion: {question}'

chunks = [{'text': f'chunk{i}', 'score': s} for i, s in enumerate([0.9, 0.4, 0.8, 0.2])]
print(arrange_prompt('Answer only from the context.', chunks, 'refund window?'))
```

**Remember:** Order matters. Best evidence first and last; filler in the middle is where attention thins out.

**Common mistake:** Stuffing 100 retrieved chunks in retrieval order and assuming the model reads them all equally.

## 10. Choosing an encoding scheme

Long context is not the same as long attention. Models reliably use the beginning and end of a long prompt and get vaguer in the middle. Put the instruction and the most important evidence at the edges, and do not assume a 200k window means 200k of usable attention.

```python
def arrange_prompt(instruction, chunks, question):
    """Most relevant chunks at the edges, weakest in the middle."""
    ranked = sorted(chunks, key=lambda c: -c['score'])
    head = ranked[0::2]           # strongest alternate to the front
    tail = ranked[1::2][::-1]     # rest to the back
    body = '\n'.join(c['text'] for c in head + tail)
    return f'{instruction}\n\n{body}\n\nQuestion: {question}'

chunks = [{'text': f'chunk{i}', 'score': s} for i, s in enumerate([0.9, 0.4, 0.8, 0.2])]
print(arrange_prompt('Answer only from the context.', chunks, 'refund window?'))
```

**Remember:** Order matters. Best evidence first and last; filler in the middle is where attention thins out.

**Common mistake:** Stuffing 100 retrieved chunks in retrieval order and assuming the model reads them all equally.

---

## What you should be able to do after Day 127

- Explain **Why attention is order-blind** to someone else without notes.
- Explain **Sinusoidal positional encoding** to someone else without notes.
- Explain **Learned positional embeddings** to someone else without notes.
- Explain **Relative position encodings** to someone else without notes.
- Explain **RoPE rotary embeddings** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
