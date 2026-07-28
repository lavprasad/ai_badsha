# Day 35 — The machine learning problem framing

Aaj ka goal: **The machine learning problem framing** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Starting from the decision, not the data |
| 2 | Supervised, unsupervised, reinforcement |
| 3 | Classification vs regression vs ranking |
| 4 | Choosing a target variable |
| 5 | Choosing an evaluation metric |
| 6 | Defining the unit of prediction |
| 7 | Baselines you must beat |
| 8 | Feasibility: is the signal even there |
| 9 | When not to use machine learning |
| 10 | Writing a one-page problem statement |

---

## 1. Starting from the decision, not the data

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

Practice: `examples/01_starting_from_the_decision_not_the_data.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Supervised, unsupervised, reinforcement

### Aasaan Bhasha

Zyadatar fail hue ML projects modelling par nahi, framing par fail hue. Likh kar rakho: is prediction se kaunsa decision badlega, prediction ki unit kya hai, kaunsa metric safalta naapta hai, aur sabse bewakoof baseline kitna laata hai. Agar ek rule aapke model ko haraata hai, to rule hi ship karo.

### Chhota code

```python
BRIEF = {
    'decision': 'Which support tickets get routed to the billing team',
    'unit': 'one ticket at creation time',
    'target': 'team that eventually resolved it',
    'metric': 'macro F1, because small teams matter as much as big ones',
    'baseline': 'keyword rules -> 0.61 macro F1',
    'available_at_predict_time': ['subject', 'body', 'customer_plan'],
    'not_available': ['resolution_time', 'agent_notes'],
}
for k, v in BRIEF.items():
    print(f'{k:>26}: {v}')
```

**Yaad rakho:** Features list karne se pehle likho ki *prediction ke waqt* kaunsa data maujood hoga. Wahi list zyadatar leaks maar deti hai.

**Aam galti:** Chhe hafte model banana aur phir pata chalna ki jo decision ye support karta hai wo pehle se automated hai.

Practice: `examples/02_supervised_unsupervised_reinforcement.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Classification vs regression vs ranking

### Aasaan Bhasha

Collaborative filtering kehta hai: jinhe wo pasand aaya jo aapko pasand aaya, unhe X bhi pasand aaya. Matrix factorisation latent user aur item vectors seekhta hai jinka dot product rating predict karta hai. Cold-start problem — naye users aur naye items bina history ke — content features se hal hoti hai, aur factorisation se nahi.

### Chhota code

```python
import numpy as np

R = np.array([
    [5, 3, 0, 1],
    [4, 0, 0, 1],
    [1, 1, 0, 5],
    [0, 0, 5, 4],
], dtype=float)
mask = R > 0

rng = np.random.default_rng(0)
U, V = rng.normal(size=(4, 2)) * 0.1, rng.normal(size=(4, 2)) * 0.1
for _ in range(3000):
    err = (U @ V.T - R) * mask
    U -= 0.02 * (err @ V + 0.05 * U)
    V -= 0.02 * (err.T @ U + 0.05 * V)
print((U @ V.T).round(2))
```

**Yaad rakho:** Recommenders ko ranking metrics (precision@k, NDCG) se evaluate karo, ratings par RMSE se nahi.

**Aam galti:** Aisa feedback loop banana jo hamesha wahi recommend karta hai jo pehle se recommend kar raha tha.

Practice: `examples/03_classification_vs_regression_vs_ranking.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Choosing a target variable

### Aasaan Bhasha

Zyadatar fail hue ML projects modelling par nahi, framing par fail hue. Likh kar rakho: is prediction se kaunsa decision badlega, prediction ki unit kya hai, kaunsa metric safalta naapta hai, aur sabse bewakoof baseline kitna laata hai. Agar ek rule aapke model ko haraata hai, to rule hi ship karo.

### Chhota code

```python
BRIEF = {
    'decision': 'Which support tickets get routed to the billing team',
    'unit': 'one ticket at creation time',
    'target': 'team that eventually resolved it',
    'metric': 'macro F1, because small teams matter as much as big ones',
    'baseline': 'keyword rules -> 0.61 macro F1',
    'available_at_predict_time': ['subject', 'body', 'customer_plan'],
    'not_available': ['resolution_time', 'agent_notes'],
}
for k, v in BRIEF.items():
    print(f'{k:>26}: {v}')
