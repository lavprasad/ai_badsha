# Day 05 — Objects, errors and clean code

Today's goal: work through **Objects, errors and clean code** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Classes and instances |
| 2 | __init__, attributes and methods |
| 3 | Dunder methods: __repr__, __len__ |
| 4 | Dataclasses for config objects |
| 5 | Inheritance vs composition |
| 6 | Exceptions: raise, try, except |
| 7 | Custom exception classes |
| 8 | assert for invariants |
| 9 | Type hints and why they help |
| 10 | Writing code your future self can read |

---

## 1. Classes and instances

A class bundles data with the operations that keep it valid. For plain config or record objects, `@dataclass` gives you `__init__`, `__repr__` and `__eq__` for free. Prefer composition over inheritance: deep class trees are hard to change and easy to break.

```python
from dataclasses import dataclass, field

@dataclass
class TrainConfig:
    lr: float = 1e-3
    epochs: int = 10
    tags: list[str] = field(default_factory=list)   # never a bare []

    def __post_init__(self):
        assert self.lr > 0, 'learning rate must be positive'

cfg = TrainConfig(lr=3e-4, epochs=5)
print(cfg)
```

**Remember:** In a dataclass, mutable defaults need `field(default_factory=...)`, not a literal.

**Common mistake:** Building a five-level inheritance hierarchy for what a dict and two functions would have solved.

## 2. __init__, attributes and methods

A class bundles data with the operations that keep it valid. For plain config or record objects, `@dataclass` gives you `__init__`, `__repr__` and `__eq__` for free. Prefer composition over inheritance: deep class trees are hard to change and easy to break.

```python
from dataclasses import dataclass, field

@dataclass
class TrainConfig:
    lr: float = 1e-3
    epochs: int = 10
    tags: list[str] = field(default_factory=list)   # never a bare []

    def __post_init__(self):
        assert self.lr > 0, 'learning rate must be positive'

cfg = TrainConfig(lr=3e-4, epochs=5)
print(cfg)
```

**Remember:** In a dataclass, mutable defaults need `field(default_factory=...)`, not a literal.

**Common mistake:** Building a five-level inheritance hierarchy for what a dict and two functions would have solved.

## 3. Dunder methods: __repr__, __len__

A class bundles data with the operations that keep it valid. For plain config or record objects, `@dataclass` gives you `__init__`, `__repr__` and `__eq__` for free. Prefer composition over inheritance: deep class trees are hard to change and easy to break.

```python
from dataclasses import dataclass, field

@dataclass
class TrainConfig:
    lr: float = 1e-3
    epochs: int = 10
    tags: list[str] = field(default_factory=list)   # never a bare []

    def __post_init__(self):
        assert self.lr > 0, 'learning rate must be positive'

cfg = TrainConfig(lr=3e-4, epochs=5)
print(cfg)
```

**Remember:** In a dataclass, mutable defaults need `field(default_factory=...)`, not a literal.

**Common mistake:** Building a five-level inheritance hierarchy for what a dict and two functions would have solved.

## 4. Dataclasses for config objects

A class bundles data with the operations that keep it valid. For plain config or record objects, `@dataclass` gives you `__init__`, `__repr__` and `__eq__` for free. Prefer composition over inheritance: deep class trees are hard to change and easy to break.

```python
from dataclasses import dataclass, field

@dataclass
class TrainConfig:
    lr: float = 1e-3
    epochs: int = 10
    tags: list[str] = field(default_factory=list)   # never a bare []

    def __post_init__(self):
        assert self.lr > 0, 'learning rate must be positive'

cfg = TrainConfig(lr=3e-4, epochs=5)
print(cfg)
```

**Remember:** In a dataclass, mutable defaults need `field(default_factory=...)`, not a literal.

**Common mistake:** Building a five-level inheritance hierarchy for what a dict and two functions would have solved.

## 5. Inheritance vs composition

A class bundles data with the operations that keep it valid. For plain config or record objects, `@dataclass` gives you `__init__`, `__repr__` and `__eq__` for free. Prefer composition over inheritance: deep class trees are hard to change and easy to break.

