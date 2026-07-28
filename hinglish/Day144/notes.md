# Day 144 — Knowledge in language models

Aaj ka goal: **Knowledge in language models** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Parametric vs retrieved knowledge |
| 2 | Knowledge cutoffs |
| 3 | Model editing |
| 4 | Knowledge graphs alongside LLMs |
| 5 | Entity linking |
| 6 | Fact verification |
| 7 | Temporal reasoning failures |
| 8 | Numerical and counting weaknesses |
| 9 | When to use a database instead |
| 10 | Designing the knowledge boundary |

---

## 1. Parametric vs retrieved knowledge

### Aasaan Bhasha

Model ke weights me duniya ka ek jama hua, lossy snapshot hai, uske cutoff tak. Jo bhi badalta hai — prices, policies, staff, inventory — wo database ya retrieval index me hona chahiye, weights me nahi. Ye lakeer saaf khinch do aur hallucination rate kaafi gir jaata hai.

### Chhota code

```python
KNOWLEDGE_ROUTING = {
    'current account balance':  'database — never the model',
    'company refund policy':    'retrieval from the policy doc',
    'what is a p-value':        'model weights are fine',
    'yesterday\'s ticket count': 'database aggregate',
    'summarise this email':     'model, with the email in context',
}
for question, source in KNOWLEDGE_ROUTING.items():
    print(f'{question:<28} -> {source}')
print('\nRule: if it can change without a retrain, it must not live in weights.')
```

**Yaad rakho:** Agar koi fact kal badal sakta hai, to use retrieve karo. Agar nahi badal sakta, to weights use rakh sakte hain.

**Aam galti:** Prices ko model me fine-tune kar dena aur har price list update par poora job dobara chalana.

Practice: `examples/01_parametric_vs_retrieved_knowledge.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Knowledge cutoffs

### Aasaan Bhasha

Model ke weights me duniya ka ek jama hua, lossy snapshot hai, uske cutoff tak. Jo bhi badalta hai — prices, policies, staff, inventory — wo database ya retrieval index me hona chahiye, weights me nahi. Ye lakeer saaf khinch do aur hallucination rate kaafi gir jaata hai.

### Chhota code

```python
KNOWLEDGE_ROUTING = {
    'current account balance':  'database — never the model',
    'company refund policy':    'retrieval from the policy doc',
    'what is a p-value':        'model weights are fine',
    'yesterday\'s ticket count': 'database aggregate',
    'summarise this email':     'model, with the email in context',
}
for question, source in KNOWLEDGE_ROUTING.items():
    print(f'{question:<28} -> {source}')
print('\nRule: if it can change without a retrain, it must not live in weights.')
```

**Yaad rakho:** Agar koi fact kal badal sakta hai, to use retrieve karo. Agar nahi badal sakta, to weights use rakh sakte hain.

**Aam galti:** Prices ko model me fine-tune kar dena aur har price list update par poora job dobara chalana.

Practice: `examples/02_knowledge_cutoffs.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Model editing

### Aasaan Bhasha

Model ke weights me duniya ka ek jama hua, lossy snapshot hai, uske cutoff tak. Jo bhi badalta hai — prices, policies, staff, inventory — wo database ya retrieval index me hona chahiye, weights me nahi. Ye lakeer saaf khinch do aur hallucination rate kaafi gir jaata hai.

### Chhota code

```python
KNOWLEDGE_ROUTING = {
    'current account balance':  'database — never the model',
    'company refund policy':    'retrieval from the policy doc',
    'what is a p-value':        'model weights are fine',
    'yesterday\'s ticket count': 'database aggregate',
    'summarise this email':     'model, with the email in context',
}
for question, source in KNOWLEDGE_ROUTING.items():
    print(f'{question:<28} -> {source}')
print('\nRule: if it can change without a retrain, it must not live in weights.')
```

**Yaad rakho:** Agar koi fact kal badal sakta hai, to use retrieve karo. Agar nahi badal sakta, to weights use rakh sakte hain.

**Aam galti:** Prices ko model me fine-tune kar dena aur har price list update par poora job dobara chalana.

