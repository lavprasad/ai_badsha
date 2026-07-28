# Day 20 — Optimisation theory

Aaj ka goal: **Optimisation theory** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Objective functions and minima |
| 2 | Convex vs non-convex landscapes |
| 3 | Local minima, saddle points, plateaus |
| 4 | Gradient descent in one dimension |
| 5 | The learning rate trade-off |
| 6 | Momentum intuition |
| 7 | Newton's method and why we rarely use it |
| 8 | Constrained optimisation and Lagrange multipliers |
| 9 | Stopping criteria |
| 10 | Implementing descent from scratch |

---

## 1. Objective functions and minima

### Aasaan Bhasha

Convex loss ka ek hi neeche hota hai, to koi bhi dhalaan wahi pahucha degi. Neural network ka loss convex nahi hota — usme valleys, plateaus aur saddle points hote hain. High dimensions me saddle points asli local minima se kahin zyada milte hain, isiliye momentum wale optimisers itna madad karte hain.

### Chhota code

```python
import numpy as np

def loss(w):
    return (w - 3) ** 2 + 1        # convex bowl, minimum at w=3

w, lr = 0.0, 0.1
for step in range(30):
    grad = 2 * (w - 3)
    w -= lr * grad
print(f'converged to w={w:.4f}, loss={loss(w):.4f}')
```

**Yaad rakho:** Agar loss oscillate ya explode kare, to sabse pehle learning rate aadha karo, baaki kuch badalne se pehle.

**Aam galti:** Architecture ko dosh dena jabki asli problem das guna bada learning rate hai.

Practice: `examples/01_objective_functions_and_minima.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Convex vs non-convex landscapes

### Aasaan Bhasha

Convex loss ka ek hi neeche hota hai, to koi bhi dhalaan wahi pahucha degi. Neural network ka loss convex nahi hota — usme valleys, plateaus aur saddle points hote hain. High dimensions me saddle points asli local minima se kahin zyada milte hain, isiliye momentum wale optimisers itna madad karte hain.

### Chhota code

```python
import numpy as np

def loss(w):
    return (w - 3) ** 2 + 1        # convex bowl, minimum at w=3

w, lr = 0.0, 0.1
for step in range(30):
    grad = 2 * (w - 3)
    w -= lr * grad
print(f'converged to w={w:.4f}, loss={loss(w):.4f}')
```

**Yaad rakho:** Agar loss oscillate ya explode kare, to sabse pehle learning rate aadha karo, baaki kuch badalne se pehle.

**Aam galti:** Architecture ko dosh dena jabki asli problem das guna bada learning rate hai.

Practice: `examples/02_convex_vs_non_convex_landscapes.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Local minima, saddle points, plateaus

### Aasaan Bhasha

Convex loss ka ek hi neeche hota hai, to koi bhi dhalaan wahi pahucha degi. Neural network ka loss convex nahi hota — usme valleys, plateaus aur saddle points hote hain. High dimensions me saddle points asli local minima se kahin zyada milte hain, isiliye momentum wale optimisers itna madad karte hain.

### Chhota code

```python
import numpy as np

def loss(w):
    return (w - 3) ** 2 + 1        # convex bowl, minimum at w=3

w, lr = 0.0, 0.1
for step in range(30):
    grad = 2 * (w - 3)
    w -= lr * grad
print(f'converged to w={w:.4f}, loss={loss(w):.4f}')
```

**Yaad rakho:** Agar loss oscillate ya explode kare, to sabse pehle learning rate aadha karo, baaki kuch badalne se pehle.

**Aam galti:** Architecture ko dosh dena jabki asli problem das guna bada learning rate hai.

Practice: `examples/03_local_minima_saddle_points_plateaus.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Gradient descent in one dimension

### Aasaan Bhasha

Derivative batata hai: input ko thoda hilaun to output kitna hilega? Gradient ye jawab ek saath har input ke liye deta hai, isliye wo chadhaai ki taraf point karta hai. Training gradient ke ulte chal kar neeche utarti hai. Chain rule hi wo cheez hai jo ye jawab layers ke poore stack me pahuchata hai.

### Chhota code

```python
import numpy as np

def f(x):
    return x ** 2 + 3 * x

def numeric_grad(fn, x, h=1e-6):
    return (fn(x + h) - fn(x - h)) / (2 * h)

x = 2.0
print('numeric  ', numeric_grad(f, x))
print('analytic ', 2 * x + 3)   # should match to ~1e-6
```

**Yaad rakho:** Central difference `(f(x+h)-f(x-h))/2h` haath se likhe gradient ko check karne ka sabse sasta tarika hai.

**Aam galti:** Aise derivation par bharosa karna jise aapne kabhi gradient-check nahi kiya; sign ki galti train dheere karti hai, saaf fail nahi hoti.

Practice: `examples/04_gradient_descent_in_one_dimension.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. The learning rate trade-off

### Aasaan Bhasha

Convex loss ka ek hi neeche hota hai, to koi bhi dhalaan wahi pahucha degi. Neural network ka loss convex nahi hota — usme valleys, plateaus aur saddle points hote hain. High dimensions me saddle points asli local minima se kahin zyada milte hain, isiliye momentum wale optimisers itna madad karte hain.

### Chhota code

```python
import numpy as np

def loss(w):
    return (w - 3) ** 2 + 1        # convex bowl, minimum at w=3

w, lr = 0.0, 0.1
for step in range(30):
    grad = 2 * (w - 3)
    w -= lr * grad
print(f'converged to w={w:.4f}, loss={loss(w):.4f}')
```

**Yaad rakho:** Agar loss oscillate ya explode kare, to sabse pehle learning rate aadha karo, baaki kuch badalne se pehle.

