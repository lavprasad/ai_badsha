# Day 26 — Information theory

Aaj ka goal: **Information theory** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

### Aasaan Bhasha

Entropy surprise naapti hai: fair coin me 1 bit, do-headed coin me 0. Cross-entropy naapti hai ki sach dekh kar aapka model kitna chaunka — isiliye wo classifiers aur language models ka loss hai. Perplexity bas exp(cross-entropy) hai, matlab 'kitne effective choices'.

### Chhota code

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

**Yaad rakho:** `log` se pehle probabilities clip karo — `log(0)` `-inf` hai aur poora batch kharab kar deta hai.

**Aam galti:** Softmax do baar lagana (ek model me, ek loss me) aur flat, untrainable gradients paana.

Practice: `examples/01_information_as_surprise.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Entropy

### Aasaan Bhasha

Entropy surprise naapti hai: fair coin me 1 bit, do-headed coin me 0. Cross-entropy naapti hai ki sach dekh kar aapka model kitna chaunka — isiliye wo classifiers aur language models ka loss hai. Perplexity bas exp(cross-entropy) hai, matlab 'kitne effective choices'.

### Chhota code

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

**Yaad rakho:** `log` se pehle probabilities clip karo — `log(0)` `-inf` hai aur poora batch kharab kar deta hai.

**Aam galti:** Softmax do baar lagana (ek model me, ek loss me) aur flat, untrainable gradients paana.

Practice: `examples/02_entropy.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Cross-entropy

### Aasaan Bhasha

Entropy surprise naapti hai: fair coin me 1 bit, do-headed coin me 0. Cross-entropy naapti hai ki sach dekh kar aapka model kitna chaunka — isiliye wo classifiers aur language models ka loss hai. Perplexity bas exp(cross-entropy) hai, matlab 'kitne effective choices'.

### Chhota code

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

**Yaad rakho:** `log` se pehle probabilities clip karo — `log(0)` `-inf` hai aur poora batch kharab kar deta hai.

**Aam galti:** Softmax do baar lagana (ek model me, ek loss me) aur flat, untrainable gradients paana.

Practice: `examples/03_cross_entropy.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. KL divergence

### Aasaan Bhasha

Entropy surprise naapti hai: fair coin me 1 bit, do-headed coin me 0. Cross-entropy naapti hai ki sach dekh kar aapka model kitna chaunka — isiliye wo classifiers aur language models ka loss hai. Perplexity bas exp(cross-entropy) hai, matlab 'kitne effective choices'.

### Chhota code

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

**Yaad rakho:** `log` se pehle probabilities clip karo — `log(0)` `-inf` hai aur poora batch kharab kar deta hai.

**Aam galti:** Softmax do baar lagana (ek model me, ek loss me) aur flat, untrainable gradients paana.

Practice: `examples/04_kl_divergence.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Mutual information

### Aasaan Bhasha

Entropy surprise naapti hai: fair coin me 1 bit, do-headed coin me 0. Cross-entropy naapti hai ki sach dekh kar aapka model kitna chaunka — isiliye wo classifiers aur language models ka loss hai. Perplexity bas exp(cross-entropy) hai, matlab 'kitne effective choices'.

### Chhota code

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

**Yaad rakho:** `log` se pehle probabilities clip karo — `log(0)` `-inf` hai aur poora batch kharab kar deta hai.

**Aam galti:** Softmax do baar lagana (ek model me, ek loss me) aur flat, untrainable gradients paana.

Practice: `examples/05_mutual_information.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Perplexity in language models

### Aasaan Bhasha

Entropy surprise naapti hai: fair coin me 1 bit, do-headed coin me 0. Cross-entropy naapti hai ki sach dekh kar aapka model kitna chaunka — isiliye wo classifiers aur language models ka loss hai. Perplexity bas exp(cross-entropy) hai, matlab 'kitne effective choices'.

### Chhota code

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

**Yaad rakho:** `log` se pehle probabilities clip karo — `log(0)` `-inf` hai aur poora batch kharab kar deta hai.

**Aam galti:** Softmax do baar lagana (ek model me, ek loss me) aur flat, untrainable gradients paana.

Practice: `examples/06_perplexity_in_language_models.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Coding length intuition

### Aasaan Bhasha

Entropy surprise naapti hai: fair coin me 1 bit, do-headed coin me 0. Cross-entropy naapti hai ki sach dekh kar aapka model kitna chaunka — isiliye wo classifiers aur language models ka loss hai. Perplexity bas exp(cross-entropy) hai, matlab 'kitne effective choices'.

### Chhota code

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

**Yaad rakho:** `log` se pehle probabilities clip karo — `log(0)` `-inf` hai aur poora batch kharab kar deta hai.

**Aam galti:** Softmax do baar lagana (ek model me, ek loss me) aur flat, untrainable gradients paana.

Practice: `examples/07_coding_length_intuition.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Entropy in decision-tree splits

### Aasaan Bhasha

Entropy surprise naapti hai: fair coin me 1 bit, do-headed coin me 0. Cross-entropy naapti hai ki sach dekh kar aapka model kitna chaunka — isiliye wo classifiers aur language models ka loss hai. Perplexity bas exp(cross-entropy) hai, matlab 'kitne effective choices'.

### Chhota code

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

**Yaad rakho:** `log` se pehle probabilities clip karo — `log(0)` `-inf` hai aur poora batch kharab kar deta hai.

**Aam galti:** Softmax do baar lagana (ek model me, ek loss me) aur flat, untrainable gradients paana.

Practice: `examples/08_entropy_in_decision_tree_splits.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Cross-entropy as the classification loss

### Aasaan Bhasha

Entropy surprise naapti hai: fair coin me 1 bit, do-headed coin me 0. Cross-entropy naapti hai ki sach dekh kar aapka model kitna chaunka — isiliye wo classifiers aur language models ka loss hai. Perplexity bas exp(cross-entropy) hai, matlab 'kitne effective choices'.

### Chhota code

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

**Yaad rakho:** `log` se pehle probabilities clip karo — `log(0)` `-inf` hai aur poora batch kharab kar deta hai.

**Aam galti:** Softmax do baar lagana (ek model me, ek loss me) aur flat, untrainable gradients paana.

Practice: `examples/09_cross_entropy_as_the_classification_loss.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Computing all of these in NumPy

### Aasaan Bhasha

Entropy surprise naapti hai: fair coin me 1 bit, do-headed coin me 0. Cross-entropy naapti hai ki sach dekh kar aapka model kitna chaunka — isiliye wo classifiers aur language models ka loss hai. Perplexity bas exp(cross-entropy) hai, matlab 'kitne effective choices'.

### Chhota code

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

**Yaad rakho:** `log` se pehle probabilities clip karo — `log(0)` `-inf` hai aur poora batch kharab kar deta hai.

**Aam galti:** Softmax do baar lagana (ek model me, ek loss me) aur flat, untrainable gradients paana.

Practice: `examples/10_computing_all_of_these_in_numpy.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 26 ke baad aapko ye aana chahiye

- **Information as surprise** ko bina notes dekhe kisi dost ko samjha sakna.
- **Entropy** ko bina notes dekhe kisi dost ko samjha sakna.
- **Cross-entropy** ko bina notes dekhe kisi dost ko samjha sakna.
- **KL divergence** ko bina notes dekhe kisi dost ko samjha sakna.
- **Mutual information** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