Practice: `examples/03_model_editing.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Knowledge graphs alongside LLMs

### Aasaan Bhasha

GNN edges ke saath messages bhejta hai: har node apne padosiyon se khud ko update karta hai, k baar, taaki information k hops tak safar kare. Fraud rings, molecules aur social graphs ke liye badhiya — jahan bhi rishte nodes se zyada signal rakhte hain.

### Chhota code

```python
import numpy as np

# One round of mean-aggregation message passing
A = np.array([[0, 1, 1, 0],
              [1, 0, 1, 0],
              [1, 1, 0, 1],
              [0, 0, 1, 0]], dtype=float)
H = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0], [0.5, 0.5]])

deg = A.sum(axis=1, keepdims=True)
H_next = np.tanh((A @ H) / np.maximum(deg, 1))
print(H_next.round(3))
```

**Yaad rakho:** Bahut zyada message-passing layers over-smoothing kar deti hain — har node ek jaisa vector ban jaata hai.

**Aam galti:** Graph data ko randomly split karna, jisse ek node ke apne padosi train aur test dono me aa jaate hain.

Practice: `examples/04_knowledge_graphs_alongside_llms.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Entity linking

### Aasaan Bhasha

Model ke weights me duniya ka ek jama hua, lossy snapshot hai, uske cutoff tak. Jo bhi badalta hai — prices, policies, staff, inventory — wo database ya retrieval index me hona chahiye, weights me nahi. Ye lakeer saaf khinch do aur hallucination rate kaafi gir jaata hai.

### Chhota code

```python
KNOWLEDGE_ROUTING = {
    'current account balance':  'database — never the model',
    'company refund policy':    'retrieval from the policy doc',
    'what is a p-value':        'model weights are fine',
    'yesterday\'s ticket count': 'database aggregate',
    'summarise this email':     'model, with the email in context',
}
for question, source in KNOWLEDGE_ROUTING.items():
    print(f'{question:<28} -> {source}')
print('\nRule: if it can change without a retrain, it must not live in weights.')
```

**Yaad rakho:** Agar koi fact kal badal sakta hai, to use retrieve karo. Agar nahi badal sakta, to weights use rakh sakte hain.

**Aam galti:** Prices ko model me fine-tune kar dena aur har price list update par poora job dobara chalana.

Practice: `examples/05_entity_linking.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Fact verification

### Aasaan Bhasha

Model ke weights me duniya ka ek jama hua, lossy snapshot hai, uske cutoff tak. Jo bhi badalta hai — prices, policies, staff, inventory — wo database ya retrieval index me hona chahiye, weights me nahi. Ye lakeer saaf khinch do aur hallucination rate kaafi gir jaata hai.

### Chhota code

```python
KNOWLEDGE_ROUTING = {
    'current account balance':  'database — never the model',
    'company refund policy':    'retrieval from the policy doc',
    'what is a p-value':        'model weights are fine',
    'yesterday\'s ticket count': 'database aggregate',
    'summarise this email':     'model, with the email in context',
}
for question, source in KNOWLEDGE_ROUTING.items():
    print(f'{question:<28} -> {source}')
print('\nRule: if it can change without a retrain, it must not live in weights.')
```

**Yaad rakho:** Agar koi fact kal badal sakta hai, to use retrieve karo. Agar nahi badal sakta, to weights use rakh sakte hain.

**Aam galti:** Prices ko model me fine-tune kar dena aur har price list update par poora job dobara chalana.

Practice: `examples/06_fact_verification.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Temporal reasoning failures

### Aasaan Bhasha

Model ke weights me duniya ka ek jama hua, lossy snapshot hai, uske cutoff tak. Jo bhi badalta hai — prices, policies, staff, inventory — wo database ya retrieval index me hona chahiye, weights me nahi. Ye lakeer saaf khinch do aur hallucination rate kaafi gir jaata hai.

### Chhota code

```python
KNOWLEDGE_ROUTING = {
    'current account balance':  'database — never the model',
    'company refund policy':    'retrieval from the policy doc',
    'what is a p-value':        'model weights are fine',
    'yesterday\'s ticket count': 'database aggregate',
    'summarise this email':     'model, with the email in context',
}
for question, source in KNOWLEDGE_ROUTING.items():
    print(f'{question:<28} -> {source}')
print('\nRule: if it can change without a retrain, it must not live in weights.')
```

**Yaad rakho:** Agar koi fact kal badal sakta hai, to use retrieve karo. Agar nahi badal sakta, to weights use rakh sakte hain.

