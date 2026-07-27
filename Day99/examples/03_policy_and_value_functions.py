"""Day 99 — Reinforcement learning foundations
Concept 3: Policy and value functions

Run:  python 03_policy_and_value_functions.py
"""

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

# ---------------------------------------------------------------------
# Remember: Reward shaping decides what the agent actually learns — and it will exploit any loophole you leave.
# Common mistake: Rewarding a proxy metric and getting an agent that maximises the proxy while failing the real goal.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
