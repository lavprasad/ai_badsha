# Day 100 — Advanced reinforcement learning

Today's goal: work through **advanced reinforcement learning** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Actor-critic methods |
| 2 | Advantage estimation |
| 3 | PPO and clipped objectives |
| 4 | Continuous action spaces |
| 5 | Sample efficiency problems |
| 6 | Offline reinforcement learning |
| 7 | Simulation and the sim-to-real gap |
| 8 | RL from human feedback preview |
| 9 | When RL is the wrong tool |
| 10 | A gridworld agent from scratch |

---

## 1. Actor-critic methods

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

## 2. Advantage estimation

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

## 3. PPO and clipped objectives

Multimodal models put images and text in one shared embedding space, so a picture of a dog lands near the words 'a dog'. That single trick gives you zero-shot classification, image search by description, and captioning — with no task-specific training.

```python
import numpy as np

# CLIP-style zero-shot: embed image and candidate captions, pick the closest
rng = np.random.default_rng(0)
image_vec = rng.normal(size=16)
image_vec /= np.linalg.norm(image_vec)

labels = ['a photo of a dog', 'a photo of a car', 'a photo of a plate of food']
label_vecs = rng.normal(size=(3, 16))
label_vecs /= np.linalg.norm(label_vecs, axis=1, keepdims=True)

scores = label_vecs @ image_vec
print('zero-shot pick:', labels[int(np.argmax(scores))], scores.round(3))
```

**Remember:** Zero-shot quality depends heavily on prompt wording — 'a photo of a {}' beats a bare noun.

**Common mistake:** Feeding an image at the wrong resolution or normalisation and getting silent quality loss.

## 4. Continuous action spaces

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

## 5. Sample efficiency problems

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

## 6. Offline reinforcement learning

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

## 7. Simulation and the sim-to-real gap

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

## 8. RL from human feedback preview

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

## 9. When RL is the wrong tool

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

## 10. A gridworld agent from scratch

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

---

## What you should be able to do after Day 100

- Explain **Actor-critic methods** to someone else without notes.
- Explain **Advantage estimation** to someone else without notes.
- Explain **PPO and clipped objectives** to someone else without notes.
- Explain **Continuous action spaces** to someone else without notes.
- Explain **Sample efficiency problems** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
