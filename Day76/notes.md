# Day 76 — The artificial neuron

Today's goal: work through **the artificial neuron** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Inputs, weights, bias |
| 2 | The weighted sum |
| 3 | Activation functions |
| 4 | The perceptron and its limits |
| 5 | XOR and why one layer is not enough |
| 6 | Layers and forward propagation |
| 7 | Matrix form of a layer |
| 8 | Batch dimension |
| 9 | Counting parameters |
| 10 | A forward pass in pure NumPy |

---

## 1. Inputs, weights, bias

A neuron computes `activation(w·x + b)`. Stack them in layers and you can approximate any continuous function. Without the non-linear activation, ten stacked layers collapse algebraically into one linear layer — the non-linearity is the whole point.

```python
import numpy as np

def relu(z):
    return np.maximum(0, z)

rng = np.random.default_rng(0)
x = rng.normal(size=(1, 4))
W1, b1 = rng.normal(size=(4, 8)) * 0.5, np.zeros(8)
W2, b2 = rng.normal(size=(8, 1)) * 0.5, np.zeros(1)

h = relu(x @ W1 + b1)
out = h @ W2 + b2
print('hidden', h.round(3))
print('output', out.round(3))
```

**Remember:** Depth without non-linearity is width. Check that every hidden layer has an activation.

**Common mistake:** Initialising all weights to zero, so every neuron gets the same gradient and learns the same thing.

## 2. The weighted sum

A neuron computes `activation(w·x + b)`. Stack them in layers and you can approximate any continuous function. Without the non-linear activation, ten stacked layers collapse algebraically into one linear layer — the non-linearity is the whole point.

```python
import numpy as np

def relu(z):
    return np.maximum(0, z)

rng = np.random.default_rng(0)
x = rng.normal(size=(1, 4))
W1, b1 = rng.normal(size=(4, 8)) * 0.5, np.zeros(8)
W2, b2 = rng.normal(size=(8, 1)) * 0.5, np.zeros(1)

h = relu(x @ W1 + b1)
out = h @ W2 + b2
print('hidden', h.round(3))
print('output', out.round(3))
```

**Remember:** Depth without non-linearity is width. Check that every hidden layer has an activation.

**Common mistake:** Initialising all weights to zero, so every neuron gets the same gradient and learns the same thing.

## 3. Activation functions

A neuron computes `activation(w·x + b)`. Stack them in layers and you can approximate any continuous function. Without the non-linear activation, ten stacked layers collapse algebraically into one linear layer — the non-linearity is the whole point.

```python
import numpy as np

def relu(z):
    return np.maximum(0, z)

rng = np.random.default_rng(0)
x = rng.normal(size=(1, 4))
W1, b1 = rng.normal(size=(4, 8)) * 0.5, np.zeros(8)
W2, b2 = rng.normal(size=(8, 1)) * 0.5, np.zeros(1)

h = relu(x @ W1 + b1)
out = h @ W2 + b2
print('hidden', h.round(3))
print('output', out.round(3))
```

**Remember:** Depth without non-linearity is width. Check that every hidden layer has an activation.

**Common mistake:** Initialising all weights to zero, so every neuron gets the same gradient and learns the same thing.

## 4. The perceptron and its limits

A neuron computes `activation(w·x + b)`. Stack them in layers and you can approximate any continuous function. Without the non-linear activation, ten stacked layers collapse algebraically into one linear layer — the non-linearity is the whole point.

```python
import numpy as np

def relu(z):
    return np.maximum(0, z)

rng = np.random.default_rng(0)
x = rng.normal(size=(1, 4))
W1, b1 = rng.normal(size=(4, 8)) * 0.5, np.zeros(8)
W2, b2 = rng.normal(size=(8, 1)) * 0.5, np.zeros(1)

h = relu(x @ W1 + b1)
out = h @ W2 + b2
print('hidden', h.round(3))
print('output', out.round(3))
```

**Remember:** Depth without non-linearity is width. Check that every hidden layer has an activation.

**Common mistake:** Initialising all weights to zero, so every neuron gets the same gradient and learns the same thing.

## 5. XOR and why one layer is not enough

A neuron computes `activation(w·x + b)`. Stack them in layers and you can approximate any continuous function. Without the non-linear activation, ten stacked layers collapse algebraically into one linear layer — the non-linearity is the whole point.

```python
import numpy as np

def relu(z):
    return np.maximum(0, z)

rng = np.random.default_rng(0)
x = rng.normal(size=(1, 4))
W1, b1 = rng.normal(size=(4, 8)) * 0.5, np.zeros(8)
W2, b2 = rng.normal(size=(8, 1)) * 0.5, np.zeros(1)

h = relu(x @ W1 + b1)
out = h @ W2 + b2
print('hidden', h.round(3))
print('output', out.round(3))
```

**Remember:** Depth without non-linearity is width. Check that every hidden layer has an activation.

