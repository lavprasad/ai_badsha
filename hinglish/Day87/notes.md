# Day 87 — Debugging neural networks

Aaj ka goal: **Debugging neural networks** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Overfit a single batch first |
| 2 | Check loss at initialisation |
| 3 | Verify the data reaching the model |
| 4 | Shape errors and how to read them |
| 5 | NaN loss: causes and fixes |
| 6 | Exploding and vanishing gradients |
| 7 | Learning rate diagnosis from the curve |
| 8 | Dead ReLU detection |
| 9 | Comparing against a simple baseline |
| 10 | A deep learning debugging checklist |

---

## 1. Overfit a single batch first

### Aasaan Bhasha

Debug ek tay kram me karo, sabse sasta test pehle. Kya model 20 rows par zero loss tak overfit kar sakta hai? Nahi, to bug data ya wiring me hai, capacity me nahi. Kya step zero par loss wahi hai jo random guessing se aana chahiye? Nahi, to labels ya output layer galat hai.

### Chhota code

```python
import numpy as np

def sanity_report(X, y, n_classes):
    print('shapes        ', X.shape, y.shape)
    print('nan in X      ', bool(np.isnan(X).any()))
    const = [i for i in range(X.shape[1]) if np.std(X[:, i]) == 0]
    print('constant cols ', const)
    counts = np.bincount(y, minlength=n_classes)
    print('class counts  ', counts)
    print('expected loss at init ~', round(float(np.log(n_classes)), 4))

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 5)); X[:, 2] = 1.0     # planted constant column
sanity_report(X, rng.integers(0, 3, 200), 3)
```

**Yaad rakho:** Initialisation par expected cross-entropy ln(n_classes) hoti hai. Alag value matlab wiring bug.

**Aam galti:** Do din hyperparameters tune karna aise pipeline par jiske labels ek row se shift the.

Practice: `examples/01_overfit_a_single_batch_first.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Check loss at initialisation

### Aasaan Bhasha

Debug ek tay kram me karo, sabse sasta test pehle. Kya model 20 rows par zero loss tak overfit kar sakta hai? Nahi, to bug data ya wiring me hai, capacity me nahi. Kya step zero par loss wahi hai jo random guessing se aana chahiye? Nahi, to labels ya output layer galat hai.

### Chhota code

```python
import numpy as np

def sanity_report(X, y, n_classes):
    print('shapes        ', X.shape, y.shape)
    print('nan in X      ', bool(np.isnan(X).any()))
    const = [i for i in range(X.shape[1]) if np.std(X[:, i]) == 0]
    print('constant cols ', const)
    counts = np.bincount(y, minlength=n_classes)
    print('class counts  ', counts)
    print('expected loss at init ~', round(float(np.log(n_classes)), 4))

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 5)); X[:, 2] = 1.0     # planted constant column
sanity_report(X, rng.integers(0, 3, 200), 3)
```

**Yaad rakho:** Initialisation par expected cross-entropy ln(n_classes) hoti hai. Alag value matlab wiring bug.

**Aam galti:** Do din hyperparameters tune karna aise pipeline par jiske labels ek row se shift the.

Practice: `examples/02_check_loss_at_initialisation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Verify the data reaching the model

### Aasaan Bhasha

Aaj ka idea — **Verify the data reaching the model** — Debugging neural networks ke theme ke andar aata hai. Ise trivia nahi, ek tool ki tarah padho: ye kaam kya karta hai, aapke data ke baare me kya maan kar chalta hai, aur wo maanyata jhooth nikle to kya tootta hai?

### Chhota code

```python
# Explore: Verify the data reaching the model
print("practice: Verify the data reaching the model")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Yaad rakho:** `Verify the data reaching the model` use karne se pehle ek assumption likho jo ye aapke data ke baare me maanta hai.

**Aam galti:** `Verify the data reaching the model` ko tutorial se copy-paste kar lena bina jaane ki wo kya maanta hai aur kab fail hota hai.

Practice: `examples/03_verify_the_data_reaching_the_model.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Shape errors and how to read them

