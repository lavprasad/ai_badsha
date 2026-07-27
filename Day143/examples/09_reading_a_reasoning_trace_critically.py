"""Day 143 — Reasoning and thinking models
Concept 9: Reading a reasoning trace critically

Run:  python 09_reading_a_reasoning_trace_critically.py
"""

from collections import Counter

def self_consistency(samples):
    counts = Counter(samples)
    answer, votes = counts.most_common(1)[0]
    return answer, votes / len(samples)

print(self_consistency(['42', '42', '17', '42', '43']))

USE_REASONING = {
    'multi-step arithmetic / planning': True,
    'code with a failing test to fix': True,
    'reformat this JSON': False,
    'classify sentiment': False,
}
for task, use in USE_REASONING.items():
    print(f'{task:<38} -> {"reason" if use else "direct answer"}')

# ---------------------------------------------------------------------
# Remember: A reasoning trace is not proof. The stated reasoning can be wrong while the answer is right, and vice versa.
# Common mistake: Enabling extended thinking globally and tripling cost on tasks that never needed a single reasoning token.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
