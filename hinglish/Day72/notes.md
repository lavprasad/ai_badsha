# Day 72 — Debugging a model that will not learn

Aaj ka goal: **Debugging a model that will not learn** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Check the data before the model |
| 2 | Verify labels and their alignment |
| 3 | Overfit a tiny subset deliberately |
| 4 | Check for constant or leaky features |
| 5 | Inspect the loss curve |
| 6 | Compare against the dummy baseline |
| 7 | Look at the worst predictions by hand |
| 8 | Check the split for contamination |
| 9 | Simplify until it works, then rebuild |
| 10 | A systematic debugging checklist |

---

## 1. Check the data before the model

### Aasaan Bhasha

Debug ek tay kram me karo, sabse sasta test pehle. Kya model 20 rows par zero loss tak overfit kar sakta hai? Nahi, to bug data ya wiring me hai, capacity me nahi. Kya step zero par loss wahi hai jo random guessing se aana chahiye? Nahi, to labels ya output layer galat hai.

### Chhota code

```python
import numpy as np

def sanity_report(X, y, n_classes):
    print('shapes        ', X.shape, y.shape)
    print('nan in X      ', bool(np.isnan(X).any()))
    const = [i for i in range(X.shape[1]) if np.std(X[:, i]) == 0]
    print('constant cols ', const)
    counts = np.bincount(y, minlength=n_classes)
    print('class counts  ', counts)
    print('expected loss at init ~', round(float(np.log(n_classes)), 4))

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 5)); X[:, 2] = 1.0     # planted constant column
sanity_report(X, rng.integers(0, 3, 200), 3)
```

**Yaad rakho:** Initialisation par expected cross-entropy ln(n_classes) hoti hai. Alag value matlab wiring bug.

**Aam galti:** Do din hyperparameters tune karna aise pipeline par jiske labels ek row se shift the.

Practice: `examples/01_check_the_data_before_the_model.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Verify labels and their alignment

### Aasaan Bhasha

Supervised tuning ke baad models human preference se align kiye jaate hain. RLHF human comparisons par reward model train karta hai, phir PPO se uske khilaaf optimise karta hai. DPO reward model chhod kar seedhe preference pairs optimise karta hai — simple, sasta, aur ab aam choice.

### Chhota code

```python
import numpy as np

# DPO intuition: raise logprob of the chosen reply relative to the rejected one,
# while a KL term keeps you near the reference model.
policy = {'chosen': -2.0, 'rejected': -2.5}     # log-probs under the trained model
ref = {'chosen': -2.4, 'rejected': -2.3}        # log-probs under the frozen reference
beta = 0.1

margin = beta * ((policy['chosen'] - ref['chosen']) - (policy['rejected'] - ref['rejected']))
loss = -np.log(1 / (1 + np.exp(-margin)))
print(f'margin {margin:.4f}  dpo loss {loss:.4f}')
```

**Yaad rakho:** Alignment us cheez ka proxy optimise karta hai jo insaan chahte hain; proxy hamesha game kiya ja sakta hai.

**Aam galti:** Reward model ko itna over-optimise kar dena ki outputs chaploos aur bekaar ho jaayein — classic reward hacking.

Practice: `examples/02_verify_labels_and_their_alignment.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Overfit a tiny subset deliberately

### Aasaan Bhasha

Debug ek tay kram me karo, sabse sasta test pehle. Kya model 20 rows par zero loss tak overfit kar sakta hai? Nahi, to bug data ya wiring me hai, capacity me nahi. Kya step zero par loss wahi hai jo random guessing se aana chahiye? Nahi, to labels ya output layer galat hai.

### Chhota code

```python
import numpy as np

def sanity_report(X, y, n_classes):
    print('shapes        ', X.shape, y.shape)
    print('nan in X      ', bool(np.isnan(X).any()))
    const = [i for i in range(X.shape[1]) if np.std(X[:, i]) == 0]
    print('constant cols ', const)
    counts = np.bincount(y, minlength=n_classes)
    print('class counts  ', counts)
    print('expected loss at init ~', round(float(np.log(n_classes)), 4))

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 5)); X[:, 2] = 1.0     # planted constant column
sanity_report(X, rng.integers(0, 3, 200), 3)
```

