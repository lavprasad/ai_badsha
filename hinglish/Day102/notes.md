# Day 102 — Hardware and performance

Aaj ka goal: **Hardware and performance** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | CPU vs GPU vs TPU |
| 2 | Memory bandwidth as the real bottleneck |
| 3 | Batch size and utilisation |
| 4 | Mixed precision: fp16 and bf16 |
| 5 | Gradient checkpointing |
| 6 | Profiling a training run |
| 7 | Data loading bottlenecks |
| 8 | Multi-GPU data parallelism |
| 9 | Model and pipeline parallelism |
| 10 | Estimating training cost before you start |

---

## 1. CPU vs GPU vs TPU

### Aasaan Bhasha

GPU isliye jeette hain kyunki wo hazaaron multiply-add saath karte hain. Model aur data ek hi device par hone chahiye warna error. Mixed precision (bf16/fp16) memory aadhi kar deta hai aur modern cards par throughput lagbhag double, accuracy me lagbhag kuch kharcha kiye bina.

### Chhota code

```python
import torch

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print('using', device)

x = torch.randn(1000, 1000, device=device)
y = x @ x.T
print(y.shape, y.device)

if device == 'cuda':
    print('allocated MB', round(torch.cuda.memory_allocated() / 1e6, 1))
```

**Yaad rakho:** CUDA OOM par sabse pehle batch size ghatao; effective batch banaye rakhne ke liye gradient accumulation use karo.

**Aam galti:** Har step ka poora loss tensor list me rakhna — wo poora graph pakde rehta hai aur memory leak karta hai.

Practice: `examples/01_cpu_vs_gpu_vs_tpu.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Memory bandwidth as the real bottleneck

### Aasaan Bhasha

Zyadatar training runs compute-bound nahi hote; wo data ka intezaar kar rahe hote hain. Bada GPU khareedne se pehle utilisation dekho: agar wo 30% par baitha hai to fix aur data-loader workers ya tez storage format hai. Shuru karne se pehle cost ka andaaza lagao — ghante x instance price aisa number hai jise aap approve ya reject kar sakte ho.

### Chhota code

```python
def training_estimate(samples, epochs, samples_per_sec, gpu_cost_per_hour):
    steps = samples * epochs
    hours = steps / samples_per_sec / 3600
    return {'hours': round(hours, 2), 'cost': round(hours * gpu_cost_per_hour, 2)}

print(training_estimate(samples=1_200_000, epochs=3, samples_per_sec=850, gpu_cost_per_hour=2.5))
print('If GPU utilization < 60%, fix the data pipeline before scaling hardware.')
```

**Yaad rakho:** Scale karne se pehle profile karo. Dheema `__getitem__` chhote GPU se zyada paisa barbaad karta hai.

**Aam galti:** Chaar GPUs kiraye par lena aise bottleneck ke liye jo asal me single-threaded JPEG decode tha.

Practice: `examples/02_memory_bandwidth_as_the_real_bottleneck.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Batch size and utilisation

### Aasaan Bhasha

Zyadatar training runs compute-bound nahi hote; wo data ka intezaar kar rahe hote hain. Bada GPU khareedne se pehle utilisation dekho: agar wo 30% par baitha hai to fix aur data-loader workers ya tez storage format hai. Shuru karne se pehle cost ka andaaza lagao — ghante x instance price aisa number hai jise aap approve ya reject kar sakte ho.

### Chhota code

```python
def training_estimate(samples, epochs, samples_per_sec, gpu_cost_per_hour):
    steps = samples * epochs
    hours = steps / samples_per_sec / 3600
    return {'hours': round(hours, 2), 'cost': round(hours * gpu_cost_per_hour, 2)}

print(training_estimate(samples=1_200_000, epochs=3, samples_per_sec=850, gpu_cost_per_hour=2.5))
print('If GPU utilization < 60%, fix the data pipeline before scaling hardware.')
```

**Yaad rakho:** Scale karne se pehle profile karo. Dheema `__getitem__` chhote GPU se zyada paisa barbaad karta hai.

**Aam galti:** Chaar GPUs kiraye par lena aise bottleneck ke liye jo asal me single-threaded JPEG decode tha.

Practice: `examples/03_batch_size_and_utilisation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Mixed precision: fp16 and bf16

### Aasaan Bhasha

Imbalanced data par accuracy sab chhupa leti hai. Precision poochti hai 'jinhe maine flag kiya unme se kitne asli the'; recall poochti hai 'jo asli the unme se kitne maine pakde'. Threshold se aap ek ko doosre ke badle bechte ho, aur kaunsi galti zyada mehngi hai ye business tay karta hai.

### Chhota code

```python
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=2000, weights=[0.95, 0.05], random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, stratify=y, random_state=0)
m = LogisticRegression(max_iter=1000).fit(Xtr, ytr)
print(confusion_matrix(yte, m.predict(Xte)))
print(classification_report(yte, m.predict(Xte), digits=3))
print('roc auc', round(roc_auc_score(yte, m.predict_proba(Xte)[:, 1]), 4))
```

**Yaad rakho:** Decision threshold validation data par tune karo; 0.5 ek default hai, decision nahi.

**Aam galti:** Bhaari imbalanced problem par ROC-AUC optimise karna jahan imaandaar metric precision-recall AUC hai.

Practice: `examples/04_mixed_precision_fp16_and_bf16.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Gradient checkpointing

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

