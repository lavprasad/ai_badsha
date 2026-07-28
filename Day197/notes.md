# Day 197 — The AI job landscape

Today's goal: work through **The AI job landscape** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Research scientist vs ML engineer vs data scientist |
| 2 | AI engineer and the LLM application role |
| 3 | Data engineer and platform roles |
| 4 | What each role actually does daily |
| 5 | Skills that transfer between them |
| 6 | Domain specialisation as leverage |
| 7 | Startup vs enterprise trade-offs |
| 8 | Building a portfolio for a target role |
| 9 | Open source contributions |
| 10 | Choosing your next two years |

---

## 1. Research scientist vs ML engineer vs data scientist

ML code needs the same tests as any code, plus data tests: schema, ranges, null rates, class balance. Add one behavioural test per known failure mode — a test that would have caught last quarter's outage is worth more than 90% coverage.

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

**Remember:** Test the data contract, not just the function — bad data breaks more models than bad code.

**Common mistake:** Testing only the happy path, so an all-null column silently trains a constant model.

Practice: open `examples/01_research_scientist_vs_ml_engineer_vs_dat.py`, predict the output, change one line, predict again.

## 2. AI engineer and the LLM application role

The roles differ less in algorithms than in where they spend their day: research on experiments, ML engineering on pipelines and serving, AI engineering on prompts, retrieval and evals, data engineering on the plumbing everything else depends on. Pick by which day you want, not by which title sounds best.

```python
ROLES = {
    'Research scientist': 'novel methods, papers, experiments — mostly large labs',
    'ML engineer':        'training pipelines, serving, monitoring, scale',
    'AI engineer':        'LLM apps: prompts, RAG, agents, evals, product surface',
    'Data engineer':      'ingestion, warehouses, contracts — the foundation',
    'Data scientist':     'analysis, experiments, decisions — often no deployed model',
}
for role, day in ROLES.items():
    print(f'{role:<20} {day}')
```

**Remember:** One project you can defend end to end beats ten tutorials on your CV.

**Common mistake:** Chasing the title with the highest salary into work you find tedious every single day.

Practice: open `examples/02_ai_engineer_and_the_llm_application_role.py`, predict the output, change one line, predict again.

## 3. Data engineer and platform roles

The roles differ less in algorithms than in where they spend their day: research on experiments, ML engineering on pipelines and serving, AI engineering on prompts, retrieval and evals, data engineering on the plumbing everything else depends on. Pick by which day you want, not by which title sounds best.

```python
ROLES = {
    'Research scientist': 'novel methods, papers, experiments — mostly large labs',
    'ML engineer':        'training pipelines, serving, monitoring, scale',
    'AI engineer':        'LLM apps: prompts, RAG, agents, evals, product surface',
    'Data engineer':      'ingestion, warehouses, contracts — the foundation',
    'Data scientist':     'analysis, experiments, decisions — often no deployed model',
}
for role, day in ROLES.items():
    print(f'{role:<20} {day}')
```

**Remember:** One project you can defend end to end beats ten tutorials on your CV.

**Common mistake:** Chasing the title with the highest salary into work you find tedious every single day.

Practice: open `examples/03_data_engineer_and_platform_roles.py`, predict the output, change one line, predict again.

## 4. What each role actually does daily

The roles differ less in algorithms than in where they spend their day: research on experiments, ML engineering on pipelines and serving, AI engineering on prompts, retrieval and evals, data engineering on the plumbing everything else depends on. Pick by which day you want, not by which title sounds best.

```python
ROLES = {
    'Research scientist': 'novel methods, papers, experiments — mostly large labs',
    'ML engineer':        'training pipelines, serving, monitoring, scale',
    'AI engineer':        'LLM apps: prompts, RAG, agents, evals, product surface',
    'Data engineer':      'ingestion, warehouses, contracts — the foundation',
    'Data scientist':     'analysis, experiments, decisions — often no deployed model',
}
for role, day in ROLES.items():
    print(f'{role:<20} {day}')
```

**Remember:** One project you can defend end to end beats ten tutorials on your CV.

**Common mistake:** Chasing the title with the highest salary into work you find tedious every single day.

Practice: open `examples/04_what_each_role_actually_does_daily.py`, predict the output, change one line, predict again.

## 5. Skills that transfer between them

The roles differ less in algorithms than in where they spend their day: research on experiments, ML engineering on pipelines and serving, AI engineering on prompts, retrieval and evals, data engineering on the plumbing everything else depends on. Pick by which day you want, not by which title sounds best.

