# Day 161 — Memory for AI applications

Aaj ka goal: **Memory for AI applications** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Short-term context vs long-term memory |
| 2 | Conversation summarisation |
| 3 | Fact extraction and storage |
| 4 | Vector memory and its failure modes |
| 5 | Structured memory in a database |
| 6 | Recency, relevance and importance scoring |
| 7 | Forgetting and expiry |
| 8 | Privacy and user control over memory |
| 9 | Memory conflicts and contradictions |
| 10 | Designing a memory schema |

---

## 1. Short-term context vs long-term memory

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

Practice: `examples/01_short_term_context_vs_long_term_memory.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Conversation summarisation

### Aasaan Bhasha

Context window se badi documents ke liye tree me summarise karo: chunk karo, har ek ka summary banao, phir summaries ka summary. Har level par detail khoti hai, isliye jo cheezein bachni hi chahiye (numbers, naam, decisions) unhe prose ke saath structured extraction me alag rakho.

### Chhota code

```python
def map_reduce_summarize(chunks, summarize, combine_at=4):
    level = [summarize(c) for c in chunks]
    rounds = 1
    while len(level) > 1:
        level = [summarize(' '.join(level[i:i + combine_at]))
                 for i in range(0, len(level), combine_at)]
        rounds += 1
    return level[0], rounds

fake = lambda t: t[:40]
docs = [f'section {i} content ' * 5 for i in range(9)]
summary, rounds = map_reduce_summarize(docs, fake)
print(f'{len(docs)} chunks -> {rounds} rounds -> {summary!r}')
```

**Yaad rakho:** Facts structurally extract karo aur prose alag se summarise karo — summarisation sabse pehle numbers khoti hai.

**Aam galti:** Summary ki quality ROUGE se aankna, jo word overlap ko inaam deta hai aur sach hone ki parwah nahi karta.

Practice: `examples/02_conversation_summarisation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Fact extraction and storage

### Aasaan Bhasha

RAG jawaabon ko aapke documents me jodta hai: chunk karo, embed karo, store karo, sawaal ke liye top-k retrieve karo, aur prompt me daal do. Retrieval ki quality hi poora khel hai — galat teen chunks se perfect model ka jawab bhi galat hi rahega.

### Chhota code

```python
import numpy as np

docs = [
    'Refunds are processed within 5 business days.',
    'Our office is in Pune, open 9am to 6pm.',
    'Enterprise plans include a dedicated support engineer.',
]

def fake_embed(text):                       # stand-in for a real embedding model
    rng = np.random.default_rng(abs(hash(text)) % (2 ** 32))
    v = rng.normal(size=32)
    return v / np.linalg.norm(v)

index = np.array([fake_embed(d) for d in docs])
q = fake_embed('how long do refunds take')
top = int(np.argmax(index @ q))
print('retrieved:', docs[top])
print('\\nReal pipeline: chunk 300-800 tokens with overlap -> embed -> ANN index -> rerank -> prompt.')
```

**Yaad rakho:** Jawab me har retrieved chunk ka source dikhao taaki users use verify kar sakein.

**Aam galti:** Aankh band karke 1000 characters par chunk karna aur tables aur code blocks ko beech se kaat dena.

Practice: `examples/03_fact_extraction_and_storage.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Vector memory and its failure modes

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

Practice: `examples/04_vector_memory_and_its_failure_modes.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Structured memory in a database

### Aasaan Bhasha

Aaj ka idea — **Structured memory in a database** — Memory for AI applications ke theme ke andar aata hai. Ise trivia nahi, ek tool ki tarah padho: ye kaam kya karta hai, aapke data ke baare me kya maan kar chalta hai, aur wo maanyata jhooth nikle to kya tootta hai?

### Chhota code

```python
# Explore: Structured memory in a database
print("practice: Structured memory in a database")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Yaad rakho:** `Structured memory in a database` use karne se pehle ek assumption likho jo ye aapke data ke baare me maanta hai.

**Aam galti:** `Structured memory in a database` ko tutorial se copy-paste kar lena bina jaane ki wo kya maanta hai aur kab fail hota hai.

Practice: `examples/05_structured_memory_in_a_database.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Recency, relevance and importance scoring

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

Practice: `examples/06_recency_relevance_and_importance_scoring.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Forgetting and expiry

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

Practice: `examples/07_forgetting_and_expiry.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Privacy and user control over memory

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

Practice: `examples/08_privacy_and_user_control_over_memory.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Memory conflicts and contradictions

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

Practice: `examples/09_memory_conflicts_and_contradictions.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Designing a memory schema

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

Practice: `examples/10_designing_a_memory_schema.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 161 ke baad aapko ye aana chahiye

- **Short-term context vs long-term memory** ko bina notes dekhe kisi dost ko samjha sakna.
- **Conversation summarisation** ko bina notes dekhe kisi dost ko samjha sakna.
- **Fact extraction and storage** ko bina notes dekhe kisi dost ko samjha sakna.
- **Vector memory and its failure modes** ko bina notes dekhe kisi dost ko samjha sakna.
- **Structured memory in a database** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
