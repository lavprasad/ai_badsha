# Day 176 — Testing machine learning code

Today's goal: work through **testing machine learning code** — ten concepts, ten runnable examples, five questions.

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

ML code needs the same tests as any code, plus data tests: schema, ranges, null rates, class balance. Add one behavioural test per known failure mode — a test that would have caught last quarter's outage is worth more than 90% coverage.

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

**Remember:** Test the data contract, not just the function — bad data breaks more models than bad code.

**Common mistake:** Testing only the happy path, so an all-null column silently trains a constant model.

## 2. Data schema tests

ML tests come in layers: unit tests on transforms, contract tests on data, metamorphic tests on behaviour (adding an irrelevant feature must not change the prediction), and a tiny end-to-end run on a fixture dataset. Keep the whole suite under a minute or nobody will run it.

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

**Remember:** Every test that touches randomness must pass an explicit seed. Global seeding is not enough under parallelism.

**Common mistake:** A test suite so slow that CI skips it and bugs reach production anyway.

## 3. Model contract tests: shape and range

If you cannot explain a decision, you cannot defend it — and in credit, hiring and healthcare you are legally required to. Permutation importance is model-agnostic and honest. SHAP gives per-prediction attributions with a solid theoretical basis but costs real compute.

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

**Remember:** Permutation importance on the TEST set answers 'what does this model rely on to generalise'.

**Common mistake:** Presenting importance as causation — the model found correlation, nothing more.

## 4. Behavioural tests for known cases

Classification says what; detection says what and where. Boxes are scored by IoU (intersection over union) and duplicates are removed with non-maximum suppression. Segmentation goes further and labels every pixel.

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

**Remember:** IoU >= 0.5 is the usual 'correct detection' threshold; report mAP, not accuracy.

**Common mistake:** Mixing box formats (xywh vs xyxy) between the model and the evaluation code.

## 5. Metamorphic testing

ML tests come in layers: unit tests on transforms, contract tests on data, metamorphic tests on behaviour (adding an irrelevant feature must not change the prediction), and a tiny end-to-end run on a fixture dataset. Keep the whole suite under a minute or nobody will run it.

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

**Remember:** Every test that touches randomness must pass an explicit seed. Global seeding is not enough under parallelism.

**Common mistake:** A test suite so slow that CI skips it and bugs reach production anyway.

## 6. Fixture datasets

ML tests come in layers: unit tests on transforms, contract tests on data, metamorphic tests on behaviour (adding an irrelevant feature must not change the prediction), and a tiny end-to-end run on a fixture dataset. Keep the whole suite under a minute or nobody will run it.

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

**Remember:** Every test that touches randomness must pass an explicit seed. Global seeding is not enough under parallelism.

**Common mistake:** A test suite so slow that CI skips it and bugs reach production anyway.

## 7. Testing training runs cheaply

ML tests come in layers: unit tests on transforms, contract tests on data, metamorphic tests on behaviour (adding an irrelevant feature must not change the prediction), and a tiny end-to-end run on a fixture dataset. Keep the whole suite under a minute or nobody will run it.

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

**Remember:** Every test that touches randomness must pass an explicit seed. Global seeding is not enough under parallelism.

**Common mistake:** A test suite so slow that CI skips it and bugs reach production anyway.

## 8. Golden-file tests for prompts

ML tests come in layers: unit tests on transforms, contract tests on data, metamorphic tests on behaviour (adding an irrelevant feature must not change the prediction), and a tiny end-to-end run on a fixture dataset. Keep the whole suite under a minute or nobody will run it.

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

**Remember:** Every test that touches randomness must pass an explicit seed. Global seeding is not enough under parallelism.

**Common mistake:** A test suite so slow that CI skips it and bugs reach production anyway.

## 9. Flaky tests from randomness

ML tests come in layers: unit tests on transforms, contract tests on data, metamorphic tests on behaviour (adding an irrelevant feature must not change the prediction), and a tiny end-to-end run on a fixture dataset. Keep the whole suite under a minute or nobody will run it.

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

**Remember:** Every test that touches randomness must pass an explicit seed. Global seeding is not enough under parallelism.

**Common mistake:** A test suite so slow that CI skips it and bugs reach production anyway.

## 10. A test suite you actually run

ML tests come in layers: unit tests on transforms, contract tests on data, metamorphic tests on behaviour (adding an irrelevant feature must not change the prediction), and a tiny end-to-end run on a fixture dataset. Keep the whole suite under a minute or nobody will run it.

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

**Remember:** Every test that touches randomness must pass an explicit seed. Global seeding is not enough under parallelism.

**Common mistake:** A test suite so slow that CI skips it and bugs reach production anyway.

---

## What you should be able to do after Day 176

- Explain **Unit tests for transforms** to someone else without notes.
- Explain **Data schema tests** to someone else without notes.
- Explain **Model contract tests: shape and range** to someone else without notes.
- Explain **Behavioural tests for known cases** to someone else without notes.
- Explain **Metamorphic testing** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
