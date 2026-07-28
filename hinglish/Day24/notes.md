# Day 24 — Inferential statistics

Aaj ka goal: **Inferential statistics** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Population vs sample |
| 2 | Sampling distributions and standard error |
| 3 | Confidence intervals |
| 4 | Null and alternative hypotheses |
| 5 | p-values and what they are not |
| 6 | t-test and chi-square test |
| 7 | Type I and Type II errors |
| 8 | Statistical power and sample size |
| 9 | Multiple comparisons and correction |
| 10 | Bootstrapping without formulas |

---

## 1. Population vs sample

### Aasaan Bhasha

Aap sample naapte ho aur population ke baare me daawa karna chahte ho. Type I error jhoothi cheekh hai; Type II asli effect chook jaana. Power ye chance hai ki aap di gayi size ka asli effect pakad paoge — ise data jama karne se pehle tay karo, warna aap aisa experiment chalaoge jo kabhi safal ho hi nahi sakta tha.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
a = rng.normal(10.0, 2.0, 60)
b = rng.normal(11.0, 2.0, 60)

# Welch t-statistic, no scipy needed
se = np.sqrt(a.var(ddof=1) / len(a) + b.var(ddof=1) / len(b))
t = (b.mean() - a.mean()) / se
print(f'mean diff {b.mean() - a.mean():.3f}  t = {t:.2f}')
print('|t| > 2 is roughly the 5% threshold at these sample sizes')

# Twenty independent tests at 5%: expect one false positive by chance alone
print('expected false positives in 20 tests:', 20 * 0.05)
```

**Yaad rakho:** 20 hypotheses ko p<0.05 par test karne se average ek false positive milta hi hai. Uske liye correction karo.

**Aam galti:** Baad me data ko pandrah tarah se kaat kar wahi ek slice report karna jo significant nikla.

Practice: `examples/01_population_vs_sample.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Sampling distributions and standard error

### Aasaan Bhasha

Distribution batati hai kaunsi values likely hain. Measurement noise ke liye Gaussian, haan/na ke liye Bernoulli, per-interval counts ke liye Poisson. Sahi distribution chunna hi apna loss function chunna hai: Gaussian likelihood se MSE aata hai, Bernoulli se cross-entropy.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
normal = rng.normal(loc=0, scale=1, size=10_000)
coin = rng.binomial(n=1, p=0.3, size=10_000)

print('normal mean/std', round(normal.mean(), 3), round(normal.std(), 3))
print('coin heads rate ', coin.mean())
```

**Yaad rakho:** Jab result dobara banana ho to RNG hamesha seed karo (`default_rng(0)`).

**Aam galti:** Skewed, bounded ya count data par Gaussian maan lena aur phir residuals dekh kar hairan hona.

Practice: `examples/02_sampling_distributions_and_standard_erro.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Confidence intervals

### Aasaan Bhasha

p-value matlab P(itna extreme data | kuch ho hi nahi raha). Ye ye nahi batata ki aapka idea sahi hai. Confidence interval zyada kaam ka hai kyunki wo effect size aur uncertainty saath dikhata hai — 'significant' 0.1% lift shayad ship karne layak hi na ho.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
control = rng.normal(10.0, 2.0, 500)
variant = rng.normal(10.3, 2.0, 500)

diff = variant.mean() - control.mean()
se = np.sqrt(control.var(ddof=1) / 500 + variant.var(ddof=1) / 500)
print(f'lift {diff:.3f}  95% CI [{diff - 1.96 * se:.3f}, {diff + 1.96 * se:.3f}]')
```

**Yaad rakho:** Sample size aur metric data dekhne se PEHLE decide karo.

**Aam galti:** Roz jhaank kar p < 0.05 hote hi test rok dena — isse false positives bahut badh jaate hain.

Practice: `examples/03_confidence_intervals.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Null and alternative hypotheses

### Aasaan Bhasha

Aap sample naapte ho aur population ke baare me daawa karna chahte ho. Type I error jhoothi cheekh hai; Type II asli effect chook jaana. Power ye chance hai ki aap di gayi size ka asli effect pakad paoge — ise data jama karne se pehle tay karo, warna aap aisa experiment chalaoge jo kabhi safal ho hi nahi sakta tha.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
a = rng.normal(10.0, 2.0, 60)
b = rng.normal(11.0, 2.0, 60)

