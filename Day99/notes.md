# Day 99 — Reinforcement learning foundations

Today's goal: work through **Reinforcement learning foundations** — ten concepts, ten runnable examples, five questions.

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

An agent is a loop: the model picks a tool, your code runs it, the result goes back into context, repeat until done. Power comes from the tools, not the prompt. Cap the iterations, log every step, and require confirmation before anything irreversible.

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

**Remember:** Always bound the loop. An unbounded agent burns money and finds creative ways to fail.

**Common mistake:** Giving an agent a shell tool with no allowlist and no confirmation step.

Practice: open `examples/01_agent_environment_reward.py`, predict the output, change one line, predict again.

## 2. Markov decision processes

Accuracy hides everything on imbalanced data. Precision asks 'of the ones I flagged, how many were real'; recall asks 'of the real ones, how many did I catch'. You trade one for the other with the threshold, and the business decides which error hurts more.

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

**Remember:** Tune the decision threshold on validation data; 0.5 is a default, not a decision.

**Common mistake:** Optimising ROC-AUC on a heavily imbalanced problem where precision-recall AUC is the honest metric.

Practice: open `examples/02_markov_decision_processes.py`, predict the output, change one line, predict again.

## 3. Policy and value functions

RL learns from reward instead of labels. The agent takes actions, the environment returns state and reward, and the agent learns a policy that maximises long-term return. The hard part is exploration versus exploitation and the fact that reward is delayed and sparse.

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

**Remember:** Reward shaping decides what the agent actually learns — and it will exploit any loophole you leave.

**Common mistake:** Rewarding a proxy metric and getting an agent that maximises the proxy while failing the real goal.

Practice: open `examples/03_policy_and_value_functions.py`, predict the output, change one line, predict again.

## 4. The Bellman equation

RL learns from reward instead of labels. The agent takes actions, the environment returns state and reward, and the agent learns a policy that maximises long-term return. The hard part is exploration versus exploitation and the fact that reward is delayed and sparse.

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

**Remember:** Reward shaping decides what the agent actually learns — and it will exploit any loophole you leave.

**Common mistake:** Rewarding a proxy metric and getting an agent that maximises the proxy while failing the real goal.

Practice: open `examples/04_the_bellman_equation.py`, predict the output, change one line, predict again.

## 5. Exploration vs exploitation

LoRA freezes the base weights and trains two small low-rank matrices whose product is added to each target layer. You update ~0.1% of the parameters, the checkpoint is megabytes not gigabytes, and you can swap adapters per customer. QLoRA adds 4-bit base weights so a 7B model fits on one consumer GPU.

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

**Remember:** Initialise B to zeros so the adapted model starts exactly equal to the base model.

**Common mistake:** Setting rank far too high — you lose the efficiency and gain the overfitting.

Practice: open `examples/05_exploration_vs_exploitation.py`, predict the output, change one line, predict again.

## 6. Multi-armed bandits

RL learns from reward instead of labels. The agent takes actions, the environment returns state and reward, and the agent learns a policy that maximises long-term return. The hard part is exploration versus exploitation and the fact that reward is delayed and sparse.

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

**Remember:** Reward shaping decides what the agent actually learns — and it will exploit any loophole you leave.

**Common mistake:** Rewarding a proxy metric and getting an agent that maximises the proxy while failing the real goal.

Practice: open `examples/06_multi_armed_bandits.py`, predict the output, change one line, predict again.

## 7. Q-learning

RL learns from reward instead of labels. The agent takes actions, the environment returns state and reward, and the agent learns a policy that maximises long-term return. The hard part is exploration versus exploitation and the fact that reward is delayed and sparse.

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

**Remember:** Reward shaping decides what the agent actually learns — and it will exploit any loophole you leave.

**Common mistake:** Rewarding a proxy metric and getting an agent that maximises the proxy while failing the real goal.

Practice: open `examples/07_q_learning.py`, predict the output, change one line, predict again.

## 8. Deep Q-networks

RL learns from reward instead of labels. The agent takes actions, the environment returns state and reward, and the agent learns a policy that maximises long-term return. The hard part is exploration versus exploitation and the fact that reward is delayed and sparse.

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

**Remember:** Reward shaping decides what the agent actually learns — and it will exploit any loophole you leave.

**Common mistake:** Rewarding a proxy metric and getting an agent that maximises the proxy while failing the real goal.

Practice: open `examples/08_deep_q_networks.py`, predict the output, change one line, predict again.

## 9. Policy gradients and REINFORCE

The derivative answers: if I nudge this input a little, how much does the output move? The gradient is that answer for every input at once, so it points uphill. Training walks downhill by stepping against the gradient. The chain rule is what lets you propagate that answer through a stack of layers.

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

**Remember:** A central difference `(f(x+h)-f(x-h))/2h` is the cheapest way to check a hand-written gradient.

**Common mistake:** Trusting a derivation you never gradient-checked; a sign error trains slowly instead of failing loudly.

Practice: open `examples/09_policy_gradients_and_reinforce.py`, predict the output, change one line, predict again.

## 10. Reward hacking

RL learns from reward instead of labels. The agent takes actions, the environment returns state and reward, and the agent learns a policy that maximises long-term return. The hard part is exploration versus exploitation and the fact that reward is delayed and sparse.

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

**Remember:** Reward shaping decides what the agent actually learns — and it will exploit any loophole you leave.

**Common mistake:** Rewarding a proxy metric and getting an agent that maximises the proxy while failing the real goal.

Practice: open `examples/10_reward_hacking.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 99

- Explain **Agent, environment, reward** to someone else without notes.
- Explain **Markov decision processes** to someone else without notes.
- Explain **Policy and value functions** to someone else without notes.
- Explain **The Bellman equation** to someone else without notes.
- Explain **Exploration vs exploitation** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
