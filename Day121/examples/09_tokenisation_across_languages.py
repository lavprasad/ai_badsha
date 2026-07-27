"""Day 121 — Tokenisation
Concept 9: Tokenisation across languages

Run:  python 09_tokenisation_across_languages.py
"""

from collections import Counter

def bpe_merges(words, n_merges=3):
    corpus = {' '.join(w) + ' </w>': c for w, c in words.items()}
    for _ in range(n_merges):
        pairs = Counter()
        for word, freq in corpus.items():
            syms = word.split()
            for a, b in zip(syms, syms[1:]):
                pairs[(a, b)] += freq
        if not pairs:
            break
        best = max(pairs, key=pairs.get)
        merged = ''.join(best)
        corpus = {w.replace(' '.join(best), merged): c for w, c in corpus.items()}
        print('merged', best, '->', merged)
    return corpus

bpe_merges({'low': 5, 'lower': 2, 'newest': 6, 'widest': 3})

# ---------------------------------------------------------------------
# Remember: Roughly 1 token ~ 4 characters of English; other languages cost far more tokens per word.
# Common mistake: Estimating cost or context usage in words instead of tokens and overflowing the window in production.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
