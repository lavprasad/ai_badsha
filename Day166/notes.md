# Day 166 — Cost engineering

Today's goal: work through **Cost engineering** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Token economics |
| 2 | Prompt compression |
| 3 | Prompt caching |
| 4 | Model routing by difficulty |
| 5 | Small model first, escalate on failure |
| 6 | Batch processing for offline jobs |
| 7 | Caching identical requests |
| 8 | Truncating context intelligently |
| 9 | Measuring cost per resolved task |
| 10 | A cost dashboard for your app |

---

## 1. Token economics

Cost per token is the wrong metric; cost per resolved task is the right one. A cheap model that fails half the time and escalates costs more than the expensive model. Route by difficulty, cache aggressively, and measure end-to-end.

```python
def cost_per_resolved(price_per_call, success_rate, escalation_price):
    return price_per_call + (1 - success_rate) * escalation_price

options = [
    ('small model',  0.001, 0.62),
    ('large model',  0.020, 0.94),
    ('small->large', 0.001 + 0.38 * 0.020, 0.96),
]
for name, price, success in options:
    print(f'{name:<14} cost/resolved = {cost_per_resolved(price, success, 2.00):.4f}')
print('\n(escalation to a human costed at 2.00)')
```

**Remember:** Always price the failure path. Human escalation usually dominates every model cost in the table.

**Common mistake:** Switching to the cheapest model, watching token spend drop, and never noticing support load doubled.

## 2. Prompt compression

Cost per token is the wrong metric; cost per resolved task is the right one. A cheap model that fails half the time and escalates costs more than the expensive model. Route by difficulty, cache aggressively, and measure end-to-end.

```python
def cost_per_resolved(price_per_call, success_rate, escalation_price):
    return price_per_call + (1 - success_rate) * escalation_price

options = [
    ('small model',  0.001, 0.62),
    ('large model',  0.020, 0.94),
    ('small->large', 0.001 + 0.38 * 0.020, 0.96),
]
for name, price, success in options:
    print(f'{name:<14} cost/resolved = {cost_per_resolved(price, success, 2.00):.4f}')
print('\n(escalation to a human costed at 2.00)')
```

**Remember:** Always price the failure path. Human escalation usually dominates every model cost in the table.

**Common mistake:** Switching to the cheapest model, watching token spend drop, and never noticing support load doubled.

## 3. Prompt caching

The Messages API takes a system prompt plus alternating user/assistant turns and returns content blocks. Put stable content (long instructions, retrieved corpora) at the front and mark it cacheable — cache hits cut both latency and cost sharply. Stream when a human is waiting.

```python
# pip install anthropic ; export ANTHROPIC_API_KEY=...
# import anthropic
# client = anthropic.Anthropic()
# resp = client.messages.create(
#     model='claude-sonnet-5',
#     max_tokens=1024,
#     system=[{'type': 'text', 'text': LONG_STABLE_INSTRUCTIONS,
#              'cache_control': {'type': 'ephemeral'}}],
#     messages=[{'role': 'user', 'content': 'Summarise the attached policy.'}],
# )
# print(resp.content[0].text)
print('Stable prefix first + cache_control -> cheaper, faster repeat calls.')
```

**Remember:** Never hard-code an API key. Read it from the environment and keep it out of git.

**Common mistake:** Rebuilding the prompt in a different order each call, so nothing ever hits the cache.

## 4. Model routing by difficulty

Cost per token is the wrong metric; cost per resolved task is the right one. A cheap model that fails half the time and escalates costs more than the expensive model. Route by difficulty, cache aggressively, and measure end-to-end.

```python
def cost_per_resolved(price_per_call, success_rate, escalation_price):
    return price_per_call + (1 - success_rate) * escalation_price

options = [
    ('small model',  0.001, 0.62),
    ('large model',  0.020, 0.94),
    ('small->large', 0.001 + 0.38 * 0.020, 0.96),
]
for name, price, success in options:
    print(f'{name:<14} cost/resolved = {cost_per_resolved(price, success, 2.00):.4f}')
print('\n(escalation to a human costed at 2.00)')
```

**Remember:** Always price the failure path. Human escalation usually dominates every model cost in the table.

**Common mistake:** Switching to the cheapest model, watching token spend drop, and never noticing support load doubled.

## 5. Small model first, escalate on failure

Cost per token is the wrong metric; cost per resolved task is the right one. A cheap model that fails half the time and escalates costs more than the expensive model. Route by difficulty, cache aggressively, and measure end-to-end.

```python
def cost_per_resolved(price_per_call, success_rate, escalation_price):
    return price_per_call + (1 - success_rate) * escalation_price

options = [
    ('small model',  0.001, 0.62),
    ('large model',  0.020, 0.94),
    ('small->large', 0.001 + 0.38 * 0.020, 0.96),
]
for name, price, success in options:
    print(f'{name:<14} cost/resolved = {cost_per_resolved(price, success, 2.00):.4f}')
print('\n(escalation to a human costed at 2.00)')
```

