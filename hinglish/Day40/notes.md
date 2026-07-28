# Day 40 — Encoding and scaling

Aaj ka goal: **Encoding and scaling** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | One-hot encoding |
| 2 | Ordinal encoding when order is real |
| 3 | Target encoding and its leakage risk |
| 4 | Hashing trick for high cardinality |
| 5 | Handling unseen categories at inference |
| 6 | StandardScaler vs MinMaxScaler |
| 7 | RobustScaler for outlier-heavy data |
| 8 | Log and power transforms |
| 9 | Which models need scaling and which do not |
| 10 | Fitting transforms on train only |

---

## 1. One-hot encoding

### Aasaan Bhasha

Models ko numbers chahiye. Kam-cardinality nominal categories ke liye one-hot safe hai. Label/ordinal encoding jhootha order bana deta hai, jab tak order asli na ho (small < medium < large). Target encoding powerful hai aur bura leak karta hai jab tak use cross-validation folds ke andar fit na kiya jaaye.

### Chhota code

```python
import pandas as pd

df = pd.DataFrame({'size': ['small', 'large', 'medium'], 'city': ['pune', 'delhi', 'pune']})

order = {'small': 0, 'medium': 1, 'large': 2}     # real order -> ordinal is fine
df['size_ord'] = df['size'].map(order)

print(pd.get_dummies(df[['city']], prefix='city', dtype=int))
print(df)
```

**Yaad rakho:** Inference par unseen categories handle karo — pehle hi decide karo ki wo 'other' banengi ya error.

**Aam galti:** 50,000 values wale ID column ko one-hot karke memory uda dena, bina kisi signal ke.

Practice: `examples/01_one_hot_encoding.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Ordinal encoding when order is real

### Aasaan Bhasha

Models ko numbers chahiye. Kam-cardinality nominal categories ke liye one-hot safe hai. Label/ordinal encoding jhootha order bana deta hai, jab tak order asli na ho (small < medium < large). Target encoding powerful hai aur bura leak karta hai jab tak use cross-validation folds ke andar fit na kiya jaaye.

### Chhota code

```python
import pandas as pd

df = pd.DataFrame({'size': ['small', 'large', 'medium'], 'city': ['pune', 'delhi', 'pune']})

order = {'small': 0, 'medium': 1, 'large': 2}     # real order -> ordinal is fine
df['size_ord'] = df['size'].map(order)

print(pd.get_dummies(df[['city']], prefix='city', dtype=int))
print(df)
```

**Yaad rakho:** Inference par unseen categories handle karo — pehle hi decide karo ki wo 'other' banengi ya error.

**Aam galti:** 50,000 values wale ID column ko one-hot karke memory uda dena, bina kisi signal ke.

Practice: `examples/02_ordinal_encoding_when_order_is_real.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Target encoding and its leakage risk

### Aasaan Bhasha

Models ko numbers chahiye. Kam-cardinality nominal categories ke liye one-hot safe hai. Label/ordinal encoding jhootha order bana deta hai, jab tak order asli na ho (small < medium < large). Target encoding powerful hai aur bura leak karta hai jab tak use cross-validation folds ke andar fit na kiya jaaye.

### Chhota code

```python
import pandas as pd

df = pd.DataFrame({'size': ['small', 'large', 'medium'], 'city': ['pune', 'delhi', 'pune']})

order = {'small': 0, 'medium': 1, 'large': 2}     # real order -> ordinal is fine
df['size_ord'] = df['size'].map(order)

print(pd.get_dummies(df[['city']], prefix='city', dtype=int))
print(df)
```

**Yaad rakho:** Inference par unseen categories handle karo — pehle hi decide karo ki wo 'other' banengi ya error.

**Aam galti:** 50,000 values wale ID column ko one-hot karke memory uda dena, bina kisi signal ke.

Practice: `examples/03_target_encoding_and_its_leakage_risk.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Hashing trick for high cardinality

### Aasaan Bhasha

Data parallelism model ki copies banata hai aur batch baant deta hai; model parallelism model ko baantta hai jab wo ek device par na aaye. Profiling ke baad hi scale karo — 'humein aur GPUs chahiye' wali zyadatar problems asal me dheema data loader hoti hain.

### Chhota code

```python
# Effective batch = per_device_batch * n_devices * grad_accum_steps
per_device, devices, accum = 8, 4, 4
print('effective batch size', per_device * devices * accum)
print('\\nGradient accumulation gives a large effective batch on small memory:')
print('  for i, batch in enumerate(loader):')
print('      loss = model(batch).loss / accum')
print('      loss.backward()')
print('      if (i + 1) % accum == 0:')
print('          opt.step(); opt.zero_grad()')
```

**Yaad rakho:** Pehle profile karo. GPU 30% utilisation par matlab bottleneck data pipeline hai, GPU nahi.

**Aam galti:** Batch scale karte waqt learning rate galat scale karna — bade batch ko aam taur par bada LR chahiye.

Practice: `examples/04_hashing_trick_for_high_cardinality.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Handling unseen categories at inference

### Aasaan Bhasha

Data parallelism model ki copies banata hai aur batch baant deta hai; model parallelism model ko baantta hai jab wo ek device par na aaye. Profiling ke baad hi scale karo — 'humein aur GPUs chahiye' wali zyadatar problems asal me dheema data loader hoti hain.

### Chhota code

