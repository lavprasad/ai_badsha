# Day 63 — Calibration and probability quality

Today's goal: work through **Calibration and probability quality** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | What a calibrated probability means |
| 2 | Reliability diagrams |
| 3 | Brier score |
| 4 | Platt scaling |
| 5 | Isotonic regression |
| 6 | Why boosted trees are miscalibrated |
| 7 | Calibration under class imbalance |
| 8 | Calibrating on a held-out set |
| 9 | Decision thresholds from calibrated scores |
| 10 | Expected value of a decision |

---

## 1. What a calibrated probability means

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

Practice: open `examples/01_what_a_calibrated_probability_means.py`, predict the output, change one line, predict again.

## 2. Reliability diagrams

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

Practice: open `examples/02_reliability_diagrams.py`, predict the output, change one line, predict again.

## 3. Brier score

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

Practice: open `examples/03_brier_score.py`, predict the output, change one line, predict again.

## 4. Platt scaling

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

Practice: open `examples/04_platt_scaling.py`, predict the output, change one line, predict again.

## 5. Isotonic regression

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

Practice: open `examples/05_isotonic_regression.py`, predict the output, change one line, predict again.

## 6. Why boosted trees are miscalibrated

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

Practice: open `examples/06_why_boosted_trees_are_miscalibrated.py`, predict the output, change one line, predict again.

## 7. Calibration under class imbalance

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

Practice: open `examples/07_calibration_under_class_imbalance.py`, predict the output, change one line, predict again.

## 8. Calibrating on a held-out set

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

Practice: open `examples/08_calibrating_on_a_held_out_set.py`, predict the output, change one line, predict again.

## 9. Decision thresholds from calibrated scores

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

Practice: open `examples/09_decision_thresholds_from_calibrated_scor.py`, predict the output, change one line, predict again.

## 10. Expected value of a decision

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

Practice: open `examples/10_expected_value_of_a_decision.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 63

- Explain **What a calibrated probability means** to someone else without notes.
- Explain **Reliability diagrams** to someone else without notes.
- Explain **Brier score** to someone else without notes.
- Explain **Platt scaling** to someone else without notes.
- Explain **Isotonic regression** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
