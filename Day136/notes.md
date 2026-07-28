# Day 136 — Text generation quality

Today's goal: work through **Text generation quality** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Fluency versus factuality |
| 2 | Hallucination causes |
| 3 | Grounding in sources |
| 4 | Citations and verifiability |
| 5 | Self-consistency sampling |
| 6 | Verification passes |
| 7 | Abstaining when uncertain |
| 8 | Measuring hallucination rate |
| 9 | User-facing uncertainty communication |
| 10 | Designing for graceful wrongness |

---

## 1. Fluency versus factuality

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

## 2. Hallucination causes

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

## 3. Grounding in sources

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

## 4. Citations and verifiability

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

## 5. Self-consistency sampling

A distribution says which values are likely. Gaussian for measurement noise, Bernoulli for yes/no, Poisson for counts per interval. Choosing the right one is choosing your loss function: Gaussian likelihood gives MSE, Bernoulli gives cross-entropy.

```python
import numpy as np

rng = np.random.default_rng(0)
normal = rng.normal(loc=0, scale=1, size=10_000)
coin = rng.binomial(n=1, p=0.3, size=10_000)

print('normal mean/std', round(normal.mean(), 3), round(normal.std(), 3))
print('coin heads rate ', coin.mean())
```

**Remember:** Always seed your RNG (`default_rng(0)`) when you want a result someone else can reproduce.

**Common mistake:** Assuming Gaussian for skewed, bounded, or count data and then being surprised by the residuals.

## 6. Verification passes

Today's idea — **Verification passes** — sits inside the theme of Text generation quality. Read it as a tool, not trivia: what job does it do, what does it assume about your data, and what breaks when that assumption is false?

```python
# Explore: Verification passes
print("practice: Verification passes")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Remember:** State one assumption `Verification passes` makes about your data before you use it.

**Common mistake:** Copy-pasting `Verification passes` from a tutorial without knowing what it assumes or when it fails.

## 7. Abstaining when uncertain

Today's idea — **Abstaining when uncertain** — sits inside the theme of Text generation quality. Read it as a tool, not trivia: what job does it do, what does it assume about your data, and what breaks when that assumption is false?

```python
# Explore: Abstaining when uncertain
print("practice: Abstaining when uncertain")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Remember:** State one assumption `Abstaining when uncertain` makes about your data before you use it.

**Common mistake:** Copy-pasting `Abstaining when uncertain` from a tutorial without knowing what it assumes or when it fails.

## 8. Measuring hallucination rate

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

## 9. User-facing uncertainty communication

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

## 10. Designing for graceful wrongness

Today's idea — **Designing for graceful wrongness** — sits inside the theme of Text generation quality. Read it as a tool, not trivia: what job does it do, what does it assume about your data, and what breaks when that assumption is false?

```python
# Explore: Designing for graceful wrongness
print("practice: Designing for graceful wrongness")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Remember:** State one assumption `Designing for graceful wrongness` makes about your data before you use it.

**Common mistake:** Copy-pasting `Designing for graceful wrongness` from a tutorial without knowing what it assumes or when it fails.

---

## What you should be able to do after Day 136

- Explain **Fluency versus factuality** to someone else without notes.
- Explain **Hallucination causes** to someone else without notes.
- Explain **Grounding in sources** to someone else without notes.
- Explain **Citations and verifiability** to someone else without notes.
- Explain **Self-consistency sampling** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