Practice: `examples/05_gradient_checkpointing.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Profiling a training run

### Aasaan Bhasha

Zyadatar training runs compute-bound nahi hote; wo data ka intezaar kar rahe hote hain. Bada GPU khareedne se pehle utilisation dekho: agar wo 30% par baitha hai to fix aur data-loader workers ya tez storage format hai. Shuru karne se pehle cost ka andaaza lagao — ghante x instance price aisa number hai jise aap approve ya reject kar sakte ho.

### Chhota code

```python
def training_estimate(samples, epochs, samples_per_sec, gpu_cost_per_hour):
    steps = samples * epochs
    hours = steps / samples_per_sec / 3600
    return {'hours': round(hours, 2), 'cost': round(hours * gpu_cost_per_hour, 2)}

print(training_estimate(samples=1_200_000, epochs=3, samples_per_sec=850, gpu_cost_per_hour=2.5))
print('If GPU utilization < 60%, fix the data pipeline before scaling hardware.')
```

**Yaad rakho:** Scale karne se pehle profile karo. Dheema `__getitem__` chhote GPU se zyada paisa barbaad karta hai.

**Aam galti:** Chaar GPUs kiraye par lena aise bottleneck ke liye jo asal me single-threaded JPEG decode tha.

Practice: `examples/06_profiling_a_training_run.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Data loading bottlenecks

### Aasaan Bhasha

Zyadatar training runs compute-bound nahi hote; wo data ka intezaar kar rahe hote hain. Bada GPU khareedne se pehle utilisation dekho: agar wo 30% par baitha hai to fix aur data-loader workers ya tez storage format hai. Shuru karne se pehle cost ka andaaza lagao — ghante x instance price aisa number hai jise aap approve ya reject kar sakte ho.

### Chhota code

```python
def training_estimate(samples, epochs, samples_per_sec, gpu_cost_per_hour):
    steps = samples * epochs
    hours = steps / samples_per_sec / 3600
    return {'hours': round(hours, 2), 'cost': round(hours * gpu_cost_per_hour, 2)}

print(training_estimate(samples=1_200_000, epochs=3, samples_per_sec=850, gpu_cost_per_hour=2.5))
print('If GPU utilization < 60%, fix the data pipeline before scaling hardware.')
```

**Yaad rakho:** Scale karne se pehle profile karo. Dheema `__getitem__` chhote GPU se zyada paisa barbaad karta hai.

**Aam galti:** Chaar GPUs kiraye par lena aise bottleneck ke liye jo asal me single-threaded JPEG decode tha.

Practice: `examples/07_data_loading_bottlenecks.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Multi-GPU data parallelism

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

Practice: `examples/08_multi_gpu_data_parallelism.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Model and pipeline parallelism

### Aasaan Bhasha

Pipeline preprocessing aur model ko ek hi object me jod deta hai jo ek unit ki tarah fit aur predict karta hai. Leakage ke khilaaf yahi sabse achhi dhaal hai, aur deployment ko chhe alag steps ke bajaye ek artefact milta hai jise yaad rakhne ki zaroorat nahi.

### Chhota code

```python
import numpy as np, pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression

df = pd.DataFrame({'age': [25, np.nan, 40, 33], 'city': ['pune', 'delhi', 'pune', 'delhi']})
y = [0, 1, 0, 1]

pre = ColumnTransformer([
    ('num', Pipeline([('imp', SimpleImputer(strategy='median')), ('sc', StandardScaler())]), ['age']),
    ('cat', OneHotEncoder(handle_unknown='ignore'), ['city']),
])
model = Pipeline([('pre', pre), ('clf', LogisticRegression())]).fit(df, y)
print(model.predict(df))
```

**Yaad rakho:** `handle_unknown='ignore'` production ko us category par crash hone se bachata hai jo training me kabhi nahi dikhi.

**Aam galti:** Notebook me preprocess karna aur serving code likhte waqt ek step bhool jaana.

Practice: `examples/09_model_and_pipeline_parallelism.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Estimating training cost before you start

### Aasaan Bhasha

Zyadatar training runs compute-bound nahi hote; wo data ka intezaar kar rahe hote hain. Bada GPU khareedne se pehle utilisation dekho: agar wo 30% par baitha hai to fix aur data-loader workers ya tez storage format hai. Shuru karne se pehle cost ka andaaza lagao — ghante x instance price aisa number hai jise aap approve ya reject kar sakte ho.

### Chhota code

```python
def training_estimate(samples, epochs, samples_per_sec, gpu_cost_per_hour):
    steps = samples * epochs
    hours = steps / samples_per_sec / 3600
    return {'hours': round(hours, 2), 'cost': round(hours * gpu_cost_per_hour, 2)}

print(training_estimate(samples=1_200_000, epochs=3, samples_per_sec=850, gpu_cost_per_hour=2.5))
print('If GPU utilization < 60%, fix the data pipeline before scaling hardware.')
```

**Yaad rakho:** Scale karne se pehle profile karo. Dheema `__getitem__` chhote GPU se zyada paisa barbaad karta hai.

**Aam galti:** Chaar GPUs kiraye par lena aise bottleneck ke liye jo asal me single-threaded JPEG decode tha.

Practice: `examples/10_estimating_training_cost_before_you_star.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 102 ke baad aapko ye aana chahiye

- **CPU vs GPU vs TPU** ko bina notes dekhe kisi dost ko samjha sakna.
- **Memory bandwidth as the real bottleneck** ko bina notes dekhe kisi dost ko samjha sakna.
- **Batch size and utilisation** ko bina notes dekhe kisi dost ko samjha sakna.
- **Mixed precision: fp16 and bf16** ko bina notes dekhe kisi dost ko samjha sakna.
- **Gradient checkpointing** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
