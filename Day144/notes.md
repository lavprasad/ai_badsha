# Day 144 — Knowledge in language models

Today's goal: work through **Knowledge in language models** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Parametric vs retrieved knowledge |
| 2 | Knowledge cutoffs |
| 3 | Model editing |
| 4 | Knowledge graphs alongside LLMs |
| 5 | Entity linking |
| 6 | Fact verification |
| 7 | Temporal reasoning failures |
| 8 | Numerical and counting weaknesses |
| 9 | When to use a database instead |
| 10 | Designing the knowledge boundary |

---

## 1. Parametric vs retrieved knowledge

A model's weights hold a frozen, lossy snapshot of the world up to its cutoff. Anything that changes — prices, policies, staff, inventory — belongs in a database or a retrieval index, not in weights. Draw that boundary explicitly and the hallucination rate falls sharply.

```python
KNOWLEDGE_ROUTING = {
    'current account balance':  'database — never the model',
    'company refund policy':    'retrieval from the policy doc',
    'what is a p-value':        'model weights are fine',
    'yesterday\'s ticket count': 'database aggregate',
    'summarise this email':     'model, with the email in context',
}
for question, source in KNOWLEDGE_ROUTING.items():
    print(f'{question:<28} -> {source}')
print('\nRule: if it can change without a retrain, it must not live in weights.')
```

**Remember:** If a fact can change tomorrow, retrieve it. If it cannot, the weights may hold it.

**Common mistake:** Fine-tuning prices into a model and re-running the whole job every time the price list updates.

## 2. Knowledge cutoffs

A model's weights hold a frozen, lossy snapshot of the world up to its cutoff. Anything that changes — prices, policies, staff, inventory — belongs in a database or a retrieval index, not in weights. Draw that boundary explicitly and the hallucination rate falls sharply.

```python
KNOWLEDGE_ROUTING = {
    'current account balance':  'database — never the model',
    'company refund policy':    'retrieval from the policy doc',
    'what is a p-value':        'model weights are fine',
    'yesterday\'s ticket count': 'database aggregate',
    'summarise this email':     'model, with the email in context',
}
for question, source in KNOWLEDGE_ROUTING.items():
    print(f'{question:<28} -> {source}')
print('\nRule: if it can change without a retrain, it must not live in weights.')
```

**Remember:** If a fact can change tomorrow, retrieve it. If it cannot, the weights may hold it.

**Common mistake:** Fine-tuning prices into a model and re-running the whole job every time the price list updates.

## 3. Model editing

A model's weights hold a frozen, lossy snapshot of the world up to its cutoff. Anything that changes — prices, policies, staff, inventory — belongs in a database or a retrieval index, not in weights. Draw that boundary explicitly and the hallucination rate falls sharply.

```python
KNOWLEDGE_ROUTING = {
    'current account balance':  'database — never the model',
    'company refund policy':    'retrieval from the policy doc',
    'what is a p-value':        'model weights are fine',
    'yesterday\'s ticket count': 'database aggregate',
    'summarise this email':     'model, with the email in context',
}
for question, source in KNOWLEDGE_ROUTING.items():
    print(f'{question:<28} -> {source}')
print('\nRule: if it can change without a retrain, it must not live in weights.')
```

**Remember:** If a fact can change tomorrow, retrieve it. If it cannot, the weights may hold it.

**Common mistake:** Fine-tuning prices into a model and re-running the whole job every time the price list updates.

## 4. Knowledge graphs alongside LLMs

A GNN passes messages along edges: each node updates itself from its neighbours, repeated k times so information travels k hops. Good for fraud rings, molecules and social graphs — anywhere the relationships carry more signal than the nodes.

```python
import numpy as np

# One round of mean-aggregation message passing
A = np.array([[0, 1, 1, 0],
              [1, 0, 1, 0],
              [1, 1, 0, 1],
              [0, 0, 1, 0]], dtype=float)
H = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0], [0.5, 0.5]])

deg = A.sum(axis=1, keepdims=True)
H_next = np.tanh((A @ H) / np.maximum(deg, 1))
print(H_next.round(3))
```

**Remember:** Too many message-passing layers causes over-smoothing — every node converges to the same vector.

**Common mistake:** Splitting graph data randomly so a node's own neighbours end up in both train and test.

## 5. Entity linking

A model's weights hold a frozen, lossy snapshot of the world up to its cutoff. Anything that changes — prices, policies, staff, inventory — belongs in a database or a retrieval index, not in weights. Draw that boundary explicitly and the hallucination rate falls sharply.

```python
KNOWLEDGE_ROUTING = {
    'current account balance':  'database — never the model',
    'company refund policy':    'retrieval from the policy doc',
    'what is a p-value':        'model weights are fine',
    'yesterday\'s ticket count': 'database aggregate',
    'summarise this email':     'model, with the email in context',
}
for question, source in KNOWLEDGE_ROUTING.items():
    print(f'{question:<28} -> {source}')
print('\nRule: if it can change without a retrain, it must not live in weights.')
```

**Remember:** If a fact can change tomorrow, retrieve it. If it cannot, the weights may hold it.

