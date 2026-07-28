# Day 189 — Working on an AI team

Aaj ka goal: **Working on an AI team** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Roles: research, ML engineer, data engineer, product |
| 2 | Writing a design doc |
| 3 | Estimating ML work honestly |
| 4 | Communicating uncertainty to stakeholders |
| 5 | Code review for ML |
| 6 | Sharing datasets and models internally |
| 7 | Documentation that survives handover |
| 8 | Managing expectations about AI |
| 9 | Prioritising with limited compute |
| 10 | Making a research result shippable |

---

## 1. Roles: research, ML engineer, data engineer, product

### Aasaan Bhasha

ML estimates isliye bharosemand nahi hote kyunki jab tak aap dekh na lo, aapko pata hi nahi hota ki signal hai bhi ya nahi. Phases me estimate do, kill criteria ke saath: 'do hafte ye dekhne ke liye ki baseline rule ko haraata hai; nahi to hum ruk jaayenge'. Stakeholders uncertainty ko chhooti hui deadline se kahin behtar sweekar karte hain.

### Chhota code

```python
PLAN = [
    ('Phase 0: feasibility', '1 week',  'Does a baseline beat the current rule at all?'),
    ('Phase 1: baseline',    '2 weeks', 'Honest CV score + error analysis'),
    ('Phase 2: productionise','3 weeks', 'Serving, monitoring, fallback path'),
    ('Phase 3: iterate',     'ongoing', 'Flywheel from real feedback'),
]
for name, dur, gate in PLAN:
    print(f'{name:<24} {dur:<9} kill criterion: {gate}')
print('\nEach phase can end the project. That is the point.')
```

**Yaad rakho:** Ranges aur kill criteria do, kabhi bhi aise kaam ki ek fix date nahi jiski feasibility hi unknown hai.

**Aam galti:** Planning meeting me 95% accuracy ka vaada karna, is se pehle ki kisi ne data dekha bhi ho.

Practice: `examples/01_roles_research_ml_engineer_data_engineer.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Writing a design doc

### Aasaan Bhasha

ML estimates isliye bharosemand nahi hote kyunki jab tak aap dekh na lo, aapko pata hi nahi hota ki signal hai bhi ya nahi. Phases me estimate do, kill criteria ke saath: 'do hafte ye dekhne ke liye ki baseline rule ko haraata hai; nahi to hum ruk jaayenge'. Stakeholders uncertainty ko chhooti hui deadline se kahin behtar sweekar karte hain.

### Chhota code

```python
PLAN = [
    ('Phase 0: feasibility', '1 week',  'Does a baseline beat the current rule at all?'),
    ('Phase 1: baseline',    '2 weeks', 'Honest CV score + error analysis'),
    ('Phase 2: productionise','3 weeks', 'Serving, monitoring, fallback path'),
    ('Phase 3: iterate',     'ongoing', 'Flywheel from real feedback'),
]
for name, dur, gate in PLAN:
    print(f'{name:<24} {dur:<9} kill criterion: {gate}')
print('\nEach phase can end the project. That is the point.')
```

**Yaad rakho:** Ranges aur kill criteria do, kabhi bhi aise kaam ki ek fix date nahi jiski feasibility hi unknown hai.

**Aam galti:** Planning meeting me 95% accuracy ka vaada karna, is se pehle ki kisi ne data dekha bhi ho.

Practice: `examples/02_writing_a_design_doc.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Estimating ML work honestly

### Aasaan Bhasha

ML estimates isliye bharosemand nahi hote kyunki jab tak aap dekh na lo, aapko pata hi nahi hota ki signal hai bhi ya nahi. Phases me estimate do, kill criteria ke saath: 'do hafte ye dekhne ke liye ki baseline rule ko haraata hai; nahi to hum ruk jaayenge'. Stakeholders uncertainty ko chhooti hui deadline se kahin behtar sweekar karte hain.

### Chhota code

```python
PLAN = [
    ('Phase 0: feasibility', '1 week',  'Does a baseline beat the current rule at all?'),
    ('Phase 1: baseline',    '2 weeks', 'Honest CV score + error analysis'),
    ('Phase 2: productionise','3 weeks', 'Serving, monitoring, fallback path'),
    ('Phase 3: iterate',     'ongoing', 'Flywheel from real feedback'),
]
for name, dur, gate in PLAN:
    print(f'{name:<24} {dur:<9} kill criterion: {gate}')
print('\nEach phase can end the project. That is the point.')
```

**Yaad rakho:** Ranges aur kill criteria do, kabhi bhi aise kaam ki ek fix date nahi jiski feasibility hi unknown hai.

**Aam galti:** Planning meeting me 95% accuracy ka vaada karna, is se pehle ki kisi ne data dekha bhi ho.