**Yaad rakho:** Initialisation par expected cross-entropy ln(n_classes) hoti hai. Alag value matlab wiring bug.

**Aam galti:** Do din hyperparameters tune karna aise pipeline par jiske labels ek row se shift the.

Practice: `examples/03_overfit_a_tiny_subset_deliberately.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Check for constant or leaky features

### Aasaan Bhasha

Debug ek tay kram me karo, sabse sasta test pehle. Kya model 20 rows par zero loss tak overfit kar sakta hai? Nahi, to bug data ya wiring me hai, capacity me nahi. Kya step zero par loss wahi hai jo random guessing se aana chahiye? Nahi, to labels ya output layer galat hai.

### Chhota code

```python
import numpy as np

def sanity_report(X, y, n_classes):
    print('shapes        ', X.shape, y.shape)
    print('nan in X      ', bool(np.isnan(X).any()))
    const = [i for i in range(X.shape[1]) if np.std(X[:, i]) == 0]
    print('constant cols ', const)
    counts = np.bincount(y, minlength=n_classes)
    print('class counts  ', counts)
    print('expected loss at init ~', round(float(np.log(n_classes)), 4))

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 5)); X[:, 2] = 1.0     # planted constant column
sanity_report(X, rng.integers(0, 3, 200), 3)
```

**Yaad rakho:** Initialisation par expected cross-entropy ln(n_classes) hoti hai. Alag value matlab wiring bug.

**Aam galti:** Do din hyperparameters tune karna aise pipeline par jiske labels ek row se shift the.

Practice: `examples/04_check_for_constant_or_leaky_features.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Inspect the loss curve

### Aasaan Bhasha

Debug ek tay kram me karo, sabse sasta test pehle. Kya model 20 rows par zero loss tak overfit kar sakta hai? Nahi, to bug data ya wiring me hai, capacity me nahi. Kya step zero par loss wahi hai jo random guessing se aana chahiye? Nahi, to labels ya output layer galat hai.

### Chhota code

```python
import numpy as np

def sanity_report(X, y, n_classes):
    print('shapes        ', X.shape, y.shape)
    print('nan in X      ', bool(np.isnan(X).any()))
    const = [i for i in range(X.shape[1]) if np.std(X[:, i]) == 0]
    print('constant cols ', const)
    counts = np.bincount(y, minlength=n_classes)
    print('class counts  ', counts)
    print('expected loss at init ~', round(float(np.log(n_classes)), 4))

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 5)); X[:, 2] = 1.0     # planted constant column
sanity_report(X, rng.integers(0, 3, 200), 3)
```

**Yaad rakho:** Initialisation par expected cross-entropy ln(n_classes) hoti hai. Alag value matlab wiring bug.

**Aam galti:** Do din hyperparameters tune karna aise pipeline par jiske labels ek row se shift the.

Practice: `examples/05_inspect_the_loss_curve.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Compare against the dummy baseline

### Aasaan Bhasha

Har scikit-learn model ke wahi teen methods hain, matlab algorithm badalna ek line ka kaam hai. Har problem `DummyClassifier` se shuru karo — agar aapka asli model 'hamesha majority class bolo' ko saaf farq se nahi haraata, to gadbad data me hai, model me nahi.

### Chhota code

```python
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, stratify=y, random_state=0)

baseline = DummyClassifier(strategy='most_frequent').fit(Xtr, ytr)
model = RandomForestClassifier(n_estimators=200, random_state=0).fit(Xtr, ytr)
print(f'dummy {baseline.score(Xte, yte):.3f}   model {model.score(Xte, yte):.3f}')
```

**Yaad rakho:** Apne model ka score dummy ke score ke bagal me batao. Akela number kuch matlab nahi rakhta.

**Aam galti:** Aise data par 92% accuracy ka jashn manana jahan 91% rows ek hi class ki hain.

Practice: `examples/06_compare_against_the_dummy_baseline.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Look at the worst predictions by hand

### Aasaan Bhasha

Debug ek tay kram me karo, sabse sasta test pehle. Kya model 20 rows par zero loss tak overfit kar sakta hai? Nahi, to bug data ya wiring me hai, capacity me nahi. Kya step zero par loss wahi hai jo random guessing se aana chahiye? Nahi, to labels ya output layer galat hai.

