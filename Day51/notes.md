# Day 51 — Naive Bayes

Today's goal: work through **Naive Bayes** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | The conditional independence assumption |
| 2 | Gaussian Naive Bayes |
| 3 | Multinomial Naive Bayes for text |
| 4 | Bernoulli Naive Bayes |
| 5 | Laplace smoothing |
| 6 | Why it works despite a false assumption |
| 7 | Speed as a feature |
| 8 | Calibration problems |
| 9 | A spam classifier in 10 lines |
| 10 | When to prefer it over logistic regression |

---

## 1. The conditional independence assumption

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

Practice: open `examples/01_the_conditional_independence_assumption.py`, predict the output, change one line, predict again.

## 2. Gaussian Naive Bayes

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

Practice: open `examples/02_gaussian_naive_bayes.py`, predict the output, change one line, predict again.

## 3. Multinomial Naive Bayes for text

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

Practice: open `examples/03_multinomial_naive_bayes_for_text.py`, predict the output, change one line, predict again.

## 4. Bernoulli Naive Bayes

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

Practice: open `examples/04_bernoulli_naive_bayes.py`, predict the output, change one line, predict again.

## 5. Laplace smoothing

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

Practice: open `examples/05_laplace_smoothing.py`, predict the output, change one line, predict again.

## 6. Why it works despite a false assumption

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

Practice: open `examples/06_why_it_works_despite_a_false_assumption.py`, predict the output, change one line, predict again.

## 7. Speed as a feature

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

Practice: open `examples/07_speed_as_a_feature.py`, predict the output, change one line, predict again.

## 8. Calibration problems

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

Practice: open `examples/08_calibration_problems.py`, predict the output, change one line, predict again.

## 9. A spam classifier in 10 lines

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

Practice: open `examples/09_a_spam_classifier_in_10_lines.py`, predict the output, change one line, predict again.

## 10. When to prefer it over logistic regression

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

Practice: open `examples/10_when_to_prefer_it_over_logistic_regressi.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 51

- Explain **The conditional independence assumption** to someone else without notes.
- Explain **Gaussian Naive Bayes** to someone else without notes.
- Explain **Multinomial Naive Bayes for text** to someone else without notes.
- Explain **Bernoulli Naive Bayes** to someone else without notes.
- Explain **Laplace smoothing** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