Practice: `examples/03_estimating_ml_work_honestly.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Communicating uncertainty to stakeholders

### Aasaan Bhasha

ML estimates isliye bharosemand nahi hote kyunki jab tak aap dekh na lo, aapko pata hi nahi hota ki signal hai bhi ya nahi. Phases me estimate do, kill criteria ke saath: 'do hafte ye dekhne ke liye ki baseline rule ko haraata hai; nahi to hum ruk jaayenge'. Stakeholders uncertainty ko chhooti hui deadline se kahin behtar sweekar karte hain.

### Chhota code

```python
PLAN = [
    ('Phase 0: feasibility', '1 week',  'Does a baseline beat the current rule at all?'),
    ('Phase 1: baseline',    '2 weeks', 'Honest CV score + error analysis'),
    ('Phase 2: productionise','3 weeks', 'Serving, monitoring, fallback path'),
    ('Phase 3: iterate',     'ongoing', 'Flywheel from real feedback'),
]
for name, dur, gate in PLAN:
    print(f'{name:<24} {dur:<9} kill criterion: {gate}')
print('\nEach phase can end the project. That is the point.')
```

**Yaad rakho:** Ranges aur kill criteria do, kabhi bhi aise kaam ki ek fix date nahi jiski feasibility hi unknown hai.

**Aam galti:** Planning meeting me 95% accuracy ka vaada karna, is se pehle ki kisi ne data dekha bhi ho.

Practice: `examples/04_communicating_uncertainty_to_stakeholder.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Code review for ML

### Aasaan Bhasha

ML estimates isliye bharosemand nahi hote kyunki jab tak aap dekh na lo, aapko pata hi nahi hota ki signal hai bhi ya nahi. Phases me estimate do, kill criteria ke saath: 'do hafte ye dekhne ke liye ki baseline rule ko haraata hai; nahi to hum ruk jaayenge'. Stakeholders uncertainty ko chhooti hui deadline se kahin behtar sweekar karte hain.

### Chhota code

```python
PLAN = [
    ('Phase 0: feasibility', '1 week',  'Does a baseline beat the current rule at all?'),
    ('Phase 1: baseline',    '2 weeks', 'Honest CV score + error analysis'),
    ('Phase 2: productionise','3 weeks', 'Serving, monitoring, fallback path'),
    ('Phase 3: iterate',     'ongoing', 'Flywheel from real feedback'),
]
for name, dur, gate in PLAN:
    print(f'{name:<24} {dur:<9} kill criterion: {gate}')
print('\nEach phase can end the project. That is the point.')
```

**Yaad rakho:** Ranges aur kill criteria do, kabhi bhi aise kaam ki ek fix date nahi jiski feasibility hi unknown hai.

**Aam galti:** Planning meeting me 95% accuracy ka vaada karna, is se pehle ki kisi ne data dekha bhi ho.

Practice: `examples/05_code_review_for_ml.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Sharing datasets and models internally

### Aasaan Bhasha

ML estimates isliye bharosemand nahi hote kyunki jab tak aap dekh na lo, aapko pata hi nahi hota ki signal hai bhi ya nahi. Phases me estimate do, kill criteria ke saath: 'do hafte ye dekhne ke liye ki baseline rule ko haraata hai; nahi to hum ruk jaayenge'. Stakeholders uncertainty ko chhooti hui deadline se kahin behtar sweekar karte hain.

### Chhota code

```python
PLAN = [
    ('Phase 0: feasibility', '1 week',  'Does a baseline beat the current rule at all?'),
    ('Phase 1: baseline',    '2 weeks', 'Honest CV score + error analysis'),
    ('Phase 2: productionise','3 weeks', 'Serving, monitoring, fallback path'),
    ('Phase 3: iterate',     'ongoing', 'Flywheel from real feedback'),
]
for name, dur, gate in PLAN:
    print(f'{name:<24} {dur:<9} kill criterion: {gate}')
print('\nEach phase can end the project. That is the point.')
```

**Yaad rakho:** Ranges aur kill criteria do, kabhi bhi aise kaam ki ek fix date nahi jiski feasibility hi unknown hai.

**Aam galti:** Planning meeting me 95% accuracy ka vaada karna, is se pehle ki kisi ne data dekha bhi ho.

Practice: `examples/06_sharing_datasets_and_models_internally.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Documentation that survives handover

### Aasaan Bhasha

ML estimates isliye bharosemand nahi hote kyunki jab tak aap dekh na lo, aapko pata hi nahi hota ki signal hai bhi ya nahi. Phases me estimate do, kill criteria ke saath: 'do hafte ye dekhne ke liye ki baseline rule ko haraata hai; nahi to hum ruk jaayenge'. Stakeholders uncertainty ko chhooti hui deadline se kahin behtar sweekar karte hain.

### Chhota code

```python
PLAN = [
    ('Phase 0: feasibility', '1 week',  'Does a baseline beat the current rule at all?'),
    ('Phase 1: baseline',    '2 weeks', 'Honest CV score + error analysis'),
    ('Phase 2: productionise','3 weeks', 'Serving, monitoring, fallback path'),
    ('Phase 3: iterate',     'ongoing', 'Flywheel from real feedback'),
]
for name, dur, gate in PLAN:
    print(f'{name:<24} {dur:<9} kill criterion: {gate}')
print('\nEach phase can end the project. That is the point.')
```