### Chhota code

```python
import numpy as np

def sanity_report(X, y, n_classes):
    print('shapes        ', X.shape, y.shape)
    print('nan in X      ', bool(np.isnan(X).any()))
    const = [i for i in range(X.shape[1]) if np.std(X[:, i]) == 0]
    print('constant cols ', const)
    counts = np.bincount(y, minlength=n_classes)
    print('class counts  ', counts)
    print('expected loss at init ~', round(float(np.log(n_classes)), 4))

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 5)); X[:, 2] = 1.0     # planted constant column
sanity_report(X, rng.integers(0, 3, 200), 3)
```

**Yaad rakho:** Initialisation par expected cross-entropy ln(n_classes) hoti hai. Alag value matlab wiring bug.

**Aam galti:** Do din hyperparameters tune karna aise pipeline par jiske labels ek row se shift the.

Practice: `examples/07_look_at_the_worst_predictions_by_hand.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Check the split for contamination

### Aasaan Bhasha

Debug ek tay kram me karo, sabse sasta test pehle. Kya model 20 rows par zero loss tak overfit kar sakta hai? Nahi, to bug data ya wiring me hai, capacity me nahi. Kya step zero par loss wahi hai jo random guessing se aana chahiye? Nahi, to labels ya output layer galat hai.

### Chhota code

```python
import numpy as np

def sanity_report(X, y, n_classes):
    print('shapes        ', X.shape, y.shape)
    print('nan in X      ', bool(np.isnan(X).any()))
    const = [i for i in range(X.shape[1]) if np.std(X[:, i]) == 0]
    print('constant cols ', const)
    counts = np.bincount(y, minlength=n_classes)
    print('class counts  ', counts)
    print('expected loss at init ~', round(float(np.log(n_classes)), 4))

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 5)); X[:, 2] = 1.0     # planted constant column
sanity_report(X, rng.integers(0, 3, 200), 3)
```

**Yaad rakho:** Initialisation par expected cross-entropy ln(n_classes) hoti hai. Alag value matlab wiring bug.

**Aam galti:** Do din hyperparameters tune karna aise pipeline par jiske labels ek row se shift the.

Practice: `examples/08_check_the_split_for_contamination.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Simplify until it works, then rebuild

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

Practice: `examples/09_simplify_until_it_works_then_rebuild.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. A systematic debugging checklist

### Aasaan Bhasha

Debug ek tay kram me karo, sabse sasta test pehle. Kya model 20 rows par zero loss tak overfit kar sakta hai? Nahi, to bug data ya wiring me hai, capacity me nahi. Kya step zero par loss wahi hai jo random guessing se aana chahiye? Nahi, to labels ya output layer galat hai.

### Chhota code

```python
import numpy as np

def sanity_report(X, y, n_classes):
    print('shapes        ', X.shape, y.shape)
    print('nan in X      ', bool(np.isnan(X).any()))
    const = [i for i in range(X.shape[1]) if np.std(X[:, i]) == 0]
    print('constant cols ', const)
    counts = np.bincount(y, minlength=n_classes)
    print('class counts  ', counts)
    print('expected loss at init ~', round(float(np.log(n_classes)), 4))

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 5)); X[:, 2] = 1.0     # planted constant column
sanity_report(X, rng.integers(0, 3, 200), 3)
```

**Yaad rakho:** Initialisation par expected cross-entropy ln(n_classes) hoti hai. Alag value matlab wiring bug.

**Aam galti:** Do din hyperparameters tune karna aise pipeline par jiske labels ek row se shift the.

Practice: `examples/10_a_systematic_debugging_checklist.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 72 ke baad aapko ye aana chahiye

- **Check the data before the model** ko bina notes dekhe kisi dost ko samjha sakna.
- **Verify labels and their alignment** ko bina notes dekhe kisi dost ko samjha sakna.
- **Overfit a tiny subset deliberately** ko bina notes dekhe kisi dost ko samjha sakna.
- **Check for constant or leaky features** ko bina notes dekhe kisi dost ko samjha sakna.
- **Inspect the loss curve** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
