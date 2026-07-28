# Day 168 — Data flywheels

Aaj ka goal: **Data flywheels** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Capturing user feedback |
| 2 | Implicit signals: edits, retries, abandonment |
| 3 | Building a labelling loop |
| 4 | Active learning: label what is uncertain |
| 5 | Turning corrections into eval cases |
| 6 | Retraining and re-prompting cadence |
| 7 | Avoiding feedback loop bias |
| 8 | Privacy constraints on user data |
| 9 | Measuring flywheel velocity |
| 10 | Designing the loop from day one |

---

## 1. Capturing user feedback

### Aasaan Bhasha

Jin examples par aapka model galat hota hai wo aapke sabse keemti training data hain, aur wo muft hain — agar aap unhe capture karo. Pehle din se inputs, outputs aur corrections log karo; launch ke baad feedback loop lagane ka matlab hai zero se shuru karna.

### Chhota code

```python
import numpy as np

def select_for_labelling(probs, budget=5):
    """Label where the model is least certain — uncertainty sampling."""
    margin = np.abs(probs - 0.5)
    return np.argsort(margin)[:budget]

rng = np.random.default_rng(0)
probs = rng.random(20)
pick = select_for_labelling(probs)
print('label these rows first:', pick)
print('their probabilities    :', probs[pick].round(3))
print('\n50 uncertain labels beat 5000 random ones.')
```

**Yaad rakho:** Sirf thumbs-down nahi, correction capture karo. 'Isse kya kehna chahiye tha' hi training signal hai.

**Aam galti:** Bina logging ke ship karna, phir teen mahine traffic ke baad sudhaarne ke liye koi data hi na hona.

Practice: `examples/01_capturing_user_feedback.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Implicit signals: edits, retries, abandonment

### Aasaan Bhasha

ML code ko baaki code jaise tests chahiye, plus data tests: schema, ranges, null rates, class balance. Har known failure mode ke liye ek behavioural test jodo — ek test jo pichhli baar ka outage pakad leta, wo 90% coverage se zyada keemti hai.

### Chhota code

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

**Yaad rakho:** Data contract test karo, sirf function nahi — kharab data kharab code se zyada models todta hai.

**Aam galti:** Sirf happy path test karna, jisse poora-null column chupchap constant model train kar deta hai.

Practice: `examples/02_implicit_signals_edits_retries_abandonme.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Building a labelling loop

### Aasaan Bhasha

Projects wahi jagah hain jahan seekha hua chipakta hai. Pehle ek patli end-to-end slice banao — data load, kuch bewakoof train, evaluate, ek prediction serve — phir ek-ek layer sudharo. Pehle din chalne wala baseline us perfect model se behtar hai jo kabhi ship hi nahi hota.

### Chhota code

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

**Yaad rakho:** Hyperparameters tune karne me ek din lagane se pehle galat predictions dekhne me ek ghanta lagao.

**Aam galti:** Chhe hafte feature engineering karna bina kisi baseline ke jo sabit kare ki kisi cheez se fayda hua.

Practice: `examples/03_building_a_labelling_loop.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Active learning: label what is uncertain

### Aasaan Bhasha

Jin examples par aapka model galat hota hai wo aapke sabse keemti training data hain, aur wo muft hain — agar aap unhe capture karo. Pehle din se inputs, outputs aur corrections log karo; launch ke baad feedback loop lagane ka matlab hai zero se shuru karna.

### Chhota code

```python
import numpy as np

def select_for_labelling(probs, budget=5):
    """Label where the model is least certain — uncertainty sampling."""
    margin = np.abs(probs - 0.5)
    return np.argsort(margin)[:budget]

rng = np.random.default_rng(0)
probs = rng.random(20)
pick = select_for_labelling(probs)
print('label these rows first:', pick)
print('their probabilities    :', probs[pick].round(3))
print('\n50 uncertain labels beat 5000 random ones.')
```

**Yaad rakho:** Sirf thumbs-down nahi, correction capture karo. 'Isse kya kehna chahiye tha' hi training signal hai.

**Aam galti:** Bina logging ke ship karna, phir teen mahine traffic ke baad sudhaarne ke liye koi data hi na hona.

Practice: `examples/04_active_learning_label_what_is_uncertain.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Turning corrections into eval cases

### Aasaan Bhasha

Vibes prompt change se nahi bachte. Asli inputs ka chhota golden set banao expected outputs ke saath, har change par chalao, aur score track karo. Open-ended quality ke liye LLM judge use karo, par pehle judge ko human ratings se calibrate karo.

### Chhota code