**Remember:** Always price the failure path. Human escalation usually dominates every model cost in the table.

**Common mistake:** Switching to the cheapest model, watching token spend drop, and never noticing support load doubled.

## 6. Batch processing for offline jobs

Accuracy hides everything on imbalanced data. Precision asks 'of the ones I flagged, how many were real'; recall asks 'of the real ones, how many did I catch'. You trade one for the other with the threshold, and the business decides which error hurts more.

```python
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=2000, weights=[0.95, 0.05], random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, stratify=y, random_state=0)
m = LogisticRegression(max_iter=1000).fit(Xtr, ytr)
print(confusion_matrix(yte, m.predict(Xte)))
print(classification_report(yte, m.predict(Xte), digits=3))
print('roc auc', round(roc_auc_score(yte, m.predict_proba(Xte)[:, 1]), 4))
```

**Remember:** Tune the decision threshold on validation data; 0.5 is a default, not a decision.

**Common mistake:** Optimising ROC-AUC on a heavily imbalanced problem where precision-recall AUC is the honest metric.

## 7. Caching identical requests

Cost per token is the wrong metric; cost per resolved task is the right one. A cheap model that fails half the time and escalates costs more than the expensive model. Route by difficulty, cache aggressively, and measure end-to-end.

```python
def cost_per_resolved(price_per_call, success_rate, escalation_price):
    return price_per_call + (1 - success_rate) * escalation_price

options = [
    ('small model',  0.001, 0.62),
    ('large model',  0.020, 0.94),
    ('small->large', 0.001 + 0.38 * 0.020, 0.96),
]
for name, price, success in options:
    print(f'{name:<14} cost/resolved = {cost_per_resolved(price, success, 2.00):.4f}')
print('\n(escalation to a human costed at 2.00)')
```

**Remember:** Always price the failure path. Human escalation usually dominates every model cost in the table.

**Common mistake:** Switching to the cheapest model, watching token spend drop, and never noticing support load doubled.

## 8. Truncating context intelligently

Cost per token is the wrong metric; cost per resolved task is the right one. A cheap model that fails half the time and escalates costs more than the expensive model. Route by difficulty, cache aggressively, and measure end-to-end.

```python
def cost_per_resolved(price_per_call, success_rate, escalation_price):
    return price_per_call + (1 - success_rate) * escalation_price

options = [
    ('small model',  0.001, 0.62),
    ('large model',  0.020, 0.94),
    ('small->large', 0.001 + 0.38 * 0.020, 0.96),
]
for name, price, success in options:
    print(f'{name:<14} cost/resolved = {cost_per_resolved(price, success, 2.00):.4f}')
print('\n(escalation to a human costed at 2.00)')
```

**Remember:** Always price the failure path. Human escalation usually dominates every model cost in the table.

**Common mistake:** Switching to the cheapest model, watching token spend drop, and never noticing support load doubled.

## 9. Measuring cost per resolved task

Cost per token is the wrong metric; cost per resolved task is the right one. A cheap model that fails half the time and escalates costs more than the expensive model. Route by difficulty, cache aggressively, and measure end-to-end.

```python
def cost_per_resolved(price_per_call, success_rate, escalation_price):
    return price_per_call + (1 - success_rate) * escalation_price

options = [
    ('small model',  0.001, 0.62),
    ('large model',  0.020, 0.94),
    ('small->large', 0.001 + 0.38 * 0.020, 0.96),
]
for name, price, success in options:
    print(f'{name:<14} cost/resolved = {cost_per_resolved(price, success, 2.00):.4f}')
print('\n(escalation to a human costed at 2.00)')
```

**Remember:** Always price the failure path. Human escalation usually dominates every model cost in the table.

**Common mistake:** Switching to the cheapest model, watching token spend drop, and never noticing support load doubled.

## 10. A cost dashboard for your app

Cost per token is the wrong metric; cost per resolved task is the right one. A cheap model that fails half the time and escalates costs more than the expensive model. Route by difficulty, cache aggressively, and measure end-to-end.

```python
def cost_per_resolved(price_per_call, success_rate, escalation_price):
    return price_per_call + (1 - success_rate) * escalation_price

options = [
    ('small model',  0.001, 0.62),
    ('large model',  0.020, 0.94),
    ('small->large', 0.001 + 0.38 * 0.020, 0.96),
]
for name, price, success in options:
    print(f'{name:<14} cost/resolved = {cost_per_resolved(price, success, 2.00):.4f}')
print('\n(escalation to a human costed at 2.00)')
```

**Remember:** Always price the failure path. Human escalation usually dominates every model cost in the table.

**Common mistake:** Switching to the cheapest model, watching token spend drop, and never noticing support load doubled.

---

## What you should be able to do after Day 166

- Explain **Token economics** to someone else without notes.
- Explain **Prompt compression** to someone else without notes.
- Explain **Prompt caching** to someone else without notes.
- Explain **Model routing by difficulty** to someone else without notes.
- Explain **Small model first, escalate on failure** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
