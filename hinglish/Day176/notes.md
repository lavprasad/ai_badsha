# Day 176 — Testing machine learning code

Aaj ka goal: **Testing machine learning code** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Unit tests for transforms |
| 2 | Data schema tests |
| 3 | Model contract tests: shape and range |
| 4 | Behavioural tests for known cases |
| 5 | Metamorphic testing |
| 6 | Fixture datasets |
| 7 | Testing training runs cheaply |
| 8 | Golden-file tests for prompts |
| 9 | Flaky tests from randomness |
| 10 | A test suite you actually run |

---

## 1. Unit tests for transforms

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

Practice: `examples/01_unit_tests_for_transforms.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Data schema tests

### Aasaan Bhasha

ML tests parton me aate hain: transforms par unit tests, data par contract tests, behaviour par metamorphic tests (bemaani feature jodne se prediction nahi badalni chahiye), aur fixture dataset par chhota end-to-end run. Poora suite ek minute ke andar rakho warna koi use chalayega hi nahi.

### Chhota code

```python
import numpy as np

def predict(x, w):
    return float(x @ w)

def test_metamorphic_scaling():
    """Doubling all inputs must double a linear prediction."""
    w = np.array([2.0, -1.0])
    x = np.array([3.0, 4.0])
    assert abs(predict(2 * x, w) - 2 * predict(x, w)) < 1e-9

def test_deterministic():
    """Same seed, same result — or your test suite will flake forever."""
    a = np.random.default_rng(42).normal(size=5)
    b = np.random.default_rng(42).normal(size=5)
    assert np.allclose(a, b)

test_metamorphic_scaling()
test_deterministic()
print('all tests passed')
```

**Yaad rakho:** Randomness chhoone wale har test ko explicit seed milna chahiye. Parallelism ke neeche global seeding kaafi nahi hai.

**Aam galti:** Itna dheema test suite ki CI use skip kar de aur bugs phir bhi production tak pahuch jaayein.

Practice: `examples/02_data_schema_tests.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Model contract tests: shape and range

### Aasaan Bhasha

Agar aap decision samjha nahi sakte, to aap use defend bhi nahi kar sakte — aur credit, hiring aur healthcare me ye legally zaroori hai. Permutation importance model-agnostic aur imaandaar hai. SHAP per-prediction attributions deta hai theoretical base ke saath par sach me compute maangta hai.

### Chhota code

```python
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

X, y = load_breast_cancer(return_X_y=True)
names = load_breast_cancer().feature_names
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0)
m = RandomForestClassifier(n_estimators=200, random_state=0, n_jobs=-1).fit(Xtr, ytr)

imp = permutation_importance(m, Xte, yte, n_repeats=10, random_state=0)
for i in np.argsort(-imp.importances_mean)[:5]:
    print(f'{names[i]:<28} {imp.importances_mean[i]:.4f}')
```

**Yaad rakho:** TEST set par permutation importance batati hai ki generalise karne ke liye model kis par tik raha hai.

**Aam galti:** Importance ko causation ki tarah pesh karna — model ne correlation dhoonda hai, bas.

Practice: `examples/03_model_contract_tests_shape_and_range.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Behavioural tests for known cases

### Aasaan Bhasha

Classification batati hai kya; detection batata hai kya aur kahan. Boxes ko IoU (intersection over union) se score kiya jaata hai aur duplicates non-maximum suppression se hataye jaate hain. Segmentation isse aage ja kar har pixel ko label karta hai.

### Chhota code

```python
def iou(a, b):
    """Boxes as (x1, y1, x2, y2)."""
    x1, y1 = max(a[0], b[0]), max(a[1], b[1])
    x2, y2 = min(a[2], b[2]), min(a[3], b[3])
    inter = max(0, x2 - x1) * max(0, y2 - y1)
    area_a = (a[2] - a[0]) * (a[3] - a[1])
    area_b = (b[2] - b[0]) * (b[3] - b[1])
    return inter / (area_a + area_b - inter)

print(round(iou((0, 0, 10, 10), (5, 5, 15, 15)), 4))   # 0.1429
```

**Yaad rakho:** IoU >= 0.5 aam 'sahi detection' threshold hai; accuracy nahi, mAP report karo.

**Aam galti:** Model aur evaluation code ke beech box formats mila dena (xywh vs xyxy).

Practice: `examples/04_behavioural_tests_for_known_cases.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Metamorphic testing