```python
GOLDEN = [
    {'input': 'charged twice', 'expect': 'BILLING'},
    {'input': 'crashes on upload', 'expect': 'BUG'},
    {'input': 'please add dark mode', 'expect': 'FEATURE'},
]

def classify(text):                      # stand-in for the real model call
    t = text.lower()
    if 'charg' in t or 'bill' in t:
        return 'BILLING'
    if 'crash' in t or 'error' in t:
        return 'BUG'
    return 'FEATURE'

hits = sum(classify(c['input']) == c['expect'] for c in GOLDEN)
print(f'eval score {hits}/{len(GOLDEN)}')
assert hits == len(GOLDEN), 'regression: fix before shipping'
```

**Yaad rakho:** Aapke chune hue 50 asli examples 5000 synthetic examples se behtar hain jinhe kisi ne check hi nahi kiya.

**Aam galti:** Shukravaar ko bina eval ke prompt badalna aur somvaar ko customers se pata chalna.

Practice: `examples/05_turning_corrections_into_eval_cases.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Retraining and re-prompting cadence

### Aasaan Bhasha

Prompt English me likha gaya program hai. Role, task, format aur constraints ke baare me specific raho. Few-shot examples format kisi bhi description se behtar sikhaate hain. Reasoning steps maangna multi-step problems par madad karta hai aur simple lookups par tokens barbaad karta hai.

### Chhota code

```python
prompt = '''You are a support triage assistant.

Classify the ticket into exactly one of: BILLING, BUG, FEATURE, OTHER.
Return JSON only: {"label": ..., "confidence": 0.0-1.0}

Examples:
Ticket: "charged twice this month" -> {"label": "BILLING", "confidence": 0.95}
Ticket: "app crashes on upload"    -> {"label": "BUG", "confidence": 0.92}

Ticket: "can you add dark mode?"
'''
print(prompt)
print('Structure: role -> task -> allowed outputs -> format -> examples -> input.')
```

**Yaad rakho:** Output format sabse aakhir me rakho aur use example ki tarah dikhao — models sabse paas wala pattern copy karte hain.

**Aam galti:** Dhundhla prompt likhna, dhundhla output paana, aur model ko dosh dena.

Practice: `examples/06_retraining_and_re_prompting_cadence.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Avoiding feedback loop bias

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

Practice: `examples/07_avoiding_feedback_loop_bias.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Privacy constraints on user data

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

Practice: `examples/08_privacy_constraints_on_user_data.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Measuring flywheel velocity

### Aasaan Bhasha

ML code ko baaki code jaise tests chahiye, plus data tests: schema, ranges, null rates, class balance. Har known failure mode ke liye ek behavioural test jodo — ek test jo pichhli baar ka outage pakad leta, wo 90% coverage se zyada keemti hai.

### Chhota code

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

**Yaad rakho:** Data contract test karo, sirf function nahi — kharab data kharab code se zyada models todta hai.

**Aam galti:** Sirf happy path test karna, jisse poora-null column chupchap constant model train kar deta hai.

Practice: `examples/09_measuring_flywheel_velocity.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Designing the loop from day one

### Aasaan Bhasha

Jin examples par aapka model galat hota hai wo aapke sabse keemti training data hain, aur wo muft hain — agar aap unhe capture karo. Pehle din se inputs, outputs aur corrections log karo; launch ke baad feedback loop lagane ka matlab hai zero se shuru karna.

### Chhota code

```python
import numpy as np

def select_for_labelling(probs, budget=5):
    """Label where the model is least certain — uncertainty sampling."""
    margin = np.abs(probs - 0.5)
    return np.argsort(margin)[:budget]

rng = np.random.default_rng(0)
probs = rng.random(20)
pick = select_for_labelling(probs)
print('label these rows first:', pick)
print('their probabilities    :', probs[pick].round(3))
print('\n50 uncertain labels beat 5000 random ones.')
```

**Yaad rakho:** Sirf thumbs-down nahi, correction capture karo. 'Isse kya kehna chahiye tha' hi training signal hai.

**Aam galti:** Bina logging ke ship karna, phir teen mahine traffic ke baad sudhaarne ke liye koi data hi na hona.

Practice: `examples/10_designing_the_loop_from_day_one.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 168 ke baad aapko ye aana chahiye

- **Capturing user feedback** ko bina notes dekhe kisi dost ko samjha sakna.
- **Implicit signals: edits, retries, abandonment** ko bina notes dekhe kisi dost ko samjha sakna.
- **Building a labelling loop** ko bina notes dekhe kisi dost ko samjha sakna.
- **Active learning: label what is uncertain** ko bina notes dekhe kisi dost ko samjha sakna.
- **Turning corrections into eval cases** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
