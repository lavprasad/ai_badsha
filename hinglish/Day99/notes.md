# Day 99 — Reinforcement learning foundations

Aaj ka goal: **Reinforcement learning foundations** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Agent, environment, reward |
| 2 | Markov decision processes |
| 3 | Policy and value functions |
| 4 | The Bellman equation |
| 5 | Exploration vs exploitation |
| 6 | Multi-armed bandits |
| 7 | Q-learning |
| 8 | Deep Q-networks |
| 9 | Policy gradients and REINFORCE |
| 10 | Reward hacking |

---

## 1. Agent, environment, reward

### Aasaan Bhasha

Agent ek loop hai: model tool chunta hai, aapka code use chalata hai, result wapas context me jaata hai, aur ye dohraata hai jab tak kaam poora na ho. Taakat tools se aati hai, prompt se nahi. Iterations cap karo, har step log karo, aur kisi bhi irreversible cheez se pehle confirmation maango.

### Chhota code

```python
def calculator(expr):
    return eval(expr, {'__builtins__': {}}, {})   # locked-down namespace only

TOOLS = {'calc': calculator}

def agent_loop(plan, max_steps=5):
    """`plan` stands in for the model's tool choices."""
    history = []
    for step, (tool, arg) in enumerate(plan[:max_steps], 1):
        result = TOOLS[tool](arg)
        history.append((step, tool, arg, result))
        print(f'step {step}: {tool}({arg!r}) -> {result}')
    return history

agent_loop([('calc', '2 + 2'), ('calc', '(2 + 2) * 10')])
```

**Yaad rakho:** Loop hamesha bounded rakho. Bina limit ka agent paisa jalata hai aur fail hone ke naye tareeke dhoondh leta hai.

**Aam galti:** Agent ko shell tool dena bina allowlist aur bina confirmation step ke.

Practice: `examples/01_agent_environment_reward.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Markov decision processes

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

Practice: `examples/02_markov_decision_processes.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Policy and value functions

### Aasaan Bhasha

RL labels ke bajaye reward se seekhta hai. Agent actions leta hai, environment state aur reward lautata hai, aur agent aisi policy seekhta hai jo long-term return maximise kare. Mushkil hissa exploration vs exploitation hai aur ye ki reward delayed aur sparse hota hai.

### Chhota code

```python
import numpy as np

# Q-learning on a 5-state corridor; reward only at the right end.
n, actions = 5, 2      # 0 = left, 1 = right
Q = np.zeros((n, actions))
alpha, gamma, eps = 0.5, 0.9, 0.2
rng = np.random.default_rng(0)

for episode in range(500):
    s = 0
    for _ in range(50):
        a = rng.integers(actions) if rng.random() < eps else int(np.argmax(Q[s]))
        s2 = max(0, s - 1) if a == 0 else min(n - 1, s + 1)
        r = 1.0 if s2 == n - 1 else 0.0
        Q[s, a] += alpha * (r + gamma * Q[s2].max() - Q[s, a])
        s = s2
        if r:
            break
print(Q.round(2))
print('learned policy:', ['left' if a == 0 else 'right' for a in Q.argmax(axis=1)])
```

**Yaad rakho:** Reward shaping hi tay karta hai ki agent asal me kya seekhega — aur wo har chhod ka faayda uthaega.

**Aam galti:** Proxy metric par reward dena aur aisa agent paana jo proxy maximise karta hai par asli goal fail karta hai.

Practice: `examples/03_policy_and_value_functions.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. The Bellman equation

### Aasaan Bhasha

RL labels ke bajaye reward se seekhta hai. Agent actions leta hai, environment state aur reward lautata hai, aur agent aisi policy seekhta hai jo long-term return maximise kare. Mushkil hissa exploration vs exploitation hai aur ye ki reward delayed aur sparse hota hai.

### Chhota code

```python
import numpy as np

# Q-learning on a 5-state corridor; reward only at the right end.
n, actions = 5, 2      # 0 = left, 1 = right
Q = np.zeros((n, actions))
alpha, gamma, eps = 0.5, 0.9, 0.2
rng = np.random.default_rng(0)

for episode in range(500):
    s = 0
    for _ in range(50):
        a = rng.integers(actions) if rng.random() < eps else int(np.argmax(Q[s]))
        s2 = max(0, s - 1) if a == 0 else min(n - 1, s + 1)
        r = 1.0 if s2 == n - 1 else 0.0
        Q[s, a] += alpha * (r + gamma * Q[s2].max() - Q[s, a])
        s = s2
        if r:
            break