### Aasaan Bhasha

Agar aap decision samjha nahi sakte, to aap use defend bhi nahi kar sakte — aur credit, hiring aur healthcare me ye legally zaroori hai. Permutation importance model-agnostic aur imaandaar hai. SHAP per-prediction attributions deta hai theoretical base ke saath par sach me compute maangta hai.

### Chhota code

```python
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

X, y = load_breast_cancer(return_X_y=True)
names = load_breast_cancer().feature_names
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0)
m = RandomForestClassifier(n_estimators=200, random_state=0, n_jobs=-1).fit(Xtr, ytr)

imp = permutation_importance(m, Xte, yte, n_repeats=10, random_state=0)
for i in np.argsort(-imp.importances_mean)[:5]:
    print(f'{names[i]:<28} {imp.importances_mean[i]:.4f}')
```

**Yaad rakho:** TEST set par permutation importance batati hai ki generalise karne ke liye model kis par tik raha hai.

**Aam galti:** Importance ko causation ki tarah pesh karna — model ne correlation dhoonda hai, bas.

Practice: `examples/04_shape_errors_and_how_to_read_them.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. NaN loss: causes and fixes

### Aasaan Bhasha

Missing data information hai, sirf noise nahi. Kuch bharne se pehle poochho ki **kyun** missing hai: jo sensor sirf load par fail hota hai wo randomly missing nahi hai. Phir chuno: rows drop, column drop, statistic se fill, ya ek explicit 'ye missing tha' indicator column.

### Chhota code

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'age': [25, np.nan, 40, np.nan]})
print(df.isna().sum())

df['age_missing'] = df['age'].isna().astype(int)   # keep the signal
df['age'] = df['age'].fillna(df['age'].median())    # then fill
print(df)
```

**Yaad rakho:** Fill karne wali statistic sirf TRAIN split par nikalo, phir test par lagao.

**Aam galti:** Poore dataset ke mean se fill karna — ye test ki information training me leak kar deta hai.

Practice: `examples/05_nan_loss_causes_and_fixes.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Exploding and vanishing gradients

### Aasaan Bhasha

Derivative batata hai: input ko thoda hilaun to output kitna hilega? Gradient ye jawab ek saath har input ke liye deta hai, isliye wo chadhaai ki taraf point karta hai. Training gradient ke ulte chal kar neeche utarti hai. Chain rule hi wo cheez hai jo ye jawab layers ke poore stack me pahuchata hai.

### Chhota code

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

**Yaad rakho:** Central difference `(f(x+h)-f(x-h))/2h` haath se likhe gradient ko check karne ka sabse sasta tarika hai.

**Aam galti:** Aise derivation par bharosa karna jise aapne kabhi gradient-check nahi kiya; sign ki galti train dheere karti hai, saaf fail nahi hoti.

Practice: `examples/06_exploding_and_vanishing_gradients.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Learning rate diagnosis from the curve

### Aasaan Bhasha

Gradient descent baar-baar gradient ke ulte kadam rakhta hai. Full-batch stable par dheema; stochastic shor wala par chhote gaddhon se nikal jaata hai; mini-batch practical beech ka raasta hai. Learning rate wo ek knob hai jise aap sabse zyada ghumaoge.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
X = rng.normal(size=(1000, 3))
true_w = np.array([1.0, -2.0, 0.5])
y = X @ true_w + rng.normal(scale=0.1, size=1000)

w, lr, batch = np.zeros(3), 0.1, 32
for epoch in range(20):
    idx = rng.permutation(len(X))
    for start in range(0, len(X), batch):
        b = idx[start:start + batch]
        grad = 2 * X[b].T @ (X[b] @ w - y[b]) / len(b)
        w -= lr * grad
