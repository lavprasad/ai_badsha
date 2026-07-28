# Day 188 — AI system architecture

Today's goal: work through **AI system architecture** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Components of a production AI system |
| 2 | Synchronous vs asynchronous flows |
| 3 | Queues and workers |
| 4 | Caching layers |
| 5 | Fallback and degradation paths |
| 6 | Multi-region considerations |
| 7 | Vendor lock-in and abstraction layers |
| 8 | Build vs buy per component |
| 9 | Cost architecture |
| 10 | Drawing your system on one page |

---

## 1. Components of a production AI system

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

Practice: open `examples/01_components_of_a_production_ai_system.py`, predict the output, change one line, predict again.

## 2. Synchronous vs asynchronous flows

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

Practice: open `examples/02_synchronous_vs_asynchronous_flows.py`, predict the output, change one line, predict again.

## 3. Queues and workers

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

Practice: open `examples/03_queues_and_workers.py`, predict the output, change one line, predict again.

## 4. Caching layers

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

Practice: open `examples/04_caching_layers.py`, predict the output, change one line, predict again.

## 5. Fallback and degradation paths

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

Practice: open `examples/05_fallback_and_degradation_paths.py`, predict the output, change one line, predict again.

## 6. Multi-region considerations

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

Practice: open `examples/06_multi_region_considerations.py`, predict the output, change one line, predict again.

## 7. Vendor lock-in and abstraction layers

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

Practice: open `examples/07_vendor_lock_in_and_abstraction_layers.py`, predict the output, change one line, predict again.

## 8. Build vs buy per component

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

Practice: open `examples/08_build_vs_buy_per_component.py`, predict the output, change one line, predict again.

## 9. Cost architecture

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

Practice: open `examples/09_cost_architecture.py`, predict the output, change one line, predict again.

## 10. Drawing your system on one page

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

Practice: open `examples/10_drawing_your_system_on_one_page.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 188

- Explain **Components of a production AI system** to someone else without notes.
- Explain **Synchronous vs asynchronous flows** to someone else without notes.
- Explain **Queues and workers** to someone else without notes.
- Explain **Caching layers** to someone else without notes.
- Explain **Fallback and degradation paths** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
