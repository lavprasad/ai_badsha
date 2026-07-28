# Day 32 — Logistic regression, mathematically

Aaj ka goal: **Logistic regression, mathematically** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | From linear score to probability |
| 2 | The sigmoid and the logit |
| 3 | Odds and log-odds interpretation |
| 4 | Maximum likelihood for Bernoulli data |
| 5 | Deriving the cross-entropy loss |
| 6 | The gradient of logistic loss |
| 7 | Decision boundaries |
| 8 | Multiclass with softmax |
| 9 | Regularised logistic regression |
| 10 | Implementing it from scratch |

---

## 1. From linear score to probability

### Aasaan Bhasha

Bayes rule evidence ke saath belief update karta hai: posterior = likelihood x prior / evidence. Applied ML ki sabse common galti prior ignore karna hai — 10000 me 1 wali bimari ke liye 99% accurate test bhi zyadatar false positives hi deta hai.

### Chhota code

```python
prior = 1 / 10_000          # base rate of the disease
sensitivity = 0.99          # P(positive | sick)
false_positive = 0.01       # P(positive | healthy)

evidence = sensitivity * prior + false_positive * (1 - prior)
posterior = sensitivity * prior / evidence
print(f'P(sick | positive) = {posterior:.4f}')   # ~0.0098
```

**Yaad rakho:** Rare events par precision gir hi jaati hai, chahe classifier accuracy par kitna bhi accha lage.

**Aam galti:** Imbalanced problem par accuracy report karna jahan hamesha 'no' bolne se 99% mil jaata hai.

Practice: `examples/01_from_linear_score_to_probability.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. The sigmoid and the logit

### Aasaan Bhasha

Logistic regression linear score ko sigmoid se dabaa kar probability banata hai. Coefficients log-odds hain: +0.7 matlab odds lagbhag double. Jahan decision regulator ko samjhana pade, wahan aaj bhi yahi default hai.

### Chhota code

```python
import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-np.clip(z, -500, 500)))

rng = np.random.default_rng(0)
X = rng.normal(size=(400, 2))
y = (X[:, 0] + X[:, 1] > 0).astype(float)

w, b, lr = np.zeros(2), 0.0, 0.5
for _ in range(500):
    p = sigmoid(X @ w + b)
    w -= lr * (X.T @ (p - y)) / len(y)
    b -= lr * float((p - y).mean())
print('weights', np.round(w, 2), 'acc', ((sigmoid(X @ w + b) > 0.5) == y).mean())
```

**Yaad rakho:** Sigmoid ka input clip karo — bade negative number ka `exp` overflow hokar NaN de deta hai.

**Aam galti:** Raw output ko calibrated probability maan lena bina kabhi calibration curve dekhe.

Practice: `examples/02_the_sigmoid_and_the_logit.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Odds and log-odds interpretation

### Aasaan Bhasha

Logistic regression linear score ko sigmoid se dabaa kar probability banata hai. Coefficients log-odds hain: +0.7 matlab odds lagbhag double. Jahan decision regulator ko samjhana pade, wahan aaj bhi yahi default hai.

### Chhota code

```python
import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-np.clip(z, -500, 500)))

rng = np.random.default_rng(0)
X = rng.normal(size=(400, 2))
y = (X[:, 0] + X[:, 1] > 0).astype(float)

w, b, lr = np.zeros(2), 0.0, 0.5
for _ in range(500):
    p = sigmoid(X @ w + b)
    w -= lr * (X.T @ (p - y)) / len(y)
    b -= lr * float((p - y).mean())
print('weights', np.round(w, 2), 'acc', ((sigmoid(X @ w + b) > 0.5) == y).mean())
```

**Yaad rakho:** Sigmoid ka input clip karo — bade negative number ka `exp` overflow hokar NaN de deta hai.

**Aam galti:** Raw output ko calibrated probability maan lena bina kabhi calibration curve dekhe.

Practice: `examples/03_odds_and_log_odds_interpretation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Maximum likelihood for Bernoulli data

### Aasaan Bhasha

Bayes rule evidence ke saath belief update karta hai: posterior = likelihood x prior / evidence. Applied ML ki sabse common galti prior ignore karna hai — 10000 me 1 wali bimari ke liye 99% accurate test bhi zyadatar false positives hi deta hai.

### Chhota code

```python
prior = 1 / 10_000          # base rate of the disease
sensitivity = 0.99          # P(positive | sick)
false_positive = 0.01       # P(positive | healthy)

evidence = sensitivity * prior + false_positive * (1 - prior)
posterior = sensitivity * prior / evidence
print(f'P(sick | positive) = {posterior:.4f}')   # ~0.0098
```

**Yaad rakho:** Rare events par precision gir hi jaati hai, chahe classifier accuracy par kitna bhi accha lage.

**Aam galti:** Imbalanced problem par accuracy report karna jahan hamesha 'no' bolne se 99% mil jaata hai.

Practice: `examples/04_maximum_likelihood_for_bernoulli_data.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Deriving the cross-entropy loss

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

Practice: `examples/05_deriving_the_cross_entropy_loss.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. The gradient of logistic loss

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

Practice: `examples/06_the_gradient_of_logistic_loss.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Decision boundaries