```

**Yaad rakho:** Features list karne se pehle likho ki *prediction ke waqt* kaunsa data maujood hoga. Wahi list zyadatar leaks maar deti hai.

**Aam galti:** Chhe hafte model banana aur phir pata chalna ki jo decision ye support karta hai wo pehle se automated hai.

Practice: `examples/04_choosing_a_target_variable.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Choosing an evaluation metric

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

Practice: `examples/05_choosing_an_evaluation_metric.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Defining the unit of prediction

### Aasaan Bhasha

Zyadatar fail hue ML projects modelling par nahi, framing par fail hue. Likh kar rakho: is prediction se kaunsa decision badlega, prediction ki unit kya hai, kaunsa metric safalta naapta hai, aur sabse bewakoof baseline kitna laata hai. Agar ek rule aapke model ko haraata hai, to rule hi ship karo.

### Chhota code

```python
BRIEF = {
    'decision': 'Which support tickets get routed to the billing team',
    'unit': 'one ticket at creation time',
    'target': 'team that eventually resolved it',
    'metric': 'macro F1, because small teams matter as much as big ones',
    'baseline': 'keyword rules -> 0.61 macro F1',
    'available_at_predict_time': ['subject', 'body', 'customer_plan'],
    'not_available': ['resolution_time', 'agent_notes'],
}
for k, v in BRIEF.items():
    print(f'{k:>26}: {v}')
```

**Yaad rakho:** Features list karne se pehle likho ki *prediction ke waqt* kaunsa data maujood hoga. Wahi list zyadatar leaks maar deti hai.

**Aam galti:** Chhe hafte model banana aur phir pata chalna ki jo decision ye support karta hai wo pehle se automated hai.

Practice: `examples/06_defining_the_unit_of_prediction.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Baselines you must beat

### Aasaan Bhasha

Zyadatar fail hue ML projects modelling par nahi, framing par fail hue. Likh kar rakho: is prediction se kaunsa decision badlega, prediction ki unit kya hai, kaunsa metric safalta naapta hai, aur sabse bewakoof baseline kitna laata hai. Agar ek rule aapke model ko haraata hai, to rule hi ship karo.

### Chhota code

```python
BRIEF = {
    'decision': 'Which support tickets get routed to the billing team',
    'unit': 'one ticket at creation time',
    'target': 'team that eventually resolved it',
    'metric': 'macro F1, because small teams matter as much as big ones',
    'baseline': 'keyword rules -> 0.61 macro F1',
    'available_at_predict_time': ['subject', 'body', 'customer_plan'],
    'not_available': ['resolution_time', 'agent_notes'],
}
for k, v in BRIEF.items():
    print(f'{k:>26}: {v}')
```

**Yaad rakho:** Features list karne se pehle likho ki *prediction ke waqt* kaunsa data maujood hoga. Wahi list zyadatar leaks maar deti hai.

**Aam galti:** Chhe hafte model banana aur phir pata chalna ki jo decision ye support karta hai wo pehle se automated hai.

Practice: `examples/07_baselines_you_must_beat.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Feasibility: is the signal even there

### Aasaan Bhasha

Zyadatar fail hue ML projects modelling par nahi, framing par fail hue. Likh kar rakho: is prediction se kaunsa decision badlega, prediction ki unit kya hai, kaunsa metric safalta naapta hai, aur sabse bewakoof baseline kitna laata hai. Agar ek rule aapke model ko haraata hai, to rule hi ship karo.

### Chhota code

```python
BRIEF = {
    'decision': 'Which support tickets get routed to the billing team',
    'unit': 'one ticket at creation time',
    'target': 'team that eventually resolved it',
    'metric': 'macro F1, because small teams matter as much as big ones',
    'baseline': 'keyword rules -> 0.61 macro F1',
    'available_at_predict_time': ['subject', 'body', 'customer_plan'],
    'not_available': ['resolution_time', 'agent_notes'],
}
for k, v in BRIEF.items():
    print(f'{k:>26}: {v}')
