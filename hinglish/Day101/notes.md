# Day 101 — Model compression

Aaj ka goal: **Model compression** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Why inference cost matters more than training cost |
| 2 | Quantisation: int8 and int4 |
| 3 | Post-training vs quantisation-aware training |
| 4 | Pruning: structured and unstructured |
| 5 | Knowledge distillation |
| 6 | Low-rank factorisation |
| 7 | Operator fusion |
| 8 | ONNX and runtime portability |
| 9 | Measuring the accuracy/latency trade-off |
| 10 | Shrinking a model for edge deployment |

---

## 1. Why inference cost matters more than training cost

### Aasaan Bhasha

Temperature 0 lagbhag deterministic hai aur extraction ke liye sahi; zyada values creative kaam ke liye variety deti hain. Top-p sabse chhota set rakhta hai jo probability mass ka p cover kare. Cost per token in aur out hai, isliye prompt chhota karna sabse sasta optimisation hai.

### Chhota code

```python
import numpy as np

def sample(logits, temperature=1.0, top_p=0.9, seed=0):
    z = np.array(logits) / max(temperature, 1e-6)
    p = np.exp(z - z.max())
    p /= p.sum()
    order = np.argsort(-p)
    keep = order[:max(1, int(np.searchsorted(np.cumsum(p[order]), top_p) + 1))]
    p2 = p[keep] / p[keep].sum()
    return int(np.random.default_rng(seed).choice(keep, p=p2))

logits = [3.0, 2.0, 1.0, 0.5]
print('greedy-ish (T=0.1):', sample(logits, temperature=0.1))
print('creative  (T=1.5):', sample(logits, temperature=1.5, seed=3))
```

**Yaad rakho:** Jise aap parse karoge uske liye temperature 0 use karo; randomness prose ke liye bachaao.

**Aam galti:** Temperature 1 par extraction chala kar hafte bhar 'random' JSON failures debug karna.

Practice: `examples/01_why_inference_cost_matters_more_than_tra.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Quantisation: int8 and int4

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

Practice: `examples/02_quantisation_int8_and_int4.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Post-training vs quantisation-aware training

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

Practice: `examples/03_post_training_vs_quantisation_aware_trai.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Pruning: structured and unstructured

### Aasaan Bhasha

Tree haan/na sawaal poochta hai aur split karke har taraf ko purer banata hai. Isse scaling nahi chahiye, ye mixed types sambhal leta hai, aur flowchart jaisa padhta hai. Bina rok-tok chhod do to ye training set ko poora ratt leta hai, isliye depth aur leaf-size limits zaroori hain.

### Chhota code

```python
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
tree = DecisionTreeClassifier(max_depth=3, min_samples_leaf=5, random_state=0).fit(X, y)
print(export_text(tree, feature_names=load_iris().feature_names))
```

**Yaad rakho:** Ek bina-prune ka tree lagbhag hamesha chhote forest se kharab hota hai — par wo padha ja sakta hai, jo kabhi-kabhi jeet jaata hai.

**Aam galti:** Gehre tree ke feature importances par bharosa karna; wo unstable hain aur high-cardinality columns ki taraf jhukte hain.

Practice: `examples/04_pruning_structured_and_unstructured.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Knowledge distillation

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

Practice: `examples/05_knowledge_distillation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Low-rank factorisation

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

Practice: `examples/06_low_rank_factorisation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Operator fusion

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

Practice: `examples/07_operator_fusion.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. ONNX and runtime portability

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

Practice: `examples/08_onnx_and_runtime_portability.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Measuring the accuracy/latency trade-off

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

Practice: `examples/09_measuring_the_accuracy_latency_trade_off.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Shrinking a model for edge deployment

### Aasaan Bhasha

Container code, dependencies aur interpreter ko package kar deta hai taaki har jagah ek jaisa chale. Versions pin karo, slim base use karo, aur bade model weights image layer se bahar rakho — unhe mount ya download karo.

### Chhota code

```python
DOCKERFILE = '''
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
'''
print(DOCKERFILE)
print('Copy requirements first so the pip layer caches across code changes.')
```

**Yaad rakho:** `--no-cache-dir` aur slim base images chhoti rakhte hain; chhoti images tez deploy hoti hain.

**Aam galti:** `pip install` se pehle `COPY . .` likhna, jisse har code edit par dependency cache toot jaata hai.

Practice: `examples/10_shrinking_a_model_for_edge_deployment.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 101 ke baad aapko ye aana chahiye

- **Why inference cost matters more than training cost** ko bina notes dekhe kisi dost ko samjha sakna.
- **Quantisation: int8 and int4** ko bina notes dekhe kisi dost ko samjha sakna.
- **Post-training vs quantisation-aware training** ko bina notes dekhe kisi dost ko samjha sakna.
- **Pruning: structured and unstructured** ko bina notes dekhe kisi dost ko samjha sakna.
- **Knowledge distillation** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