**Aam galti:** Prices ko model me fine-tune kar dena aur har price list update par poora job dobara chalana.

Practice: `examples/07_temporal_reasoning_failures.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Numerical and counting weaknesses

### Aasaan Bhasha

Model ke weights me duniya ka ek jama hua, lossy snapshot hai, uske cutoff tak. Jo bhi badalta hai — prices, policies, staff, inventory — wo database ya retrieval index me hona chahiye, weights me nahi. Ye lakeer saaf khinch do aur hallucination rate kaafi gir jaata hai.

### Chhota code

```python
KNOWLEDGE_ROUTING = {
    'current account balance':  'database — never the model',
    'company refund policy':    'retrieval from the policy doc',
    'what is a p-value':        'model weights are fine',
    'yesterday\'s ticket count': 'database aggregate',
    'summarise this email':     'model, with the email in context',
}
for question, source in KNOWLEDGE_ROUTING.items():
    print(f'{question:<28} -> {source}')
print('\nRule: if it can change without a retrain, it must not live in weights.')
```

**Yaad rakho:** Agar koi fact kal badal sakta hai, to use retrieve karo. Agar nahi badal sakta, to weights use rakh sakte hain.

**Aam galti:** Prices ko model me fine-tune kar dena aur har price list update par poora job dobara chalana.

Practice: `examples/08_numerical_and_counting_weaknesses.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. When to use a database instead

### Aasaan Bhasha

Model ke weights me duniya ka ek jama hua, lossy snapshot hai, uske cutoff tak. Jo bhi badalta hai — prices, policies, staff, inventory — wo database ya retrieval index me hona chahiye, weights me nahi. Ye lakeer saaf khinch do aur hallucination rate kaafi gir jaata hai.

### Chhota code

```python
KNOWLEDGE_ROUTING = {
    'current account balance':  'database — never the model',
    'company refund policy':    'retrieval from the policy doc',
    'what is a p-value':        'model weights are fine',
    'yesterday\'s ticket count': 'database aggregate',
    'summarise this email':     'model, with the email in context',
}
for question, source in KNOWLEDGE_ROUTING.items():
    print(f'{question:<28} -> {source}')
print('\nRule: if it can change without a retrain, it must not live in weights.')
```

**Yaad rakho:** Agar koi fact kal badal sakta hai, to use retrieve karo. Agar nahi badal sakta, to weights use rakh sakte hain.

**Aam galti:** Prices ko model me fine-tune kar dena aur har price list update par poora job dobara chalana.

Practice: `examples/09_when_to_use_a_database_instead.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Designing the knowledge boundary

### Aasaan Bhasha

Model ke weights me duniya ka ek jama hua, lossy snapshot hai, uske cutoff tak. Jo bhi badalta hai — prices, policies, staff, inventory — wo database ya retrieval index me hona chahiye, weights me nahi. Ye lakeer saaf khinch do aur hallucination rate kaafi gir jaata hai.

### Chhota code

```python
KNOWLEDGE_ROUTING = {
    'current account balance':  'database — never the model',
    'company refund policy':    'retrieval from the policy doc',
    'what is a p-value':        'model weights are fine',
    'yesterday\'s ticket count': 'database aggregate',
    'summarise this email':     'model, with the email in context',
}
for question, source in KNOWLEDGE_ROUTING.items():
    print(f'{question:<28} -> {source}')
print('\nRule: if it can change without a retrain, it must not live in weights.')
```

**Yaad rakho:** Agar koi fact kal badal sakta hai, to use retrieve karo. Agar nahi badal sakta, to weights use rakh sakte hain.

**Aam galti:** Prices ko model me fine-tune kar dena aur har price list update par poora job dobara chalana.

Practice: `examples/10_designing_the_knowledge_boundary.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 144 ke baad aapko ye aana chahiye

- **Parametric vs retrieved knowledge** ko bina notes dekhe kisi dost ko samjha sakna.
- **Knowledge cutoffs** ko bina notes dekhe kisi dost ko samjha sakna.
- **Model editing** ko bina notes dekhe kisi dost ko samjha sakna.
- **Knowledge graphs alongside LLMs** ko bina notes dekhe kisi dost ko samjha sakna.
- **Entity linking** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
