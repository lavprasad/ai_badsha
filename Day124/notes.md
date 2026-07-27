# Day 124 — Sequence models for NLP

Today's goal: work through **sequence models for nlp** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | RNNs for text |
| 2 | LSTM for sequence labelling |
| 3 | Bidirectional context |
| 4 | Sequence-to-sequence translation |
| 5 | Teacher forcing |
| 6 | Beam search decoding |
| 7 | The context bottleneck |
| 8 | Attention added to seq2seq |
| 9 | Why this architecture ended |
| 10 | What still carries over |

---

## 1. RNNs for text

An RNN carries a hidden state along the sequence, so order matters. Plain RNNs forget quickly because gradients vanish over long spans; LSTM and GRU add gates that let information flow unchanged across many steps. Transformers have largely replaced them, but the intuition about state and memory still matters.

```python
import numpy as np

def rnn_forward(xs, Wx, Wh, b):
    h = np.zeros(Wh.shape[0])
    states = []
    for x in xs:
        h = np.tanh(Wx @ x + Wh @ h + b)   # state carries forward
        states.append(h.copy())
    return np.array(states)

rng = np.random.default_rng(0)
xs = rng.normal(size=(5, 3))
states = rnn_forward(xs, rng.normal(size=(4, 3)) * 0.3, rng.normal(size=(4, 4)) * 0.3, np.zeros(4))
print('states shape', states.shape)
```

**Remember:** RNNs are inherently sequential — they cannot parallelise across time, which is why transformers won.

**Common mistake:** Feeding unsorted variable-length sequences without padding masks, so padding tokens pollute the state.

## 2. LSTM for sequence labelling

An RNN carries a hidden state along the sequence, so order matters. Plain RNNs forget quickly because gradients vanish over long spans; LSTM and GRU add gates that let information flow unchanged across many steps. Transformers have largely replaced them, but the intuition about state and memory still matters.

```python
import numpy as np

def rnn_forward(xs, Wx, Wh, b):
    h = np.zeros(Wh.shape[0])
    states = []
    for x in xs:
        h = np.tanh(Wx @ x + Wh @ h + b)   # state carries forward
        states.append(h.copy())
    return np.array(states)

rng = np.random.default_rng(0)
xs = rng.normal(size=(5, 3))
states = rnn_forward(xs, rng.normal(size=(4, 3)) * 0.3, rng.normal(size=(4, 4)) * 0.3, np.zeros(4))
print('states shape', states.shape)
```

**Remember:** RNNs are inherently sequential — they cannot parallelise across time, which is why transformers won.

**Common mistake:** Feeding unsorted variable-length sequences without padding masks, so padding tokens pollute the state.

## 3. Bidirectional context

An RNN carries a hidden state along the sequence, so order matters. Plain RNNs forget quickly because gradients vanish over long spans; LSTM and GRU add gates that let information flow unchanged across many steps. Transformers have largely replaced them, but the intuition about state and memory still matters.

```python
import numpy as np

def rnn_forward(xs, Wx, Wh, b):
    h = np.zeros(Wh.shape[0])
    states = []
    for x in xs:
        h = np.tanh(Wx @ x + Wh @ h + b)   # state carries forward
        states.append(h.copy())
    return np.array(states)

rng = np.random.default_rng(0)
xs = rng.normal(size=(5, 3))
states = rnn_forward(xs, rng.normal(size=(4, 3)) * 0.3, rng.normal(size=(4, 4)) * 0.3, np.zeros(4))
print('states shape', states.shape)
```

**Remember:** RNNs are inherently sequential — they cannot parallelise across time, which is why transformers won.

**Common mistake:** Feeding unsorted variable-length sequences without padding masks, so padding tokens pollute the state.

## 4. Sequence-to-sequence translation

An RNN carries a hidden state along the sequence, so order matters. Plain RNNs forget quickly because gradients vanish over long spans; LSTM and GRU add gates that let information flow unchanged across many steps. Transformers have largely replaced them, but the intuition about state and memory still matters.

```python
import numpy as np

def rnn_forward(xs, Wx, Wh, b):
    h = np.zeros(Wh.shape[0])
    states = []
    for x in xs:
        h = np.tanh(Wx @ x + Wh @ h + b)   # state carries forward
        states.append(h.copy())
    return np.array(states)

rng = np.random.default_rng(0)
xs = rng.normal(size=(5, 3))
states = rnn_forward(xs, rng.normal(size=(4, 3)) * 0.3, rng.normal(size=(4, 4)) * 0.3, np.zeros(4))
print('states shape', states.shape)
```

**Remember:** RNNs are inherently sequential — they cannot parallelise across time, which is why transformers won.

**Common mistake:** Feeding unsorted variable-length sequences without padding masks, so padding tokens pollute the state.

## 5. Teacher forcing

An RNN carries a hidden state along the sequence, so order matters. Plain RNNs forget quickly because gradients vanish over long spans; LSTM and GRU add gates that let information flow unchanged across many steps. Transformers have largely replaced them, but the intuition about state and memory still matters.

```python
import numpy as np

def rnn_forward(xs, Wx, Wh, b):
    h = np.zeros(Wh.shape[0])
    states = []
    for x in xs:
        h = np.tanh(Wx @ x + Wh @ h + b)   # state carries forward
        states.append(h.copy())
    return np.array(states)

rng = np.random.default_rng(0)
xs = rng.normal(size=(5, 3))
states = rnn_forward(xs, rng.normal(size=(4, 3)) * 0.3, rng.normal(size=(4, 4)) * 0.3, np.zeros(4))
print('states shape', states.shape)
```

**Remember:** RNNs are inherently sequential — they cannot parallelise across time, which is why transformers won.

