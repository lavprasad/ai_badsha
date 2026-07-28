# Day 125 — The transformer architecture

Aaj ka goal: **The transformer architecture** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | The 2017 idea: attention is all you need |
| 2 | Input embeddings and positional encoding |
| 3 | Self-attention block |
| 4 | Multi-head attention |
| 5 | Feed-forward network per position |
| 6 | Residual connections and LayerNorm |
| 7 | Encoder stack |
| 8 | Decoder stack and causal masking |
| 9 | Parameter count breakdown |
| 10 | Drawing the block from memory |

---

## 1. The 2017 idea: attention is all you need

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

Practice: `examples/01_the_2017_idea_attention_is_all_you_need.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Input embeddings and positional encoding

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

Practice: `examples/02_input_embeddings_and_positional_encoding.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Self-attention block

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

Practice: `examples/03_self_attention_block.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Multi-head attention

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

Practice: `examples/04_multi_head_attention.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Feed-forward network per position

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

Practice: `examples/05_feed_forward_network_per_position.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Residual connections and LayerNorm

### Aasaan Bhasha

Vector numbers ki list hai jiski ek direction aur lambai hoti hai. Dot product alignment naapta hai: same direction par bada positive, perpendicular par zero. Cosine similarity wahi dot product hai lambai hata kar — isliye wo alag-alag magnitude ke embeddings ko theek se compare karta hai.

### Chhota code

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 4.0, 6.0])

print('dot   ', a @ b)
print('norm  ', np.linalg.norm(a))
cos = (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))
print('cosine', cos)   # 1.0 -> same direction
```

**Yaad rakho:** Cosine similarity magnitude ignore karti hai; Euclidean distance nahi. Apne sawaal ke hisaab se chuno.

**Aam galti:** Raw embeddings ko Euclidean distance se compare karna jab sirf direction ka matlab hai.

Practice: `examples/06_residual_connections_and_layernorm.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Encoder stack

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

Practice: `examples/07_encoder_stack.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Decoder stack and causal masking

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

Practice: `examples/08_decoder_stack_and_causal_masking.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Parameter count breakdown

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

Practice: `examples/09_parameter_count_breakdown.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Drawing the block from memory

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

Practice: `examples/10_drawing_the_block_from_memory.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 125 ke baad aapko ye aana chahiye

- **The 2017 idea: attention is all you need** ko bina notes dekhe kisi dost ko samjha sakna.
- **Input embeddings and positional encoding** ko bina notes dekhe kisi dost ko samjha sakna.
- **Self-attention block** ko bina notes dekhe kisi dost ko samjha sakna.
- **Multi-head attention** ko bina notes dekhe kisi dost ko samjha sakna.
- **Feed-forward network per position** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
