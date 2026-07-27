"""Day 133 — Inference and decoding
Concept 8: Stop sequences

Run:  python 08_stop_sequences.py
"""

import numpy as np

def generate(next_dist, max_tokens=20, stop=('.',), greedy=True, seed=0):
    rng = np.random.default_rng(seed)
    out = []
    for _ in range(max_tokens):
        tokens, probs = next_dist(out)
        tok = tokens[int(np.argmax(probs))] if greedy else rng.choice(tokens, p=probs)
        out.append(tok)
        if tok in stop:
            break
    return ''.join(out)

vocab = list('abc.')
dist = lambda hist: (vocab, np.array([0.4, 0.3, 0.2, 0.1]))
print('greedy :', generate(dist))
print('sampled:', generate(dist, greedy=False))

# ---------------------------------------------------------------------
# Remember: Always set max_tokens and stop sequences. They are the difference between a bug and a bill.
# Common mistake: Leaving max_tokens unbounded on a retry loop and burning a month's budget overnight.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
