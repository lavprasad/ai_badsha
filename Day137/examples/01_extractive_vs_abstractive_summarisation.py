"""Day 137 — Summarisation and extraction
Concept 1: Extractive vs abstractive summarisation

Run:  python 01_extractive_vs_abstractive_summarisation.py
"""

def map_reduce_summarize(chunks, summarize, combine_at=4):
    level = [summarize(c) for c in chunks]
    rounds = 1
    while len(level) > 1:
        level = [summarize(' '.join(level[i:i + combine_at]))
                 for i in range(0, len(level), combine_at)]
        rounds += 1
    return level[0], rounds

fake = lambda t: t[:40]
docs = [f'section {i} content ' * 5 for i in range(9)]
summary, rounds = map_reduce_summarize(docs, fake)
print(f'{len(docs)} chunks -> {rounds} rounds -> {summary!r}')

# ---------------------------------------------------------------------
# Remember: Extract facts structurally and summarise prose separately — summarisation loses numbers first.
# Common mistake: Judging summary quality by ROUGE, which rewards word overlap and ignores whether it is true.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
