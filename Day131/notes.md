# Day 131 — Post-training: SFT and alignment

Today's goal: work through **Post-training: SFT and alignment** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Base models do not follow instructions |
| 2 | Supervised fine-tuning data format |
| 3 | Masking the loss to the response only |
| 4 | Data quality over quantity |
| 5 | Reward models |
| 6 | RLHF with PPO |
| 7 | Direct preference optimisation |
| 8 | Constitutional and rule-based methods |
| 9 | Sycophancy and reward hacking |
| 10 | Evaluating alignment |

---

## 1. Base models do not follow instructions

Fine-tuning continues training a pretrained model on your examples. It teaches format, tone and task shape far better than it teaches new facts — for facts, use retrieval. A few hundred excellent examples usually beat ten thousand mediocre ones.

```python
# Typical SFT record: the model learns the assistant turn only.
example = {
    'messages': [
        {'role': 'system', 'content': 'You extract invoice fields as JSON.'},
        {'role': 'user', 'content': 'Invoice 4471, dated 2024-03-02, total Rs 15,300.'},
        {'role': 'assistant', 'content': '{"id": "4471", "date": "2024-03-02", "total": 15300}'},
    ]
}
import json
print(json.dumps(example, indent=2))
print('\\nRule: mask the loss on system+user tokens; train only on the assistant response.')
```

**Remember:** Fine-tune for behaviour and format. Use RAG for knowledge that changes.

**Common mistake:** Fine-tuning to inject company facts, then re-training every time a policy document changes.

## 2. Supervised fine-tuning data format

Hyperparameters are the settings you choose, not learn. Grid search is exhaustive and wasteful; random search finds good regions faster in high dimensions; Bayesian search learns from previous trials. Always search inside cross-validation.

```python
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
import numpy as np

X, y = load_breast_cancer(return_X_y=True)
space = {
    'n_estimators': [100, 300, 600],
    'max_depth': [None, 4, 8, 16],
    'min_samples_leaf': [1, 2, 4, 8],
}
search = RandomizedSearchCV(
    RandomForestClassifier(random_state=0, n_jobs=-1),
    space, n_iter=12, cv=5, random_state=0,
).fit(X, y)
print(search.best_params_, round(search.best_score_, 4))
```

**Remember:** Fix the random seed and log every trial, or you cannot reproduce your own best model.

**Common mistake:** Tuning 40 hyperparameters on 400 rows — you are now fitting the validation set.

## 3. Masking the loss to the response only

Fine-tuning continues training a pretrained model on your examples. It teaches format, tone and task shape far better than it teaches new facts — for facts, use retrieval. A few hundred excellent examples usually beat ten thousand mediocre ones.

```python
# Typical SFT record: the model learns the assistant turn only.
example = {
    'messages': [
        {'role': 'system', 'content': 'You extract invoice fields as JSON.'},
        {'role': 'user', 'content': 'Invoice 4471, dated 2024-03-02, total Rs 15,300.'},
        {'role': 'assistant', 'content': '{"id": "4471", "date": "2024-03-02", "total": 15300}'},
    ]
}
import json
print(json.dumps(example, indent=2))
print('\\nRule: mask the loss on system+user tokens; train only on the assistant response.')
```

**Remember:** Fine-tune for behaviour and format. Use RAG for knowledge that changes.

**Common mistake:** Fine-tuning to inject company facts, then re-training every time a policy document changes.

## 4. Data quality over quantity

Fine-tuning continues training a pretrained model on your examples. It teaches format, tone and task shape far better than it teaches new facts — for facts, use retrieval. A few hundred excellent examples usually beat ten thousand mediocre ones.

```python
# Typical SFT record: the model learns the assistant turn only.
example = {
    'messages': [
        {'role': 'system', 'content': 'You extract invoice fields as JSON.'},
        {'role': 'user', 'content': 'Invoice 4471, dated 2024-03-02, total Rs 15,300.'},
        {'role': 'assistant', 'content': '{"id": "4471", "date": "2024-03-02", "total": 15300}'},
    ]
}
import json
print(json.dumps(example, indent=2))
print('\\nRule: mask the loss on system+user tokens; train only on the assistant response.')
```

**Remember:** Fine-tune for behaviour and format. Use RAG for knowledge that changes.

**Common mistake:** Fine-tuning to inject company facts, then re-training every time a policy document changes.

## 5. Reward models

Fine-tuning continues training a pretrained model on your examples. It teaches format, tone and task shape far better than it teaches new facts — for facts, use retrieval. A few hundred excellent examples usually beat ten thousand mediocre ones.

```python
# Typical SFT record: the model learns the assistant turn only.
example = {
    'messages': [
        {'role': 'system', 'content': 'You extract invoice fields as JSON.'},
        {'role': 'user', 'content': 'Invoice 4471, dated 2024-03-02, total Rs 15,300.'},
        {'role': 'assistant', 'content': '{"id": "4471", "date": "2024-03-02", "total": 15300}'},
    ]
}
import json
print(json.dumps(example, indent=2))
print('\\nRule: mask the loss on system+user tokens; train only on the assistant response.')
```

**Remember:** Fine-tune for behaviour and format. Use RAG for knowledge that changes.

