# Day 116 — Edge and mobile vision

Aaj ka goal: **Edge and mobile vision** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Latency and power constraints |
| 2 | Model choice for edge devices |
| 3 | Quantised inference |
| 4 | ONNX Runtime and TFLite |
| 5 | Camera pipeline integration |
| 6 | Batching vs streaming |
| 7 | Thermal throttling |
| 8 | On-device privacy advantages |
| 9 | Measuring real device performance |
| 10 | Deploying a detector to a Raspberry Pi |

---

## 1. Latency and power constraints

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

Practice: `examples/01_latency_and_power_constraints.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Model choice for edge devices

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

Practice: `examples/02_model_choice_for_edge_devices.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Quantised inference

### Aasaan Bhasha

Device par aap accuracy ke badle latency, memory aur battery lete ho. Portable runtime me export karo, quantise karo, aur asli hardware par naapo — desktop benchmarks thermal load ke neeche phone ke baare me lagbhag kuch nahi batate.

### Chhota code

```python
BUDGET = {'latency_ms': 100, 'model_mb': 25, 'ram_mb': 150}

candidates = [
    {'name': 'resnet50-fp32',   'latency_ms': 340, 'model_mb': 98, 'ram_mb': 420},
    {'name': 'mobilenetv3-int8','latency_ms':  38, 'model_mb':  6, 'ram_mb':  90},
    {'name': 'efficientnet-b0', 'latency_ms': 120, 'model_mb': 21, 'ram_mb': 180},
]
for c in candidates:
    fits = all(c[k] <= v for k, v in BUDGET.items())
    print(f"{c['name']:<20} {'FITS' if fits else 'over budget'}")
```

**Yaad rakho:** Target device par naapo, garam aur load ke neeche — apne laptop par, ek baar, thanda nahi.

**Aam galti:** Latency desktop GPU par validate karna aur pata chalna ki phone 40 second baad throttle kar deta hai.

Practice: `examples/03_quantised_inference.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. ONNX Runtime and TFLite

### Aasaan Bhasha

Training cost ek baar lagti hai; inference cost har request par hamesha ke liye. Distillation chhote student ko bade teacher ke outputs par train karta hai, quantisation weights ko kam bits me rakhta hai, aur ONNX ek artefact deta hai jo kai runtimes par chalta hai. Jitni accuracy jaa rahi hai use utni latency ke faayde ke saath naapo.

### Chhota code

```python
# Memory footprint by precision, for a 7B parameter model
params = 7e9
for name, bits in [('fp32', 32), ('fp16/bf16', 16), ('int8', 8), ('int4', 4)]:
    gb = params * bits / 8 / 1e9
    print(f'{name:<10} {bits:>2} bits -> {gb:6.1f} GB of weights')
print('\nPlus KV cache and activations at runtime — budget roughly 20-30% more.')
```

**Yaad rakho:** Quantise karo, apne khud ke eval set par quality naapo, phir decide karo. Published benchmarks aapka task nahi hain.

**Aam galti:** int4 model isliye ship kar dena ki wo fit ho gaya, bina kabhi naape ki usne kitni accuracy li.

Practice: `examples/04_onnx_runtime_and_tflite.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Camera pipeline integration

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

Practice: `examples/05_camera_pipeline_integration.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Batching vs streaming

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

Practice: `examples/06_batching_vs_streaming.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Thermal throttling

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

Practice: `examples/07_thermal_throttling.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. On-device privacy advantages

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

Practice: `examples/08_on_device_privacy_advantages.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Measuring real device performance

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

Practice: `examples/09_measuring_real_device_performance.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Deploying a detector to a Raspberry Pi

### Aasaan Bhasha

Device par aap accuracy ke badle latency, memory aur battery lete ho. Portable runtime me export karo, quantise karo, aur asli hardware par naapo — desktop benchmarks thermal load ke neeche phone ke baare me lagbhag kuch nahi batate.

### Chhota code

```python
BUDGET = {'latency_ms': 100, 'model_mb': 25, 'ram_mb': 150}

candidates = [
    {'name': 'resnet50-fp32',   'latency_ms': 340, 'model_mb': 98, 'ram_mb': 420},
    {'name': 'mobilenetv3-int8','latency_ms':  38, 'model_mb':  6, 'ram_mb':  90},
    {'name': 'efficientnet-b0', 'latency_ms': 120, 'model_mb': 21, 'ram_mb': 180},
]
for c in candidates:
    fits = all(c[k] <= v for k, v in BUDGET.items())
    print(f"{c['name']:<20} {'FITS' if fits else 'over budget'}")
```

**Yaad rakho:** Target device par naapo, garam aur load ke neeche — apne laptop par, ek baar, thanda nahi.

**Aam galti:** Latency desktop GPU par validate karna aur pata chalna ki phone 40 second baad throttle kar deta hai.

Practice: `examples/10_deploying_a_detector_to_a_raspberry_pi.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 116 ke baad aapko ye aana chahiye

- **Latency and power constraints** ko bina notes dekhe kisi dost ko samjha sakna.
- **Model choice for edge devices** ko bina notes dekhe kisi dost ko samjha sakna.
- **Quantised inference** ko bina notes dekhe kisi dost ko samjha sakna.
- **ONNX Runtime and TFLite** ko bina notes dekhe kisi dost ko samjha sakna.
- **Camera pipeline integration** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
