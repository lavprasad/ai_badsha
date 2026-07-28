# Day 29 — Numerical computing pitfalls

Aaj ka goal: **Numerical computing pitfalls** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Floating point representation |
| 2 | Catastrophic cancellation |
| 3 | Overflow and underflow |
| 4 | The log-sum-exp trick |
| 5 | Epsilon in denominators |
| 6 | NaN propagation and how to find the source |
| 7 | Deterministic seeds vs true randomness |
| 8 | Reproducibility across hardware |
| 9 | Numerical gradient checking |
| 10 | Debugging a silently wrong computation |

---

## 1. Floating point representation

### Aasaan Bhasha

Floats approximations hain. Do lagbhag barabar numbers ghatane se precision khatm ho jaati hai; bade numbers ka exponent inf me overflow karta hai; bahut chhote number se divide karna phat jaata hai. Log-sum-exp trick aur denominator me chhota epsilon — yahi do fixes aap baar-baar use karoge.

### Chhota code

```python
import numpy as np

print(0.1 + 0.2 == 0.3, 0.1 + 0.2)          # False — welcome to floats

def logsumexp(x):
    m = np.max(x)
    return m + np.log(np.sum(np.exp(x - m)))   # never exp() a big number directly

big = np.array([1000.0, 1001.0, 1002.0])
print('naive :', np.log(np.sum(np.exp(big))))  # inf
print('stable:', logsumexp(big))

def safe_ratio(a, b, eps=1e-12):
    return a / (b + eps)
print(safe_ratio(1.0, 0.0))
```

**Yaad rakho:** Floats ko tolerance se compare karo (`np.isclose`), `==` se kabhi nahi.

**Aam galti:** Training me gehre andar `nan` milna aur tab pata chalna ki baarah steps pehle ek `exp()` overflow ho gaya tha.

Practice: `examples/01_floating_point_representation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Catastrophic cancellation

### Aasaan Bhasha

Floats approximations hain. Do lagbhag barabar numbers ghatane se precision khatm ho jaati hai; bade numbers ka exponent inf me overflow karta hai; bahut chhote number se divide karna phat jaata hai. Log-sum-exp trick aur denominator me chhota epsilon — yahi do fixes aap baar-baar use karoge.

### Chhota code

```python
import numpy as np

print(0.1 + 0.2 == 0.3, 0.1 + 0.2)          # False — welcome to floats

def logsumexp(x):
    m = np.max(x)
    return m + np.log(np.sum(np.exp(x - m)))   # never exp() a big number directly

big = np.array([1000.0, 1001.0, 1002.0])
print('naive :', np.log(np.sum(np.exp(big))))  # inf
print('stable:', logsumexp(big))

def safe_ratio(a, b, eps=1e-12):
    return a / (b + eps)
print(safe_ratio(1.0, 0.0))
```

**Yaad rakho:** Floats ko tolerance se compare karo (`np.isclose`), `==` se kabhi nahi.

**Aam galti:** Training me gehre andar `nan` milna aur tab pata chalna ki baarah steps pehle ek `exp()` overflow ho gaya tha.

Practice: `examples/02_catastrophic_cancellation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Overflow and underflow

### Aasaan Bhasha

Floats approximations hain. Do lagbhag barabar numbers ghatane se precision khatm ho jaati hai; bade numbers ka exponent inf me overflow karta hai; bahut chhote number se divide karna phat jaata hai. Log-sum-exp trick aur denominator me chhota epsilon — yahi do fixes aap baar-baar use karoge.

### Chhota code

```python
import numpy as np

print(0.1 + 0.2 == 0.3, 0.1 + 0.2)          # False — welcome to floats

def logsumexp(x):
    m = np.max(x)
    return m + np.log(np.sum(np.exp(x - m)))   # never exp() a big number directly

big = np.array([1000.0, 1001.0, 1002.0])
print('naive :', np.log(np.sum(np.exp(big))))  # inf
print('stable:', logsumexp(big))

def safe_ratio(a, b, eps=1e-12):
    return a / (b + eps)
print(safe_ratio(1.0, 0.0))
```

**Yaad rakho:** Floats ko tolerance se compare karo (`np.isclose`), `==` se kabhi nahi.

**Aam galti:** Training me gehre andar `nan` milna aur tab pata chalna ki baarah steps pehle ek `exp()` overflow ho gaya tha.

Practice: `examples/03_overflow_and_underflow.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. The log-sum-exp trick

### Aasaan Bhasha

Floats approximations hain. Do lagbhag barabar numbers ghatane se precision khatm ho jaati hai; bade numbers ka exponent inf me overflow karta hai; bahut chhote number se divide karna phat jaata hai. Log-sum-exp trick aur denominator me chhota epsilon — yahi do fixes aap baar-baar use karoge.

### Chhota code

```python
import numpy as np

print(0.1 + 0.2 == 0.3, 0.1 + 0.2)          # False — welcome to floats

def logsumexp(x):
    m = np.max(x)
    return m + np.log(np.sum(np.exp(x - m)))   # never exp() a big number directly

big = np.array([1000.0, 1001.0, 1002.0])
print('naive :', np.log(np.sum(np.exp(big))))  # inf
print('stable:', logsumexp(big))

def safe_ratio(a, b, eps=1e-12):
    return a / (b + eps)
print(safe_ratio(1.0, 0.0))
```

**Yaad rakho:** Floats ko tolerance se compare karo (`np.isclose`), `==` se kabhi nahi.

**Aam galti:** Training me gehre andar `nan` milna aur tab pata chalna ki baarah steps pehle ek `exp()` overflow ho gaya tha.

Practice: `examples/04_the_log_sum_exp_trick.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Epsilon in denominators

