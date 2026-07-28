# Day 150 — Designing with LLMs

Aaj ka goal: **Designing with LLMs** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | What LLMs are good and bad at |
| 2 | Choosing between rules, ML and LLMs |
| 3 | Task decomposition |
| 4 | Deterministic scaffolding around a stochastic core |
| 5 | Where to put validation |
| 6 | Failure budgets |
| 7 | Human-in-the-loop design |
| 8 | Cost modelling before building |
| 9 | Latency budgets |
| 10 | Writing an LLM system design doc |

---

## 1. What LLMs are good and bad at

### Aasaan Bhasha

Stochastic hisse ko sabse chhote possible dabbe me rakho. Deterministic code tay kare ki kya call karna hai, jo wapas aaye use validate kare, aur permissions lagu kare; model beech me bas dhundhla bhaasha wala kaam kare. Un dono ke beech ki har seemaa ek validation ki jagah hai.

### Chhota code

```python
def extract_and_act(text, model_call, db):
    raw = model_call(text)                       # 1. fuzzy: model reads language
    try:                                          # 2. deterministic: validate
        amount = float(raw['amount'])
        account = str(raw['account'])
    except (KeyError, ValueError, TypeError):
        return {'status': 'rejected', 'reason': 'unparseable model output'}
    if not 0 < amount <= 10_000:                  # 3. deterministic: business rules
        return {'status': 'escalate', 'reason': 'amount outside auto-approve band'}
    return {'status': 'approved', 'account': account, 'amount': amount}

print(extract_and_act('refund 500', lambda t: {'amount': '500', 'account': 'A-1'}, db=None))
print(extract_and_act('refund lots', lambda t: {'amount': '99000', 'account': 'A-1'}, db=None))
```

**Yaad rakho:** Model prastaav deta hai; aapka code faisla karta hai. Kisi action se pehle aakhri check model output kabhi na ho.

**Aam galti:** Model ke apne 'confidence: 0.98' field par aise bharosa karna jaise wo calibrated probability ho.

Practice: `examples/01_what_llms_are_good_and_bad_at.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Choosing between rules, ML and LLMs

### Aasaan Bhasha

Stochastic hisse ko sabse chhote possible dabbe me rakho. Deterministic code tay kare ki kya call karna hai, jo wapas aaye use validate kare, aur permissions lagu kare; model beech me bas dhundhla bhaasha wala kaam kare. Un dono ke beech ki har seemaa ek validation ki jagah hai.

### Chhota code

```python
def extract_and_act(text, model_call, db):
    raw = model_call(text)                       # 1. fuzzy: model reads language
    try:                                          # 2. deterministic: validate
        amount = float(raw['amount'])
        account = str(raw['account'])
    except (KeyError, ValueError, TypeError):
        return {'status': 'rejected', 'reason': 'unparseable model output'}
    if not 0 < amount <= 10_000:                  # 3. deterministic: business rules
        return {'status': 'escalate', 'reason': 'amount outside auto-approve band'}
    return {'status': 'approved', 'account': account, 'amount': amount}

print(extract_and_act('refund 500', lambda t: {'amount': '500', 'account': 'A-1'}, db=None))
print(extract_and_act('refund lots', lambda t: {'amount': '99000', 'account': 'A-1'}, db=None))
```

**Yaad rakho:** Model prastaav deta hai; aapka code faisla karta hai. Kisi action se pehle aakhri check model output kabhi na ho.

**Aam galti:** Model ke apne 'confidence: 0.98' field par aise bharosa karna jaise wo calibrated probability ho.

Practice: `examples/02_choosing_between_rules_ml_and_llms.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Task decomposition

### Aasaan Bhasha

Eigenvectors wo directions hain jinhe matrix sirf khinchta hai, ghumata nahi; eigenvalue khinchne ka factor hai. SVD isi ko har matrix ke liye general kar deta hai aur PCA, low-rank compression aur LoRA adapters ke peeche yahi engine hai.

### Chhota code

```python
import numpy as np

X = np.random.default_rng(0).normal(size=(100, 5))
U, S, Vt = np.linalg.svd(X, full_matrices=False)
print('singular values', np.round(S, 2))

energy = np.cumsum(S ** 2) / np.sum(S ** 2)
print('variance kept by first 2 dims:', round(float(energy[1]), 3))
```

**Yaad rakho:** Descending order me sorted singular values batate hain ki kitne dimensions me sach me information hai.

**Aam galti:** Bina scaling ke PCA/SVD chalana, jisse sabse badi unit wala column har component par chha jaata hai.

