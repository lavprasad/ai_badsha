# Day 196 — Reading research

Today's goal: work through **Reading research** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Where papers appear: arXiv and conferences |
| 2 | The three-pass reading method |
| 3 | Distinguishing contribution from packaging |
| 4 | Reading the limitations section first |
| 5 | Checking baselines for fairness |
| 6 | Reproducibility red flags |
| 7 | Following citation trails |
| 8 | Keeping a paper notebook |
| 9 | Implementing one idea per month |
| 10 | Staying current without drowning |

---

## 1. Where papers appear: arXiv and conferences

Read in three passes: title/abstract/figures (5 minutes, decide if it matters), method and results (30 minutes, understand the idea), then full detail only if you will implement it. The limitations section is usually the most honest paragraph in the paper — read it early.

```python
PASS_1 = ['title', 'abstract', 'figures and captions', 'conclusion']
PASS_2 = ['method section', 'experimental setup', 'baselines used', 'results tables']
PASS_3 = ['every equation', 'appendix', 'reimplement the core idea']

for i, (name, items) in enumerate([('5 min', PASS_1), ('30 min', PASS_2), ('hours', PASS_3)], 1):
    print(f'Pass {i} ({name}): ' + ', '.join(items))
print('\nStop after pass 1 for 90% of papers. That is not laziness, that is triage.')
```

**Remember:** Check which baselines they compared against. A weak baseline makes any method look strong.

**Common mistake:** Reading twenty papers and implementing none — understanding without building fades in a week.

Practice: open `examples/01_where_papers_appear_arxiv_and_conference.py`, predict the output, change one line, predict again.

## 2. The three-pass reading method

Read in three passes: title/abstract/figures (5 minutes, decide if it matters), method and results (30 minutes, understand the idea), then full detail only if you will implement it. The limitations section is usually the most honest paragraph in the paper — read it early.

```python
PASS_1 = ['title', 'abstract', 'figures and captions', 'conclusion']
PASS_2 = ['method section', 'experimental setup', 'baselines used', 'results tables']
PASS_3 = ['every equation', 'appendix', 'reimplement the core idea']

for i, (name, items) in enumerate([('5 min', PASS_1), ('30 min', PASS_2), ('hours', PASS_3)], 1):
    print(f'Pass {i} ({name}): ' + ', '.join(items))
print('\nStop after pass 1 for 90% of papers. That is not laziness, that is triage.')
```

**Remember:** Check which baselines they compared against. A weak baseline makes any method look strong.

**Common mistake:** Reading twenty papers and implementing none — understanding without building fades in a week.

Practice: open `examples/02_the_three_pass_reading_method.py`, predict the output, change one line, predict again.

## 3. Distinguishing contribution from packaging

Read in three passes: title/abstract/figures (5 minutes, decide if it matters), method and results (30 minutes, understand the idea), then full detail only if you will implement it. The limitations section is usually the most honest paragraph in the paper — read it early.

```python
PASS_1 = ['title', 'abstract', 'figures and captions', 'conclusion']
PASS_2 = ['method section', 'experimental setup', 'baselines used', 'results tables']
PASS_3 = ['every equation', 'appendix', 'reimplement the core idea']

for i, (name, items) in enumerate([('5 min', PASS_1), ('30 min', PASS_2), ('hours', PASS_3)], 1):
    print(f'Pass {i} ({name}): ' + ', '.join(items))
print('\nStop after pass 1 for 90% of papers. That is not laziness, that is triage.')
```

**Remember:** Check which baselines they compared against. A weak baseline makes any method look strong.

**Common mistake:** Reading twenty papers and implementing none — understanding without building fades in a week.

Practice: open `examples/03_distinguishing_contribution_from_packagi.py`, predict the output, change one line, predict again.

## 4. Reading the limitations section first

Read in three passes: title/abstract/figures (5 minutes, decide if it matters), method and results (30 minutes, understand the idea), then full detail only if you will implement it. The limitations section is usually the most honest paragraph in the paper — read it early.

```python
PASS_1 = ['title', 'abstract', 'figures and captions', 'conclusion']
PASS_2 = ['method section', 'experimental setup', 'baselines used', 'results tables']
PASS_3 = ['every equation', 'appendix', 'reimplement the core idea']

for i, (name, items) in enumerate([('5 min', PASS_1), ('30 min', PASS_2), ('hours', PASS_3)], 1):
    print(f'Pass {i} ({name}): ' + ', '.join(items))
print('\nStop after pass 1 for 90% of papers. That is not laziness, that is triage.')
```

**Remember:** Check which baselines they compared against. A weak baseline makes any method look strong.

**Common mistake:** Reading twenty papers and implementing none — understanding without building fades in a week.

Practice: open `examples/04_reading_the_limitations_section_first.py`, predict the output, change one line, predict again.

