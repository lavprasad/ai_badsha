# Day 75 — Why deep learning

Today's goal: work through **Why deep learning** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Representation learning vs feature engineering |
| 2 | What deep nets buy you and what they cost |
| 3 | Where deep learning beats trees, and where it does not |
| 4 | The hardware and data that made it work |
| 5 | Universal approximation, honestly read |
| 6 | Depth vs width |
| 7 | Modern deep learning timeline |
| 8 | Frameworks: PyTorch, TensorFlow, JAX |
| 9 | The five-line training loop preview |
| 10 | Setting expectations for this phase |

---

## 1. Representation learning vs feature engineering

Feature engineering is where domain knowledge beats compute. A ratio, a lag, a time-since-last-event, or a count over a window often adds more than switching algorithms. Selection then removes features that add variance without signal.

```python
import pandas as pd

df = pd.DataFrame({
    'clicks': [10, 5, 0, 30],
    'impressions': [100, 200, 50, 300],
    'ts': pd.to_datetime(['2024-01-01', '2024-01-05', '2024-02-01', '2024-02-10']),
})
df['ctr'] = df['clicks'] / df['impressions'].clip(lower=1)   # ratio beats raw counts
df['days_since_prev'] = df['ts'].diff().dt.days.fillna(0)
df['is_weekend'] = df['ts'].dt.dayofweek.isin([5, 6]).astype(int)
print(df)
```

**Remember:** Every engineered feature must be computable at prediction time with data you will actually have.

**Common mistake:** Building a feature from a column that is only filled in AFTER the event you are predicting.

Practice: open `examples/01_representation_learning_vs_feature_engin.py`, predict the output, change one line, predict again.

## 2. What deep nets buy you and what they cost

Deep learning earns its cost when raw inputs have structure a human cannot hand-engineer: pixels, audio, text. On a 50-column business table, gradient boosting usually wins with a fraction of the effort. Universal approximation says a big enough net *can* represent the function — it says nothing about whether your data and optimiser will find it.

```python
CHOOSE = {
    'tabular, <100k rows':      'gradient boosting — almost always',
    'tabular, huge + embeddings': 'deep nets can win, measure both',
    'images / audio / video':   'deep nets, pretrained backbone',
    'text understanding':       'transformer, pretrained',
    'strict interpretability':  'linear or a small tree',
    'tiny data (<1000 rows)':   'simple model + strong regularization',
}
for k, v in CHOOSE.items():
    print(f'{k:<28} -> {v}')
```

**Remember:** Capacity is not the bottleneck in most projects — data quality and framing are.

**Common mistake:** Reaching for a neural network on 3,000 tabular rows and losing to a random forest built in one line.

Practice: open `examples/02_what_deep_nets_buy_you_and_what_they_cos.py`, predict the output, change one line, predict again.

## 3. Where deep learning beats trees, and where it does not

Deep learning earns its cost when raw inputs have structure a human cannot hand-engineer: pixels, audio, text. On a 50-column business table, gradient boosting usually wins with a fraction of the effort. Universal approximation says a big enough net *can* represent the function — it says nothing about whether your data and optimiser will find it.

```python
CHOOSE = {
    'tabular, <100k rows':      'gradient boosting — almost always',
    'tabular, huge + embeddings': 'deep nets can win, measure both',
    'images / audio / video':   'deep nets, pretrained backbone',
    'text understanding':       'transformer, pretrained',
    'strict interpretability':  'linear or a small tree',
    'tiny data (<1000 rows)':   'simple model + strong regularization',
}
for k, v in CHOOSE.items():
    print(f'{k:<28} -> {v}')
```

**Remember:** Capacity is not the bottleneck in most projects — data quality and framing are.

**Common mistake:** Reaching for a neural network on 3,000 tabular rows and losing to a random forest built in one line.

Practice: open `examples/03_where_deep_learning_beats_trees_and_wher.py`, predict the output, change one line, predict again.

## 4. The hardware and data that made it work

