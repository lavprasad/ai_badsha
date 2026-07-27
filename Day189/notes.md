# Day 189 — Working on an AI team

Today's goal: work through **working on an ai team** — ten concepts, ten runnable examples, five questions.

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

ML estimates are unreliable because you do not know if the signal exists until you look. Estimate in phases with kill criteria: 'two weeks to establish whether a baseline beats the rule; if not, we stop'. Stakeholders accept uncertainty far better than a missed deadline.

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

**Remember:** Give ranges and kill criteria, never a single date for work whose feasibility is unknown.

**Common mistake:** Promising 95% accuracy in a planning meeting before anyone has looked at the data.

## 2. Writing a design doc

ML estimates are unreliable because you do not know if the signal exists until you look. Estimate in phases with kill criteria: 'two weeks to establish whether a baseline beats the rule; if not, we stop'. Stakeholders accept uncertainty far better than a missed deadline.

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

**Remember:** Give ranges and kill criteria, never a single date for work whose feasibility is unknown.

**Common mistake:** Promising 95% accuracy in a planning meeting before anyone has looked at the data.

## 3. Estimating ML work honestly

ML estimates are unreliable because you do not know if the signal exists until you look. Estimate in phases with kill criteria: 'two weeks to establish whether a baseline beats the rule; if not, we stop'. Stakeholders accept uncertainty far better than a missed deadline.

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

**Remember:** Give ranges and kill criteria, never a single date for work whose feasibility is unknown.

**Common mistake:** Promising 95% accuracy in a planning meeting before anyone has looked at the data.

## 4. Communicating uncertainty to stakeholders

ML estimates are unreliable because you do not know if the signal exists until you look. Estimate in phases with kill criteria: 'two weeks to establish whether a baseline beats the rule; if not, we stop'. Stakeholders accept uncertainty far better than a missed deadline.

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

**Remember:** Give ranges and kill criteria, never a single date for work whose feasibility is unknown.

**Common mistake:** Promising 95% accuracy in a planning meeting before anyone has looked at the data.

## 5. Code review for ML

ML estimates are unreliable because you do not know if the signal exists until you look. Estimate in phases with kill criteria: 'two weeks to establish whether a baseline beats the rule; if not, we stop'. Stakeholders accept uncertainty far better than a missed deadline.

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

**Remember:** Give ranges and kill criteria, never a single date for work whose feasibility is unknown.

**Common mistake:** Promising 95% accuracy in a planning meeting before anyone has looked at the data.

## 6. Sharing datasets and models internally

ML estimates are unreliable because you do not know if the signal exists until you look. Estimate in phases with kill criteria: 'two weeks to establish whether a baseline beats the rule; if not, we stop'. Stakeholders accept uncertainty far better than a missed deadline.

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

**Remember:** Give ranges and kill criteria, never a single date for work whose feasibility is unknown.

**Common mistake:** Promising 95% accuracy in a planning meeting before anyone has looked at the data.

## 7. Documentation that survives handover

ML estimates are unreliable because you do not know if the signal exists until you look. Estimate in phases with kill criteria: 'two weeks to establish whether a baseline beats the rule; if not, we stop'. Stakeholders accept uncertainty far better than a missed deadline.

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

**Remember:** Give ranges and kill criteria, never a single date for work whose feasibility is unknown.

**Common mistake:** Promising 95% accuracy in a planning meeting before anyone has looked at the data.

## 8. Managing expectations about AI

ML estimates are unreliable because you do not know if the signal exists until you look. Estimate in phases with kill criteria: 'two weeks to establish whether a baseline beats the rule; if not, we stop'. Stakeholders accept uncertainty far better than a missed deadline.

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

**Remember:** Give ranges and kill criteria, never a single date for work whose feasibility is unknown.

**Common mistake:** Promising 95% accuracy in a planning meeting before anyone has looked at the data.

## 9. Prioritising with limited compute

Bayes' rule updates a belief with evidence: posterior = likelihood x prior / evidence. The most common mistake in applied ML is ignoring the prior — a 99%-accurate test for a 1-in-10000 disease still gives mostly false positives.

```python
prior = 1 / 10_000          # base rate of the disease
sensitivity = 0.99          # P(positive | sick)
false_positive = 0.01       # P(positive | healthy)

evidence = sensitivity * prior + false_positive * (1 - prior)
posterior = sensitivity * prior / evidence
print(f'P(sick | positive) = {posterior:.4f}')   # ~0.0098
```

**Remember:** Rare events make precision collapse no matter how good the classifier looks on accuracy.

**Common mistake:** Reporting accuracy on an imbalanced problem where predicting 'no' always scores 99%.

## 10. Making a research result shippable

ML estimates are unreliable because you do not know if the signal exists until you look. Estimate in phases with kill criteria: 'two weeks to establish whether a baseline beats the rule; if not, we stop'. Stakeholders accept uncertainty far better than a missed deadline.

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

**Remember:** Give ranges and kill criteria, never a single date for work whose feasibility is unknown.

**Common mistake:** Promising 95% accuracy in a planning meeting before anyone has looked at the data.

---

## What you should be able to do after Day 189

- Explain **Roles: research, ML engineer, data engineer, product** to someone else without notes.
- Explain **Writing a design doc** to someone else without notes.
- Explain **Estimating ML work honestly** to someone else without notes.
- Explain **Communicating uncertainty to stakeholders** to someone else without notes.
- Explain **Code review for ML** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
