# Day 138 — Conversational systems

Aaj ka goal: **Conversational systems** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Turns, roles and system prompts |
| 2 | Conversation state and memory |
| 3 | Context window management |
| 4 | Summarising older turns |
| 5 | Persona and tone control |
| 6 | Handling out-of-scope requests |
| 7 | Escalation to a human |
| 8 | Multi-turn evaluation |
| 9 | Latency perception and streaming |
| 10 | Building a grounded support bot |

---

## 1. Turns, roles and system prompts

### Aasaan Bhasha

Prompt English me likha gaya program hai. Role, task, format aur constraints ke baare me specific raho. Few-shot examples format kisi bhi description se behtar sikhaate hain. Reasoning steps maangna multi-step problems par madad karta hai aur simple lookups par tokens barbaad karta hai.

### Chhota code

```python
prompt = '''You are a support triage assistant.

Classify the ticket into exactly one of: BILLING, BUG, FEATURE, OTHER.
Return JSON only: {"label": ..., "confidence": 0.0-1.0}

Examples:
Ticket: "charged twice this month" -> {"label": "BILLING", "confidence": 0.95}
Ticket: "app crashes on upload"    -> {"label": "BUG", "confidence": 0.92}

Ticket: "can you add dark mode?"
'''
print(prompt)
print('Structure: role -> task -> allowed outputs -> format -> examples -> input.')
```

**Yaad rakho:** Output format sabse aakhir me rakho aur use example ki tarah dikhao — models sabse paas wala pattern copy karte hain.

**Aam galti:** Dhundhla prompt likhna, dhundhla output paana, aur model ko dosh dena.

Practice: `examples/01_turns_roles_and_system_prompts.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Conversation state and memory

### Aasaan Bhasha

Context memory nahi hai. Context wo hai jo is request me aata hai; memory wo hai jise aap jaan-boojh kar store aur retrieve karte ho. Schema explicitly design karo — kya store hoga, kaise expire hoga, conflicts kaise sulajhenge — warna aapko aisa assistant milega jo wo baat pooray vishwas se dohraata hai jo user ne pichhle mahine sudhar di thi.

### Chhota code

```python
import time

class Memory:
    def __init__(self, ttl_days=90):
        self.items, self.ttl = [], ttl_days * 86400

    def add(self, key, value, ts):
        self.items = [i for i in self.items if i['key'] != key]   # newest wins
        self.items.append({'key': key, 'value': value, 'ts': ts})

    def recall(self, now):
        return [i for i in self.items if now - i['ts'] < self.ttl]

m = Memory(ttl_days=30)
m.add('preferred_name', 'Sam', ts=0)
m.add('preferred_name', 'Samir', ts=100)      # correction replaces, not appends
print(m.recall(now=200))
print(m.recall(now=30 * 86400 + 200))          # expired
```

**Yaad rakho:** Correction ko overwrite karna chahiye, saath rehna nahi. Do ulti memories dono retrieve ho jaayengi.

**Aam galti:** Har kahi hui baat hamesha ke liye vector store me jod dena, jisse purani aur sudhri hui baatein retrieval par ladti hain.

Practice: `examples/02_conversation_state_and_memory.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Context window management

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

Practice: `examples/03_context_window_management.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Summarising older turns

### Aasaan Bhasha

Context memory nahi hai. Context wo hai jo is request me aata hai; memory wo hai jise aap jaan-boojh kar store aur retrieve karte ho. Schema explicitly design karo — kya store hoga, kaise expire hoga, conflicts kaise sulajhenge — warna aapko aisa assistant milega jo wo baat pooray vishwas se dohraata hai jo user ne pichhle mahine sudhar di thi.

### Chhota code

```python
import time

class Memory:
    def __init__(self, ttl_days=90):
        self.items, self.ttl = [], ttl_days * 86400

    def add(self, key, value, ts):
        self.items = [i for i in self.items if i['key'] != key]   # newest wins
        self.items.append({'key': key, 'value': value, 'ts': ts})

    def recall(self, now):
        return [i for i in self.items if now - i['ts'] < self.ttl]

m = Memory(ttl_days=30)
m.add('preferred_name', 'Sam', ts=0)
m.add('preferred_name', 'Samir', ts=100)      # correction replaces, not appends
print(m.recall(now=200))
print(m.recall(now=30 * 86400 + 200))          # expired
```

**Yaad rakho:** Correction ko overwrite karna chahiye, saath rehna nahi. Do ulti memories dono retrieve ho jaayengi.

**Aam galti:** Har kahi hui baat hamesha ke liye vector store me jod dena, jisse purani aur sudhri hui baatein retrieval par ladti hain.

Practice: `examples/04_summarising_older_turns.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Persona and tone control

### Aasaan Bhasha

Context memory nahi hai. Context wo hai jo is request me aata hai; memory wo hai jise aap jaan-boojh kar store aur retrieve karte ho. Schema explicitly design karo — kya store hoga, kaise expire hoga, conflicts kaise sulajhenge — warna aapko aisa assistant milega jo wo baat pooray vishwas se dohraata hai jo user ne pichhle mahine sudhar di thi.

### Chhota code