Deep learning earns its cost when raw inputs have structure a human cannot hand-engineer: pixels, audio, text. On a 50-column business table, gradient boosting usually wins with a fraction of the effort. Universal approximation says a big enough net *can* represent the function — it says nothing about whether your data and optimiser will find it.

```python
CHOOSE = {
    'tabular, <100k rows':      'gradient boosting — almost always',
    'tabular, huge + embeddings': 'deep nets can win, measure both',
    'images / audio / video':   'deep nets, pretrained backbone',
    'text understanding':       'transformer, pretrained',
    'strict interpretability':  'linear or a small tree',
    'tiny data (<1000 rows)':   'simple model + strong regularization',
}
for k, v in CHOOSE.items():
    print(f'{k:<28} -> {v}')
```

**Remember:** Capacity is not the bottleneck in most projects — data quality and framing are.

**Common mistake:** Reaching for a neural network on 3,000 tabular rows and losing to a random forest built in one line.

Practice: open `examples/04_the_hardware_and_data_that_made_it_work.py`, predict the output, change one line, predict again.

## 5. Universal approximation, honestly read

Deep learning earns its cost when raw inputs have structure a human cannot hand-engineer: pixels, audio, text. On a 50-column business table, gradient boosting usually wins with a fraction of the effort. Universal approximation says a big enough net *can* represent the function — it says nothing about whether your data and optimiser will find it.

```python
CHOOSE = {
    'tabular, <100k rows':      'gradient boosting — almost always',
    'tabular, huge + embeddings': 'deep nets can win, measure both',
    'images / audio / video':   'deep nets, pretrained backbone',
    'text understanding':       'transformer, pretrained',
    'strict interpretability':  'linear or a small tree',
    'tiny data (<1000 rows)':   'simple model + strong regularization',
}
for k, v in CHOOSE.items():
    print(f'{k:<28} -> {v}')
```

**Remember:** Capacity is not the bottleneck in most projects — data quality and framing are.

**Common mistake:** Reaching for a neural network on 3,000 tabular rows and losing to a random forest built in one line.

Practice: open `examples/05_universal_approximation_honestly_read.py`, predict the output, change one line, predict again.

## 6. Depth vs width

Deep learning earns its cost when raw inputs have structure a human cannot hand-engineer: pixels, audio, text. On a 50-column business table, gradient boosting usually wins with a fraction of the effort. Universal approximation says a big enough net *can* represent the function — it says nothing about whether your data and optimiser will find it.

```python
CHOOSE = {
    'tabular, <100k rows':      'gradient boosting — almost always',
    'tabular, huge + embeddings': 'deep nets can win, measure both',
    'images / audio / video':   'deep nets, pretrained backbone',
    'text understanding':       'transformer, pretrained',
    'strict interpretability':  'linear or a small tree',
    'tiny data (<1000 rows)':   'simple model + strong regularization',
}
for k, v in CHOOSE.items():
    print(f'{k:<28} -> {v}')
```

**Remember:** Capacity is not the bottleneck in most projects — data quality and framing are.

**Common mistake:** Reaching for a neural network on 3,000 tabular rows and losing to a random forest built in one line.

Practice: open `examples/06_depth_vs_width.py`, predict the output, change one line, predict again.

## 7. Modern deep learning timeline

Deep learning earns its cost when raw inputs have structure a human cannot hand-engineer: pixels, audio, text. On a 50-column business table, gradient boosting usually wins with a fraction of the effort. Universal approximation says a big enough net *can* represent the function — it says nothing about whether your data and optimiser will find it.

```python
CHOOSE = {
    'tabular, <100k rows':      'gradient boosting — almost always',
    'tabular, huge + embeddings': 'deep nets can win, measure both',
    'images / audio / video':   'deep nets, pretrained backbone',
    'text understanding':       'transformer, pretrained',
    'strict interpretability':  'linear or a small tree',
    'tiny data (<1000 rows)':   'simple model + strong regularization',
}
for k, v in CHOOSE.items():
    print(f'{k:<28} -> {v}')
```

**Remember:** Capacity is not the bottleneck in most projects — data quality and framing are.

