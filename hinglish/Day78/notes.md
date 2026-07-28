# Day 78 — Loss functions

Aaj ka goal: **Loss functions** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Loss as the objective you actually optimise |
| 2 | Mean squared error |
| 3 | Mean absolute error and Huber |
| 4 | Binary cross-entropy |
| 5 | Categorical cross-entropy |
| 6 | Logits vs probabilities in loss functions |
| 7 | Class weights inside the loss |
| 8 | Label smoothing |
| 9 | Contrastive and triplet loss |
| 10 | Custom losses for business costs |

---

## 1. Loss as the objective you actually optimise

### Aasaan Bhasha

Loss hi wo ek cheez hai jise model sach me optimise karta hai — baaki sab sajावat hai. Cross-entropy implementations ko logits do (probabilities nahi) jab wo logits maangti hain. Agar ek false negative false positive se das guna mehnga hai, to use loss ya threshold me likho, slide me nahi.

### Chhota code

```python
import numpy as np

def weighted_bce(y, p, w_pos=10.0, eps=1e-12):
    p = np.clip(p, eps, 1 - eps)
    return float(-np.mean(w_pos * y * np.log(p) + (1 - y) * np.log(1 - p)))

y = np.array([1.0, 0.0, 0.0, 1.0])
misses_positive = np.array([0.2, 0.1, 0.1, 0.3])
misses_negative = np.array([0.9, 0.8, 0.7, 0.9])
print('missing positives costs', round(weighted_bce(y, misses_positive), 3))
print('false alarms cost      ', round(weighted_bce(y, misses_negative), 3))
```

**Yaad rakho:** Har error type ki asli keemat loss ya threshold me daalo — model use khud andaaza nahi laga sakta.

**Aam galti:** Fraud model ke liye saadi accuracy optimise karna jahan ek chook 10,000x false alarm ke barabar hai.

Practice: `examples/01_loss_as_the_objective_you_actually_optim.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Mean squared error

### Aasaan Bhasha

Mean ko outliers kheench lete hain; median ko nahi. Dono report karo, saath me spread bhi. Jab mean aur median me bada farq ho to distribution skewed hai aur average aapse jhooth bol raha hai.

### Chhota code

```python
import numpy as np

salaries = np.array([30, 32, 35, 33, 31, 900])   # one founder
print('mean  ', salaries.mean())     # 176.8 — misleading
print('median', np.median(salaries)) # 32.5  — honest
print('p95   ', np.percentile(salaries, 95))

q1, q3 = np.percentile(salaries, [25, 75])
iqr = q3 - q1
print('outliers', salaries[(salaries < q1 - 1.5 * iqr) | (salaries > q3 + 1.5 * iqr)])
```

**Yaad rakho:** Skewed data ke liye median + IQR batao, mean + std sirf roughly symmetric data ke liye.

**Aam galti:** 'Outliers' ko apne aap hata dena jabki wahi events aapko predict karne ke liye rakha gaya tha.

Practice: `examples/02_mean_squared_error.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Mean absolute error and Huber

### Aasaan Bhasha

Mean ko outliers kheench lete hain; median ko nahi. Dono report karo, saath me spread bhi. Jab mean aur median me bada farq ho to distribution skewed hai aur average aapse jhooth bol raha hai.

### Chhota code

```python
import numpy as np

salaries = np.array([30, 32, 35, 33, 31, 900])   # one founder
print('mean  ', salaries.mean())     # 176.8 — misleading
print('median', np.median(salaries)) # 32.5  — honest
print('p95   ', np.percentile(salaries, 95))

q1, q3 = np.percentile(salaries, [25, 75])
iqr = q3 - q1
print('outliers', salaries[(salaries < q1 - 1.5 * iqr) | (salaries > q3 + 1.5 * iqr)])
```

**Yaad rakho:** Skewed data ke liye median + IQR batao, mean + std sirf roughly symmetric data ke liye.

**Aam galti:** 'Outliers' ko apne aap hata dena jabki wahi events aapko predict karne ke liye rakha gaya tha.

Practice: `examples/03_mean_absolute_error_and_huber.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Binary cross-entropy

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

Practice: `examples/04_binary_cross_entropy.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Categorical cross-entropy

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

Practice: `examples/05_categorical_cross_entropy.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Logits vs probabilities in loss functions

### Aasaan Bhasha

Loss hi wo ek cheez hai jise model sach me optimise karta hai — baaki sab sajावat hai. Cross-entropy implementations ko logits do (probabilities nahi) jab wo logits maangti hain. Agar ek false negative false positive se das guna mehnga hai, to use loss ya threshold me likho, slide me nahi.

### Chhota code

```python
import numpy as np

def weighted_bce(y, p, w_pos=10.0, eps=1e-12):
    p = np.clip(p, eps, 1 - eps)
    return float(-np.mean(w_pos * y * np.log(p) + (1 - y) * np.log(1 - p)))

y = np.array([1.0, 0.0, 0.0, 1.0])
misses_positive = np.array([0.2, 0.1, 0.1, 0.3])
misses_negative = np.array([0.9, 0.8, 0.7, 0.9])
print('missing positives costs', round(weighted_bce(y, misses_positive), 3))
print('false alarms cost      ', round(weighted_bce(y, misses_negative), 3))
```

**Yaad rakho:** Har error type ki asli keemat loss ya threshold me daalo — model use khud andaaza nahi laga sakta.

**Aam galti:** Fraud model ke liye saadi accuracy optimise karna jahan ek chook 10,000x false alarm ke barabar hai.

Practice: `examples/06_logits_vs_probabilities_in_loss_function.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Class weights inside the loss