**Common mistake:** Fine-tuning prices into a model and re-running the whole job every time the price list updates.

## 6. Fact verification

A model's weights hold a frozen, lossy snapshot of the world up to its cutoff. Anything that changes — prices, policies, staff, inventory — belongs in a database or a retrieval index, not in weights. Draw that boundary explicitly and the hallucination rate falls sharply.

```python
KNOWLEDGE_ROUTING = {
    'current account balance':  'database — never the model',
    'company refund policy':    'retrieval from the policy doc',
    'what is a p-value':        'model weights are fine',
    'yesterday\'s ticket count': 'database aggregate',
    'summarise this email':     'model, with the email in context',
}
for question, source in KNOWLEDGE_ROUTING.items():
    print(f'{question:<28} -> {source}')
print('\nRule: if it can change without a retrain, it must not live in weights.')
```

**Remember:** If a fact can change tomorrow, retrieve it. If it cannot, the weights may hold it.

**Common mistake:** Fine-tuning prices into a model and re-running the whole job every time the price list updates.

## 7. Temporal reasoning failures

A model's weights hold a frozen, lossy snapshot of the world up to its cutoff. Anything that changes — prices, policies, staff, inventory — belongs in a database or a retrieval index, not in weights. Draw that boundary explicitly and the hallucination rate falls sharply.

```python
KNOWLEDGE_ROUTING = {
    'current account balance':  'database — never the model',
    'company refund policy':    'retrieval from the policy doc',
    'what is a p-value':        'model weights are fine',
    'yesterday\'s ticket count': 'database aggregate',
    'summarise this email':     'model, with the email in context',
}
for question, source in KNOWLEDGE_ROUTING.items():
    print(f'{question:<28} -> {source}')
print('\nRule: if it can change without a retrain, it must not live in weights.')
```

**Remember:** If a fact can change tomorrow, retrieve it. If it cannot, the weights may hold it.

**Common mistake:** Fine-tuning prices into a model and re-running the whole job every time the price list updates.

## 8. Numerical and counting weaknesses

A model's weights hold a frozen, lossy snapshot of the world up to its cutoff. Anything that changes — prices, policies, staff, inventory — belongs in a database or a retrieval index, not in weights. Draw that boundary explicitly and the hallucination rate falls sharply.

```python
KNOWLEDGE_ROUTING = {
    'current account balance':  'database — never the model',
    'company refund policy':    'retrieval from the policy doc',
    'what is a p-value':        'model weights are fine',
    'yesterday\'s ticket count': 'database aggregate',
    'summarise this email':     'model, with the email in context',
}
for question, source in KNOWLEDGE_ROUTING.items():
    print(f'{question:<28} -> {source}')
print('\nRule: if it can change without a retrain, it must not live in weights.')
```

**Remember:** If a fact can change tomorrow, retrieve it. If it cannot, the weights may hold it.

**Common mistake:** Fine-tuning prices into a model and re-running the whole job every time the price list updates.

## 9. When to use a database instead

A model's weights hold a frozen, lossy snapshot of the world up to its cutoff. Anything that changes — prices, policies, staff, inventory — belongs in a database or a retrieval index, not in weights. Draw that boundary explicitly and the hallucination rate falls sharply.

```python
KNOWLEDGE_ROUTING = {
    'current account balance':  'database — never the model',
    'company refund policy':    'retrieval from the policy doc',
    'what is a p-value':        'model weights are fine',
    'yesterday\'s ticket count': 'database aggregate',
    'summarise this email':     'model, with the email in context',
}
for question, source in KNOWLEDGE_ROUTING.items():
    print(f'{question:<28} -> {source}')
print('\nRule: if it can change without a retrain, it must not live in weights.')
```

**Remember:** If a fact can change tomorrow, retrieve it. If it cannot, the weights may hold it.

**Common mistake:** Fine-tuning prices into a model and re-running the whole job every time the price list updates.

## 10. Designing the knowledge boundary

A model's weights hold a frozen, lossy snapshot of the world up to its cutoff. Anything that changes — prices, policies, staff, inventory — belongs in a database or a retrieval index, not in weights. Draw that boundary explicitly and the hallucination rate falls sharply.

```python
KNOWLEDGE_ROUTING = {
    'current account balance':  'database — never the model',
    'company refund policy':    'retrieval from the policy doc',
    'what is a p-value':        'model weights are fine',
    'yesterday\'s ticket count': 'database aggregate',
    'summarise this email':     'model, with the email in context',
}
for question, source in KNOWLEDGE_ROUTING.items():
    print(f'{question:<28} -> {source}')
print('\nRule: if it can change without a retrain, it must not live in weights.')
```

**Remember:** If a fact can change tomorrow, retrieve it. If it cannot, the weights may hold it.

**Common mistake:** Fine-tuning prices into a model and re-running the whole job every time the price list updates.

---

## What you should be able to do after Day 144

- Explain **Parametric vs retrieved knowledge** to someone else without notes.
- Explain **Knowledge cutoffs** to someone else without notes.
- Explain **Model editing** to someone else without notes.
- Explain **Knowledge graphs alongside LLMs** to someone else without notes.
- Explain **Entity linking** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
