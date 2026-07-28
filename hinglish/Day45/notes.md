# Day 45 — Your first model, end to end

Aaj ka goal: **Your first model, end to end** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | The scikit-learn estimator API |
| 2 | fit, predict, score |
| 3 | Loading a built-in dataset |
| 4 | Splitting the data |
| 5 | Training a logistic regression |
| 6 | Reading the accuracy honestly |
| 7 | Comparing against a dummy baseline |
| 8 | Inspecting the coefficients |
| 9 | Saving and reloading the model |
| 10 | The seven-line template you will reuse forever |

---

## 1. The scikit-learn estimator API

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

Practice: `examples/01_the_scikit_learn_estimator_api.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. fit, predict, score

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

Practice: `examples/02_fit_predict_score.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Loading a built-in dataset

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

Practice: `examples/03_loading_a_built_in_dataset.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Splitting the data

### Aasaan Bhasha

Aaj ka idea — **Splitting the data** — Your first model, end to end ke theme ke andar aata hai. Ise trivia nahi, ek tool ki tarah padho: ye kaam kya karta hai, aapke data ke baare me kya maan kar chalta hai, aur wo maanyata jhooth nikle to kya tootta hai?

### Chhota code

```python
# Explore: Splitting the data
print("practice: Splitting the data")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Yaad rakho:** `Splitting the data` use karne se pehle ek assumption likho jo ye aapke data ke baare me maanta hai.

**Aam galti:** `Splitting the data` ko tutorial se copy-paste kar lena bina jaane ki wo kya maanta hai aur kab fail hota hai.

Practice: `examples/04_splitting_the_data.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Training a logistic regression

### Aasaan Bhasha

Logistic regression linear score ko sigmoid se dabaa kar probability banata hai. Coefficients log-odds hain: +0.7 matlab odds lagbhag double. Jahan decision regulator ko samjhana pade, wahan aaj bhi yahi default hai.

### Chhota code

```python
import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-np.clip(z, -500, 500)))

rng = np.random.default_rng(0)
X = rng.normal(size=(400, 2))
y = (X[:, 0] + X[:, 1] > 0).astype(float)

w, b, lr = np.zeros(2), 0.0, 0.5
for _ in range(500):
    p = sigmoid(X @ w + b)
    w -= lr * (X.T @ (p - y)) / len(y)
    b -= lr * float((p - y).mean())
print('weights', np.round(w, 2), 'acc', ((sigmoid(X @ w + b) > 0.5) == y).mean())
```

**Yaad rakho:** Sigmoid ka input clip karo — bade negative number ka `exp` overflow hokar NaN de deta hai.

**Aam galti:** Raw output ko calibrated probability maan lena bina kabhi calibration curve dekhe.

Practice: `examples/05_training_a_logistic_regression.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Reading the accuracy honestly

### Aasaan Bhasha

Imbalanced data par accuracy sab chhupa leti hai. Precision poochti hai 'jinhe maine flag kiya unme se kitne asli the'; recall poochti hai 'jo asli the unme se kitne maine pakde'. Threshold se aap ek ko doosre ke badle bechte ho, aur kaunsi galti zyada mehngi hai ye business tay karta hai.

### Chhota code

```python
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=2000, weights=[0.95, 0.05], random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, stratify=y, random_state=0)
m = LogisticRegression(max_iter=1000).fit(Xtr, ytr)
print(confusion_matrix(yte, m.predict(Xte)))
print(classification_report(yte, m.predict(Xte), digits=3))
print('roc auc', round(roc_auc_score(yte, m.predict_proba(Xte)[:, 1]), 4))
```

**Yaad rakho:** Decision threshold validation data par tune karo; 0.5 ek default hai, decision nahi.

**Aam galti:** Bhaari imbalanced problem par ROC-AUC optimise karna jahan imaandaar metric precision-recall AUC hai.

Practice: `examples/06_reading_the_accuracy_honestly.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Comparing against a dummy baseline

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

Practice: `examples/07_comparing_against_a_dummy_baseline.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Inspecting the coefficients

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

Practice: `examples/08_inspecting_the_coefficients.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Saving and reloading the model

### Aasaan Bhasha

Aaj ka idea — **Saving and reloading the model** — Your first model, end to end ke theme ke andar aata hai. Ise trivia nahi, ek tool ki tarah padho: ye kaam kya karta hai, aapke data ke baare me kya maan kar chalta hai, aur wo maanyata jhooth nikle to kya tootta hai?

### Chhota code

```python
# Explore: Saving and reloading the model
print("practice: Saving and reloading the model")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Yaad rakho:** `Saving and reloading the model` use karne se pehle ek assumption likho jo ye aapke data ke baare me maanta hai.

**Aam galti:** `Saving and reloading the model` ko tutorial se copy-paste kar lena bina jaane ki wo kya maanta hai aur kab fail hota hai.

Practice: `examples/09_saving_and_reloading_the_model.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. The seven-line template you will reuse forever

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

Practice: `examples/10_the_seven_line_template_you_will_reuse_f.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 45 ke baad aapko ye aana chahiye

- **The scikit-learn estimator API** ko bina notes dekhe kisi dost ko samjha sakna.
- **fit, predict, score** ko bina notes dekhe kisi dost ko samjha sakna.
- **Loading a built-in dataset** ko bina notes dekhe kisi dost ko samjha sakna.
- **Splitting the data** ko bina notes dekhe kisi dost ko samjha sakna.
- **Training a logistic regression** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
