# Day 195 — Writing about your work

Today's goal: work through **Writing about your work** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Structure of a good technical write-up |
| 2 | Leading with the result |
| 3 | Explaining the method without jargon |
| 4 | Charts that carry the argument |
| 5 | Reporting limitations builds trust |
| 6 | Reproducibility section |
| 7 | README as the front door |
| 8 | Blog post vs repository documentation |
| 9 | Getting feedback before publishing |
| 10 | Publishing on GitHub Pages |

---

## 1. Structure of a good technical write-up

Lead with the result, then the method, then the caveats. Most readers stop after two paragraphs, so the first two must contain the finding and why it matters. A README that states the problem, the number, and how to run it is worth more than a perfect architecture diagram.

```python
README = '''
# Ticket Router

Routes support tickets to the right team. **Macro F1 0.84** vs 0.61 for the
keyword rules it replaces, measured on 4,000 held-out tickets from Q1.

## Run it
    pip install -r requirements.txt
    python -m router.train --config configs/base.yaml
    python -m router.serve

## How it works
TF-IDF + linear SVM baseline, then a fine-tuned small transformer.
The transformer wins by 0.06 F1 at 12x the inference cost — see `docs/tradeoff.md`.

## Limitations
- Trained on English tickets only; Hinglish accuracy drops to 0.71.
- Degrades on tickets under 10 words (18% of volume).
'''
print(README)
```

**Remember:** Put the number in the first paragraph. If you are hiding it, the reader assumes it is bad.

**Common mistake:** A README that explains your architecture for 400 lines and never says what score it achieved.

Practice: open `examples/01_structure_of_a_good_technical_write_up.py`, predict the output, change one line, predict again.

## 2. Leading with the result

Lead with the result, then the method, then the caveats. Most readers stop after two paragraphs, so the first two must contain the finding and why it matters. A README that states the problem, the number, and how to run it is worth more than a perfect architecture diagram.

```python
README = '''
# Ticket Router

Routes support tickets to the right team. **Macro F1 0.84** vs 0.61 for the
keyword rules it replaces, measured on 4,000 held-out tickets from Q1.

## Run it
    pip install -r requirements.txt
    python -m router.train --config configs/base.yaml
    python -m router.serve

## How it works
TF-IDF + linear SVM baseline, then a fine-tuned small transformer.
The transformer wins by 0.06 F1 at 12x the inference cost — see `docs/tradeoff.md`.

## Limitations
- Trained on English tickets only; Hinglish accuracy drops to 0.71.
- Degrades on tickets under 10 words (18% of volume).
'''
print(README)
```

**Remember:** Put the number in the first paragraph. If you are hiding it, the reader assumes it is bad.

**Common mistake:** A README that explains your architecture for 400 lines and never says what score it achieved.

Practice: open `examples/02_leading_with_the_result.py`, predict the output, change one line, predict again.

## 3. Explaining the method without jargon

Lead with the result, then the method, then the caveats. Most readers stop after two paragraphs, so the first two must contain the finding and why it matters. A README that states the problem, the number, and how to run it is worth more than a perfect architecture diagram.

```python
README = '''
# Ticket Router

Routes support tickets to the right team. **Macro F1 0.84** vs 0.61 for the
keyword rules it replaces, measured on 4,000 held-out tickets from Q1.

## Run it
    pip install -r requirements.txt
    python -m router.train --config configs/base.yaml
    python -m router.serve

## How it works
TF-IDF + linear SVM baseline, then a fine-tuned small transformer.
The transformer wins by 0.06 F1 at 12x the inference cost — see `docs/tradeoff.md`.

## Limitations
- Trained on English tickets only; Hinglish accuracy drops to 0.71.
- Degrades on tickets under 10 words (18% of volume).
'''
print(README)
```

**Remember:** Put the number in the first paragraph. If you are hiding it, the reader assumes it is bad.

**Common mistake:** A README that explains your architecture for 400 lines and never says what score it achieved.

Practice: open `examples/03_explaining_the_method_without_jargon.py`, predict the output, change one line, predict again.

## 4. Charts that carry the argument

Plot before you model. A histogram exposes skew and outliers, a scatter exposes non-linearity, and a line of residuals exposes a model that is systematically wrong. Five minutes of plotting saves hours of confused tuning.

```python
import matplotlib
matplotlib.use('Agg')          # headless-safe for scripts/CI
import matplotlib.pyplot as plt
import numpy as np

x = np.random.default_rng(0).normal(size=500)
fig, ax = plt.subplots()
ax.hist(x, bins=30)
ax.set_title('sample distribution')
fig.savefig('hist.png', dpi=120)
print('wrote hist.png')
```

**Remember:** Label the axes. An unlabelled plot is a decoration, not evidence.

**Common mistake:** Judging a model by its accuracy number alone without ever looking at the data.

Practice: open `examples/04_charts_that_carry_the_argument.py`, predict the output, change one line, predict again.

## 5. Reporting limitations builds trust

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

Practice: open `examples/05_reporting_limitations_builds_trust.py`, predict the output, change one line, predict again.

## 6. Reproducibility section

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