### Aasaan Bhasha

Jab ek class data ka 1% ho, model hamesha 'no' bolna seekh leta hai. Ise class weights (sasta, pehli choice), threshold tuning, ya resampling se theek karo. SMOTE minority points banata hai — aur use sirf training fold par hi lagana chahiye.

### Chhota code

```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import recall_score

X, y = make_classification(n_samples=3000, weights=[0.97, 0.03], random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, stratify=y, test_size=0.3, random_state=0)

plain = LogisticRegression(max_iter=1000).fit(Xtr, ytr)
weighted = LogisticRegression(max_iter=1000, class_weight='balanced').fit(Xtr, ytr)
print('recall plain   ', round(recall_score(yte, plain.predict(Xte)), 3))
print('recall balanced', round(recall_score(yte, weighted.predict(Xte)), 3))
```

**Yaad rakho:** Kuch bhi install karne se pehle `class_weight='balanced'` try karo.

**Aam galti:** Split se pehle SMOTE lagana, jisse test rows ki synthetic copies training me aa jaati hain.

Practice: `examples/07_class_weights_inside_the_loss.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Label smoothing

### Aasaan Bhasha

Loss hi wo ek cheez hai jise model sach me optimise karta hai — baaki sab sajावat hai. Cross-entropy implementations ko logits do (probabilities nahi) jab wo logits maangti hain. Agar ek false negative false positive se das guna mehnga hai, to use loss ya threshold me likho, slide me nahi.

### Chhota code

```python
import numpy as np

def weighted_bce(y, p, w_pos=10.0, eps=1e-12):
    p = np.clip(p, eps, 1 - eps)
    return float(-np.mean(w_pos * y * np.log(p) + (1 - y) * np.log(1 - p)))

y = np.array([1.0, 0.0, 0.0, 1.0])
misses_positive = np.array([0.2, 0.1, 0.1, 0.3])
misses_negative = np.array([0.9, 0.8, 0.7, 0.9])
print('missing positives costs', round(weighted_bce(y, misses_positive), 3))
print('false alarms cost      ', round(weighted_bce(y, misses_negative), 3))
```

**Yaad rakho:** Har error type ki asli keemat loss ya threshold me daalo — model use khud andaaza nahi laga sakta.

**Aam galti:** Fraud model ke liye saadi accuracy optimise karna jahan ek chook 10,000x false alarm ke barabar hai.

Practice: `examples/08_label_smoothing.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Contrastive and triplet loss

### Aasaan Bhasha

Loss hi wo ek cheez hai jise model sach me optimise karta hai — baaki sab sajावat hai. Cross-entropy implementations ko logits do (probabilities nahi) jab wo logits maangti hain. Agar ek false negative false positive se das guna mehnga hai, to use loss ya threshold me likho, slide me nahi.

### Chhota code

```python
import numpy as np

def weighted_bce(y, p, w_pos=10.0, eps=1e-12):
    p = np.clip(p, eps, 1 - eps)
    return float(-np.mean(w_pos * y * np.log(p) + (1 - y) * np.log(1 - p)))

y = np.array([1.0, 0.0, 0.0, 1.0])
misses_positive = np.array([0.2, 0.1, 0.1, 0.3])
misses_negative = np.array([0.9, 0.8, 0.7, 0.9])
print('missing positives costs', round(weighted_bce(y, misses_positive), 3))
print('false alarms cost      ', round(weighted_bce(y, misses_negative), 3))
```

**Yaad rakho:** Har error type ki asli keemat loss ya threshold me daalo — model use khud andaaza nahi laga sakta.

**Aam galti:** Fraud model ke liye saadi accuracy optimise karna jahan ek chook 10,000x false alarm ke barabar hai.

Practice: `examples/09_contrastive_and_triplet_loss.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Custom losses for business costs

### Aasaan Bhasha

Loss hi wo ek cheez hai jise model sach me optimise karta hai — baaki sab sajावat hai. Cross-entropy implementations ko logits do (probabilities nahi) jab wo logits maangti hain. Agar ek false negative false positive se das guna mehnga hai, to use loss ya threshold me likho, slide me nahi.

### Chhota code

```python
import numpy as np

def weighted_bce(y, p, w_pos=10.0, eps=1e-12):
    p = np.clip(p, eps, 1 - eps)
    return float(-np.mean(w_pos * y * np.log(p) + (1 - y) * np.log(1 - p)))

y = np.array([1.0, 0.0, 0.0, 1.0])
misses_positive = np.array([0.2, 0.1, 0.1, 0.3])
misses_negative = np.array([0.9, 0.8, 0.7, 0.9])
print('missing positives costs', round(weighted_bce(y, misses_positive), 3))
print('false alarms cost      ', round(weighted_bce(y, misses_negative), 3))
```

**Yaad rakho:** Har error type ki asli keemat loss ya threshold me daalo — model use khud andaaza nahi laga sakta.

**Aam galti:** Fraud model ke liye saadi accuracy optimise karna jahan ek chook 10,000x false alarm ke barabar hai.

Practice: `examples/10_custom_losses_for_business_costs.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 78 ke baad aapko ye aana chahiye

- **Loss as the objective you actually optimise** ko bina notes dekhe kisi dost ko samjha sakna.
- **Mean squared error** ko bina notes dekhe kisi dost ko samjha sakna.
- **Mean absolute error and Huber** ko bina notes dekhe kisi dost ko samjha sakna.
- **Binary cross-entropy** ko bina notes dekhe kisi dost ko samjha sakna.
- **Categorical cross-entropy** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