```

**Yaad rakho:** Features list karne se pehle likho ki *prediction ke waqt* kaunsa data maujood hoga. Wahi list zyadatar leaks maar deti hai.

**Aam galti:** Chhe hafte model banana aur phir pata chalna ki jo decision ye support karta hai wo pehle se automated hai.

Practice: `examples/08_feasibility_is_the_signal_even_there.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. When not to use machine learning

### Aasaan Bhasha

Zyadatar fail hue ML projects modelling par nahi, framing par fail hue. Likh kar rakho: is prediction se kaunsa decision badlega, prediction ki unit kya hai, kaunsa metric safalta naapta hai, aur sabse bewakoof baseline kitna laata hai. Agar ek rule aapke model ko haraata hai, to rule hi ship karo.

### Chhota code

```python
BRIEF = {
    'decision': 'Which support tickets get routed to the billing team',
    'unit': 'one ticket at creation time',
    'target': 'team that eventually resolved it',
    'metric': 'macro F1, because small teams matter as much as big ones',
    'baseline': 'keyword rules -> 0.61 macro F1',
    'available_at_predict_time': ['subject', 'body', 'customer_plan'],
    'not_available': ['resolution_time', 'agent_notes'],
}
for k, v in BRIEF.items():
    print(f'{k:>26}: {v}')
```

**Yaad rakho:** Features list karne se pehle likho ki *prediction ke waqt* kaunsa data maujood hoga. Wahi list zyadatar leaks maar deti hai.

**Aam galti:** Chhe hafte model banana aur phir pata chalna ki jo decision ye support karta hai wo pehle se automated hai.

Practice: `examples/09_when_not_to_use_machine_learning.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Writing a one-page problem statement

### Aasaan Bhasha

Zyadatar fail hue ML projects modelling par nahi, framing par fail hue. Likh kar rakho: is prediction se kaunsa decision badlega, prediction ki unit kya hai, kaunsa metric safalta naapta hai, aur sabse bewakoof baseline kitna laata hai. Agar ek rule aapke model ko haraata hai, to rule hi ship karo.

### Chhota code

```python
BRIEF = {
    'decision': 'Which support tickets get routed to the billing team',
    'unit': 'one ticket at creation time',
    'target': 'team that eventually resolved it',
    'metric': 'macro F1, because small teams matter as much as big ones',
    'baseline': 'keyword rules -> 0.61 macro F1',
    'available_at_predict_time': ['subject', 'body', 'customer_plan'],
    'not_available': ['resolution_time', 'agent_notes'],
}
for k, v in BRIEF.items():
    print(f'{k:>26}: {v}')
```

**Yaad rakho:** Features list karne se pehle likho ki *prediction ke waqt* kaunsa data maujood hoga. Wahi list zyadatar leaks maar deti hai.

**Aam galti:** Chhe hafte model banana aur phir pata chalna ki jo decision ye support karta hai wo pehle se automated hai.

Practice: `examples/10_writing_a_one_page_problem_statement.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 35 ke baad aapko ye aana chahiye

- **Starting from the decision, not the data** ko bina notes dekhe kisi dost ko samjha sakna.
- **Supervised, unsupervised, reinforcement** ko bina notes dekhe kisi dost ko samjha sakna.
- **Classification vs regression vs ranking** ko bina notes dekhe kisi dost ko samjha sakna.
- **Choosing a target variable** ko bina notes dekhe kisi dost ko samjha sakna.
- **Choosing an evaluation metric** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
