# Day 31 — Linear models, mathematically

Aaj ka goal: **Linear models, mathematically** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | The linear model equation |
| 2 | Least squares as a projection |
| 3 | Deriving the normal equations |
| 4 | Gradient descent solution |
| 5 | Adding a bias term correctly |
| 6 | Polynomial features |
| 7 | Multicollinearity and its symptoms |
| 8 | Ridge as constrained least squares |
| 9 | Lasso and sparsity geometry |
| 10 | Interpreting coefficients honestly |

---

## 1. The linear model equation

### Aasaan Bhasha

Aaj ka idea — **The linear model equation** — Linear models, mathematically ke theme ke andar aata hai. Ise trivia nahi, ek tool ki tarah padho: ye kaam kya karta hai, aapke data ke baare me kya maan kar chalta hai, aur wo maanyata jhooth nikle to kya tootta hai?

### Chhota code

```python
# Explore: The linear model equation
print("practice: The linear model equation")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Yaad rakho:** `The linear model equation` use karne se pehle ek assumption likho jo ye aapke data ke baare me maanta hai.

**Aam galti:** `The linear model equation` ko tutorial se copy-paste kar lena bina jaane ki wo kya maanta hai aur kab fail hota hai.

Practice: `examples/01_the_linear_model_equation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Least squares as a projection

### Aasaan Bhasha

Linear regression squared error minimise karke seedhi line fit karta hai. Ye har regression problem ka imaandaar baseline hai: tez, samajhne layak, aur wahi cheez jise aapke fancy model ko harana padega tabhi wo apni complexity kamata hai.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 1))
y = 3.0 * X[:, 0] + 2.0 + rng.normal(scale=0.5, size=200)

Xb = np.c_[np.ones(len(X)), X]                 # add bias column
w = np.linalg.lstsq(Xb, y, rcond=None)[0]      # solves the normal equations safely
print(f'intercept {w[0]:.3f}  slope {w[1]:.3f}')

resid = y - Xb @ w
print('residual mean (should be ~0):', round(float(resid.mean()), 6))
```

**Yaad rakho:** Predictions ke saamne residuals plot karo — koi bhi dikhne wala pattern matlab linear form galat hai.

**Aam galti:** Training data ka R² report karke use model performance bata dena.

Practice: `examples/02_least_squares_as_a_projection.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Deriving the normal equations

### Aasaan Bhasha

Vector numbers ki list hai jiski ek direction aur lambai hoti hai. Dot product alignment naapta hai: same direction par bada positive, perpendicular par zero. Cosine similarity wahi dot product hai lambai hata kar — isliye wo alag-alag magnitude ke embeddings ko theek se compare karta hai.

### Chhota code

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 4.0, 6.0])

print('dot   ', a @ b)
print('norm  ', np.linalg.norm(a))
cos = (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))
print('cosine', cos)   # 1.0 -> same direction
```

**Yaad rakho:** Cosine similarity magnitude ignore karti hai; Euclidean distance nahi. Apne sawaal ke hisaab se chuno.

**Aam galti:** Raw embeddings ko Euclidean distance se compare karna jab sirf direction ka matlab hai.

Practice: `examples/03_deriving_the_normal_equations.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Gradient descent solution

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

Practice: `examples/04_gradient_descent_solution.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Adding a bias term correctly

### Aasaan Bhasha

Models apne training data ka bias seekh lete hain aur phir use objectivity ke mulamme ke saath scale par lagu karte hain. Har group ke error rates naapo, sirf overall nahi. Fairness ki definitions ek doosre se sach me takraati hain — aapko ek explicitly chunni padegi aur wajah likhni padegi.

### Chhota code

```python
import numpy as np
import pandas as pd

df = pd.DataFrame({
    'group': ['a'] * 100 + ['b'] * 100,
    'y':     [1] * 50 + [0] * 50 + [1] * 50 + [0] * 50,
    'pred':  [1] * 45 + [0] * 55 + [1] * 30 + [0] * 70,
})
for g, sub in df.groupby('group'):
    tpr = ((sub.pred == 1) & (sub.y == 1)).sum() / max((sub.y == 1).sum(), 1)
    rate = (sub.pred == 1).mean()
    print(f'group {g}: selection rate {rate:.2f}  recall {tpr:.2f}')
print('Large gaps here are the finding — investigate before shipping.')
```

**Yaad rakho:** Sensitive attribute hataane se bias nahi jaata; proxies (pincode, naam) use wapas le aate hain.

**Aam galti:** Fairness ka audit sirf launch par ek baar karna aur data drift hone par dobara kabhi nahi.

Practice: `examples/05_adding_a_bias_term_correctly.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Polynomial features

### Aasaan Bhasha

Aaj ka idea — **Polynomial features** — Linear models, mathematically ke theme ke andar aata hai. Ise trivia nahi, ek tool ki tarah padho: ye kaam kya karta hai, aapke data ke baare me kya maan kar chalta hai, aur wo maanyata jhooth nikle to kya tootta hai?

### Chhota code