Practice: open `examples/06_reproducibility_section.py`, predict the output, change one line, predict again.

## 7. README as the front door

Lead with the result, then the method, then the caveats. Most readers stop after two paragraphs, so the first two must contain the finding and why it matters. A README that states the problem, the number, and how to run it is worth more than a perfect architecture diagram.

```python
README = '''
# Ticket Router

Routes support tickets to the right team. **Macro F1 0.84** vs 0.61 for the
keyword rules it replaces, measured on 4,000 held-out tickets from Q1.

## Run it
    pip install -r requirements.txt
    python -m router.train --config configs/base.yaml
    python -m router.serve

## How it works
TF-IDF + linear SVM baseline, then a fine-tuned small transformer.
The transformer wins by 0.06 F1 at 12x the inference cost — see `docs/tradeoff.md`.

## Limitations
- Trained on English tickets only; Hinglish accuracy drops to 0.71.
- Degrades on tickets under 10 words (18% of volume).
'''
print(README)
```

**Remember:** Put the number in the first paragraph. If you are hiding it, the reader assumes it is bad.

**Common mistake:** A README that explains your architecture for 400 lines and never says what score it achieved.

Practice: open `examples/07_readme_as_the_front_door.py`, predict the output, change one line, predict again.

## 8. Blog post vs repository documentation

Lead with the result, then the method, then the caveats. Most readers stop after two paragraphs, so the first two must contain the finding and why it matters. A README that states the problem, the number, and how to run it is worth more than a perfect architecture diagram.

```python
README = '''
# Ticket Router

Routes support tickets to the right team. **Macro F1 0.84** vs 0.61 for the
keyword rules it replaces, measured on 4,000 held-out tickets from Q1.

## Run it
    pip install -r requirements.txt
    python -m router.train --config configs/base.yaml
    python -m router.serve

## How it works
TF-IDF + linear SVM baseline, then a fine-tuned small transformer.
The transformer wins by 0.06 F1 at 12x the inference cost — see `docs/tradeoff.md`.

## Limitations
- Trained on English tickets only; Hinglish accuracy drops to 0.71.
- Degrades on tickets under 10 words (18% of volume).
'''
print(README)
```

**Remember:** Put the number in the first paragraph. If you are hiding it, the reader assumes it is bad.

**Common mistake:** A README that explains your architecture for 400 lines and never says what score it achieved.

Practice: open `examples/08_blog_post_vs_repository_documentation.py`, predict the output, change one line, predict again.

## 9. Getting feedback before publishing

Lead with the result, then the method, then the caveats. Most readers stop after two paragraphs, so the first two must contain the finding and why it matters. A README that states the problem, the number, and how to run it is worth more than a perfect architecture diagram.

```python
README = '''
# Ticket Router

Routes support tickets to the right team. **Macro F1 0.84** vs 0.61 for the
keyword rules it replaces, measured on 4,000 held-out tickets from Q1.

## Run it
    pip install -r requirements.txt
    python -m router.train --config configs/base.yaml
    python -m router.serve

## How it works
TF-IDF + linear SVM baseline, then a fine-tuned small transformer.
The transformer wins by 0.06 F1 at 12x the inference cost — see `docs/tradeoff.md`.

## Limitations
- Trained on English tickets only; Hinglish accuracy drops to 0.71.
- Degrades on tickets under 10 words (18% of volume).
'''
print(README)
```

**Remember:** Put the number in the first paragraph. If you are hiding it, the reader assumes it is bad.

**Common mistake:** A README that explains your architecture for 400 lines and never says what score it achieved.

Practice: open `examples/09_getting_feedback_before_publishing.py`, predict the output, change one line, predict again.

## 10. Publishing on GitHub Pages

Lead with the result, then the method, then the caveats. Most readers stop after two paragraphs, so the first two must contain the finding and why it matters. A README that states the problem, the number, and how to run it is worth more than a perfect architecture diagram.

```python
README = '''
# Ticket Router

Routes support tickets to the right team. **Macro F1 0.84** vs 0.61 for the
keyword rules it replaces, measured on 4,000 held-out tickets from Q1.

## Run it
    pip install -r requirements.txt
    python -m router.train --config configs/base.yaml
    python -m router.serve

## How it works
TF-IDF + linear SVM baseline, then a fine-tuned small transformer.
The transformer wins by 0.06 F1 at 12x the inference cost — see `docs/tradeoff.md`.

## Limitations
- Trained on English tickets only; Hinglish accuracy drops to 0.71.
- Degrades on tickets under 10 words (18% of volume).
'''
print(README)
```

**Remember:** Put the number in the first paragraph. If you are hiding it, the reader assumes it is bad.

**Common mistake:** A README that explains your architecture for 400 lines and never says what score it achieved.

Practice: open `examples/10_publishing_on_github_pages.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 195

- Explain **Structure of a good technical write-up** to someone else without notes.
- Explain **Leading with the result** to someone else without notes.
- Explain **Explaining the method without jargon** to someone else without notes.
- Explain **Charts that carry the argument** to someone else without notes.
- Explain **Reporting limitations builds trust** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