Practice: `examples/03_task_decomposition.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Deterministic scaffolding around a stochastic core

### Aasaan Bhasha

Stochastic hisse ko sabse chhote possible dabbe me rakho. Deterministic code tay kare ki kya call karna hai, jo wapas aaye use validate kare, aur permissions lagu kare; model beech me bas dhundhla bhaasha wala kaam kare. Un dono ke beech ki har seemaa ek validation ki jagah hai.

### Chhota code

```python
def extract_and_act(text, model_call, db):
    raw = model_call(text)                       # 1. fuzzy: model reads language
    try:                                          # 2. deterministic: validate
        amount = float(raw['amount'])
        account = str(raw['account'])
    except (KeyError, ValueError, TypeError):
        return {'status': 'rejected', 'reason': 'unparseable model output'}
    if not 0 < amount <= 10_000:                  # 3. deterministic: business rules
        return {'status': 'escalate', 'reason': 'amount outside auto-approve band'}
    return {'status': 'approved', 'account': account, 'amount': amount}

print(extract_and_act('refund 500', lambda t: {'amount': '500', 'account': 'A-1'}, db=None))
print(extract_and_act('refund lots', lambda t: {'amount': '99000', 'account': 'A-1'}, db=None))
```

**Yaad rakho:** Model prastaav deta hai; aapka code faisla karta hai. Kisi action se pehle aakhri check model output kabhi na ho.

**Aam galti:** Model ke apne 'confidence: 0.98' field par aise bharosa karna jaise wo calibrated probability ho.

Practice: `examples/04_deterministic_scaffolding_around_a_stoch.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Where to put validation

### Aasaan Bhasha

Stochastic hisse ko sabse chhote possible dabbe me rakho. Deterministic code tay kare ki kya call karna hai, jo wapas aaye use validate kare, aur permissions lagu kare; model beech me bas dhundhla bhaasha wala kaam kare. Un dono ke beech ki har seemaa ek validation ki jagah hai.

### Chhota code

```python
def extract_and_act(text, model_call, db):
    raw = model_call(text)                       # 1. fuzzy: model reads language
    try:                                          # 2. deterministic: validate
        amount = float(raw['amount'])
        account = str(raw['account'])
    except (KeyError, ValueError, TypeError):
        return {'status': 'rejected', 'reason': 'unparseable model output'}
    if not 0 < amount <= 10_000:                  # 3. deterministic: business rules
        return {'status': 'escalate', 'reason': 'amount outside auto-approve band'}
    return {'status': 'approved', 'account': account, 'amount': amount}

print(extract_and_act('refund 500', lambda t: {'amount': '500', 'account': 'A-1'}, db=None))
print(extract_and_act('refund lots', lambda t: {'amount': '99000', 'account': 'A-1'}, db=None))
```

**Yaad rakho:** Model prastaav deta hai; aapka code faisla karta hai. Kisi action se pehle aakhri check model output kabhi na ho.

**Aam galti:** Model ke apne 'confidence: 0.98' field par aise bharosa karna jaise wo calibrated probability ho.

Practice: `examples/05_where_to_put_validation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Failure budgets

### Aasaan Bhasha

Stochastic hisse ko sabse chhote possible dabbe me rakho. Deterministic code tay kare ki kya call karna hai, jo wapas aaye use validate kare, aur permissions lagu kare; model beech me bas dhundhla bhaasha wala kaam kare. Un dono ke beech ki har seemaa ek validation ki jagah hai.

### Chhota code

```python
def extract_and_act(text, model_call, db):
    raw = model_call(text)                       # 1. fuzzy: model reads language
    try:                                          # 2. deterministic: validate
        amount = float(raw['amount'])
        account = str(raw['account'])
    except (KeyError, ValueError, TypeError):
        return {'status': 'rejected', 'reason': 'unparseable model output'}
    if not 0 < amount <= 10_000:                  # 3. deterministic: business rules
        return {'status': 'escalate', 'reason': 'amount outside auto-approve band'}
    return {'status': 'approved', 'account': account, 'amount': amount}

print(extract_and_act('refund 500', lambda t: {'amount': '500', 'account': 'A-1'}, db=None))
print(extract_and_act('refund lots', lambda t: {'amount': '99000', 'account': 'A-1'}, db=None))
```

**Yaad rakho:** Model prastaav deta hai; aapka code faisla karta hai. Kisi action se pehle aakhri check model output kabhi na ho.

**Aam galti:** Model ke apne 'confidence: 0.98' field par aise bharosa karna jaise wo calibrated probability ho.

Practice: `examples/06_failure_budgets.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Human-in-the-loop design

### Aasaan Bhasha