### Aasaan Bhasha

ML tests parton me aate hain: transforms par unit tests, data par contract tests, behaviour par metamorphic tests (bemaani feature jodne se prediction nahi badalni chahiye), aur fixture dataset par chhota end-to-end run. Poora suite ek minute ke andar rakho warna koi use chalayega hi nahi.

### Chhota code

```python
import numpy as np

def predict(x, w):
    return float(x @ w)

def test_metamorphic_scaling():
    """Doubling all inputs must double a linear prediction."""
    w = np.array([2.0, -1.0])
    x = np.array([3.0, 4.0])
    assert abs(predict(2 * x, w) - 2 * predict(x, w)) < 1e-9

def test_deterministic():
    """Same seed, same result — or your test suite will flake forever."""
    a = np.random.default_rng(42).normal(size=5)
    b = np.random.default_rng(42).normal(size=5)
    assert np.allclose(a, b)

test_metamorphic_scaling()
test_deterministic()
print('all tests passed')
```

**Yaad rakho:** Randomness chhoone wale har test ko explicit seed milna chahiye. Parallelism ke neeche global seeding kaafi nahi hai.

**Aam galti:** Itna dheema test suite ki CI use skip kar de aur bugs phir bhi production tak pahuch jaayein.

Practice: `examples/05_metamorphic_testing.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Fixture datasets

### Aasaan Bhasha

ML tests parton me aate hain: transforms par unit tests, data par contract tests, behaviour par metamorphic tests (bemaani feature jodne se prediction nahi badalni chahiye), aur fixture dataset par chhota end-to-end run. Poora suite ek minute ke andar rakho warna koi use chalayega hi nahi.

### Chhota code

```python
import numpy as np

def predict(x, w):
    return float(x @ w)

def test_metamorphic_scaling():
    """Doubling all inputs must double a linear prediction."""
    w = np.array([2.0, -1.0])
    x = np.array([3.0, 4.0])
    assert abs(predict(2 * x, w) - 2 * predict(x, w)) < 1e-9

def test_deterministic():
    """Same seed, same result — or your test suite will flake forever."""
    a = np.random.default_rng(42).normal(size=5)
    b = np.random.default_rng(42).normal(size=5)
    assert np.allclose(a, b)

test_metamorphic_scaling()
test_deterministic()
print('all tests passed')
```

**Yaad rakho:** Randomness chhoone wale har test ko explicit seed milna chahiye. Parallelism ke neeche global seeding kaafi nahi hai.

**Aam galti:** Itna dheema test suite ki CI use skip kar de aur bugs phir bhi production tak pahuch jaayein.

Practice: `examples/06_fixture_datasets.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Testing training runs cheaply

### Aasaan Bhasha

ML tests parton me aate hain: transforms par unit tests, data par contract tests, behaviour par metamorphic tests (bemaani feature jodne se prediction nahi badalni chahiye), aur fixture dataset par chhota end-to-end run. Poora suite ek minute ke andar rakho warna koi use chalayega hi nahi.

### Chhota code

```python
import numpy as np

def predict(x, w):
    return float(x @ w)

def test_metamorphic_scaling():
    """Doubling all inputs must double a linear prediction."""
    w = np.array([2.0, -1.0])
    x = np.array([3.0, 4.0])
    assert abs(predict(2 * x, w) - 2 * predict(x, w)) < 1e-9

def test_deterministic():
    """Same seed, same result — or your test suite will flake forever."""
    a = np.random.default_rng(42).normal(size=5)
    b = np.random.default_rng(42).normal(size=5)
    assert np.allclose(a, b)

test_metamorphic_scaling()
test_deterministic()
print('all tests passed')
```

**Yaad rakho:** Randomness chhoone wale har test ko explicit seed milna chahiye. Parallelism ke neeche global seeding kaafi nahi hai.

**Aam galti:** Itna dheema test suite ki CI use skip kar de aur bugs phir bhi production tak pahuch jaayein.

Practice: `examples/07_testing_training_runs_cheaply.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Golden-file tests for prompts

### Aasaan Bhasha

ML tests parton me aate hain: transforms par unit tests, data par contract tests, behaviour par metamorphic tests (bemaani feature jodne se prediction nahi badalni chahiye), aur fixture dataset par chhota end-to-end run. Poora suite ek minute ke andar rakho warna koi use chalayega hi nahi.

### Chhota code

```python
import numpy as np

