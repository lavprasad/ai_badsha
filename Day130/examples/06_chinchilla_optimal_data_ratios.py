"""Day 130 — Pretraining language models
Concept 6: Chinchilla-optimal data ratios

Run:  python 06_chinchilla_optimal_data_ratios.py
"""

from collections import defaultdict, Counter
import random

text = 'the cat sat on the mat the cat ate the rat'.split()
model = defaultdict(Counter)
for a, b in zip(text, text[1:]):
    model[a][b] += 1

random.seed(0)
word, out = 'the', ['the']
for _ in range(6):
    nxt = model[word].most_common(1)[0][0] if model[word] else 'the'
    out.append(nxt)
    word = nxt
print(' '.join(out))   # a 2-gram LM: same objective, 10 orders of magnitude smaller

# ---------------------------------------------------------------------
# Remember: A bigger model trained on too little data is a waste — compute, parameters and tokens scale together.
# Common mistake: Believing a base model will follow instructions; that behaviour comes from the tuning stages after.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