### Aasaan Bhasha

Logistic regression linear score ko sigmoid se dabaa kar probability banata hai. Coefficients log-odds hain: +0.7 matlab odds lagbhag double. Jahan decision regulator ko samjhana pade, wahan aaj bhi yahi default hai.

### Chhota code

```python
import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-np.clip(z, -500, 500)))

rng = np.random.default_rng(0)
X = rng.normal(size=(400, 2))
y = (X[:, 0] + X[:, 1] > 0).astype(float)

w, b, lr = np.zeros(2), 0.0, 0.5
for _ in range(500):
    p = sigmoid(X @ w + b)
    w -= lr * (X.T @ (p - y)) / len(y)
    b -= lr * float((p - y).mean())
print('weights', np.round(w, 2), 'acc', ((sigmoid(X @ w + b) > 0.5) == y).mean())
```

**Yaad rakho:** Sigmoid ka input clip karo — bade negative number ka `exp` overflow hokar NaN de deta hai.

**Aam galti:** Raw output ko calibrated probability maan lena bina kabhi calibration curve dekhe.

Practice: `examples/07_decision_boundaries.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Multiclass with softmax

### Aasaan Bhasha

Logistic regression linear score ko sigmoid se dabaa kar probability banata hai. Coefficients log-odds hain: +0.7 matlab odds lagbhag double. Jahan decision regulator ko samjhana pade, wahan aaj bhi yahi default hai.

### Chhota code

```python
import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-np.clip(z, -500, 500)))

rng = np.random.default_rng(0)
X = rng.normal(size=(400, 2))
y = (X[:, 0] + X[:, 1] > 0).astype(float)

w, b, lr = np.zeros(2), 0.0, 0.5
for _ in range(500):
    p = sigmoid(X @ w + b)
    w -= lr * (X.T @ (p - y)) / len(y)
    b -= lr * float((p - y).mean())
print('weights', np.round(w, 2), 'acc', ((sigmoid(X @ w + b) > 0.5) == y).mean())
```

**Yaad rakho:** Sigmoid ka input clip karo — bade negative number ka `exp` overflow hokar NaN de deta hai.

**Aam galti:** Raw output ko calibrated probability maan lena bina kabhi calibration curve dekhe.

Practice: `examples/08_multiclass_with_softmax.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Regularised logistic regression

### Aasaan Bhasha

Logistic regression linear score ko sigmoid se dabaa kar probability banata hai. Coefficients log-odds hain: +0.7 matlab odds lagbhag double. Jahan decision regulator ko samjhana pade, wahan aaj bhi yahi default hai.

### Chhota code

```python
import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-np.clip(z, -500, 500)))

rng = np.random.default_rng(0)
X = rng.normal(size=(400, 2))
y = (X[:, 0] + X[:, 1] > 0).astype(float)

w, b, lr = np.zeros(2), 0.0, 0.5
for _ in range(500):
    p = sigmoid(X @ w + b)
    w -= lr * (X.T @ (p - y)) / len(y)
    b -= lr * float((p - y).mean())
print('weights', np.round(w, 2), 'acc', ((sigmoid(X @ w + b) > 0.5) == y).mean())
```

**Yaad rakho:** Sigmoid ka input clip karo — bade negative number ka `exp` overflow hokar NaN de deta hai.

**Aam galti:** Raw output ko calibrated probability maan lena bina kabhi calibration curve dekhe.

Practice: `examples/09_regularised_logistic_regression.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Implementing it from scratch

### Aasaan Bhasha

Logistic regression linear score ko sigmoid se dabaa kar probability banata hai. Coefficients log-odds hain: +0.7 matlab odds lagbhag double. Jahan decision regulator ko samjhana pade, wahan aaj bhi yahi default hai.

### Chhota code

```python
import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-np.clip(z, -500, 500)))

rng = np.random.default_rng(0)
X = rng.normal(size=(400, 2))
y = (X[:, 0] + X[:, 1] > 0).astype(float)

w, b, lr = np.zeros(2), 0.0, 0.5
for _ in range(500):
    p = sigmoid(X @ w + b)
    w -= lr * (X.T @ (p - y)) / len(y)
    b -= lr * float((p - y).mean())
print('weights', np.round(w, 2), 'acc', ((sigmoid(X @ w + b) > 0.5) == y).mean())
```

**Yaad rakho:** Sigmoid ka input clip karo — bade negative number ka `exp` overflow hokar NaN de deta hai.

**Aam galti:** Raw output ko calibrated probability maan lena bina kabhi calibration curve dekhe.

Practice: `examples/10_implementing_it_from_scratch.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 32 ke baad aapko ye aana chahiye

- **From linear score to probability** ko bina notes dekhe kisi dost ko samjha sakna.
- **The sigmoid and the logit** ko bina notes dekhe kisi dost ko samjha sakna.
- **Odds and log-odds interpretation** ko bina notes dekhe kisi dost ko samjha sakna.
- **Maximum likelihood for Bernoulli data** ko bina notes dekhe kisi dost ko samjha sakna.
- **Deriving the cross-entropy loss** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
