# Day 05 — Objects, errors and clean code

Aaj ka goal: **Objects, errors and clean code** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

### Aasaan Bhasha

Class data ko un operations ke saath baandhti hai jo use valid rakhte hain. Saade config ya record objects ke liye `@dataclass` aapko `__init__`, `__repr__` aur `__eq__` muft de deta hai. Inheritance par composition prefer karo: gehre class trees badalna mushkil aur todna aasan hota hai.

### Chhota code

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

**Yaad rakho:** Dataclass me mutable defaults ko `field(default_factory=...)` chahiye, literal nahi.

**Aam galti:** Us cheez ke liye paanch-level inheritance banana jise ek dict aur do functions hal kar dete.

Practice: `examples/01_classes_and_instances.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. __init__, attributes and methods

### Aasaan Bhasha

Class data ko un operations ke saath baandhti hai jo use valid rakhte hain. Saade config ya record objects ke liye `@dataclass` aapko `__init__`, `__repr__` aur `__eq__` muft de deta hai. Inheritance par composition prefer karo: gehre class trees badalna mushkil aur todna aasan hota hai.

### Chhota code

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

**Yaad rakho:** Dataclass me mutable defaults ko `field(default_factory=...)` chahiye, literal nahi.

**Aam galti:** Us cheez ke liye paanch-level inheritance banana jise ek dict aur do functions hal kar dete.

Practice: `examples/02_init_attributes_and_methods.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Dunder methods: __repr__, __len__

### Aasaan Bhasha

Class data ko un operations ke saath baandhti hai jo use valid rakhte hain. Saade config ya record objects ke liye `@dataclass` aapko `__init__`, `__repr__` aur `__eq__` muft de deta hai. Inheritance par composition prefer karo: gehre class trees badalna mushkil aur todna aasan hota hai.

### Chhota code

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

**Yaad rakho:** Dataclass me mutable defaults ko `field(default_factory=...)` chahiye, literal nahi.

**Aam galti:** Us cheez ke liye paanch-level inheritance banana jise ek dict aur do functions hal kar dete.

Practice: `examples/03_dunder_methods_repr_len.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Dataclasses for config objects

### Aasaan Bhasha

Class data ko un operations ke saath baandhti hai jo use valid rakhte hain. Saade config ya record objects ke liye `@dataclass` aapko `__init__`, `__repr__` aur `__eq__` muft de deta hai. Inheritance par composition prefer karo: gehre class trees badalna mushkil aur todna aasan hota hai.

### Chhota code

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

**Yaad rakho:** Dataclass me mutable defaults ko `field(default_factory=...)` chahiye, literal nahi.

**Aam galti:** Us cheez ke liye paanch-level inheritance banana jise ek dict aur do functions hal kar dete.

Practice: `examples/04_dataclasses_for_config_objects.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Inheritance vs composition

### Aasaan Bhasha

Class data ko un operations ke saath baandhti hai jo use valid rakhte hain. Saade config ya record objects ke liye `@dataclass` aapko `__init__`, `__repr__` aur `__eq__` muft de deta hai. Inheritance par composition prefer karo: gehre class trees badalna mushkil aur todna aasan hota hai.

### Chhota code

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

**Yaad rakho:** Dataclass me mutable defaults ko `field(default_factory=...)` chahiye, literal nahi.

**Aam galti:** Us cheez ke liye paanch-level inheritance banana jise ek dict aur do functions hal kar dete.

Practice: `examples/05_inheritance_vs_composition.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Exceptions: raise, try, except

### Aasaan Bhasha

Class data ko un operations ke saath baandhti hai jo use valid rakhte hain. Saade config ya record objects ke liye `@dataclass` aapko `__init__`, `__repr__` aur `__eq__` muft de deta hai. Inheritance par composition prefer karo: gehre class trees badalna mushkil aur todna aasan hota hai.

### Chhota code

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

**Yaad rakho:** Dataclass me mutable defaults ko `field(default_factory=...)` chahiye, literal nahi.

**Aam galti:** Us cheez ke liye paanch-level inheritance banana jise ek dict aur do functions hal kar dete.

Practice: `examples/06_exceptions_raise_try_except.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Custom exception classes

### Aasaan Bhasha

Class data ko un operations ke saath baandhti hai jo use valid rakhte hain. Saade config ya record objects ke liye `@dataclass` aapko `__init__`, `__repr__` aur `__eq__` muft de deta hai. Inheritance par composition prefer karo: gehre class trees badalna mushkil aur todna aasan hota hai.

### Chhota code

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

**Yaad rakho:** Dataclass me mutable defaults ko `field(default_factory=...)` chahiye, literal nahi.

**Aam galti:** Us cheez ke liye paanch-level inheritance banana jise ek dict aur do functions hal kar dete.

Practice: `examples/07_custom_exception_classes.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. assert for invariants

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

Practice: `examples/08_assert_for_invariants.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Type hints and why they help

### Aasaan Bhasha

Class data ko un operations ke saath baandhti hai jo use valid rakhte hain. Saade config ya record objects ke liye `@dataclass` aapko `__init__`, `__repr__` aur `__eq__` muft de deta hai. Inheritance par composition prefer karo: gehre class trees badalna mushkil aur todna aasan hota hai.

### Chhota code

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

**Yaad rakho:** Dataclass me mutable defaults ko `field(default_factory=...)` chahiye, literal nahi.

**Aam galti:** Us cheez ke liye paanch-level inheritance banana jise ek dict aur do functions hal kar dete.

Practice: `examples/09_type_hints_and_why_they_help.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Writing code your future self can read

### Aasaan Bhasha

Class data ko un operations ke saath baandhti hai jo use valid rakhte hain. Saade config ya record objects ke liye `@dataclass` aapko `__init__`, `__repr__` aur `__eq__` muft de deta hai. Inheritance par composition prefer karo: gehre class trees badalna mushkil aur todna aasan hota hai.

### Chhota code

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

**Yaad rakho:** Dataclass me mutable defaults ko `field(default_factory=...)` chahiye, literal nahi.

**Aam galti:** Us cheez ke liye paanch-level inheritance banana jise ek dict aur do functions hal kar dete.

Practice: `examples/10_writing_code_your_future_self_can_read.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 05 ke baad aapko ye aana chahiye

- **Classes and instances** ko bina notes dekhe kisi dost ko samjha sakna.
- **__init__, attributes and methods** ko bina notes dekhe kisi dost ko samjha sakna.
- **Dunder methods: __repr__, __len__** ko bina notes dekhe kisi dost ko samjha sakna.
- **Dataclasses for config objects** ko bina notes dekhe kisi dost ko samjha sakna.
- **Inheritance vs composition** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