## 5. Checking baselines for fairness

Models learn the bias in their training data and then apply it at scale with a veneer of objectivity. Measure error rates per group, not just overall. Fairness definitions genuinely conflict with each other — you must choose one explicitly and document why.

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

**Remember:** Dropping the sensitive attribute does not remove bias; proxies (pincode, name) carry it right back in.

**Common mistake:** Auditing fairness once at launch and never again as the data drifts.

Practice: open `examples/05_checking_baselines_for_fairness.py`, predict the output, change one line, predict again.

## 6. Reproducibility red flags

An experiment you cannot reproduce is an anecdote. Track for every run: code commit, data version, hyperparameters, metrics and the artefact. Six months later, 'which run produced the model in production' must have an answer.

```python
import json, hashlib, subprocess

def run_record(params, metrics, data_path=None):
    try:
        commit = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'], text=True).strip()
    except Exception:
        commit = 'unknown'
    return {
        'commit': commit,
        'params': params,
        'metrics': metrics,
        'data_sha': hashlib.sha256((data_path or 'none').encode()).hexdigest()[:12],
    }

print(json.dumps(run_record({'lr': 0.01, 'depth': 6}, {'auc': 0.912}, 'data/train.csv'), indent=2))
```

**Remember:** Log the data version alongside the code version — data changes silently, code changes loudly.

**Common mistake:** Naming files `model_final_v2_REAL_use_this.pkl` instead of using a registry.

Practice: open `examples/06_reproducibility_red_flags.py`, predict the output, change one line, predict again.

## 7. Following citation trails

A language model predicts plausible tokens, not true ones. Fluent and wrong is its default failure mode. Reduce it by grounding answers in retrieved sources, requiring citations, allowing 'I don't know', and verifying claims that carry cost.

```python
def answer_with_guard(question, chunks, threshold=0.35):
    if not chunks or max(c['score'] for c in chunks) < threshold:
        return "I don't have information about that in the provided documents."
    best = max(chunks, key=lambda c: c['score'])
    return f"{best['text']}  [source: {best['id']}]"

print(answer_with_guard('refund policy?', [{'id': 'policy.pdf#3', 'text': 'Refunds take 5 days.', 'score': 0.81}]))
print(answer_with_guard('CEO home address?', [{'id': 'policy.pdf#3', 'text': 'Refunds take 5 days.', 'score': 0.11}]))
```

**Remember:** An explicit 'not in my sources' path is worth more than any confidence score.

**Common mistake:** Shipping a chatbot with no abstain path, so it invents a policy under pressure.

Practice: open `examples/07_following_citation_trails.py`, predict the output, change one line, predict again.

## 8. Keeping a paper notebook

Notebooks keep state between cells, which is great for exploring and terrible for reproducibility. Treat the notebook as a scratchpad; once logic settles, move it into a `.py` module you can import and test.

```python
# In a notebook, cell order != execution order.
# Restart & Run All before you trust any result.
import pandas as pd
df = pd.DataFrame({'x': [1, 2, 3]})
df.head()
```

**Remember:** 'Restart kernel and run all' is the only honest test that a notebook works.

**Common mistake:** Shipping a notebook whose results depend on a deleted cell you ran ten minutes ago.

Practice: open `examples/08_keeping_a_paper_notebook.py`, predict the output, change one line, predict again.

## 9. Implementing one idea per month

Read in three passes: title/abstract/figures (5 minutes, decide if it matters), method and results (30 minutes, understand the idea), then full detail only if you will implement it. The limitations section is usually the most honest paragraph in the paper — read it early.

```python
PASS_1 = ['title', 'abstract', 'figures and captions', 'conclusion']
PASS_2 = ['method section', 'experimental setup', 'baselines used', 'results tables']
PASS_3 = ['every equation', 'appendix', 'reimplement the core idea']

for i, (name, items) in enumerate([('5 min', PASS_1), ('30 min', PASS_2), ('hours', PASS_3)], 1):
    print(f'Pass {i} ({name}): ' + ', '.join(items))
print('\nStop after pass 1 for 90% of papers. That is not laziness, that is triage.')
```

**Remember:** Check which baselines they compared against. A weak baseline makes any method look strong.

**Common mistake:** Reading twenty papers and implementing none — understanding without building fades in a week.

Practice: open `examples/09_implementing_one_idea_per_month.py`, predict the output, change one line, predict again.

## 10. Staying current without drowning

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

Practice: open `examples/10_staying_current_without_drowning.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 196

- Explain **Where papers appear: arXiv and conferences** to someone else without notes.
- Explain **The three-pass reading method** to someone else without notes.
- Explain **Distinguishing contribution from packaging** to someone else without notes.
- Explain **Reading the limitations section first** to someone else without notes.
- Explain **Checking baselines for fairness** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
