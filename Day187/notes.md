# Day 187 — Responsible AI in practice

Today's goal: work through **Responsible AI in practice** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Harms taxonomy for your product |
| 2 | Measuring performance by subgroup |
| 3 | Fairness definitions and their conflicts |
| 4 | Mitigation at data, model and threshold level |
| 5 | Transparency and model cards |
| 6 | Human oversight requirements |
| 7 | Contestability and appeals |
| 8 | Environmental cost |
| 9 | Documentation as accountability |
| 10 | Saying no to a bad use case |

---

## 1. Harms taxonomy for your product

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

Practice: open `examples/01_harms_taxonomy_for_your_product.py`, predict the output, change one line, predict again.

## 2. Measuring performance by subgroup

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

Practice: open `examples/02_measuring_performance_by_subgroup.py`, predict the output, change one line, predict again.

## 3. Fairness definitions and their conflicts

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

Practice: open `examples/03_fairness_definitions_and_their_conflicts.py`, predict the output, change one line, predict again.

## 4. Mitigation at data, model and threshold level

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

Practice: open `examples/04_mitigation_at_data_model_and_threshold_l.py`, predict the output, change one line, predict again.

## 5. Transparency and model cards

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

Practice: open `examples/05_transparency_and_model_cards.py`, predict the output, change one line, predict again.

## 6. Human oversight requirements

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

Practice: open `examples/06_human_oversight_requirements.py`, predict the output, change one line, predict again.

## 7. Contestability and appeals

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

Practice: open `examples/07_contestability_and_appeals.py`, predict the output, change one line, predict again.

## 8. Environmental cost

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

Practice: open `examples/08_environmental_cost.py`, predict the output, change one line, predict again.

## 9. Documentation as accountability

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

Practice: open `examples/09_documentation_as_accountability.py`, predict the output, change one line, predict again.

## 10. Saying no to a bad use case

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

Practice: open `examples/10_saying_no_to_a_bad_use_case.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 187

- Explain **Harms taxonomy for your product** to someone else without notes.
- Explain **Measuring performance by subgroup** to someone else without notes.
- Explain **Fairness definitions and their conflicts** to someone else without notes.
- Explain **Mitigation at data, model and threshold level** to someone else without notes.
- Explain **Transparency and model cards** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
