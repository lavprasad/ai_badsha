# Day 26 — Information theory

Today's goal: work through **Information theory** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Information as surprise |
| 2 | Entropy |
| 3 | Cross-entropy |
| 4 | KL divergence |
| 5 | Mutual information |
| 6 | Perplexity in language models |
| 7 | Coding length intuition |
| 8 | Entropy in decision-tree splits |
| 9 | Cross-entropy as the classification loss |
| 10 | Computing all of these in NumPy |

---

## 1. Information as surprise

Entropy measures surprise: a fair coin has 1 bit, a two-headed coin has 0. Cross-entropy measures how surprised your model is by the truth — which is why it is the loss for classifiers and language models. Perplexity is just exp(cross-entropy), read as 'effective number of choices'.

```python
import numpy as np

def cross_entropy(p_true, p_pred, eps=1e-12):
    p_pred = np.clip(p_pred, eps, 1 - eps)
    return -np.sum(p_true * np.log(p_pred))

truth = np.array([0, 1, 0])              # class 1 is correct
confident = np.array([0.05, 0.90, 0.05])
unsure = np.array([0.33, 0.34, 0.33])
print('confident loss', round(cross_entropy(truth, confident), 3))
print('unsure loss   ', round(cross_entropy(truth, unsure), 3))
print('perplexity    ', round(float(np.exp(cross_entropy(truth, unsure))), 3))
```

**Remember:** Clip probabilities before `log` — `log(0)` is `-inf` and poisons the whole batch.

**Common mistake:** Applying softmax twice (once in the model, once in the loss) and getting flat, untrainable gradients.

## 2. Entropy

Entropy measures surprise: a fair coin has 1 bit, a two-headed coin has 0. Cross-entropy measures how surprised your model is by the truth — which is why it is the loss for classifiers and language models. Perplexity is just exp(cross-entropy), read as 'effective number of choices'.

```python
import numpy as np

def cross_entropy(p_true, p_pred, eps=1e-12):
    p_pred = np.clip(p_pred, eps, 1 - eps)
    return -np.sum(p_true * np.log(p_pred))

truth = np.array([0, 1, 0])              # class 1 is correct
confident = np.array([0.05, 0.90, 0.05])
unsure = np.array([0.33, 0.34, 0.33])
print('confident loss', round(cross_entropy(truth, confident), 3))
print('unsure loss   ', round(cross_entropy(truth, unsure), 3))
print('perplexity    ', round(float(np.exp(cross_entropy(truth, unsure))), 3))
```

**Remember:** Clip probabilities before `log` — `log(0)` is `-inf` and poisons the whole batch.

**Common mistake:** Applying softmax twice (once in the model, once in the loss) and getting flat, untrainable gradients.

## 3. Cross-entropy

Entropy measures surprise: a fair coin has 1 bit, a two-headed coin has 0. Cross-entropy measures how surprised your model is by the truth — which is why it is the loss for classifiers and language models. Perplexity is just exp(cross-entropy), read as 'effective number of choices'.

```python
import numpy as np

def cross_entropy(p_true, p_pred, eps=1e-12):
    p_pred = np.clip(p_pred, eps, 1 - eps)
    return -np.sum(p_true * np.log(p_pred))

truth = np.array([0, 1, 0])              # class 1 is correct
confident = np.array([0.05, 0.90, 0.05])
unsure = np.array([0.33, 0.34, 0.33])
print('confident loss', round(cross_entropy(truth, confident), 3))
print('unsure loss   ', round(cross_entropy(truth, unsure), 3))
print('perplexity    ', round(float(np.exp(cross_entropy(truth, unsure))), 3))
```

**Remember:** Clip probabilities before `log` — `log(0)` is `-inf` and poisons the whole batch.

**Common mistake:** Applying softmax twice (once in the model, once in the loss) and getting flat, untrainable gradients.

## 4. KL divergence

Entropy measures surprise: a fair coin has 1 bit, a two-headed coin has 0. Cross-entropy measures how surprised your model is by the truth — which is why it is the loss for classifiers and language models. Perplexity is just exp(cross-entropy), read as 'effective number of choices'.

