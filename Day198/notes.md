# Day 198 — Interview preparation

Today's goal: work through **Interview preparation** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | ML fundamentals questions |
| 2 | Coding rounds and what they test |
| 3 | Case study and system design rounds |
| 4 | Explaining your projects clearly |
| 5 | Handling 'why did you choose that' questions |
| 6 | Discussing failures well |
| 7 | Statistics and probability questions |
| 8 | Take-home assignments |
| 9 | Questions you should ask them |
| 10 | A four-week preparation plan |

---

## 1. ML fundamentals questions

Depth beats breadth in interviews: one project you can defend end-to-end — why that metric, why that split, what failed — beats ten tutorial notebooks. Read papers with the three-pass method: abstract and figures, then method, then details only if you will implement it.

```python
PAPER_CHECKLIST = [
    'What problem, and what was the previous best?',
    'What is the single new idea? (usually one sentence)',
    'What is the evidence? Which baselines, which datasets?',
    'What did they NOT test? (the limitations section is the honest part)',
    'Could I implement the core idea in 50 lines?',
]
for q in PAPER_CHECKLIST:
    print('-', q)
```

**Remember:** If you cannot explain why your validation split is honest, you do not own the project yet.

**Common mistake:** Listing twenty frameworks on a CV and being unable to debug a shape error in any of them.

Practice: open `examples/01_ml_fundamentals_questions.py`, predict the output, change one line, predict again.

## 2. Coding rounds and what they test

Depth beats breadth in interviews: one project you can defend end-to-end — why that metric, why that split, what failed — beats ten tutorial notebooks. Read papers with the three-pass method: abstract and figures, then method, then details only if you will implement it.

```python
PAPER_CHECKLIST = [
    'What problem, and what was the previous best?',
    'What is the single new idea? (usually one sentence)',
    'What is the evidence? Which baselines, which datasets?',
    'What did they NOT test? (the limitations section is the honest part)',
    'Could I implement the core idea in 50 lines?',
]
for q in PAPER_CHECKLIST:
    print('-', q)
```

**Remember:** If you cannot explain why your validation split is honest, you do not own the project yet.

**Common mistake:** Listing twenty frameworks on a CV and being unable to debug a shape error in any of them.

Practice: open `examples/02_coding_rounds_and_what_they_test.py`, predict the output, change one line, predict again.

## 3. Case study and system design rounds

Projects are where the learning sticks. Build a thin end-to-end slice first — load data, train something dumb, evaluate, serve one prediction — then improve one layer at a time. A working baseline on day one beats a perfect model that never ships.

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

**Remember:** Spend an hour looking at wrong predictions before you spend a day tuning hyperparameters.

**Common mistake:** Six weeks of feature engineering with no baseline to prove any of it helped.

Practice: open `examples/03_case_study_and_system_design_rounds.py`, predict the output, change one line, predict again.

## 4. Explaining your projects clearly

Projects are where the learning sticks. Build a thin end-to-end slice first — load data, train something dumb, evaluate, serve one prediction — then improve one layer at a time. A working baseline on day one beats a perfect model that never ships.

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

**Remember:** Spend an hour looking at wrong predictions before you spend a day tuning hyperparameters.

**Common mistake:** Six weeks of feature engineering with no baseline to prove any of it helped.

Practice: open `examples/04_explaining_your_projects_clearly.py`, predict the output, change one line, predict again.

## 5. Handling 'why did you choose that' questions

Depth beats breadth in interviews: one project you can defend end-to-end — why that metric, why that split, what failed — beats ten tutorial notebooks. Read papers with the three-pass method: abstract and figures, then method, then details only if you will implement it.

```python
PAPER_CHECKLIST = [
    'What problem, and what was the previous best?',
    'What is the single new idea? (usually one sentence)',
    'What is the evidence? Which baselines, which datasets?',
    'What did they NOT test? (the limitations section is the honest part)',
    'Could I implement the core idea in 50 lines?',
]
for q in PAPER_CHECKLIST:
    print('-', q)
```

**Remember:** If you cannot explain why your validation split is honest, you do not own the project yet.

**Common mistake:** Listing twenty frameworks on a CV and being unable to debug a shape error in any of them.