print(Q.round(2))
print('learned policy:', ['left' if a == 0 else 'right' for a in Q.argmax(axis=1)])
```

**Yaad rakho:** Reward shaping hi tay karta hai ki agent asal me kya seekhega — aur wo har chhod ka faayda uthaega.

**Aam galti:** Proxy metric par reward dena aur aisa agent paana jo proxy maximise karta hai par asli goal fail karta hai.

Practice: `examples/04_the_bellman_equation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Exploration vs exploitation

### Aasaan Bhasha

LoRA base weights freeze kar deta hai aur do chhoti low-rank matrices train karta hai jinka product har target layer me joda jaata hai. Aap ~0.1% parameters update karte ho, checkpoint gigabytes ke bajaye megabytes ka hota hai, aur har customer ke liye adapter badla ja sakta hai. QLoRA 4-bit base weights jodta hai taaki 7B model ek consumer GPU par aa jaaye.

### Chhota code

```python
import numpy as np

d, r = 512, 8                      # full dim vs LoRA rank
rng = np.random.default_rng(0)
W = rng.normal(size=(d, d)) * 0.02  # frozen base weight
A = rng.normal(size=(d, r)) * 0.01  # trainable
B = np.zeros((r, d))                # trainable, starts at zero -> no change at step 0

delta = A @ B
print('base params   ', W.size)
print('lora params   ', A.size + B.size, f'({100 * (A.size + B.size) / W.size:.1f}%)')
print('effective W = W + A@B, shape', (W + delta).shape)
```

**Yaad rakho:** B ko zeros se initialise karo taaki adapted model bilkul base model ke barabar shuru ho.

**Aam galti:** Rank bahut zyada rakh dena — efficiency chali jaati hai aur overfitting aa jaati hai.

Practice: `examples/05_exploration_vs_exploitation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Multi-armed bandits

### Aasaan Bhasha

RL labels ke bajaye reward se seekhta hai. Agent actions leta hai, environment state aur reward lautata hai, aur agent aisi policy seekhta hai jo long-term return maximise kare. Mushkil hissa exploration vs exploitation hai aur ye ki reward delayed aur sparse hota hai.

### Chhota code

```python
import numpy as np

# Q-learning on a 5-state corridor; reward only at the right end.
n, actions = 5, 2      # 0 = left, 1 = right
Q = np.zeros((n, actions))
alpha, gamma, eps = 0.5, 0.9, 0.2
rng = np.random.default_rng(0)

for episode in range(500):
    s = 0
    for _ in range(50):
        a = rng.integers(actions) if rng.random() < eps else int(np.argmax(Q[s]))
        s2 = max(0, s - 1) if a == 0 else min(n - 1, s + 1)
        r = 1.0 if s2 == n - 1 else 0.0
        Q[s, a] += alpha * (r + gamma * Q[s2].max() - Q[s, a])
        s = s2
        if r:
            break
print(Q.round(2))
print('learned policy:', ['left' if a == 0 else 'right' for a in Q.argmax(axis=1)])
```

**Yaad rakho:** Reward shaping hi tay karta hai ki agent asal me kya seekhega — aur wo har chhod ka faayda uthaega.

**Aam galti:** Proxy metric par reward dena aur aisa agent paana jo proxy maximise karta hai par asli goal fail karta hai.

Practice: `examples/06_multi_armed_bandits.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Q-learning

### Aasaan Bhasha

RL labels ke bajaye reward se seekhta hai. Agent actions leta hai, environment state aur reward lautata hai, aur agent aisi policy seekhta hai jo long-term return maximise kare. Mushkil hissa exploration vs exploitation hai aur ye ki reward delayed aur sparse hota hai.

### Chhota code

```python
import numpy as np

# Q-learning on a 5-state corridor; reward only at the right end.
n, actions = 5, 2      # 0 = left, 1 = right
Q = np.zeros((n, actions))
alpha, gamma, eps = 0.5, 0.9, 0.2
rng = np.random.default_rng(0)

for episode in range(500):
    s = 0
    for _ in range(50):
        a = rng.integers(actions) if rng.random() < eps else int(np.argmax(Q[s]))
        s2 = max(0, s - 1) if a == 0 else min(n - 1, s + 1)
        r = 1.0 if s2 == n - 1 else 0.0
        Q[s, a] += alpha * (r + gamma * Q[s2].max() - Q[s, a])
        s = s2
        if r:
            break
print(Q.round(2))
print('learned policy:', ['left' if a == 0 else 'right' for a in Q.argmax(axis=1)])
```

