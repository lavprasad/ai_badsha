# Day 25 — A/B testing and experiment design

Today's goal: work through **A/B testing and experiment design** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Framing a decision as an experiment |
| 2 | Randomisation and control groups |
| 3 | Choosing a primary metric |
| 4 | Minimum detectable effect |
| 5 | Deciding sample size up front |
| 6 | Peeking and why it inflates false positives |
| 7 | Guardrail metrics |
| 8 | Novelty and seasonality effects |
| 9 | Analysing an A/B result |
| 10 | When an A/B test is the wrong tool |

---

## 1. Framing a decision as an experiment

A p-value is P(data this extreme | nothing is going on). It is not the probability your idea is right. A confidence interval is more useful because it shows effect size and uncertainty together — a 'significant' 0.1% lift may not be worth shipping.

```python
import numpy as np

rng = np.random.default_rng(0)
control = rng.normal(10.0, 2.0, 500)
variant = rng.normal(10.3, 2.0, 500)

diff = variant.mean() - control.mean()
se = np.sqrt(control.var(ddof=1) / 500 + variant.var(ddof=1) / 500)
print(f'lift {diff:.3f}  95% CI [{diff - 1.96 * se:.3f}, {diff + 1.96 * se:.3f}]')
```

**Remember:** Decide the sample size and the metric BEFORE looking at the data.

**Common mistake:** Peeking daily and stopping the test the moment p < 0.05 — that inflates false positives badly.

## 2. Randomisation and control groups

A p-value is P(data this extreme | nothing is going on). It is not the probability your idea is right. A confidence interval is more useful because it shows effect size and uncertainty together — a 'significant' 0.1% lift may not be worth shipping.

```python
import numpy as np

rng = np.random.default_rng(0)
control = rng.normal(10.0, 2.0, 500)
variant = rng.normal(10.3, 2.0, 500)

diff = variant.mean() - control.mean()
se = np.sqrt(control.var(ddof=1) / 500 + variant.var(ddof=1) / 500)
print(f'lift {diff:.3f}  95% CI [{diff - 1.96 * se:.3f}, {diff + 1.96 * se:.3f}]')
```

**Remember:** Decide the sample size and the metric BEFORE looking at the data.

**Common mistake:** Peeking daily and stopping the test the moment p < 0.05 — that inflates false positives badly.

## 3. Choosing a primary metric

A p-value is P(data this extreme | nothing is going on). It is not the probability your idea is right. A confidence interval is more useful because it shows effect size and uncertainty together — a 'significant' 0.1% lift may not be worth shipping.

```python
import numpy as np

rng = np.random.default_rng(0)
control = rng.normal(10.0, 2.0, 500)
variant = rng.normal(10.3, 2.0, 500)

diff = variant.mean() - control.mean()
se = np.sqrt(control.var(ddof=1) / 500 + variant.var(ddof=1) / 500)
print(f'lift {diff:.3f}  95% CI [{diff - 1.96 * se:.3f}, {diff + 1.96 * se:.3f}]')
```

**Remember:** Decide the sample size and the metric BEFORE looking at the data.

**Common mistake:** Peeking daily and stopping the test the moment p < 0.05 — that inflates false positives badly.

## 4. Minimum detectable effect

A p-value is P(data this extreme | nothing is going on). It is not the probability your idea is right. A confidence interval is more useful because it shows effect size and uncertainty together — a 'significant' 0.1% lift may not be worth shipping.

```python
import numpy as np

rng = np.random.default_rng(0)
control = rng.normal(10.0, 2.0, 500)
variant = rng.normal(10.3, 2.0, 500)

diff = variant.mean() - control.mean()
se = np.sqrt(control.var(ddof=1) / 500 + variant.var(ddof=1) / 500)
print(f'lift {diff:.3f}  95% CI [{diff - 1.96 * se:.3f}, {diff + 1.96 * se:.3f}]')
```

**Remember:** Decide the sample size and the metric BEFORE looking at the data.

**Common mistake:** Peeking daily and stopping the test the moment p < 0.05 — that inflates false positives badly.

## 5. Deciding sample size up front

A p-value is P(data this extreme | nothing is going on). It is not the probability your idea is right. A confidence interval is more useful because it shows effect size and uncertainty together — a 'significant' 0.1% lift may not be worth shipping.

```python
import numpy as np

rng = np.random.default_rng(0)
control = rng.normal(10.0, 2.0, 500)
variant = rng.normal(10.3, 2.0, 500)

diff = variant.mean() - control.mean()
se = np.sqrt(control.var(ddof=1) / 500 + variant.var(ddof=1) / 500)
print(f'lift {diff:.3f}  95% CI [{diff - 1.96 * se:.3f}, {diff + 1.96 * se:.3f}]')
```

**Remember:** Decide the sample size and the metric BEFORE looking at the data.

