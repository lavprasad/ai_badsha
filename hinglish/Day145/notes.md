# Day 145 — Small models and local AI

Aaj ka goal: **Small models and local AI** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Why small models matter |
| 2 | Distillation from a large teacher |
| 3 | Task-specific small models |
| 4 | Running models on a laptop |
| 5 | GGUF quantisation levels |
| 6 | Ollama and LM Studio |
| 7 | Privacy advantages of local inference |
| 8 | Latency and cost comparison |
| 9 | Quality gap by task type |
| 10 | Routing between small and large models |

---

## 1. Why small models matter

### Aasaan Bhasha

Aaj ka idea — **Why small models matter** — Small models and local AI ke theme ke andar aata hai. Ise trivia nahi, ek tool ki tarah padho: ye kaam kya karta hai, aapke data ke baare me kya maan kar chalta hai, aur wo maanyata jhooth nikle to kya tootta hai?

### Chhota code

```python
# Explore: Why small models matter
print("practice: Why small models matter")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Yaad rakho:** `Why small models matter` use karne se pehle ek assumption likho jo ye aapke data ke baare me maanta hai.

**Aam galti:** `Why small models matter` ko tutorial se copy-paste kar lena bina jaane ki wo kya maanta hai aur kab fail hota hai.

Practice: `examples/01_why_small_models_matter.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Distillation from a large teacher

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

Practice: `examples/02_distillation_from_a_large_teacher.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Task-specific small models

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

Practice: `examples/03_task_specific_small_models.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Running models on a laptop

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

Practice: `examples/04_running_models_on_a_laptop.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. GGUF quantisation levels

### Aasaan Bhasha

LoRA base weights freeze kar deta hai aur do chhoti low-rank matrices train karta hai jinka product har target layer me joda jaata hai. Aap ~0.1% parameters update karte ho, checkpoint gigabytes ke bajaye megabytes ka hota hai, aur har customer ke liye adapter badla ja sakta hai. QLoRA 4-bit base weights jodta hai taaki 7B model ek consumer GPU par aa jaaye.

### Chhota code

```python
import numpy as np

d, r = 512, 8                      # full dim vs LoRA rank
rng = np.random.default_rng(0)
W = rng.normal(size=(d, d)) * 0.02  # frozen base weight
A = rng.normal(size=(d, r)) * 0.01  # trainable
B = np.zeros((r, d))                # trainable, starts at zero -> no change at step 0

delta = A @ B
print('base params   ', W.size)
print('lora params   ', A.size + B.size, f'({100 * (A.size + B.size) / W.size:.1f}%)')
print('effective W = W + A@B, shape', (W + delta).shape)
```

**Yaad rakho:** B ko zeros se initialise karo taaki adapted model bilkul base model ke barabar shuru ho.

**Aam galti:** Rank bahut zyada rakh dena — efficiency chali jaati hai aur overfitting aa jaati hai.

Practice: `examples/05_gguf_quantisation_levels.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Ollama and LM Studio

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

Practice: `examples/06_ollama_and_lm_studio.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Privacy advantages of local inference

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

Practice: `examples/07_privacy_advantages_of_local_inference.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Latency and cost comparison

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

Practice: `examples/08_latency_and_cost_comparison.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Quality gap by task type

### Aasaan Bhasha

Aaj ka idea — **Quality gap by task type** — Small models and local AI ke theme ke andar aata hai. Ise trivia nahi, ek tool ki tarah padho: ye kaam kya karta hai, aapke data ke baare me kya maan kar chalta hai, aur wo maanyata jhooth nikle to kya tootta hai?

### Chhota code

```python
# Explore: Quality gap by task type
print("practice: Quality gap by task type")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Yaad rakho:** `Quality gap by task type` use karne se pehle ek assumption likho jo ye aapke data ke baare me maanta hai.

**Aam galti:** `Quality gap by task type` ko tutorial se copy-paste kar lena bina jaane ki wo kya maanta hai aur kab fail hota hai.

Practice: `examples/09_quality_gap_by_task_type.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Routing between small and large models

### Aasaan Bhasha

Aaj ka idea — **Routing between small and large models** — Small models and local AI ke theme ke andar aata hai. Ise trivia nahi, ek tool ki tarah padho: ye kaam kya karta hai, aapke data ke baare me kya maan kar chalta hai, aur wo maanyata jhooth nikle to kya tootta hai?

### Chhota code

```python
# Explore: Routing between small and large models
print("practice: Routing between small and large models")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Yaad rakho:** `Routing between small and large models` use karne se pehle ek assumption likho jo ye aapke data ke baare me maanta hai.

**Aam galti:** `Routing between small and large models` ko tutorial se copy-paste kar lena bina jaane ki wo kya maanta hai aur kab fail hota hai.

Practice: `examples/10_routing_between_small_and_large_models.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 145 ke baad aapko ye aana chahiye

- **Why small models matter** ko bina notes dekhe kisi dost ko samjha sakna.
- **Distillation from a large teacher** ko bina notes dekhe kisi dost ko samjha sakna.
- **Task-specific small models** ko bina notes dekhe kisi dost ko samjha sakna.
- **Running models on a laptop** ko bina notes dekhe kisi dost ko samjha sakna.
- **GGUF quantisation levels** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