Practice: open `examples/05_handling_why_did_you_choose_that_questio.py`, predict the output, change one line, predict again.

## 6. Discussing failures well

Depth beats breadth in interviews: one project you can defend end-to-end — why that metric, why that split, what failed — beats ten tutorial notebooks. Read papers with the three-pass method: abstract and figures, then method, then details only if you will implement it.

```python
PAPER_CHECKLIST = [
    'What problem, and what was the previous best?',
    'What is the single new idea? (usually one sentence)',
    'What is the evidence? Which baselines, which datasets?',
    'What did they NOT test? (the limitations section is the honest part)',
    'Could I implement the core idea in 50 lines?',
]
for q in PAPER_CHECKLIST:
    print('-', q)
```

**Remember:** If you cannot explain why your validation split is honest, you do not own the project yet.

**Common mistake:** Listing twenty frameworks on a CV and being unable to debug a shape error in any of them.

Practice: open `examples/06_discussing_failures_well.py`, predict the output, change one line, predict again.

## 7. Statistics and probability questions

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

Practice: open `examples/07_statistics_and_probability_questions.py`, predict the output, change one line, predict again.

## 8. Take-home assignments

Depth beats breadth in interviews: one project you can defend end-to-end — why that metric, why that split, what failed — beats ten tutorial notebooks. Read papers with the three-pass method: abstract and figures, then method, then details only if you will implement it.

```python
PAPER_CHECKLIST = [
    'What problem, and what was the previous best?',
    'What is the single new idea? (usually one sentence)',
    'What is the evidence? Which baselines, which datasets?',
    'What did they NOT test? (the limitations section is the honest part)',
    'Could I implement the core idea in 50 lines?',
]
for q in PAPER_CHECKLIST:
    print('-', q)
```

**Remember:** If you cannot explain why your validation split is honest, you do not own the project yet.

**Common mistake:** Listing twenty frameworks on a CV and being unable to debug a shape error in any of them.

Practice: open `examples/08_take_home_assignments.py`, predict the output, change one line, predict again.

## 9. Questions you should ask them

Depth beats breadth in interviews: one project you can defend end-to-end — why that metric, why that split, what failed — beats ten tutorial notebooks. Read papers with the three-pass method: abstract and figures, then method, then details only if you will implement it.

```python
PAPER_CHECKLIST = [
    'What problem, and what was the previous best?',
    'What is the single new idea? (usually one sentence)',
    'What is the evidence? Which baselines, which datasets?',
    'What did they NOT test? (the limitations section is the honest part)',
    'Could I implement the core idea in 50 lines?',
]
for q in PAPER_CHECKLIST:
    print('-', q)
```

**Remember:** If you cannot explain why your validation split is honest, you do not own the project yet.

**Common mistake:** Listing twenty frameworks on a CV and being unable to debug a shape error in any of them.

Practice: open `examples/09_questions_you_should_ask_them.py`, predict the output, change one line, predict again.

## 10. A four-week preparation plan

Depth beats breadth in interviews: one project you can defend end-to-end — why that metric, why that split, what failed — beats ten tutorial notebooks. Read papers with the three-pass method: abstract and figures, then method, then details only if you will implement it.

```python
PAPER_CHECKLIST = [
    'What problem, and what was the previous best?',
    'What is the single new idea? (usually one sentence)',
    'What is the evidence? Which baselines, which datasets?',
    'What did they NOT test? (the limitations section is the honest part)',
    'Could I implement the core idea in 50 lines?',
]
for q in PAPER_CHECKLIST:
    print('-', q)
```

**Remember:** If you cannot explain why your validation split is honest, you do not own the project yet.

**Common mistake:** Listing twenty frameworks on a CV and being unable to debug a shape error in any of them.

Practice: open `examples/10_a_four_week_preparation_plan.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 198

- Explain **ML fundamentals questions** to someone else without notes.
- Explain **Coding rounds and what they test** to someone else without notes.
- Explain **Case study and system design rounds** to someone else without notes.
- Explain **Explaining your projects clearly** to someone else without notes.
- Explain **Handling 'why did you choose that' questions** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