```python
from dataclasses import dataclass, field

@dataclass
class TrainConfig:
    lr: float = 1e-3
    epochs: int = 10
    tags: list[str] = field(default_factory=list)   # never a bare []

    def __post_init__(self):
        assert self.lr > 0, 'learning rate must be positive'

cfg = TrainConfig(lr=3e-4, epochs=5)
print(cfg)
```

**Remember:** In a dataclass, mutable defaults need `field(default_factory=...)`, not a literal.

**Common mistake:** Building a five-level inheritance hierarchy for what a dict and two functions would have solved.

## 6. Exceptions: raise, try, except

A class bundles data with the operations that keep it valid. For plain config or record objects, `@dataclass` gives you `__init__`, `__repr__` and `__eq__` for free. Prefer composition over inheritance: deep class trees are hard to change and easy to break.

```python
from dataclasses import dataclass, field

@dataclass
class TrainConfig:
    lr: float = 1e-3
    epochs: int = 10
    tags: list[str] = field(default_factory=list)   # never a bare []

    def __post_init__(self):
        assert self.lr > 0, 'learning rate must be positive'

cfg = TrainConfig(lr=3e-4, epochs=5)
print(cfg)
```

**Remember:** In a dataclass, mutable defaults need `field(default_factory=...)`, not a literal.

**Common mistake:** Building a five-level inheritance hierarchy for what a dict and two functions would have solved.

## 7. Custom exception classes

A class bundles data with the operations that keep it valid. For plain config or record objects, `@dataclass` gives you `__init__`, `__repr__` and `__eq__` for free. Prefer composition over inheritance: deep class trees are hard to change and easy to break.

```python
from dataclasses import dataclass, field

@dataclass
class TrainConfig:
    lr: float = 1e-3
    epochs: int = 10
    tags: list[str] = field(default_factory=list)   # never a bare []

    def __post_init__(self):
        assert self.lr > 0, 'learning rate must be positive'

cfg = TrainConfig(lr=3e-4, epochs=5)
print(cfg)
```

**Remember:** In a dataclass, mutable defaults need `field(default_factory=...)`, not a literal.

**Common mistake:** Building a five-level inheritance hierarchy for what a dict and two functions would have solved.

## 8. assert for invariants

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

## 9. Type hints and why they help

A class bundles data with the operations that keep it valid. For plain config or record objects, `@dataclass` gives you `__init__`, `__repr__` and `__eq__` for free. Prefer composition over inheritance: deep class trees are hard to change and easy to break.

```python
from dataclasses import dataclass, field

@dataclass
class TrainConfig:
    lr: float = 1e-3
    epochs: int = 10
    tags: list[str] = field(default_factory=list)   # never a bare []

    def __post_init__(self):
        assert self.lr > 0, 'learning rate must be positive'

cfg = TrainConfig(lr=3e-4, epochs=5)
print(cfg)
```

**Remember:** In a dataclass, mutable defaults need `field(default_factory=...)`, not a literal.

**Common mistake:** Building a five-level inheritance hierarchy for what a dict and two functions would have solved.

## 10. Writing code your future self can read

A class bundles data with the operations that keep it valid. For plain config or record objects, `@dataclass` gives you `__init__`, `__repr__` and `__eq__` for free. Prefer composition over inheritance: deep class trees are hard to change and easy to break.

```python
from dataclasses import dataclass, field

@dataclass
class TrainConfig:
    lr: float = 1e-3
    epochs: int = 10
    tags: list[str] = field(default_factory=list)   # never a bare []

    def __post_init__(self):
        assert self.lr > 0, 'learning rate must be positive'

cfg = TrainConfig(lr=3e-4, epochs=5)
print(cfg)
```

**Remember:** In a dataclass, mutable defaults need `field(default_factory=...)`, not a literal.

**Common mistake:** Building a five-level inheritance hierarchy for what a dict and two functions would have solved.

---

## What you should be able to do after Day 05

- Explain **Classes and instances** to someone else without notes.
- Explain **__init__, attributes and methods** to someone else without notes.
- Explain **Dunder methods: __repr__, __len__** to someone else without notes.
- Explain **Dataclasses for config objects** to someone else without notes.
- Explain **Inheritance vs composition** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
