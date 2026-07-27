"""Day 03 — Pythonic data handling
Concept 5: map, filter and lambda

Run:  python 05_map_filter_and_lambda.py
"""

from collections import Counter, defaultdict
from itertools import combinations

words = ['ai', 'ml', 'ai', 'data', 'ml', 'ai']
print('counts   ', Counter(words).most_common(2))

by_len = defaultdict(list)
for w in words:
    by_len[len(w)].append(w)          # no 'if key not in' needed
print('by length', dict(by_len))

scores = {'ai': 0.9, 'ml': 0.4, 'data': 0.7}
print('ranked   ', sorted(scores, key=scores.get, reverse=True))
print('squares  ', {n: n * n for n in range(4)})
print('pairs    ', list(combinations(['a', 'b', 'c'], 2)))

for i, (w, s) in enumerate(zip(scores, scores.values()), 1):
    print(f'  {i}. {w} = {s}')

# ---------------------------------------------------------------------
# Remember: `Counter` and `defaultdict` remove most of the bookkeeping code people write by hand.
# Common mistake: Building frequency counts with `if k in d: d[k] += 1 else: d[k] = 1` in every script forever.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
