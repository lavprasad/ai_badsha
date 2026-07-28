# Day 187 — Responsible AI in practice

Aaj ka goal: **Responsible AI in practice** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

### Aasaan Bhasha

Models apne training data ka bias seekh lete hain aur phir use objectivity ke mulamme ke saath scale par lagu karte hain. Har group ke error rates naapo, sirf overall nahi. Fairness ki definitions ek doosre se sach me takraati hain — aapko ek explicitly chunni padegi aur wajah likhni padegi.

### Chhota code

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

**Yaad rakho:** Sensitive attribute hataane se bias nahi jaata; proxies (pincode, naam) use wapas le aate hain.

**Aam galti:** Fairness ka audit sirf launch par ek baar karna aur data drift hone par dobara kabhi nahi.

Practice: `examples/01_harms_taxonomy_for_your_product.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Measuring performance by subgroup

### Aasaan Bhasha

Models apne training data ka bias seekh lete hain aur phir use objectivity ke mulamme ke saath scale par lagu karte hain. Har group ke error rates naapo, sirf overall nahi. Fairness ki definitions ek doosre se sach me takraati hain — aapko ek explicitly chunni padegi aur wajah likhni padegi.

### Chhota code

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

**Yaad rakho:** Sensitive attribute hataane se bias nahi jaata; proxies (pincode, naam) use wapas le aate hain.

**Aam galti:** Fairness ka audit sirf launch par ek baar karna aur data drift hone par dobara kabhi nahi.

Practice: `examples/02_measuring_performance_by_subgroup.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Fairness definitions and their conflicts

### Aasaan Bhasha

Models apne training data ka bias seekh lete hain aur phir use objectivity ke mulamme ke saath scale par lagu karte hain. Har group ke error rates naapo, sirf overall nahi. Fairness ki definitions ek doosre se sach me takraati hain — aapko ek explicitly chunni padegi aur wajah likhni padegi.

### Chhota code

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

**Yaad rakho:** Sensitive attribute hataane se bias nahi jaata; proxies (pincode, naam) use wapas le aate hain.

**Aam galti:** Fairness ka audit sirf launch par ek baar karna aur data drift hone par dobara kabhi nahi.

Practice: `examples/03_fairness_definitions_and_their_conflicts.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Mitigation at data, model and threshold level

### Aasaan Bhasha

Models apne training data ka bias seekh lete hain aur phir use objectivity ke mulamme ke saath scale par lagu karte hain. Har group ke error rates naapo, sirf overall nahi. Fairness ki definitions ek doosre se sach me takraati hain — aapko ek explicitly chunni padegi aur wajah likhni padegi.

### Chhota code

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

**Yaad rakho:** Sensitive attribute hataane se bias nahi jaata; proxies (pincode, naam) use wapas le aate hain.

**Aam galti:** Fairness ka audit sirf launch par ek baar karna aur data drift hone par dobara kabhi nahi.

Practice: `examples/04_mitigation_at_data_model_and_threshold_l.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Transparency and model cards

### Aasaan Bhasha

Models apne training data ka bias seekh lete hain aur phir use objectivity ke mulamme ke saath scale par lagu karte hain. Har group ke error rates naapo, sirf overall nahi. Fairness ki definitions ek doosre se sach me takraati hain — aapko ek explicitly chunni padegi aur wajah likhni padegi.

### Chhota code

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

**Yaad rakho:** Sensitive attribute hataane se bias nahi jaata; proxies (pincode, naam) use wapas le aate hain.

**Aam galti:** Fairness ka audit sirf launch par ek baar karna aur data drift hone par dobara kabhi nahi.

Practice: `examples/05_transparency_and_model_cards.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Human oversight requirements

### Aasaan Bhasha

Models apne training data ka bias seekh lete hain aur phir use objectivity ke mulamme ke saath scale par lagu karte hain. Har group ke error rates naapo, sirf overall nahi. Fairness ki definitions ek doosre se sach me takraati hain — aapko ek explicitly chunni padegi aur wajah likhni padegi.

### Chhota code

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

**Yaad rakho:** Sensitive attribute hataane se bias nahi jaata; proxies (pincode, naam) use wapas le aate hain.

**Aam galti:** Fairness ka audit sirf launch par ek baar karna aur data drift hone par dobara kabhi nahi.

Practice: `examples/06_human_oversight_requirements.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Contestability and appeals

### Aasaan Bhasha

Models apne training data ka bias seekh lete hain aur phir use objectivity ke mulamme ke saath scale par lagu karte hain. Har group ke error rates naapo, sirf overall nahi. Fairness ki definitions ek doosre se sach me takraati hain — aapko ek explicitly chunni padegi aur wajah likhni padegi.

### Chhota code

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

**Yaad rakho:** Sensitive attribute hataane se bias nahi jaata; proxies (pincode, naam) use wapas le aate hain.

**Aam galti:** Fairness ka audit sirf launch par ek baar karna aur data drift hone par dobara kabhi nahi.

Practice: `examples/07_contestability_and_appeals.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Environmental cost

### Aasaan Bhasha

Models apne training data ka bias seekh lete hain aur phir use objectivity ke mulamme ke saath scale par lagu karte hain. Har group ke error rates naapo, sirf overall nahi. Fairness ki definitions ek doosre se sach me takraati hain — aapko ek explicitly chunni padegi aur wajah likhni padegi.

### Chhota code

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

**Yaad rakho:** Sensitive attribute hataane se bias nahi jaata; proxies (pincode, naam) use wapas le aate hain.

**Aam galti:** Fairness ka audit sirf launch par ek baar karna aur data drift hone par dobara kabhi nahi.

Practice: `examples/08_environmental_cost.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Documentation as accountability

### Aasaan Bhasha

Models apne training data ka bias seekh lete hain aur phir use objectivity ke mulamme ke saath scale par lagu karte hain. Har group ke error rates naapo, sirf overall nahi. Fairness ki definitions ek doosre se sach me takraati hain — aapko ek explicitly chunni padegi aur wajah likhni padegi.

### Chhota code

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

**Yaad rakho:** Sensitive attribute hataane se bias nahi jaata; proxies (pincode, naam) use wapas le aate hain.

**Aam galti:** Fairness ka audit sirf launch par ek baar karna aur data drift hone par dobara kabhi nahi.

Practice: `examples/09_documentation_as_accountability.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Saying no to a bad use case

### Aasaan Bhasha

Models apne training data ka bias seekh lete hain aur phir use objectivity ke mulamme ke saath scale par lagu karte hain. Har group ke error rates naapo, sirf overall nahi. Fairness ki definitions ek doosre se sach me takraati hain — aapko ek explicitly chunni padegi aur wajah likhni padegi.

### Chhota code

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

**Yaad rakho:** Sensitive attribute hataane se bias nahi jaata; proxies (pincode, naam) use wapas le aate hain.

**Aam galti:** Fairness ka audit sirf launch par ek baar karna aur data drift hone par dobara kabhi nahi.

Practice: `examples/10_saying_no_to_a_bad_use_case.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 187 ke baad aapko ye aana chahiye

- **Harms taxonomy for your product** ko bina notes dekhe kisi dost ko samjha sakna.
- **Measuring performance by subgroup** ko bina notes dekhe kisi dost ko samjha sakna.
- **Fairness definitions and their conflicts** ko bina notes dekhe kisi dost ko samjha sakna.
- **Mitigation at data, model and threshold level** ko bina notes dekhe kisi dost ko samjha sakna.
- **Transparency and model cards** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