**Common mistake:** Feeding unsorted variable-length sequences without padding masks, so padding tokens pollute the state.

## 6. Beam search decoding

An RNN carries a hidden state along the sequence, so order matters. Plain RNNs forget quickly because gradients vanish over long spans; LSTM and GRU add gates that let information flow unchanged across many steps. Transformers have largely replaced them, but the intuition about state and memory still matters.

```python
import numpy as np

def rnn_forward(xs, Wx, Wh, b):
    h = np.zeros(Wh.shape[0])
    states = []
    for x in xs:
        h = np.tanh(Wx @ x + Wh @ h + b)   # state carries forward
        states.append(h.copy())
    return np.array(states)

rng = np.random.default_rng(0)
xs = rng.normal(size=(5, 3))
states = rnn_forward(xs, rng.normal(size=(4, 3)) * 0.3, rng.normal(size=(4, 4)) * 0.3, np.zeros(4))
print('states shape', states.shape)
```

**Remember:** RNNs are inherently sequential — they cannot parallelise across time, which is why transformers won.

**Common mistake:** Feeding unsorted variable-length sequences without padding masks, so padding tokens pollute the state.

## 7. The context bottleneck

An RNN carries a hidden state along the sequence, so order matters. Plain RNNs forget quickly because gradients vanish over long spans; LSTM and GRU add gates that let information flow unchanged across many steps. Transformers have largely replaced them, but the intuition about state and memory still matters.

```python
import numpy as np

def rnn_forward(xs, Wx, Wh, b):
    h = np.zeros(Wh.shape[0])
    states = []
    for x in xs:
        h = np.tanh(Wx @ x + Wh @ h + b)   # state carries forward
        states.append(h.copy())
    return np.array(states)

rng = np.random.default_rng(0)
xs = rng.normal(size=(5, 3))
states = rnn_forward(xs, rng.normal(size=(4, 3)) * 0.3, rng.normal(size=(4, 4)) * 0.3, np.zeros(4))
print('states shape', states.shape)
```

**Remember:** RNNs are inherently sequential — they cannot parallelise across time, which is why transformers won.

**Common mistake:** Feeding unsorted variable-length sequences without padding masks, so padding tokens pollute the state.

## 8. Attention added to seq2seq

An RNN carries a hidden state along the sequence, so order matters. Plain RNNs forget quickly because gradients vanish over long spans; LSTM and GRU add gates that let information flow unchanged across many steps. Transformers have largely replaced them, but the intuition about state and memory still matters.

```python
import numpy as np

def rnn_forward(xs, Wx, Wh, b):
    h = np.zeros(Wh.shape[0])
    states = []
    for x in xs:
        h = np.tanh(Wx @ x + Wh @ h + b)   # state carries forward
        states.append(h.copy())
    return np.array(states)

rng = np.random.default_rng(0)
xs = rng.normal(size=(5, 3))
states = rnn_forward(xs, rng.normal(size=(4, 3)) * 0.3, rng.normal(size=(4, 4)) * 0.3, np.zeros(4))
print('states shape', states.shape)
```

**Remember:** RNNs are inherently sequential — they cannot parallelise across time, which is why transformers won.

**Common mistake:** Feeding unsorted variable-length sequences without padding masks, so padding tokens pollute the state.

## 9. Why this architecture ended

An RNN carries a hidden state along the sequence, so order matters. Plain RNNs forget quickly because gradients vanish over long spans; LSTM and GRU add gates that let information flow unchanged across many steps. Transformers have largely replaced them, but the intuition about state and memory still matters.

```python
import numpy as np

def rnn_forward(xs, Wx, Wh, b):
    h = np.zeros(Wh.shape[0])
    states = []
    for x in xs:
        h = np.tanh(Wx @ x + Wh @ h + b)   # state carries forward
        states.append(h.copy())
    return np.array(states)

rng = np.random.default_rng(0)
xs = rng.normal(size=(5, 3))
states = rnn_forward(xs, rng.normal(size=(4, 3)) * 0.3, rng.normal(size=(4, 4)) * 0.3, np.zeros(4))
print('states shape', states.shape)
```

**Remember:** RNNs are inherently sequential — they cannot parallelise across time, which is why transformers won.

**Common mistake:** Feeding unsorted variable-length sequences without padding masks, so padding tokens pollute the state.

## 10. What still carries over

An RNN carries a hidden state along the sequence, so order matters. Plain RNNs forget quickly because gradients vanish over long spans; LSTM and GRU add gates that let information flow unchanged across many steps. Transformers have largely replaced them, but the intuition about state and memory still matters.

```python
import numpy as np

def rnn_forward(xs, Wx, Wh, b):
    h = np.zeros(Wh.shape[0])
    states = []
    for x in xs:
        h = np.tanh(Wx @ x + Wh @ h + b)   # state carries forward
        states.append(h.copy())
    return np.array(states)

rng = np.random.default_rng(0)
xs = rng.normal(size=(5, 3))
states = rnn_forward(xs, rng.normal(size=(4, 3)) * 0.3, rng.normal(size=(4, 4)) * 0.3, np.zeros(4))
print('states shape', states.shape)
```

**Remember:** RNNs are inherently sequential — they cannot parallelise across time, which is why transformers won.

**Common mistake:** Feeding unsorted variable-length sequences without padding masks, so padding tokens pollute the state.

---

## What you should be able to do after Day 124

- Explain **RNNs for text** to someone else without notes.
- Explain **LSTM for sequence labelling** to someone else without notes.
- Explain **Bidirectional context** to someone else without notes.
- Explain **Sequence-to-sequence translation** to someone else without notes.
- Explain **Teacher forcing** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