**Common mistake:** Reaching for a neural network on 3,000 tabular rows and losing to a random forest built in one line.

Practice: open `examples/07_modern_deep_learning_timeline.py`, predict the output, change one line, predict again.

## 8. Frameworks: PyTorch, TensorFlow, JAX

PyTorch is NumPy with gradients and a GPU. The training loop is always the same five lines: zero grads, forward, loss, backward, step. Write it out by hand once — every framework wrapper is just hiding these five.

```python
# Requires: pip install torch  (does not run inside the browser sandbox)
import torch
import torch.nn as nn

model = nn.Sequential(nn.Linear(4, 16), nn.ReLU(), nn.Linear(16, 1))
opt = torch.optim.AdamW(model.parameters(), lr=1e-3)
loss_fn = nn.MSELoss()

X = torch.randn(64, 4)
y = torch.randn(64, 1)
for step in range(50):
    opt.zero_grad()                # 1. clear old gradients
    pred = model(X)                # 2. forward
    loss = loss_fn(pred, y)        # 3. loss
    loss.backward()                # 4. backward
    opt.step()                     # 5. update
print('final loss', round(loss.item(), 4))
```

**Remember:** `opt.zero_grad()` first, every step. PyTorch accumulates gradients by design.

**Common mistake:** Calling `loss.backward()` twice without `retain_graph` and getting a confusing runtime error.

Practice: open `examples/08_frameworks_pytorch_tensorflow_jax.py`, predict the output, change one line, predict again.

## 9. The five-line training loop preview

PyTorch is NumPy with gradients and a GPU. The training loop is always the same five lines: zero grads, forward, loss, backward, step. Write it out by hand once — every framework wrapper is just hiding these five.

```python
# Requires: pip install torch  (does not run inside the browser sandbox)
import torch
import torch.nn as nn

model = nn.Sequential(nn.Linear(4, 16), nn.ReLU(), nn.Linear(16, 1))
opt = torch.optim.AdamW(model.parameters(), lr=1e-3)
loss_fn = nn.MSELoss()

X = torch.randn(64, 4)
y = torch.randn(64, 1)
for step in range(50):
    opt.zero_grad()                # 1. clear old gradients
    pred = model(X)                # 2. forward
    loss = loss_fn(pred, y)        # 3. loss
    loss.backward()                # 4. backward
    opt.step()                     # 5. update
print('final loss', round(loss.item(), 4))
```

**Remember:** `opt.zero_grad()` first, every step. PyTorch accumulates gradients by design.

**Common mistake:** Calling `loss.backward()` twice without `retain_graph` and getting a confusing runtime error.

Practice: open `examples/09_the_five_line_training_loop_preview.py`, predict the output, change one line, predict again.

## 10. Setting expectations for this phase

Deep learning earns its cost when raw inputs have structure a human cannot hand-engineer: pixels, audio, text. On a 50-column business table, gradient boosting usually wins with a fraction of the effort. Universal approximation says a big enough net *can* represent the function — it says nothing about whether your data and optimiser will find it.

```python
CHOOSE = {
    'tabular, <100k rows':      'gradient boosting — almost always',
    'tabular, huge + embeddings': 'deep nets can win, measure both',
    'images / audio / video':   'deep nets, pretrained backbone',
    'text understanding':       'transformer, pretrained',
    'strict interpretability':  'linear or a small tree',
    'tiny data (<1000 rows)':   'simple model + strong regularization',
}
for k, v in CHOOSE.items():
    print(f'{k:<28} -> {v}')
```

**Remember:** Capacity is not the bottleneck in most projects — data quality and framing are.

**Common mistake:** Reaching for a neural network on 3,000 tabular rows and losing to a random forest built in one line.

Practice: open `examples/10_setting_expectations_for_this_phase.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 75

- Explain **Representation learning vs feature engineering** to someone else without notes.
- Explain **What deep nets buy you and what they cost** to someone else without notes.
- Explain **Where deep learning beats trees, and where it does not** to someone else without notes.
- Explain **The hardware and data that made it work** to someone else without notes.
- Explain **Universal approximation, honestly read** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