# Welch t-statistic, no scipy needed
se = np.sqrt(a.var(ddof=1) / len(a) + b.var(ddof=1) / len(b))
t = (b.mean() - a.mean()) / se
print(f'mean diff {b.mean() - a.mean():.3f}  t = {t:.2f}')
print('|t| > 2 is roughly the 5% threshold at these sample sizes')

# Twenty independent tests at 5%: expect one false positive by chance alone
print('expected false positives in 20 tests:', 20 * 0.05)
```

**Yaad rakho:** 20 hypotheses ko p<0.05 par test karne se average ek false positive milta hi hai. Uske liye correction karo.

**Aam galti:** Baad me data ko pandrah tarah se kaat kar wahi ek slice report karna jo significant nikla.

Practice: `examples/04_null_and_alternative_hypotheses.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. p-values and what they are not

### Aasaan Bhasha

p-value matlab P(itna extreme data | kuch ho hi nahi raha). Ye ye nahi batata ki aapka idea sahi hai. Confidence interval zyada kaam ka hai kyunki wo effect size aur uncertainty saath dikhata hai — 'significant' 0.1% lift shayad ship karne layak hi na ho.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
control = rng.normal(10.0, 2.0, 500)
variant = rng.normal(10.3, 2.0, 500)

diff = variant.mean() - control.mean()
se = np.sqrt(control.var(ddof=1) / 500 + variant.var(ddof=1) / 500)
print(f'lift {diff:.3f}  95% CI [{diff - 1.96 * se:.3f}, {diff + 1.96 * se:.3f}]')
```

**Yaad rakho:** Sample size aur metric data dekhne se PEHLE decide karo.

**Aam galti:** Roz jhaank kar p < 0.05 hote hi test rok dena — isse false positives bahut badh jaate hain.

Practice: `examples/05_p_values_and_what_they_are_not.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. t-test and chi-square test

### Aasaan Bhasha

Aap sample naapte ho aur population ke baare me daawa karna chahte ho. Type I error jhoothi cheekh hai; Type II asli effect chook jaana. Power ye chance hai ki aap di gayi size ka asli effect pakad paoge — ise data jama karne se pehle tay karo, warna aap aisa experiment chalaoge jo kabhi safal ho hi nahi sakta tha.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
a = rng.normal(10.0, 2.0, 60)
b = rng.normal(11.0, 2.0, 60)

# Welch t-statistic, no scipy needed
se = np.sqrt(a.var(ddof=1) / len(a) + b.var(ddof=1) / len(b))
t = (b.mean() - a.mean()) / se
print(f'mean diff {b.mean() - a.mean():.3f}  t = {t:.2f}')
print('|t| > 2 is roughly the 5% threshold at these sample sizes')

# Twenty independent tests at 5%: expect one false positive by chance alone
print('expected false positives in 20 tests:', 20 * 0.05)
```

**Yaad rakho:** 20 hypotheses ko p<0.05 par test karne se average ek false positive milta hi hai. Uske liye correction karo.

**Aam galti:** Baad me data ko pandrah tarah se kaat kar wahi ek slice report karna jo significant nikla.

Practice: `examples/06_t_test_and_chi_square_test.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Type I and Type II errors

### Aasaan Bhasha

Aap sample naapte ho aur population ke baare me daawa karna chahte ho. Type I error jhoothi cheekh hai; Type II asli effect chook jaana. Power ye chance hai ki aap di gayi size ka asli effect pakad paoge — ise data jama karne se pehle tay karo, warna aap aisa experiment chalaoge jo kabhi safal ho hi nahi sakta tha.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
a = rng.normal(10.0, 2.0, 60)
b = rng.normal(11.0, 2.0, 60)

# Welch t-statistic, no scipy needed
se = np.sqrt(a.var(ddof=1) / len(a) + b.var(ddof=1) / len(b))
t = (b.mean() - a.mean()) / se
print(f'mean diff {b.mean() - a.mean():.3f}  t = {t:.2f}')
print('|t| > 2 is roughly the 5% threshold at these sample sizes')

# Twenty independent tests at 5%: expect one false positive by chance alone
print('expected false positives in 20 tests:', 20 * 0.05)
```

**Yaad rakho:** 20 hypotheses ko p<0.05 par test karne se average ek false positive milta hi hai. Uske liye correction karo.

**Aam galti:** Baad me data ko pandrah tarah se kaat kar wahi ek slice report karna jo significant nikla.

Practice: `examples/07_type_i_and_type_ii_errors.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Statistical power and sample size

