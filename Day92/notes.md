# Day 92 — Sequence models: RNNs

Today's goal: work through **sequence models: rnns** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Sequential data and order |
| 2 | The recurrent cell and hidden state |
| 3 | Backpropagation through time |
| 4 | Vanishing gradients over long sequences |
| 5 | LSTM gates |
| 6 | GRU |
| 7 | Bidirectional RNNs |
| 8 | Sequence-to-sequence architecture |
| 9 | Padding, packing and masks |
| 10 | Why transformers replaced them |

---

## 1. Sequential data and order

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

## 2. The recurrent cell and hidden state

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

## 3. Backpropagation through time

Backpropagation is the chain rule applied backwards through the computation graph, reusing intermediate results so the cost is roughly one extra forward pass. Every framework does it for you — but writing it once by hand is what makes the failure modes readable.

```python
import numpy as np

# y = (w*x + b)^2 ; d y/d w by hand
x, w, b = 2.0, 3.0, 1.0
z = w * x + b        # forward
y = z ** 2

dy_dz = 2 * z        # backward
dz_dw = x
dz_db = 1.0
print('dy/dw', dy_dz * dz_dw)   # 28.0
print('dy/db', dy_dz * dz_db)   # 14.0

h = 1e-6
print('numeric dy/dw', (((w + h) * x + b) ** 2 - ((w - h) * x + b) ** 2) / (2 * h))
```

**Remember:** Gradient-check any hand-written backward pass against a numeric estimate before trusting it.

**Common mistake:** Forgetting to zero gradients between steps, so they accumulate and the model diverges.

## 4. Vanishing gradients over long sequences

The derivative answers: if I nudge this input a little, how much does the output move? The gradient is that answer for every input at once, so it points uphill. Training walks downhill by stepping against the gradient. The chain rule is what lets you propagate that answer through a stack of layers.

```python
import numpy as np

def f(x):
    return x ** 2 + 3 * x

def numeric_grad(fn, x, h=1e-6):
    return (fn(x + h) - fn(x - h)) / (2 * h)

x = 2.0
print('numeric  ', numeric_grad(f, x))
print('analytic ', 2 * x + 3)   # should match to ~1e-6
```

**Remember:** A central difference `(f(x+h)-f(x-h))/2h` is the cheapest way to check a hand-written gradient.

**Common mistake:** Trusting a derivation you never gradient-checked; a sign error trains slowly instead of failing loudly.

## 5. LSTM gates

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

## 6. GRU

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

## 7. Bidirectional RNNs

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

## 8. Sequence-to-sequence architecture

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

## 9. Padding, packing and masks

A convolution slides a small learned filter over the image, so the same edge detector works anywhere in the frame. That weight sharing is why a CNN needs far fewer parameters than a dense net. Pooling shrinks the map and adds a little translation tolerance.

```python
import numpy as np

image = np.array([
    [0, 0, 1, 1],
    [0, 0, 1, 1],
    [0, 0, 1, 1],
    [0, 0, 1, 1],
], dtype=float)
kernel = np.array([[-1, 1], [-1, 1]], dtype=float)   # vertical edge detector

h, w = image.shape[0] - 1, image.shape[1] - 1
out = np.zeros((h, w))
for i in range(h):
    for j in range(w):
        out[i, j] = float((image[i:i + 2, j:j + 2] * kernel).sum())
print(out)   # the edge column lights up
```

**Remember:** Output size = (in - kernel + 2*pad)/stride + 1. Print shapes when a layer refuses to connect.

**Common mistake:** Forgetting the channel dimension and feeding (H,W) where the layer expects (N,C,H,W).

## 10. Why transformers replaced them

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

## What you should be able to do after Day 92

- Explain **Sequential data and order** to someone else without notes.
- Explain **The recurrent cell and hidden state** to someone else without notes.
- Explain **Backpropagation through time** to someone else without notes.
- Explain **Vanishing gradients over long sequences** to someone else without notes.
- Explain **LSTM gates** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