```python
# Effective batch = per_device_batch * n_devices * grad_accum_steps
per_device, devices, accum = 8, 4, 4
print('effective batch size', per_device * devices * accum)
print('\\nGradient accumulation gives a large effective batch on small memory:')
print('  for i, batch in enumerate(loader):')
print('      loss = model(batch).loss / accum')
print('      loss.backward()')
print('      if (i + 1) % accum == 0:')
print('          opt.step(); opt.zero_grad()')
```

**Yaad rakho:** Pehle profile karo. GPU 30% utilisation par matlab bottleneck data pipeline hai, GPU nahi.

**Aam galti:** Batch scale karte waqt learning rate galat scale karna — bade batch ko aam taur par bada LR chahiye.

Practice: `examples/05_handling_unseen_categories_at_inference.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. StandardScaler vs MinMaxScaler

### Aasaan Bhasha

Distance aur gradient wale models units ki parwah karte hain: rupaye wala salary column sirf magnitude se age column par chha jaayega. Zyadatar models ke liye standardise karo (mean 0, std 1); bounded [0,1] chahiye to min-max. Tree models ko koi farq nahi padta.

### Chhota code

```python
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
pipe = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
print('cv accuracy', cross_val_score(pipe, X, y, cv=5).mean().round(4))
```

**Yaad rakho:** Scaler ko Pipeline ke ANDAR rakho taaki cross-validation har fold me use dobara fit kare aur leak na ho.

**Aam galti:** Split se pehle poore dataset par `fit_transform` chala dena — classic, chupka, score badhaane wala leak.

Practice: `examples/06_standardscaler_vs_minmaxscaler.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. RobustScaler for outlier-heavy data

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

Practice: `examples/07_robustscaler_for_outlier_heavy_data.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Log and power transforms

### Aasaan Bhasha

Data parallelism model ki copies banata hai aur batch baant deta hai; model parallelism model ko baantta hai jab wo ek device par na aaye. Profiling ke baad hi scale karo — 'humein aur GPUs chahiye' wali zyadatar problems asal me dheema data loader hoti hain.

### Chhota code

```python
# Effective batch = per_device_batch * n_devices * grad_accum_steps
per_device, devices, accum = 8, 4, 4
print('effective batch size', per_device * devices * accum)
print('\\nGradient accumulation gives a large effective batch on small memory:')
print('  for i, batch in enumerate(loader):')
print('      loss = model(batch).loss / accum')
print('      loss.backward()')
print('      if (i + 1) % accum == 0:')
print('          opt.step(); opt.zero_grad()')
```

**Yaad rakho:** Pehle profile karo. GPU 30% utilisation par matlab bottleneck data pipeline hai, GPU nahi.

**Aam galti:** Batch scale karte waqt learning rate galat scale karna — bade batch ko aam taur par bada LR chahiye.

Practice: `examples/08_log_and_power_transforms.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Which models need scaling and which do not

### Aasaan Bhasha

Data parallelism model ki copies banata hai aur batch baant deta hai; model parallelism model ko baantta hai jab wo ek device par na aaye. Profiling ke baad hi scale karo — 'humein aur GPUs chahiye' wali zyadatar problems asal me dheema data loader hoti hain.

### Chhota code

```python
# Effective batch = per_device_batch * n_devices * grad_accum_steps
per_device, devices, accum = 8, 4, 4
print('effective batch size', per_device * devices * accum)
print('\\nGradient accumulation gives a large effective batch on small memory:')
print('  for i, batch in enumerate(loader):')
print('      loss = model(batch).loss / accum')
print('      loss.backward()')
print('      if (i + 1) % accum == 0:')
print('          opt.step(); opt.zero_grad()')
```

**Yaad rakho:** Pehle profile karo. GPU 30% utilisation par matlab bottleneck data pipeline hai, GPU nahi.

**Aam galti:** Batch scale karte waqt learning rate galat scale karna — bade batch ko aam taur par bada LR chahiye.

Practice: `examples/09_which_models_need_scaling_and_which_do_n.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Fitting transforms on train only

### Aasaan Bhasha

Data parallelism model ki copies banata hai aur batch baant deta hai; model parallelism model ko baantta hai jab wo ek device par na aaye. Profiling ke baad hi scale karo — 'humein aur GPUs chahiye' wali zyadatar problems asal me dheema data loader hoti hain.

### Chhota code

```python
# Effective batch = per_device_batch * n_devices * grad_accum_steps
per_device, devices, accum = 8, 4, 4
print('effective batch size', per_device * devices * accum)
print('\\nGradient accumulation gives a large effective batch on small memory:')
print('  for i, batch in enumerate(loader):')
print('      loss = model(batch).loss / accum')
print('      loss.backward()')
print('      if (i + 1) % accum == 0:')
print('          opt.step(); opt.zero_grad()')
```

**Yaad rakho:** Pehle profile karo. GPU 30% utilisation par matlab bottleneck data pipeline hai, GPU nahi.

**Aam galti:** Batch scale karte waqt learning rate galat scale karna — bade batch ko aam taur par bada LR chahiye.

Practice: `examples/10_fitting_transforms_on_train_only.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 40 ke baad aapko ye aana chahiye

- **One-hot encoding** ko bina notes dekhe kisi dost ko samjha sakna.
- **Ordinal encoding when order is real** ko bina notes dekhe kisi dost ko samjha sakna.
- **Target encoding and its leakage risk** ko bina notes dekhe kisi dost ko samjha sakna.
- **Hashing trick for high cardinality** ko bina notes dekhe kisi dost ko samjha sakna.
- **Handling unseen categories at inference** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