**Common mistake:** Initialising all weights to zero, so every neuron gets the same gradient and learns the same thing.

## 6. Layers and forward propagation

A neuron computes `activation(w·x + b)`. Stack them in layers and you can approximate any continuous function. Without the non-linear activation, ten stacked layers collapse algebraically into one linear layer — the non-linearity is the whole point.

```python
import numpy as np

def relu(z):
    return np.maximum(0, z)

rng = np.random.default_rng(0)
x = rng.normal(size=(1, 4))
W1, b1 = rng.normal(size=(4, 8)) * 0.5, np.zeros(8)
W2, b2 = rng.normal(size=(8, 1)) * 0.5, np.zeros(1)

h = relu(x @ W1 + b1)
out = h @ W2 + b2
print('hidden', h.round(3))
print('output', out.round(3))
```

**Remember:** Depth without non-linearity is width. Check that every hidden layer has an activation.

**Common mistake:** Initialising all weights to zero, so every neuron gets the same gradient and learns the same thing.

## 7. Matrix form of a layer

A matrix is a linear transformation. Multiplying matrices composes transformations, which is exactly what stacking neural network layers does. Shapes must line up: (m,k) @ (k,n) -> (m,n); the inner dimensions must match and they vanish.

```python
import numpy as np

A = np.random.default_rng(0).normal(size=(3, 4))
B = np.random.default_rng(1).normal(size=(4, 2))

print((A @ B).shape)      # (3, 2)
print(A.T.shape)          # (4, 3)
print(np.eye(3) @ A is not A, np.allclose(np.eye(3) @ A, A))
```

**Remember:** Read every shape error as 'the inner dimensions did not match' and print the shapes.

**Common mistake:** Reaching for `np.linalg.inv` to solve `Ax=b` instead of the numerically safer `np.linalg.solve`.

## 8. Batch dimension

A neuron computes `activation(w·x + b)`. Stack them in layers and you can approximate any continuous function. Without the non-linear activation, ten stacked layers collapse algebraically into one linear layer — the non-linearity is the whole point.

```python
import numpy as np

def relu(z):
    return np.maximum(0, z)

rng = np.random.default_rng(0)
x = rng.normal(size=(1, 4))
W1, b1 = rng.normal(size=(4, 8)) * 0.5, np.zeros(8)
W2, b2 = rng.normal(size=(8, 1)) * 0.5, np.zeros(1)

h = relu(x @ W1 + b1)
out = h @ W2 + b2
print('hidden', h.round(3))
print('output', out.round(3))
```

**Remember:** Depth without non-linearity is width. Check that every hidden layer has an activation.

**Common mistake:** Initialising all weights to zero, so every neuron gets the same gradient and learns the same thing.

## 9. Counting parameters

A neuron computes `activation(w·x + b)`. Stack them in layers and you can approximate any continuous function. Without the non-linear activation, ten stacked layers collapse algebraically into one linear layer — the non-linearity is the whole point.

```python
import numpy as np

def relu(z):
    return np.maximum(0, z)

rng = np.random.default_rng(0)
x = rng.normal(size=(1, 4))
W1, b1 = rng.normal(size=(4, 8)) * 0.5, np.zeros(8)
W2, b2 = rng.normal(size=(8, 1)) * 0.5, np.zeros(1)

h = relu(x @ W1 + b1)
out = h @ W2 + b2
print('hidden', h.round(3))
print('output', out.round(3))
```

**Remember:** Depth without non-linearity is width. Check that every hidden layer has an activation.

**Common mistake:** Initialising all weights to zero, so every neuron gets the same gradient and learns the same thing.

## 10. A forward pass in pure NumPy

A neuron computes `activation(w·x + b)`. Stack them in layers and you can approximate any continuous function. Without the non-linear activation, ten stacked layers collapse algebraically into one linear layer — the non-linearity is the whole point.

```python
import numpy as np

def relu(z):
    return np.maximum(0, z)

rng = np.random.default_rng(0)
x = rng.normal(size=(1, 4))
W1, b1 = rng.normal(size=(4, 8)) * 0.5, np.zeros(8)
W2, b2 = rng.normal(size=(8, 1)) * 0.5, np.zeros(1)

h = relu(x @ W1 + b1)
out = h @ W2 + b2
print('hidden', h.round(3))
print('output', out.round(3))
```

**Remember:** Depth without non-linearity is width. Check that every hidden layer has an activation.

**Common mistake:** Initialising all weights to zero, so every neuron gets the same gradient and learns the same thing.

---

## What you should be able to do after Day 76

- Explain **Inputs, weights, bias** to someone else without notes.
- Explain **The weighted sum** to someone else without notes.
- Explain **Activation functions** to someone else without notes.
- Explain **The perceptron and its limits** to someone else without notes.
- Explain **XOR and why one layer is not enough** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