```python
ROLES = {
    'Research scientist': 'novel methods, papers, experiments — mostly large labs',
    'ML engineer':        'training pipelines, serving, monitoring, scale',
    'AI engineer':        'LLM apps: prompts, RAG, agents, evals, product surface',
    'Data engineer':      'ingestion, warehouses, contracts — the foundation',
    'Data scientist':     'analysis, experiments, decisions — often no deployed model',
}
for role, day in ROLES.items():
    print(f'{role:<20} {day}')
```

**Remember:** One project you can defend end to end beats ten tutorials on your CV.

**Common mistake:** Chasing the title with the highest salary into work you find tedious every single day.

Practice: open `examples/05_skills_that_transfer_between_them.py`, predict the output, change one line, predict again.

## 6. Domain specialisation as leverage

RAG grounds answers in your documents: chunk, embed, store, retrieve the top-k for the question, and put them in the prompt. Retrieval quality is the whole ballgame — a perfect model answering from the wrong three chunks is still wrong.

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

**Remember:** Always show the source of each retrieved chunk in the answer so users can verify it.

**Common mistake:** Chunking blindly at 1000 characters and cutting tables and code blocks in half.

Practice: open `examples/06_domain_specialisation_as_leverage.py`, predict the output, change one line, predict again.

## 7. Startup vs enterprise trade-offs

The roles differ less in algorithms than in where they spend their day: research on experiments, ML engineering on pipelines and serving, AI engineering on prompts, retrieval and evals, data engineering on the plumbing everything else depends on. Pick by which day you want, not by which title sounds best.

```python
ROLES = {
    'Research scientist': 'novel methods, papers, experiments — mostly large labs',
    'ML engineer':        'training pipelines, serving, monitoring, scale',
    'AI engineer':        'LLM apps: prompts, RAG, agents, evals, product surface',
    'Data engineer':      'ingestion, warehouses, contracts — the foundation',
    'Data scientist':     'analysis, experiments, decisions — often no deployed model',
}
for role, day in ROLES.items():
    print(f'{role:<20} {day}')
```

**Remember:** One project you can defend end to end beats ten tutorials on your CV.

**Common mistake:** Chasing the title with the highest salary into work you find tedious every single day.

Practice: open `examples/07_startup_vs_enterprise_trade_offs.py`, predict the output, change one line, predict again.

## 8. Building a portfolio for a target role

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

Practice: open `examples/08_building_a_portfolio_for_a_target_role.py`, predict the output, change one line, predict again.

## 9. Open source contributions

The roles differ less in algorithms than in where they spend their day: research on experiments, ML engineering on pipelines and serving, AI engineering on prompts, retrieval and evals, data engineering on the plumbing everything else depends on. Pick by which day you want, not by which title sounds best.

```python
ROLES = {
    'Research scientist': 'novel methods, papers, experiments — mostly large labs',
    'ML engineer':        'training pipelines, serving, monitoring, scale',
    'AI engineer':        'LLM apps: prompts, RAG, agents, evals, product surface',
    'Data engineer':      'ingestion, warehouses, contracts — the foundation',
    'Data scientist':     'analysis, experiments, decisions — often no deployed model',
}
for role, day in ROLES.items():
    print(f'{role:<20} {day}')
```

**Remember:** One project you can defend end to end beats ten tutorials on your CV.

**Common mistake:** Chasing the title with the highest salary into work you find tedious every single day.

Practice: open `examples/09_open_source_contributions.py`, predict the output, change one line, predict again.

## 10. Choosing your next two years

The roles differ less in algorithms than in where they spend their day: research on experiments, ML engineering on pipelines and serving, AI engineering on prompts, retrieval and evals, data engineering on the plumbing everything else depends on. Pick by which day you want, not by which title sounds best.

```python
ROLES = {
    'Research scientist': 'novel methods, papers, experiments — mostly large labs',
    'ML engineer':        'training pipelines, serving, monitoring, scale',
    'AI engineer':        'LLM apps: prompts, RAG, agents, evals, product surface',
    'Data engineer':      'ingestion, warehouses, contracts — the foundation',
    'Data scientist':     'analysis, experiments, decisions — often no deployed model',
}
for role, day in ROLES.items():
    print(f'{role:<20} {day}')
```

**Remember:** One project you can defend end to end beats ten tutorials on your CV.

**Common mistake:** Chasing the title with the highest salary into work you find tedious every single day.

Practice: open `examples/10_choosing_your_next_two_years.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 197

- Explain **Research scientist vs ML engineer vs data scientist** to someone else without notes.
- Explain **AI engineer and the LLM application role** to someone else without notes.
- Explain **Data engineer and platform roles** to someone else without notes.
- Explain **What each role actually does daily** to someone else without notes.
- Explain **Skills that transfer between them** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
