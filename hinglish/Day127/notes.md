# Day 127 — Positional information

Aaj ka goal: **Positional information** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

### Aasaan Bhasha

Attention har token ko har doosre token ko dekh kar tay karne deta hai ki kya important hai. Har token ek query, ek key aur ek value deta hai; query-key dot products values par weights ban jaate hain. Multiple heads model ko ek saath kai rishton par dhyaan dene dete hain.

### Chhota code

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

**Yaad rakho:** 1/sqrt(d) wala scale sajावat nahi hai — uske bina softmax saturate ho jaata hai aur gradients mar jaate hain.

**Aam galti:** Decoder me causal mask chhod dena, jisse model agla token padh kar aasani se cheating kar leta hai.

Practice: `examples/01_why_attention_is_order_blind.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Sinusoidal positional encoding

### Aasaan Bhasha

Transformer block = attention + feed-forward, dono residual connection aur LayerNorm me lipte hue. Akeli attention order-blind hai, isliye positions alag se daali jaati hain. Encoder-only (BERT) samajhne ke liye, decoder-only (GPT) generation ke liye, encoder-decoder (T5) translation jaise tasks ke liye.

### Chhota code

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

**Yaad rakho:** Block = LayerNorm -> Attention -> residual add -> LayerNorm -> MLP -> residual add. Ise ratt lo.

**Aam galti:** Yeh maan lena ki bada context window muft hai — attention ka cost sequence length ke square se badhta hai.

Practice: `examples/02_sinusoidal_positional_encoding.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Learned positional embeddings

### Aasaan Bhasha

Embedding text ko dense vector me badalta hai jahan paas hona matlab matlab me paas hona. Keyword search ke ulat, 'car trouble' 'engine won't start' se match ho jaata hai. Har RAG system embeddings + nearest-neighbour lookup hi hai.

### Chhota code

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

**Yaad rakho:** Embeddings normalise kar do, phir cosine similarity sirf dot product hai — scale par bahut tez.

**Aam galti:** Ek hi index me do alag embedding models ke vectors mila dena; wo spaces aapas me bilkul unrelated hain.

Practice: `examples/03_learned_positional_embeddings.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Relative position encodings

### Aasaan Bhasha

Lamba context aur lambi attention ek cheez nahi hai. Models lambe prompt ki shuruaat aur ant ka bharosemand istemaal karte hain aur beech me dhundhle ho jaate hain. Instruction aur sabse zaroori evidence kinaaron par rakho, aur ye mat maano ki 200k window matlab 200k usable attention.

### Chhota code

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

**Yaad rakho:** Order maayne rakhta hai. Sabse achha evidence pehle aur aakhir me; beech me wahi jahan attention patli hoti hai.

**Aam galti:** 100 retrieved chunks retrieval order me thoons dena aur maan lena ki model sabko barabar padhta hai.

Practice: `examples/04_relative_position_encodings.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. RoPE rotary embeddings

### Aasaan Bhasha

Embedding text ko dense vector me badalta hai jahan paas hona matlab matlab me paas hona. Keyword search ke ulat, 'car trouble' 'engine won't start' se match ho jaata hai. Har RAG system embeddings + nearest-neighbour lookup hi hai.

### Chhota code

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

**Yaad rakho:** Embeddings normalise kar do, phir cosine similarity sirf dot product hai — scale par bahut tez.

**Aam galti:** Ek hi index me do alag embedding models ke vectors mila dena; wo spaces aapas me bilkul unrelated hain.

Practice: `examples/05_rope_rotary_embeddings.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. ALiBi

### Aasaan Bhasha

Lamba context aur lambi attention ek cheez nahi hai. Models lambe prompt ki shuruaat aur ant ka bharosemand istemaal karte hain aur beech me dhundhle ho jaate hain. Instruction aur sabse zaroori evidence kinaaron par rakho, aur ye mat maano ki 200k window matlab 200k usable attention.

### Chhota code

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

**Yaad rakho:** Order maayne rakhta hai. Sabse achha evidence pehle aur aakhir me; beech me wahi jahan attention patli hoti hai.

**Aam galti:** 100 retrieved chunks retrieval order me thoons dena aur maan lena ki model sabko barabar padhta hai.

Practice: `examples/06_alibi.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Context length extension methods

### Aasaan Bhasha

Lamba context aur lambi attention ek cheez nahi hai. Models lambe prompt ki shuruaat aur ant ka bharosemand istemaal karte hain aur beech me dhundhle ho jaate hain. Instruction aur sabse zaroori evidence kinaaron par rakho, aur ye mat maano ki 200k window matlab 200k usable attention.

### Chhota code

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

**Yaad rakho:** Order maayne rakhta hai. Sabse achha evidence pehle aur aakhir me; beech me wahi jahan attention patli hoti hai.

**Aam galti:** 100 retrieved chunks retrieval order me thoons dena aur maan lena ki model sabko barabar padhta hai.

Practice: `examples/07_context_length_extension_methods.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Position and long-context failure

### Aasaan Bhasha

Lamba context aur lambi attention ek cheez nahi hai. Models lambe prompt ki shuruaat aur ant ka bharosemand istemaal karte hain aur beech me dhundhle ho jaate hain. Instruction aur sabse zaroori evidence kinaaron par rakho, aur ye mat maano ki 200k window matlab 200k usable attention.

### Chhota code

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

**Yaad rakho:** Order maayne rakhta hai. Sabse achha evidence pehle aur aakhir me; beech me wahi jahan attention patli hoti hai.

**Aam galti:** 100 retrieved chunks retrieval order me thoons dena aur maan lena ki model sabko barabar padhta hai.

Practice: `examples/08_position_and_long_context_failure.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Lost in the middle effect

### Aasaan Bhasha

Lamba context aur lambi attention ek cheez nahi hai. Models lambe prompt ki shuruaat aur ant ka bharosemand istemaal karte hain aur beech me dhundhle ho jaate hain. Instruction aur sabse zaroori evidence kinaaron par rakho, aur ye mat maano ki 200k window matlab 200k usable attention.

### Chhota code

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

**Yaad rakho:** Order maayne rakhta hai. Sabse achha evidence pehle aur aakhir me; beech me wahi jahan attention patli hoti hai.

**Aam galti:** 100 retrieved chunks retrieval order me thoons dena aur maan lena ki model sabko barabar padhta hai.

Practice: `examples/09_lost_in_the_middle_effect.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Choosing an encoding scheme

### Aasaan Bhasha

Lamba context aur lambi attention ek cheez nahi hai. Models lambe prompt ki shuruaat aur ant ka bharosemand istemaal karte hain aur beech me dhundhle ho jaate hain. Instruction aur sabse zaroori evidence kinaaron par rakho, aur ye mat maano ki 200k window matlab 200k usable attention.

### Chhota code

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

**Yaad rakho:** Order maayne rakhta hai. Sabse achha evidence pehle aur aakhir me; beech me wahi jahan attention patli hoti hai.

**Aam galti:** 100 retrieved chunks retrieval order me thoons dena aur maan lena ki model sabko barabar padhta hai.

Practice: `examples/10_choosing_an_encoding_scheme.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 127 ke baad aapko ye aana chahiye

- **Why attention is order-blind** ko bina notes dekhe kisi dost ko samjha sakna.
- **Sinusoidal positional encoding** ko bina notes dekhe kisi dost ko samjha sakna.
- **Learned positional embeddings** ko bina notes dekhe kisi dost ko samjha sakna.
- **Relative position encodings** ko bina notes dekhe kisi dost ko samjha sakna.
- **RoPE rotary embeddings** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