def predict(x, w):
    return float(x @ w)

def test_metamorphic_scaling():
    """Doubling all inputs must double a linear prediction."""
    w = np.array([2.0, -1.0])
    x = np.array([3.0, 4.0])
    assert abs(predict(2 * x, w) - 2 * predict(x, w)) < 1e-9

def test_deterministic():
    """Same seed, same result — or your test suite will flake forever."""
    a = np.random.default_rng(42).normal(size=5)
    b = np.random.default_rng(42).normal(size=5)
    assert np.allclose(a, b)

test_metamorphic_scaling()
test_deterministic()
print('all tests passed')
```

**Yaad rakho:** Randomness chhoone wale har test ko explicit seed milna chahiye. Parallelism ke neeche global seeding kaafi nahi hai.

**Aam galti:** Itna dheema test suite ki CI use skip kar de aur bugs phir bhi production tak pahuch jaayein.

Practice: `examples/08_golden_file_tests_for_prompts.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Flaky tests from randomness

### Aasaan Bhasha

ML tests parton me aate hain: transforms par unit tests, data par contract tests, behaviour par metamorphic tests (bemaani feature jodne se prediction nahi badalni chahiye), aur fixture dataset par chhota end-to-end run. Poora suite ek minute ke andar rakho warna koi use chalayega hi nahi.

### Chhota code

```python
import numpy as np

def predict(x, w):
    return float(x @ w)

def test_metamorphic_scaling():
    """Doubling all inputs must double a linear prediction."""
    w = np.array([2.0, -1.0])
    x = np.array([3.0, 4.0])
    assert abs(predict(2 * x, w) - 2 * predict(x, w)) < 1e-9

def test_deterministic():
    """Same seed, same result — or your test suite will flake forever."""
    a = np.random.default_rng(42).normal(size=5)
    b = np.random.default_rng(42).normal(size=5)
    assert np.allclose(a, b)

test_metamorphic_scaling()
test_deterministic()
print('all tests passed')
```

**Yaad rakho:** Randomness chhoone wale har test ko explicit seed milna chahiye. Parallelism ke neeche global seeding kaafi nahi hai.

**Aam galti:** Itna dheema test suite ki CI use skip kar de aur bugs phir bhi production tak pahuch jaayein.

Practice: `examples/09_flaky_tests_from_randomness.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. A test suite you actually run

### Aasaan Bhasha

ML tests parton me aate hain: transforms par unit tests, data par contract tests, behaviour par metamorphic tests (bemaani feature jodne se prediction nahi badalni chahiye), aur fixture dataset par chhota end-to-end run. Poora suite ek minute ke andar rakho warna koi use chalayega hi nahi.

### Chhota code

```python
import numpy as np

def predict(x, w):
    return float(x @ w)

def test_metamorphic_scaling():
    """Doubling all inputs must double a linear prediction."""
    w = np.array([2.0, -1.0])
    x = np.array([3.0, 4.0])
    assert abs(predict(2 * x, w) - 2 * predict(x, w)) < 1e-9

def test_deterministic():
    """Same seed, same result — or your test suite will flake forever."""
    a = np.random.default_rng(42).normal(size=5)
    b = np.random.default_rng(42).normal(size=5)
    assert np.allclose(a, b)

test_metamorphic_scaling()
test_deterministic()
print('all tests passed')
```

**Yaad rakho:** Randomness chhoone wale har test ko explicit seed milna chahiye. Parallelism ke neeche global seeding kaafi nahi hai.

**Aam galti:** Itna dheema test suite ki CI use skip kar de aur bugs phir bhi production tak pahuch jaayein.

Practice: `examples/10_a_test_suite_you_actually_run.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 176 ke baad aapko ye aana chahiye

- **Unit tests for transforms** ko bina notes dekhe kisi dost ko samjha sakna.
- **Data schema tests** ko bina notes dekhe kisi dost ko samjha sakna.
- **Model contract tests: shape and range** ko bina notes dekhe kisi dost ko samjha sakna.
- **Behavioural tests for known cases** ko bina notes dekhe kisi dost ko samjha sakna.
- **Metamorphic testing** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