print('learned', np.round(w, 3), 'target', true_w)
```

**Yaad rakho:** Har epoch shuffle karo, warna model aapki file ka order seekh lega.

**Aam galti:** Learning rate ko hamesha fix rakhna, loss plateau hone par use decay na karna.

Practice: `examples/07_learning_rate_diagnosis_from_the_curve.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Dead ReLU detection

### Aasaan Bhasha

ReLU default hai: sasta, aur positive inputs par saturate nahi hota. Sigmoid aur tanh fixed range me dabate hain aur extremes par gradients maar dete hain. GELU/SiLU smooth ReLU hain jo transformers me use hote hain. Softmax scores ke vector ko probability distribution bana deta hai.

### Chhota code

```python
import numpy as np

def softmax(z):
    z = z - z.max(axis=-1, keepdims=True)   # subtract max for numerical stability
    e = np.exp(z)
    return e / e.sum(axis=-1, keepdims=True)

logits = np.array([2.0, 1.0, 0.1])
print('softmax', softmax(logits).round(4), 'sums to', softmax(logits).sum())
print('relu   ', np.maximum(0, np.array([-1.0, 0.0, 2.0])))
```

**Yaad rakho:** Softmax me `exp` se pehle hamesha max ghatao, warna bade logits inf/NaN me overflow kar jaate hain.

**Aam galti:** Aakhri layer par softmax lagana AUR aisa loss use karna jo andar khud softmax lagata hai.

Practice: `examples/08_dead_relu_detection.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Comparing against a simple baseline

### Aasaan Bhasha

Aaj ka idea — **Comparing against a simple baseline** — Debugging neural networks ke theme ke andar aata hai. Ise trivia nahi, ek tool ki tarah padho: ye kaam kya karta hai, aapke data ke baare me kya maan kar chalta hai, aur wo maanyata jhooth nikle to kya tootta hai?

### Chhota code

```python
# Explore: Comparing against a simple baseline
print("practice: Comparing against a simple baseline")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Yaad rakho:** `Comparing against a simple baseline` use karne se pehle ek assumption likho jo ye aapke data ke baare me maanta hai.

**Aam galti:** `Comparing against a simple baseline` ko tutorial se copy-paste kar lena bina jaane ki wo kya maanta hai aur kab fail hota hai.

Practice: `examples/09_comparing_against_a_simple_baseline.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. A deep learning debugging checklist

### Aasaan Bhasha

Debug ek tay kram me karo, sabse sasta test pehle. Kya model 20 rows par zero loss tak overfit kar sakta hai? Nahi, to bug data ya wiring me hai, capacity me nahi. Kya step zero par loss wahi hai jo random guessing se aana chahiye? Nahi, to labels ya output layer galat hai.

### Chhota code

```python
import numpy as np

def sanity_report(X, y, n_classes):
    print('shapes        ', X.shape, y.shape)
    print('nan in X      ', bool(np.isnan(X).any()))
    const = [i for i in range(X.shape[1]) if np.std(X[:, i]) == 0]
    print('constant cols ', const)
    counts = np.bincount(y, minlength=n_classes)
    print('class counts  ', counts)
    print('expected loss at init ~', round(float(np.log(n_classes)), 4))

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 5)); X[:, 2] = 1.0     # planted constant column
sanity_report(X, rng.integers(0, 3, 200), 3)
```

**Yaad rakho:** Initialisation par expected cross-entropy ln(n_classes) hoti hai. Alag value matlab wiring bug.

**Aam galti:** Do din hyperparameters tune karna aise pipeline par jiske labels ek row se shift the.

Practice: `examples/10_a_deep_learning_debugging_checklist.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 87 ke baad aapko ye aana chahiye

- **Overfit a single batch first** ko bina notes dekhe kisi dost ko samjha sakna.
- **Check loss at initialisation** ko bina notes dekhe kisi dost ko samjha sakna.
- **Verify the data reaching the model** ko bina notes dekhe kisi dost ko samjha sakna.
- **Shape errors and how to read them** ko bina notes dekhe kisi dost ko samjha sakna.
- **NaN loss: causes and fixes** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