**Yaad rakho:** Ranges aur kill criteria do, kabhi bhi aise kaam ki ek fix date nahi jiski feasibility hi unknown hai.

**Aam galti:** Planning meeting me 95% accuracy ka vaada karna, is se pehle ki kisi ne data dekha bhi ho.

Practice: `examples/07_documentation_that_survives_handover.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Managing expectations about AI

### Aasaan Bhasha

ML estimates isliye bharosemand nahi hote kyunki jab tak aap dekh na lo, aapko pata hi nahi hota ki signal hai bhi ya nahi. Phases me estimate do, kill criteria ke saath: 'do hafte ye dekhne ke liye ki baseline rule ko haraata hai; nahi to hum ruk jaayenge'. Stakeholders uncertainty ko chhooti hui deadline se kahin behtar sweekar karte hain.

### Chhota code

```python
PLAN = [
    ('Phase 0: feasibility', '1 week',  'Does a baseline beat the current rule at all?'),
    ('Phase 1: baseline',    '2 weeks', 'Honest CV score + error analysis'),
    ('Phase 2: productionise','3 weeks', 'Serving, monitoring, fallback path'),
    ('Phase 3: iterate',     'ongoing', 'Flywheel from real feedback'),
]
for name, dur, gate in PLAN:
    print(f'{name:<24} {dur:<9} kill criterion: {gate}')
print('\nEach phase can end the project. That is the point.')
```

**Yaad rakho:** Ranges aur kill criteria do, kabhi bhi aise kaam ki ek fix date nahi jiski feasibility hi unknown hai.

**Aam galti:** Planning meeting me 95% accuracy ka vaada karna, is se pehle ki kisi ne data dekha bhi ho.

Practice: `examples/08_managing_expectations_about_ai.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Prioritising with limited compute

### Aasaan Bhasha

Bayes rule evidence ke saath belief update karta hai: posterior = likelihood x prior / evidence. Applied ML ki sabse common galti prior ignore karna hai — 10000 me 1 wali bimari ke liye 99% accurate test bhi zyadatar false positives hi deta hai.

### Chhota code

```python
prior = 1 / 10_000          # base rate of the disease
sensitivity = 0.99          # P(positive | sick)
false_positive = 0.01       # P(positive | healthy)

evidence = sensitivity * prior + false_positive * (1 - prior)
posterior = sensitivity * prior / evidence
print(f'P(sick | positive) = {posterior:.4f}')   # ~0.0098
```

**Yaad rakho:** Rare events par precision gir hi jaati hai, chahe classifier accuracy par kitna bhi accha lage.

**Aam galti:** Imbalanced problem par accuracy report karna jahan hamesha 'no' bolne se 99% mil jaata hai.

Practice: `examples/09_prioritising_with_limited_compute.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Making a research result shippable

### Aasaan Bhasha

ML estimates isliye bharosemand nahi hote kyunki jab tak aap dekh na lo, aapko pata hi nahi hota ki signal hai bhi ya nahi. Phases me estimate do, kill criteria ke saath: 'do hafte ye dekhne ke liye ki baseline rule ko haraata hai; nahi to hum ruk jaayenge'. Stakeholders uncertainty ko chhooti hui deadline se kahin behtar sweekar karte hain.

### Chhota code

```python
PLAN = [
    ('Phase 0: feasibility', '1 week',  'Does a baseline beat the current rule at all?'),
    ('Phase 1: baseline',    '2 weeks', 'Honest CV score + error analysis'),
    ('Phase 2: productionise','3 weeks', 'Serving, monitoring, fallback path'),
    ('Phase 3: iterate',     'ongoing', 'Flywheel from real feedback'),
]
for name, dur, gate in PLAN:
    print(f'{name:<24} {dur:<9} kill criterion: {gate}')
print('\nEach phase can end the project. That is the point.')
```

**Yaad rakho:** Ranges aur kill criteria do, kabhi bhi aise kaam ki ek fix date nahi jiski feasibility hi unknown hai.

**Aam galti:** Planning meeting me 95% accuracy ka vaada karna, is se pehle ki kisi ne data dekha bhi ho.

Practice: `examples/10_making_a_research_result_shippable.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 189 ke baad aapko ye aana chahiye

- **Roles: research, ML engineer, data engineer, product** ko bina notes dekhe kisi dost ko samjha sakna.
- **Writing a design doc** ko bina notes dekhe kisi dost ko samjha sakna.
- **Estimating ML work honestly** ko bina notes dekhe kisi dost ko samjha sakna.
- **Communicating uncertainty to stakeholders** ko bina notes dekhe kisi dost ko samjha sakna.
- **Code review for ML** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