**Aam galti:** Architecture ko dosh dena jabki asli problem das guna bada learning rate hai.

Practice: `examples/05_the_learning_rate_trade_off.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Momentum intuition

### Aasaan Bhasha

Convex loss ka ek hi neeche hota hai, to koi bhi dhalaan wahi pahucha degi. Neural network ka loss convex nahi hota — usme valleys, plateaus aur saddle points hote hain. High dimensions me saddle points asli local minima se kahin zyada milte hain, isiliye momentum wale optimisers itna madad karte hain.

### Chhota code

```python
import numpy as np

def loss(w):
    return (w - 3) ** 2 + 1        # convex bowl, minimum at w=3

w, lr = 0.0, 0.1
for step in range(30):
    grad = 2 * (w - 3)
    w -= lr * grad
print(f'converged to w={w:.4f}, loss={loss(w):.4f}')
```

**Yaad rakho:** Agar loss oscillate ya explode kare, to sabse pehle learning rate aadha karo, baaki kuch badalne se pehle.

**Aam galti:** Architecture ko dosh dena jabki asli problem das guna bada learning rate hai.

Practice: `examples/06_momentum_intuition.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Newton's method and why we rarely use it

### Aasaan Bhasha

Convex loss ka ek hi neeche hota hai, to koi bhi dhalaan wahi pahucha degi. Neural network ka loss convex nahi hota — usme valleys, plateaus aur saddle points hote hain. High dimensions me saddle points asli local minima se kahin zyada milte hain, isiliye momentum wale optimisers itna madad karte hain.

### Chhota code

```python
import numpy as np

def loss(w):
    return (w - 3) ** 2 + 1        # convex bowl, minimum at w=3

w, lr = 0.0, 0.1
for step in range(30):
    grad = 2 * (w - 3)
    w -= lr * grad
print(f'converged to w={w:.4f}, loss={loss(w):.4f}')
```

**Yaad rakho:** Agar loss oscillate ya explode kare, to sabse pehle learning rate aadha karo, baaki kuch badalne se pehle.

**Aam galti:** Architecture ko dosh dena jabki asli problem das guna bada learning rate hai.

Practice: `examples/07_newton_s_method_and_why_we_rarely_use_it.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Constrained optimisation and Lagrange multipliers

### Aasaan Bhasha

Convex loss ka ek hi neeche hota hai, to koi bhi dhalaan wahi pahucha degi. Neural network ka loss convex nahi hota — usme valleys, plateaus aur saddle points hote hain. High dimensions me saddle points asli local minima se kahin zyada milte hain, isiliye momentum wale optimisers itna madad karte hain.

### Chhota code

```python
import numpy as np

def loss(w):
    return (w - 3) ** 2 + 1        # convex bowl, minimum at w=3

w, lr = 0.0, 0.1
for step in range(30):
    grad = 2 * (w - 3)
    w -= lr * grad
print(f'converged to w={w:.4f}, loss={loss(w):.4f}')
```

**Yaad rakho:** Agar loss oscillate ya explode kare, to sabse pehle learning rate aadha karo, baaki kuch badalne se pehle.

**Aam galti:** Architecture ko dosh dena jabki asli problem das guna bada learning rate hai.

Practice: `examples/08_constrained_optimisation_and_lagrange_mu.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Stopping criteria

### Aasaan Bhasha

Convex loss ka ek hi neeche hota hai, to koi bhi dhalaan wahi pahucha degi. Neural network ka loss convex nahi hota — usme valleys, plateaus aur saddle points hote hain. High dimensions me saddle points asli local minima se kahin zyada milte hain, isiliye momentum wale optimisers itna madad karte hain.

### Chhota code

```python
import numpy as np

def loss(w):
    return (w - 3) ** 2 + 1        # convex bowl, minimum at w=3

w, lr = 0.0, 0.1
for step in range(30):
    grad = 2 * (w - 3)
    w -= lr * grad
print(f'converged to w={w:.4f}, loss={loss(w):.4f}')
```

**Yaad rakho:** Agar loss oscillate ya explode kare, to sabse pehle learning rate aadha karo, baaki kuch badalne se pehle.

**Aam galti:** Architecture ko dosh dena jabki asli problem das guna bada learning rate hai.

Practice: `examples/09_stopping_criteria.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Implementing descent from scratch

### Aasaan Bhasha

Convex loss ka ek hi neeche hota hai, to koi bhi dhalaan wahi pahucha degi. Neural network ka loss convex nahi hota — usme valleys, plateaus aur saddle points hote hain. High dimensions me saddle points asli local minima se kahin zyada milte hain, isiliye momentum wale optimisers itna madad karte hain.

### Chhota code

```python
import numpy as np

def loss(w):
    return (w - 3) ** 2 + 1        # convex bowl, minimum at w=3

w, lr = 0.0, 0.1
for step in range(30):
    grad = 2 * (w - 3)
    w -= lr * grad
print(f'converged to w={w:.4f}, loss={loss(w):.4f}')
```

**Yaad rakho:** Agar loss oscillate ya explode kare, to sabse pehle learning rate aadha karo, baaki kuch badalne se pehle.

**Aam galti:** Architecture ko dosh dena jabki asli problem das guna bada learning rate hai.

Practice: `examples/10_implementing_descent_from_scratch.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 20 ke baad aapko ye aana chahiye

- **Objective functions and minima** ko bina notes dekhe kisi dost ko samjha sakna.
- **Convex vs non-convex landscapes** ko bina notes dekhe kisi dost ko samjha sakna.
- **Local minima, saddle points, plateaus** ko bina notes dekhe kisi dost ko samjha sakna.
- **Gradient descent in one dimension** ko bina notes dekhe kisi dost ko samjha sakna.
- **The learning rate trade-off** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