### Aasaan Bhasha

Floats approximations hain. Do lagbhag barabar numbers ghatane se precision khatm ho jaati hai; bade numbers ka exponent inf me overflow karta hai; bahut chhote number se divide karna phat jaata hai. Log-sum-exp trick aur denominator me chhota epsilon — yahi do fixes aap baar-baar use karoge.

### Chhota code

```python
import numpy as np

print(0.1 + 0.2 == 0.3, 0.1 + 0.2)          # False — welcome to floats

def logsumexp(x):
    m = np.max(x)
    return m + np.log(np.sum(np.exp(x - m)))   # never exp() a big number directly

big = np.array([1000.0, 1001.0, 1002.0])
print('naive :', np.log(np.sum(np.exp(big))))  # inf
print('stable:', logsumexp(big))

def safe_ratio(a, b, eps=1e-12):
    return a / (b + eps)
print(safe_ratio(1.0, 0.0))
```

**Yaad rakho:** Floats ko tolerance se compare karo (`np.isclose`), `==` se kabhi nahi.

**Aam galti:** Training me gehre andar `nan` milna aur tab pata chalna ki baarah steps pehle ek `exp()` overflow ho gaya tha.

Practice: `examples/05_epsilon_in_denominators.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. NaN propagation and how to find the source

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

Practice: `examples/06_nan_propagation_and_how_to_find_the_sour.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Deterministic seeds vs true randomness

### Aasaan Bhasha

Floats approximations hain. Do lagbhag barabar numbers ghatane se precision khatm ho jaati hai; bade numbers ka exponent inf me overflow karta hai; bahut chhote number se divide karna phat jaata hai. Log-sum-exp trick aur denominator me chhota epsilon — yahi do fixes aap baar-baar use karoge.

### Chhota code

```python
import numpy as np

print(0.1 + 0.2 == 0.3, 0.1 + 0.2)          # False — welcome to floats

def logsumexp(x):
    m = np.max(x)
    return m + np.log(np.sum(np.exp(x - m)))   # never exp() a big number directly

big = np.array([1000.0, 1001.0, 1002.0])
print('naive :', np.log(np.sum(np.exp(big))))  # inf
print('stable:', logsumexp(big))

def safe_ratio(a, b, eps=1e-12):
    return a / (b + eps)
print(safe_ratio(1.0, 0.0))
```

**Yaad rakho:** Floats ko tolerance se compare karo (`np.isclose`), `==` se kabhi nahi.

**Aam galti:** Training me gehre andar `nan` milna aur tab pata chalna ki baarah steps pehle ek `exp()` overflow ho gaya tha.

Practice: `examples/07_deterministic_seeds_vs_true_randomness.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Reproducibility across hardware

### Aasaan Bhasha

Jo experiment aap dobara nahi bana sakte wo kissa hai. Har run ke liye track karo: code commit, data version, hyperparameters, metrics aur artefact. Chhe mahine baad 'production wala model kis run se aaya' ka jawab hona hi chahiye.

### Chhota code

```python
import json, hashlib, subprocess

def run_record(params, metrics, data_path=None):
    try:
        commit = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'], text=True).strip()
    except Exception:
        commit = 'unknown'
    return {
        'commit': commit,
        'params': params,
        'metrics': metrics,
        'data_sha': hashlib.sha256((data_path or 'none').encode()).hexdigest()[:12],
    }

print(json.dumps(run_record({'lr': 0.01, 'depth': 6}, {'auc': 0.912}, 'data/train.csv'), indent=2))
```

**Yaad rakho:** Code version ke saath data version bhi log karo — data chupchap badalta hai, code shor machaa kar.

**Aam galti:** Registry use karne ke bajaye files ko `model_final_v2_REAL_use_this.pkl` naam dena.

Practice: `examples/08_reproducibility_across_hardware.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Numerical gradient checking

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

Practice: `examples/09_numerical_gradient_checking.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Debugging a silently wrong computation

### Aasaan Bhasha

Floats approximations hain. Do lagbhag barabar numbers ghatane se precision khatm ho jaati hai; bade numbers ka exponent inf me overflow karta hai; bahut chhote number se divide karna phat jaata hai. Log-sum-exp trick aur denominator me chhota epsilon — yahi do fixes aap baar-baar use karoge.

### Chhota code

```python
import numpy as np

print(0.1 + 0.2 == 0.3, 0.1 + 0.2)          # False — welcome to floats

def logsumexp(x):
    m = np.max(x)
    return m + np.log(np.sum(np.exp(x - m)))   # never exp() a big number directly

big = np.array([1000.0, 1001.0, 1002.0])
print('naive :', np.log(np.sum(np.exp(big))))  # inf
print('stable:', logsumexp(big))

def safe_ratio(a, b, eps=1e-12):
    return a / (b + eps)
print(safe_ratio(1.0, 0.0))
```

**Yaad rakho:** Floats ko tolerance se compare karo (`np.isclose`), `==` se kabhi nahi.

**Aam galti:** Training me gehre andar `nan` milna aur tab pata chalna ki baarah steps pehle ek `exp()` overflow ho gaya tha.

Practice: `examples/10_debugging_a_silently_wrong_computation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 29 ke baad aapko ye aana chahiye

- **Floating point representation** ko bina notes dekhe kisi dost ko samjha sakna.
- **Catastrophic cancellation** ko bina notes dekhe kisi dost ko samjha sakna.
- **Overflow and underflow** ko bina notes dekhe kisi dost ko samjha sakna.
- **The log-sum-exp trick** ko bina notes dekhe kisi dost ko samjha sakna.
- **Epsilon in denominators** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