```python
# Explore: Polynomial features
print("practice: Polynomial features")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Yaad rakho:** `Polynomial features` use karne se pehle ek assumption likho jo ye aapke data ke baare me maanta hai.

**Aam galti:** `Polynomial features` ko tutorial se copy-paste kar lena bina jaane ki wo kya maanta hai aur kab fail hota hai.

Practice: `examples/06_polynomial_features.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Multicollinearity and its symptoms

### Aasaan Bhasha

Aaj ka idea — **Multicollinearity and its symptoms** — Linear models, mathematically ke theme ke andar aata hai. Ise trivia nahi, ek tool ki tarah padho: ye kaam kya karta hai, aapke data ke baare me kya maan kar chalta hai, aur wo maanyata jhooth nikle to kya tootta hai?

### Chhota code

```python
# Explore: Multicollinearity and its symptoms
print("practice: Multicollinearity and its symptoms")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Yaad rakho:** `Multicollinearity and its symptoms` use karne se pehle ek assumption likho jo ye aapke data ke baare me maanta hai.

**Aam galti:** `Multicollinearity and its symptoms` ko tutorial se copy-paste kar lena bina jaane ki wo kya maanta hai aur kab fail hota hai.

Practice: `examples/07_multicollinearity_and_its_symptoms.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Ridge as constrained least squares

### Aasaan Bhasha

Linear regression squared error minimise karke seedhi line fit karta hai. Ye har regression problem ka imaandaar baseline hai: tez, samajhne layak, aur wahi cheez jise aapke fancy model ko harana padega tabhi wo apni complexity kamata hai.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 1))
y = 3.0 * X[:, 0] + 2.0 + rng.normal(scale=0.5, size=200)

Xb = np.c_[np.ones(len(X)), X]                 # add bias column
w = np.linalg.lstsq(Xb, y, rcond=None)[0]      # solves the normal equations safely
print(f'intercept {w[0]:.3f}  slope {w[1]:.3f}')

resid = y - Xb @ w
print('residual mean (should be ~0):', round(float(resid.mean()), 6))
```

**Yaad rakho:** Predictions ke saamne residuals plot karo — koi bhi dikhne wala pattern matlab linear form galat hai.

**Aam galti:** Training data ka R² report karke use model performance bata dena.

Practice: `examples/08_ridge_as_constrained_least_squares.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Lasso and sparsity geometry

### Aasaan Bhasha

Regularisation bade weights par penalty lagata hai taaki model simple explanation pasand kare. L2 (ridge) sab kuch smoothly chhota karta hai; L1 (lasso) kuch weights ko bilkul zero kar deta hai aur isi tarah features chunta hai. Elastic net dono milata hai.

### Chhota code

```python
import numpy as np
from sklearn.linear_model import Ridge, Lasso
from sklearn.datasets import make_regression

X, y = make_regression(n_samples=200, n_features=20, n_informative=5, noise=10, random_state=0)

ridge = Ridge(alpha=1.0).fit(X, y)
lasso = Lasso(alpha=1.0).fit(X, y)
print('ridge non-zero coefs', int(np.sum(np.abs(ridge.coef_) > 1e-6)))
print('lasso non-zero coefs', int(np.sum(np.abs(lasso.coef_) > 1e-6)))
```

**Yaad rakho:** Regularise karne se pehle features scale karo, warna penalty usi column ko sazaa deta hai jiski units chhoti hain.

**Aam galti:** Test set par `alpha` tune karna — use sirf train par cross-validation se chuno.

Practice: `examples/09_lasso_and_sparsity_geometry.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Interpreting coefficients honestly

### Aasaan Bhasha

ML code ko baaki code jaise tests chahiye, plus data tests: schema, ranges, null rates, class balance. Har known failure mode ke liye ek behavioural test jodo — ek test jo pichhli baar ka outage pakad leta, wo 90% coverage se zyada keemti hai.

### Chhota code

```python
import numpy as np

def preprocess(x):
    x = np.asarray(x, dtype=float)
    if np.isnan(x).any():
        raise ValueError('NaN in input')
    return (x - x.mean()) / (x.std() + 1e-8)

def test_preprocess():
    out = preprocess([1.0, 2.0, 3.0])
    assert abs(float(out.mean())) < 1e-6, 'should be zero-centred'
    assert abs(float(out.std()) - 1.0) < 1e-6, 'should be unit variance'
    try:
        preprocess([1.0, float('nan')])
    except ValueError:
        pass
    else:
        raise AssertionError('NaN should have raised')
    print('ok')

test_preprocess()
```

**Yaad rakho:** Data contract test karo, sirf function nahi — kharab data kharab code se zyada models todta hai.

**Aam galti:** Sirf happy path test karna, jisse poora-null column chupchap constant model train kar deta hai.

Practice: `examples/10_interpreting_coefficients_honestly.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 31 ke baad aapko ye aana chahiye

- **The linear model equation** ko bina notes dekhe kisi dost ko samjha sakna.
- **Least squares as a projection** ko bina notes dekhe kisi dost ko samjha sakna.
- **Deriving the normal equations** ko bina notes dekhe kisi dost ko samjha sakna.
- **Gradient descent solution** ko bina notes dekhe kisi dost ko samjha sakna.
- **Adding a bias term correctly** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