**Common mistake:** Fine-tuning to inject company facts, then re-training every time a policy document changes.

## 6. RLHF with PPO

Fine-tuning continues training a pretrained model on your examples. It teaches format, tone and task shape far better than it teaches new facts — for facts, use retrieval. A few hundred excellent examples usually beat ten thousand mediocre ones.

```python
# Typical SFT record: the model learns the assistant turn only.
example = {
    'messages': [
        {'role': 'system', 'content': 'You extract invoice fields as JSON.'},
        {'role': 'user', 'content': 'Invoice 4471, dated 2024-03-02, total Rs 15,300.'},
        {'role': 'assistant', 'content': '{"id": "4471", "date": "2024-03-02", "total": 15300}'},
    ]
}
import json
print(json.dumps(example, indent=2))
print('\\nRule: mask the loss on system+user tokens; train only on the assistant response.')
```

**Remember:** Fine-tune for behaviour and format. Use RAG for knowledge that changes.

**Common mistake:** Fine-tuning to inject company facts, then re-training every time a policy document changes.

## 7. Direct preference optimisation

Fine-tuning continues training a pretrained model on your examples. It teaches format, tone and task shape far better than it teaches new facts — for facts, use retrieval. A few hundred excellent examples usually beat ten thousand mediocre ones.

```python
# Typical SFT record: the model learns the assistant turn only.
example = {
    'messages': [
        {'role': 'system', 'content': 'You extract invoice fields as JSON.'},
        {'role': 'user', 'content': 'Invoice 4471, dated 2024-03-02, total Rs 15,300.'},
        {'role': 'assistant', 'content': '{"id": "4471", "date": "2024-03-02", "total": 15300}'},
    ]
}
import json
print(json.dumps(example, indent=2))
print('\\nRule: mask the loss on system+user tokens; train only on the assistant response.')
```

**Remember:** Fine-tune for behaviour and format. Use RAG for knowledge that changes.

**Common mistake:** Fine-tuning to inject company facts, then re-training every time a policy document changes.

## 8. Constitutional and rule-based methods

Fine-tuning continues training a pretrained model on your examples. It teaches format, tone and task shape far better than it teaches new facts — for facts, use retrieval. A few hundred excellent examples usually beat ten thousand mediocre ones.

```python
# Typical SFT record: the model learns the assistant turn only.
example = {
    'messages': [
        {'role': 'system', 'content': 'You extract invoice fields as JSON.'},
        {'role': 'user', 'content': 'Invoice 4471, dated 2024-03-02, total Rs 15,300.'},
        {'role': 'assistant', 'content': '{"id": "4471", "date": "2024-03-02", "total": 15300}'},
    ]
}
import json
print(json.dumps(example, indent=2))
print('\\nRule: mask the loss on system+user tokens; train only on the assistant response.')
```

**Remember:** Fine-tune for behaviour and format. Use RAG for knowledge that changes.

**Common mistake:** Fine-tuning to inject company facts, then re-training every time a policy document changes.

## 9. Sycophancy and reward hacking

Fine-tuning continues training a pretrained model on your examples. It teaches format, tone and task shape far better than it teaches new facts — for facts, use retrieval. A few hundred excellent examples usually beat ten thousand mediocre ones.

```python
# Typical SFT record: the model learns the assistant turn only.
example = {
    'messages': [
        {'role': 'system', 'content': 'You extract invoice fields as JSON.'},
        {'role': 'user', 'content': 'Invoice 4471, dated 2024-03-02, total Rs 15,300.'},
        {'role': 'assistant', 'content': '{"id": "4471", "date": "2024-03-02", "total": 15300}'},
    ]
}
import json
print(json.dumps(example, indent=2))
print('\\nRule: mask the loss on system+user tokens; train only on the assistant response.')
```

**Remember:** Fine-tune for behaviour and format. Use RAG for knowledge that changes.

**Common mistake:** Fine-tuning to inject company facts, then re-training every time a policy document changes.

## 10. Evaluating alignment

Fine-tuning continues training a pretrained model on your examples. It teaches format, tone and task shape far better than it teaches new facts — for facts, use retrieval. A few hundred excellent examples usually beat ten thousand mediocre ones.

```python
# Typical SFT record: the model learns the assistant turn only.
example = {
    'messages': [
        {'role': 'system', 'content': 'You extract invoice fields as JSON.'},
        {'role': 'user', 'content': 'Invoice 4471, dated 2024-03-02, total Rs 15,300.'},
        {'role': 'assistant', 'content': '{"id": "4471", "date": "2024-03-02", "total": 15300}'},
    ]
}
import json
print(json.dumps(example, indent=2))
print('\\nRule: mask the loss on system+user tokens; train only on the assistant response.')
```

**Remember:** Fine-tune for behaviour and format. Use RAG for knowledge that changes.

**Common mistake:** Fine-tuning to inject company facts, then re-training every time a policy document changes.

---

## What you should be able to do after Day 131

- Explain **Base models do not follow instructions** to someone else without notes.
- Explain **Supervised fine-tuning data format** to someone else without notes.
- Explain **Masking the loss to the response only** to someone else without notes.
- Explain **Data quality over quantity** to someone else without notes.
- Explain **Reward models** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