```python
import numpy as np

def cross_entropy(p_true, p_pred, eps=1e-12):
    p_pred = np.clip(p_pred, eps, 1 - eps)
    return -np.sum(p_true * np.log(p_pred))

truth = np.array([0, 1, 0])              # class 1 is correct
confident = np.array([0.05, 0.90, 0.05])
unsure = np.array([0.33, 0.34, 0.33])
print('confident loss', round(cross_entropy(truth, confident), 3))
print('unsure loss   ', round(cross_entropy(truth, unsure), 3))
print('perplexity    ', round(float(np.exp(cross_entropy(truth, unsure))), 3))
```

**Remember:** Clip probabilities before `log` — `log(0)` is `-inf` and poisons the whole batch.

**Common mistake:** Applying softmax twice (once in the model, once in the loss) and getting flat, untrainable gradients.

## 5. Mutual information

Entropy measures surprise: a fair coin has 1 bit, a two-headed coin has 0. Cross-entropy measures how surprised your model is by the truth — which is why it is the loss for classifiers and language models. Perplexity is just exp(cross-entropy), read as 'effective number of choices'.

```python
import numpy as np

def cross_entropy(p_true, p_pred, eps=1e-12):
    p_pred = np.clip(p_pred, eps, 1 - eps)
    return -np.sum(p_true * np.log(p_pred))

truth = np.array([0, 1, 0])              # class 1 is correct
confident = np.array([0.05, 0.90, 0.05])
unsure = np.array([0.33, 0.34, 0.33])
print('confident loss', round(cross_entropy(truth, confident), 3))
print('unsure loss   ', round(cross_entropy(truth, unsure), 3))
print('perplexity    ', round(float(np.exp(cross_entropy(truth, unsure))), 3))
```

**Remember:** Clip probabilities before `log` — `log(0)` is `-inf` and poisons the whole batch.

**Common mistake:** Applying softmax twice (once in the model, once in the loss) and getting flat, untrainable gradients.

## 6. Perplexity in language models

Entropy measures surprise: a fair coin has 1 bit, a two-headed coin has 0. Cross-entropy measures how surprised your model is by the truth — which is why it is the loss for classifiers and language models. Perplexity is just exp(cross-entropy), read as 'effective number of choices'.

```python
import numpy as np

def cross_entropy(p_true, p_pred, eps=1e-12):
    p_pred = np.clip(p_pred, eps, 1 - eps)
    return -np.sum(p_true * np.log(p_pred))

truth = np.array([0, 1, 0])              # class 1 is correct
confident = np.array([0.05, 0.90, 0.05])
unsure = np.array([0.33, 0.34, 0.33])
print('confident loss', round(cross_entropy(truth, confident), 3))
print('unsure loss   ', round(cross_entropy(truth, unsure), 3))
print('perplexity    ', round(float(np.exp(cross_entropy(truth, unsure))), 3))
```

**Remember:** Clip probabilities before `log` — `log(0)` is `-inf` and poisons the whole batch.

**Common mistake:** Applying softmax twice (once in the model, once in the loss) and getting flat, untrainable gradients.

## 7. Coding length intuition

Entropy measures surprise: a fair coin has 1 bit, a two-headed coin has 0. Cross-entropy measures how surprised your model is by the truth — which is why it is the loss for classifiers and language models. Perplexity is just exp(cross-entropy), read as 'effective number of choices'.

```python
import numpy as np

def cross_entropy(p_true, p_pred, eps=1e-12):
    p_pred = np.clip(p_pred, eps, 1 - eps)
    return -np.sum(p_true * np.log(p_pred))

truth = np.array([0, 1, 0])              # class 1 is correct
confident = np.array([0.05, 0.90, 0.05])
unsure = np.array([0.33, 0.34, 0.33])
print('confident loss', round(cross_entropy(truth, confident), 3))
print('unsure loss   ', round(cross_entropy(truth, unsure), 3))
print('perplexity    ', round(float(np.exp(cross_entropy(truth, unsure))), 3))
```

