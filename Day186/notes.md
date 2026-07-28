# Day 186 — Privacy, security and compliance

Today's goal: work through **Privacy, security and compliance** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | PII identification and handling |
| 2 | Anonymisation and pseudonymisation |
| 3 | Differential privacy basics |
| 4 | Federated learning |
| 5 | Data retention policies |
| 6 | GDPR and DPDP obligations |
| 7 | Model inversion and membership inference |
| 8 | Secrets management |
| 9 | Audit trails |
| 10 | Working with a compliance team |

---

## 1. PII identification and handling

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

Practice: open `examples/01_pii_identification_and_handling.py`, predict the output, change one line, predict again.

## 2. Anonymisation and pseudonymisation

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

Practice: open `examples/02_anonymisation_and_pseudonymisation.py`, predict the output, change one line, predict again.

## 3. Differential privacy basics

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

Practice: open `examples/03_differential_privacy_basics.py`, predict the output, change one line, predict again.

## 4. Federated learning

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

Practice: open `examples/04_federated_learning.py`, predict the output, change one line, predict again.

## 5. Data retention policies

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

Practice: open `examples/05_data_retention_policies.py`, predict the output, change one line, predict again.

## 6. GDPR and DPDP obligations

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

Practice: open `examples/06_gdpr_and_dpdp_obligations.py`, predict the output, change one line, predict again.

## 7. Model inversion and membership inference

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

Practice: open `examples/07_model_inversion_and_membership_inference.py`, predict the output, change one line, predict again.

## 8. Secrets management

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

Practice: open `examples/08_secrets_management.py`, predict the output, change one line, predict again.

## 9. Audit trails

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

Practice: open `examples/09_audit_trails.py`, predict the output, change one line, predict again.

## 10. Working with a compliance team

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

Practice: open `examples/10_working_with_a_compliance_team.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 186

- Explain **PII identification and handling** to someone else without notes.
- Explain **Anonymisation and pseudonymisation** to someone else without notes.
- Explain **Differential privacy basics** to someone else without notes.
- Explain **Federated learning** to someone else without notes.
- Explain **Data retention policies** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