**Yaad rakho:** Reward shaping hi tay karta hai ki agent asal me kya seekhega — aur wo har chhod ka faayda uthaega.

**Aam galti:** Proxy metric par reward dena aur aisa agent paana jo proxy maximise karta hai par asli goal fail karta hai.

Practice: `examples/07_q_learning.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Deep Q-networks

### Aasaan Bhasha

RL labels ke bajaye reward se seekhta hai. Agent actions leta hai, environment state aur reward lautata hai, aur agent aisi policy seekhta hai jo long-term return maximise kare. Mushkil hissa exploration vs exploitation hai aur ye ki reward delayed aur sparse hota hai.

### Chhota code

```python
import numpy as np

# Q-learning on a 5-state corridor; reward only at the right end.
n, actions = 5, 2      # 0 = left, 1 = right
Q = np.zeros((n, actions))
alpha, gamma, eps = 0.5, 0.9, 0.2
rng = np.random.default_rng(0)

for episode in range(500):
    s = 0
    for _ in range(50):
        a = rng.integers(actions) if rng.random() < eps else int(np.argmax(Q[s]))
        s2 = max(0, s - 1) if a == 0 else min(n - 1, s + 1)
        r = 1.0 if s2 == n - 1 else 0.0
        Q[s, a] += alpha * (r + gamma * Q[s2].max() - Q[s, a])
        s = s2
        if r:
            break
print(Q.round(2))
print('learned policy:', ['left' if a == 0 else 'right' for a in Q.argmax(axis=1)])
```

**Yaad rakho:** Reward shaping hi tay karta hai ki agent asal me kya seekhega — aur wo har chhod ka faayda uthaega.

**Aam galti:** Proxy metric par reward dena aur aisa agent paana jo proxy maximise karta hai par asli goal fail karta hai.

Practice: `examples/08_deep_q_networks.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Policy gradients and REINFORCE

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

Practice: `examples/09_policy_gradients_and_reinforce.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Reward hacking

### Aasaan Bhasha

RL labels ke bajaye reward se seekhta hai. Agent actions leta hai, environment state aur reward lautata hai, aur agent aisi policy seekhta hai jo long-term return maximise kare. Mushkil hissa exploration vs exploitation hai aur ye ki reward delayed aur sparse hota hai.

### Chhota code

```python
import numpy as np

# Q-learning on a 5-state corridor; reward only at the right end.
n, actions = 5, 2      # 0 = left, 1 = right
Q = np.zeros((n, actions))
alpha, gamma, eps = 0.5, 0.9, 0.2
rng = np.random.default_rng(0)

for episode in range(500):
    s = 0
    for _ in range(50):
        a = rng.integers(actions) if rng.random() < eps else int(np.argmax(Q[s]))
        s2 = max(0, s - 1) if a == 0 else min(n - 1, s + 1)
        r = 1.0 if s2 == n - 1 else 0.0
        Q[s, a] += alpha * (r + gamma * Q[s2].max() - Q[s, a])
        s = s2
        if r:
            break
print(Q.round(2))
print('learned policy:', ['left' if a == 0 else 'right' for a in Q.argmax(axis=1)])
```

**Yaad rakho:** Reward shaping hi tay karta hai ki agent asal me kya seekhega — aur wo har chhod ka faayda uthaega.

**Aam galti:** Proxy metric par reward dena aur aisa agent paana jo proxy maximise karta hai par asli goal fail karta hai.

Practice: `examples/10_reward_hacking.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 99 ke baad aapko ye aana chahiye

- **Agent, environment, reward** ko bina notes dekhe kisi dost ko samjha sakna.
- **Markov decision processes** ko bina notes dekhe kisi dost ko samjha sakna.
- **Policy and value functions** ko bina notes dekhe kisi dost ko samjha sakna.
- **The Bellman equation** ko bina notes dekhe kisi dost ko samjha sakna.
- **Exploration vs exploitation** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
