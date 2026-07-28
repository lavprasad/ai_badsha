# Day 20 — Optimisation theory

Today's goal: work through **Optimisation theory** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Objective functions and minima |
| 2 | Convex vs non-convex landscapes |
| 3 | Local minima, saddle points, plateaus |
| 4 | Gradient descent in one dimension |
| 5 | The learning rate trade-off |
| 6 | Momentum intuition |
| 7 | Newton's method and why we rarely use it |
| 8 | Constrained optimisation and Lagrange multipliers |
| 9 | Stopping criteria |
| 10 | Implementing descent from scratch |

---

## 1. Objective functions and minima

A convex loss has one bottom, so any downhill path finds it. Neural network losses are not convex — they have valleys, plateaus and saddle points. In high dimensions saddles are far more common than true local minima, which is why momentum-based optimisers help so much.

```python
import numpy as np

def loss(w):
    return (w - 3) ** 2 + 1        # convex bowl, minimum at w=3

w, lr = 0.0, 0.1
for step in range(30):
    grad = 2 * (w - 3)
    w -= lr * grad
print(f'converged to w={w:.4f}, loss={loss(w):.4f}')
```

**Remember:** If the loss oscillates or explodes, halve the learning rate before changing anything else.

**Common mistake:** Blaming the model architecture for what is really a learning rate ten times too large.

Practice: open `examples/01_objective_functions_and_minima.py`, predict the output, change one line, predict again.

## 2. Convex vs non-convex landscapes

A convex loss has one bottom, so any downhill path finds it. Neural network losses are not convex — they have valleys, plateaus and saddle points. In high dimensions saddles are far more common than true local minima, which is why momentum-based optimisers help so much.

```python
import numpy as np

def loss(w):
    return (w - 3) ** 2 + 1        # convex bowl, minimum at w=3

w, lr = 0.0, 0.1
for step in range(30):
    grad = 2 * (w - 3)
    w -= lr * grad
print(f'converged to w={w:.4f}, loss={loss(w):.4f}')
```

**Remember:** If the loss oscillates or explodes, halve the learning rate before changing anything else.

**Common mistake:** Blaming the model architecture for what is really a learning rate ten times too large.

Practice: open `examples/02_convex_vs_non_convex_landscapes.py`, predict the output, change one line, predict again.

## 3. Local minima, saddle points, plateaus

A convex loss has one bottom, so any downhill path finds it. Neural network losses are not convex — they have valleys, plateaus and saddle points. In high dimensions saddles are far more common than true local minima, which is why momentum-based optimisers help so much.

```python
import numpy as np

def loss(w):
    return (w - 3) ** 2 + 1        # convex bowl, minimum at w=3

w, lr = 0.0, 0.1
for step in range(30):
    grad = 2 * (w - 3)
    w -= lr * grad
print(f'converged to w={w:.4f}, loss={loss(w):.4f}')
```

**Remember:** If the loss oscillates or explodes, halve the learning rate before changing anything else.

**Common mistake:** Blaming the model architecture for what is really a learning rate ten times too large.

Practice: open `examples/03_local_minima_saddle_points_plateaus.py`, predict the output, change one line, predict again.

## 4. Gradient descent in one dimension

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

Practice: open `examples/04_gradient_descent_in_one_dimension.py`, predict the output, change one line, predict again.

## 5. The learning rate trade-off

A convex loss has one bottom, so any downhill path finds it. Neural network losses are not convex — they have valleys, plateaus and saddle points. In high dimensions saddles are far more common than true local minima, which is why momentum-based optimisers help so much.

```python
import numpy as np

def loss(w):
    return (w - 3) ** 2 + 1        # convex bowl, minimum at w=3

w, lr = 0.0, 0.1
for step in range(30):
    grad = 2 * (w - 3)
    w -= lr * grad
print(f'converged to w={w:.4f}, loss={loss(w):.4f}')
```

**Remember:** If the loss oscillates or explodes, halve the learning rate before changing anything else.

**Common mistake:** Blaming the model architecture for what is really a learning rate ten times too large.

Practice: open `examples/05_the_learning_rate_trade_off.py`, predict the output, change one line, predict again.

## 6. Momentum intuition

A convex loss has one bottom, so any downhill path finds it. Neural network losses are not convex — they have valleys, plateaus and saddle points. In high dimensions saddles are far more common than true local minima, which is why momentum-based optimisers help so much.