```python
import time

class Memory:
    def __init__(self, ttl_days=90):
        self.items, self.ttl = [], ttl_days * 86400

    def add(self, key, value, ts):
        self.items = [i for i in self.items if i['key'] != key]   # newest wins
        self.items.append({'key': key, 'value': value, 'ts': ts})

    def recall(self, now):
        return [i for i in self.items if now - i['ts'] < self.ttl]

m = Memory(ttl_days=30)
m.add('preferred_name', 'Sam', ts=0)
m.add('preferred_name', 'Samir', ts=100)      # correction replaces, not appends
print(m.recall(now=200))
print(m.recall(now=30 * 86400 + 200))          # expired
```

**Yaad rakho:** Correction ko overwrite karna chahiye, saath rehna nahi. Do ulti memories dono retrieve ho jaayengi.

**Aam galti:** Har kahi hui baat hamesha ke liye vector store me jod dena, jisse purani aur sudhri hui baatein retrieval par ladti hain.

Practice: `examples/05_persona_and_tone_control.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Handling out-of-scope requests

### Aasaan Bhasha

Default arguments ek hi baar evaluate hote hain, function define hone ke waqt. Isliye mutable default (list, dict, set) har call me share hota hai — ye bug aise dikhta hai ki 'mera function pichhli call yaad rakhta hai'. `None` use karo aur asli default andar banao.

### Chhota code

```python
def bad(item, bucket=[]):        # created ONCE
    bucket.append(item)
    return bucket

def good(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket

print(bad(1), bad(2))     # [1] [1, 2]  <- leaked
print(good(1), good(2))   # [1] [2]     <- correct
```

**Yaad rakho:** Default arguments immutable hone chahiye. `None` plus ek check hi standard fix hai.

**Aam galti:** Aisa `def f(x, cache={})` jo process ki har call me chupchap state jama karta rehta hai.

Practice: `examples/06_handling_out_of_scope_requests.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Escalation to a human

### Aasaan Bhasha

Context memory nahi hai. Context wo hai jo is request me aata hai; memory wo hai jise aap jaan-boojh kar store aur retrieve karte ho. Schema explicitly design karo — kya store hoga, kaise expire hoga, conflicts kaise sulajhenge — warna aapko aisa assistant milega jo wo baat pooray vishwas se dohraata hai jo user ne pichhle mahine sudhar di thi.

### Chhota code

```python
import time

class Memory:
    def __init__(self, ttl_days=90):
        self.items, self.ttl = [], ttl_days * 86400

    def add(self, key, value, ts):
        self.items = [i for i in self.items if i['key'] != key]   # newest wins
        self.items.append({'key': key, 'value': value, 'ts': ts})

    def recall(self, now):
        return [i for i in self.items if now - i['ts'] < self.ttl]

m = Memory(ttl_days=30)
m.add('preferred_name', 'Sam', ts=0)
m.add('preferred_name', 'Samir', ts=100)      # correction replaces, not appends
print(m.recall(now=200))
print(m.recall(now=30 * 86400 + 200))          # expired
```

**Yaad rakho:** Correction ko overwrite karna chahiye, saath rehna nahi. Do ulti memories dono retrieve ho jaayengi.

**Aam galti:** Har kahi hui baat hamesha ke liye vector store me jod dena, jisse purani aur sudhri hui baatein retrieval par ladti hain.

Practice: `examples/07_escalation_to_a_human.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Multi-turn evaluation

### Aasaan Bhasha

Vibes prompt change se nahi bachte. Asli inputs ka chhota golden set banao expected outputs ke saath, har change par chalao, aur score track karo. Open-ended quality ke liye LLM judge use karo, par pehle judge ko human ratings se calibrate karo.

### Chhota code

```python
GOLDEN = [
    {'input': 'charged twice', 'expect': 'BILLING'},
    {'input': 'crashes on upload', 'expect': 'BUG'},
    {'input': 'please add dark mode', 'expect': 'FEATURE'},
]

def classify(text):                      # stand-in for the real model call
    t = text.lower()
    if 'charg' in t or 'bill' in t:
        return 'BILLING'
    if 'crash' in t or 'error' in t:
        return 'BUG'
    return 'FEATURE'

hits = sum(classify(c['input']) == c['expect'] for c in GOLDEN)
print(f'eval score {hits}/{len(GOLDEN)}')
assert hits == len(GOLDEN), 'regression: fix before shipping'
```

**Yaad rakho:** Aapke chune hue 50 asli examples 5000 synthetic examples se behtar hain jinhe kisi ne check hi nahi kiya.

**Aam galti:** Shukravaar ko bina eval ke prompt badalna aur somvaar ko customers se pata chalna.

Practice: `examples/08_multi_turn_evaluation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Latency perception and streaming

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

Practice: `examples/09_latency_perception_and_streaming.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Building a grounded support bot

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

Practice: `examples/10_building_a_grounded_support_bot.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 138 ke baad aapko ye aana chahiye

- **Turns, roles and system prompts** ko bina notes dekhe kisi dost ko samjha sakna.
- **Conversation state and memory** ko bina notes dekhe kisi dost ko samjha sakna.
- **Context window management** ko bina notes dekhe kisi dost ko samjha sakna.
- **Summarising older turns** ko bina notes dekhe kisi dost ko samjha sakna.
- **Persona and tone control** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