**Common mistake:** Peeking daily and stopping the test the moment p < 0.05 — that inflates false positives badly.

## 6. Peeking and why it inflates false positives

A p-value is P(data this extreme | nothing is going on). It is not the probability your idea is right. A confidence interval is more useful because it shows effect size and uncertainty together — a 'significant' 0.1% lift may not be worth shipping.

```python
import numpy as np

rng = np.random.default_rng(0)
control = rng.normal(10.0, 2.0, 500)
variant = rng.normal(10.3, 2.0, 500)

diff = variant.mean() - control.mean()
se = np.sqrt(control.var(ddof=1) / 500 + variant.var(ddof=1) / 500)
print(f'lift {diff:.3f}  95% CI [{diff - 1.96 * se:.3f}, {diff + 1.96 * se:.3f}]')
```

**Remember:** Decide the sample size and the metric BEFORE looking at the data.

**Common mistake:** Peeking daily and stopping the test the moment p < 0.05 — that inflates false positives badly.

## 7. Guardrail metrics

A p-value is P(data this extreme | nothing is going on). It is not the probability your idea is right. A confidence interval is more useful because it shows effect size and uncertainty together — a 'significant' 0.1% lift may not be worth shipping.

```python
import numpy as np

rng = np.random.default_rng(0)
control = rng.normal(10.0, 2.0, 500)
variant = rng.normal(10.3, 2.0, 500)

diff = variant.mean() - control.mean()
se = np.sqrt(control.var(ddof=1) / 500 + variant.var(ddof=1) / 500)
print(f'lift {diff:.3f}  95% CI [{diff - 1.96 * se:.3f}, {diff + 1.96 * se:.3f}]')
```

**Remember:** Decide the sample size and the metric BEFORE looking at the data.

**Common mistake:** Peeking daily and stopping the test the moment p < 0.05 — that inflates false positives badly.

## 8. Novelty and seasonality effects

A p-value is P(data this extreme | nothing is going on). It is not the probability your idea is right. A confidence interval is more useful because it shows effect size and uncertainty together — a 'significant' 0.1% lift may not be worth shipping.

```python
import numpy as np

rng = np.random.default_rng(0)
control = rng.normal(10.0, 2.0, 500)
variant = rng.normal(10.3, 2.0, 500)

diff = variant.mean() - control.mean()
se = np.sqrt(control.var(ddof=1) / 500 + variant.var(ddof=1) / 500)
print(f'lift {diff:.3f}  95% CI [{diff - 1.96 * se:.3f}, {diff + 1.96 * se:.3f}]')
```

**Remember:** Decide the sample size and the metric BEFORE looking at the data.

**Common mistake:** Peeking daily and stopping the test the moment p < 0.05 — that inflates false positives badly.

## 9. Analysing an A/B result

A p-value is P(data this extreme | nothing is going on). It is not the probability your idea is right. A confidence interval is more useful because it shows effect size and uncertainty together — a 'significant' 0.1% lift may not be worth shipping.

```python
import numpy as np

rng = np.random.default_rng(0)
control = rng.normal(10.0, 2.0, 500)
variant = rng.normal(10.3, 2.0, 500)

diff = variant.mean() - control.mean()
se = np.sqrt(control.var(ddof=1) / 500 + variant.var(ddof=1) / 500)
print(f'lift {diff:.3f}  95% CI [{diff - 1.96 * se:.3f}, {diff + 1.96 * se:.3f}]')
```

**Remember:** Decide the sample size and the metric BEFORE looking at the data.

**Common mistake:** Peeking daily and stopping the test the moment p < 0.05 — that inflates false positives badly.

## 10. When an A/B test is the wrong tool

A p-value is P(data this extreme | nothing is going on). It is not the probability your idea is right. A confidence interval is more useful because it shows effect size and uncertainty together — a 'significant' 0.1% lift may not be worth shipping.

```python
import numpy as np

rng = np.random.default_rng(0)
control = rng.normal(10.0, 2.0, 500)
variant = rng.normal(10.3, 2.0, 500)

diff = variant.mean() - control.mean()
se = np.sqrt(control.var(ddof=1) / 500 + variant.var(ddof=1) / 500)
print(f'lift {diff:.3f}  95% CI [{diff - 1.96 * se:.3f}, {diff + 1.96 * se:.3f}]')
```

**Remember:** Decide the sample size and the metric BEFORE looking at the data.

**Common mistake:** Peeking daily and stopping the test the moment p < 0.05 — that inflates false positives badly.

---

## What you should be able to do after Day 25

- Explain **Framing a decision as an experiment** to someone else without notes.
- Explain **Randomisation and control groups** to someone else without notes.
- Explain **Choosing a primary metric** to someone else without notes.
- Explain **Minimum detectable effect** to someone else without notes.
- Explain **Deciding sample size up front** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