**Remember:** Clip probabilities before `log` — `log(0)` is `-inf` and poisons the whole batch.

**Common mistake:** Applying softmax twice (once in the model, once in the loss) and getting flat, untrainable gradients.

## 8. Entropy in decision-tree splits

Entropy measures surprise: a fair coin has 1 bit, a two-headed coin has 0. Cross-entropy measures how surprised your model is by the truth — which is why it is the loss for classifiers and language models. Perplexity is just exp(cross-entropy), read as 'effective number of choices'.

```python
import numpy as np

def cross_entropy(p_true, p_pred, eps=1e-12):
    p_pred = np.clip(p_pred, eps, 1 - eps)
    return -np.sum(p_true * np.log(p_pred))

truth = np.array([0, 1, 0])              # class 1 is correct
confident = np.array([0.05, 0.90, 0.05])
unsure = np.array([0.33, 0.34, 0.33])
print('confident loss', round(cross_entropy(truth, confident), 3))
print('unsure loss   ', round(cross_entropy(truth, unsure), 3))
print('perplexity    ', round(float(np.exp(cross_entropy(truth, unsure))), 3))
```

**Remember:** Clip probabilities before `log` — `log(0)` is `-inf` and poisons the whole batch.

**Common mistake:** Applying softmax twice (once in the model, once in the loss) and getting flat, untrainable gradients.

## 9. Cross-entropy as the classification loss

Entropy measures surprise: a fair coin has 1 bit, a two-headed coin has 0. Cross-entropy measures how surprised your model is by the truth — which is why it is the loss for classifiers and language models. Perplexity is just exp(cross-entropy), read as 'effective number of choices'.

```python
import numpy as np

def cross_entropy(p_true, p_pred, eps=1e-12):
    p_pred = np.clip(p_pred, eps, 1 - eps)
    return -np.sum(p_true * np.log(p_pred))

truth = np.array([0, 1, 0])              # class 1 is correct
confident = np.array([0.05, 0.90, 0.05])
unsure = np.array([0.33, 0.34, 0.33])
print('confident loss', round(cross_entropy(truth, confident), 3))
print('unsure loss   ', round(cross_entropy(truth, unsure), 3))
print('perplexity    ', round(float(np.exp(cross_entropy(truth, unsure))), 3))
```

**Remember:** Clip probabilities before `log` — `log(0)` is `-inf` and poisons the whole batch.

**Common mistake:** Applying softmax twice (once in the model, once in the loss) and getting flat, untrainable gradients.

## 10. Computing all of these in NumPy

Entropy measures surprise: a fair coin has 1 bit, a two-headed coin has 0. Cross-entropy measures how surprised your model is by the truth — which is why it is the loss for classifiers and language models. Perplexity is just exp(cross-entropy), read as 'effective number of choices'.

```python
import numpy as np

def cross_entropy(p_true, p_pred, eps=1e-12):
    p_pred = np.clip(p_pred, eps, 1 - eps)
    return -np.sum(p_true * np.log(p_pred))

truth = np.array([0, 1, 0])              # class 1 is correct
confident = np.array([0.05, 0.90, 0.05])
unsure = np.array([0.33, 0.34, 0.33])
print('confident loss', round(cross_entropy(truth, confident), 3))
print('unsure loss   ', round(cross_entropy(truth, unsure), 3))
print('perplexity    ', round(float(np.exp(cross_entropy(truth, unsure))), 3))
```

**Remember:** Clip probabilities before `log` — `log(0)` is `-inf` and poisons the whole batch.

**Common mistake:** Applying softmax twice (once in the model, once in the loss) and getting flat, untrainable gradients.

---

## What you should be able to do after Day 26

- Explain **Information as surprise** to someone else without notes.
- Explain **Entropy** to someone else without notes.
- Explain **Cross-entropy** to someone else without notes.
- Explain **KL divergence** to someone else without notes.
- Explain **Mutual information** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