### Aasaan Bhasha

Aap sample naapte ho aur population ke baare me daawa karna chahte ho. Type I error jhoothi cheekh hai; Type II asli effect chook jaana. Power ye chance hai ki aap di gayi size ka asli effect pakad paoge — ise data jama karne se pehle tay karo, warna aap aisa experiment chalaoge jo kabhi safal ho hi nahi sakta tha.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
a = rng.normal(10.0, 2.0, 60)
b = rng.normal(11.0, 2.0, 60)

# Welch t-statistic, no scipy needed
se = np.sqrt(a.var(ddof=1) / len(a) + b.var(ddof=1) / len(b))
t = (b.mean() - a.mean()) / se
print(f'mean diff {b.mean() - a.mean():.3f}  t = {t:.2f}')
print('|t| > 2 is roughly the 5% threshold at these sample sizes')

# Twenty independent tests at 5%: expect one false positive by chance alone
print('expected false positives in 20 tests:', 20 * 0.05)
```

**Yaad rakho:** 20 hypotheses ko p<0.05 par test karne se average ek false positive milta hi hai. Uske liye correction karo.

**Aam galti:** Baad me data ko pandrah tarah se kaat kar wahi ek slice report karna jo significant nikla.

Practice: `examples/08_statistical_power_and_sample_size.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Multiple comparisons and correction

### Aasaan Bhasha

Aap sample naapte ho aur population ke baare me daawa karna chahte ho. Type I error jhoothi cheekh hai; Type II asli effect chook jaana. Power ye chance hai ki aap di gayi size ka asli effect pakad paoge — ise data jama karne se pehle tay karo, warna aap aisa experiment chalaoge jo kabhi safal ho hi nahi sakta tha.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
a = rng.normal(10.0, 2.0, 60)
b = rng.normal(11.0, 2.0, 60)

# Welch t-statistic, no scipy needed
se = np.sqrt(a.var(ddof=1) / len(a) + b.var(ddof=1) / len(b))
t = (b.mean() - a.mean()) / se
print(f'mean diff {b.mean() - a.mean():.3f}  t = {t:.2f}')
print('|t| > 2 is roughly the 5% threshold at these sample sizes')

# Twenty independent tests at 5%: expect one false positive by chance alone
print('expected false positives in 20 tests:', 20 * 0.05)
```

**Yaad rakho:** 20 hypotheses ko p<0.05 par test karne se average ek false positive milta hi hai. Uske liye correction karo.

**Aam galti:** Baad me data ko pandrah tarah se kaat kar wahi ek slice report karna jo significant nikla.

Practice: `examples/09_multiple_comparisons_and_correction.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Bootstrapping without formulas

### Aasaan Bhasha

Bagging bahut saare trees ko bootstrap samples aur random feature subsets par train karke average kar leta hai. Averaging wo variance kaat deta hai jo single trees ko unpredictable banata hai. Tabular data par jab bina tuning ke kuch chalta hua chahiye, random forest best default hai.

### Chhota code

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score

X, y = load_breast_cancer(return_X_y=True)
rf = RandomForestClassifier(n_estimators=300, min_samples_leaf=2, n_jobs=-1, random_state=0)
print('cv accuracy', cross_val_score(rf, X, y, cv=5).mean().round(4))

rf.fit(X, y)
top = sorted(zip(load_breast_cancer().feature_names, rf.feature_importances_), key=lambda t: -t[1])[:5]
print('top features', [(n, round(v, 3)) for n, v in top])
```

**Yaad rakho:** Zyada trees kabhi overfit nahi karte — sirf time lagta hai. Depth aur leaf size hi fit control karte hain.

**Aam galti:** Business decisions ke liye impurity-based importances use karna, permutation importance ke bajaye.

Practice: `examples/10_bootstrapping_without_formulas.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 24 ke baad aapko ye aana chahiye

- **Population vs sample** ko bina notes dekhe kisi dost ko samjha sakna.
- **Sampling distributions and standard error** ko bina notes dekhe kisi dost ko samjha sakna.
- **Confidence intervals** ko bina notes dekhe kisi dost ko samjha sakna.
- **Null and alternative hypotheses** ko bina notes dekhe kisi dost ko samjha sakna.
- **p-values and what they are not** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