```python
import numpy as np

def loss(w):
    return (w - 3) ** 2 + 1        # convex bowl, minimum at w=3

w, lr = 0.0, 0.1
for step in range(30):
    grad = 2 * (w - 3)
    w -= lr * grad
print(f'converged to w={w:.4f}, loss={loss(w):.4f}')
```

**Remember:** If the loss oscillates or explodes, halve the learning rate before changing anything else.

**Common mistake:** Blaming the model architecture for what is really a learning rate ten times too large.

Practice: open `examples/06_momentum_intuition.py`, predict the output, change one line, predict again.

## 7. Newton's method and why we rarely use it

A convex loss has one bottom, so any downhill path finds it. Neural network losses are not convex — they have valleys, plateaus and saddle points. In high dimensions saddles are far more common than true local minima, which is why momentum-based optimisers help so much.

```python
import numpy as np

def loss(w):
    return (w - 3) ** 2 + 1        # convex bowl, minimum at w=3

w, lr = 0.0, 0.1
for step in range(30):
    grad = 2 * (w - 3)
    w -= lr * grad
print(f'converged to w={w:.4f}, loss={loss(w):.4f}')
```

**Remember:** If the loss oscillates or explodes, halve the learning rate before changing anything else.

**Common mistake:** Blaming the model architecture for what is really a learning rate ten times too large.

Practice: open `examples/07_newton_s_method_and_why_we_rarely_use_it.py`, predict the output, change one line, predict again.

## 8. Constrained optimisation and Lagrange multipliers

A convex loss has one bottom, so any downhill path finds it. Neural network losses are not convex — they have valleys, plateaus and saddle points. In high dimensions saddles are far more common than true local minima, which is why momentum-based optimisers help so much.

```python
import numpy as np

def loss(w):
    return (w - 3) ** 2 + 1        # convex bowl, minimum at w=3

w, lr = 0.0, 0.1
for step in range(30):
    grad = 2 * (w - 3)
    w -= lr * grad
print(f'converged to w={w:.4f}, loss={loss(w):.4f}')
```

**Remember:** If the loss oscillates or explodes, halve the learning rate before changing anything else.

**Common mistake:** Blaming the model architecture for what is really a learning rate ten times too large.

Practice: open `examples/08_constrained_optimisation_and_lagrange_mu.py`, predict the output, change one line, predict again.

## 9. Stopping criteria

A convex loss has one bottom, so any downhill path finds it. Neural network losses are not convex — they have valleys, plateaus and saddle points. In high dimensions saddles are far more common than true local minima, which is why momentum-based optimisers help so much.

```python
import numpy as np

def loss(w):
    return (w - 3) ** 2 + 1        # convex bowl, minimum at w=3

w, lr = 0.0, 0.1
for step in range(30):
    grad = 2 * (w - 3)
    w -= lr * grad
print(f'converged to w={w:.4f}, loss={loss(w):.4f}')
```

**Remember:** If the loss oscillates or explodes, halve the learning rate before changing anything else.

**Common mistake:** Blaming the model architecture for what is really a learning rate ten times too large.

Practice: open `examples/09_stopping_criteria.py`, predict the output, change one line, predict again.

## 10. Implementing descent from scratch

A convex loss has one bottom, so any downhill path finds it. Neural network losses are not convex — they have valleys, plateaus and saddle points. In high dimensions saddles are far more common than true local minima, which is why momentum-based optimisers help so much.

```python
import numpy as np

def loss(w):
    return (w - 3) ** 2 + 1        # convex bowl, minimum at w=3

w, lr = 0.0, 0.1
for step in range(30):
    grad = 2 * (w - 3)
    w -= lr * grad
print(f'converged to w={w:.4f}, loss={loss(w):.4f}')
```

**Remember:** If the loss oscillates or explodes, halve the learning rate before changing anything else.

**Common mistake:** Blaming the model architecture for what is really a learning rate ten times too large.

Practice: open `examples/10_implementing_descent_from_scratch.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 20

- Explain **Objective functions and minima** to someone else without notes.
- Explain **Convex vs non-convex landscapes** to someone else without notes.
- Explain **Local minima, saddle points, plateaus** to someone else without notes.
- Explain **Gradient descent in one dimension** to someone else without notes.
- Explain **The learning rate trade-off** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