Stochastic hisse ko sabse chhote possible dabbe me rakho. Deterministic code tay kare ki kya call karna hai, jo wapas aaye use validate kare, aur permissions lagu kare; model beech me bas dhundhla bhaasha wala kaam kare. Un dono ke beech ki har seemaa ek validation ki jagah hai.

### Chhota code

```python
def extract_and_act(text, model_call, db):
    raw = model_call(text)                       # 1. fuzzy: model reads language
    try:                                          # 2. deterministic: validate
        amount = float(raw['amount'])
        account = str(raw['account'])
    except (KeyError, ValueError, TypeError):
        return {'status': 'rejected', 'reason': 'unparseable model output'}
    if not 0 < amount <= 10_000:                  # 3. deterministic: business rules
        return {'status': 'escalate', 'reason': 'amount outside auto-approve band'}
    return {'status': 'approved', 'account': account, 'amount': amount}

print(extract_and_act('refund 500', lambda t: {'amount': '500', 'account': 'A-1'}, db=None))
print(extract_and_act('refund lots', lambda t: {'amount': '99000', 'account': 'A-1'}, db=None))
```

**Yaad rakho:** Model prastaav deta hai; aapka code faisla karta hai. Kisi action se pehle aakhri check model output kabhi na ho.

**Aam galti:** Model ke apne 'confidence: 0.98' field par aise bharosa karna jaise wo calibrated probability ho.

Practice: `examples/07_human_in_the_loop_design.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Cost modelling before building

### Aasaan Bhasha

Projects wahi jagah hain jahan seekha hua chipakta hai. Pehle ek patli end-to-end slice banao — data load, kuch bewakoof train, evaluate, ek prediction serve — phir ek-ek layer sudharo. Pehle din chalne wala baseline us perfect model se behtar hai jo kabhi ship hi nahi hota.

### Chhota code

```python
STEPS = [
    '1. Define the decision the model supports and the metric that measures it',
    '2. Get the data; write the loader; assert the schema',
    '3. Dumb baseline (mean / majority class) -> this is the bar',
    '4. Simple model + honest validation split',
    '5. Error analysis: look at 30 wrong predictions by hand',
    '6. Improve the biggest error bucket, not the leaderboard',
    '7. Serve it, log inputs and outputs, monitor drift',
]
for s in STEPS:
    print(s)
```

**Yaad rakho:** Hyperparameters tune karne me ek din lagane se pehle galat predictions dekhne me ek ghanta lagao.

**Aam galti:** Chhe hafte feature engineering karna bina kisi baseline ke jo sabit kare ki kisi cheez se fayda hua.

Practice: `examples/08_cost_modelling_before_building.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Latency budgets

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

Practice: `examples/09_latency_budgets.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Writing an LLM system design doc

### Aasaan Bhasha

Stochastic hisse ko sabse chhote possible dabbe me rakho. Deterministic code tay kare ki kya call karna hai, jo wapas aaye use validate kare, aur permissions lagu kare; model beech me bas dhundhla bhaasha wala kaam kare. Un dono ke beech ki har seemaa ek validation ki jagah hai.

### Chhota code

```python
def extract_and_act(text, model_call, db):
    raw = model_call(text)                       # 1. fuzzy: model reads language
    try:                                          # 2. deterministic: validate
        amount = float(raw['amount'])
        account = str(raw['account'])
    except (KeyError, ValueError, TypeError):
        return {'status': 'rejected', 'reason': 'unparseable model output'}
    if not 0 < amount <= 10_000:                  # 3. deterministic: business rules
        return {'status': 'escalate', 'reason': 'amount outside auto-approve band'}
    return {'status': 'approved', 'account': account, 'amount': amount}

print(extract_and_act('refund 500', lambda t: {'amount': '500', 'account': 'A-1'}, db=None))
print(extract_and_act('refund lots', lambda t: {'amount': '99000', 'account': 'A-1'}, db=None))
```

**Yaad rakho:** Model prastaav deta hai; aapka code faisla karta hai. Kisi action se pehle aakhri check model output kabhi na ho.

**Aam galti:** Model ke apne 'confidence: 0.98' field par aise bharosa karna jaise wo calibrated probability ho.

Practice: `examples/10_writing_an_llm_system_design_doc.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 150 ke baad aapko ye aana chahiye

- **What LLMs are good and bad at** ko bina notes dekhe kisi dost ko samjha sakna.
- **Choosing between rules, ML and LLMs** ko bina notes dekhe kisi dost ko samjha sakna.
- **Task decomposition** ko bina notes dekhe kisi dost ko samjha sakna.
- **Deterministic scaffolding around a stochastic core** ko bina notes dekhe kisi dost ko samjha sakna.
- **Where to put validation** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
