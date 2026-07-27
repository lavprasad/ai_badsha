"""Day 127 — Positional information
Concept 9: Lost in the middle effect

Run:  python 09_lost_in_the_middle_effect.py
"""

def arrange_prompt(instruction, chunks, question):
    """Most relevant chunks at the edges, weakest in the middle."""
    ranked = sorted(chunks, key=lambda c: -c['score'])
    head = ranked[0::2]           # strongest alternate to the front
    tail = ranked[1::2][::-1]     # rest to the back
    body = '\n'.join(c['text'] for c in head + tail)
    return f'{instruction}\n\n{body}\n\nQuestion: {question}'

chunks = [{'text': f'chunk{i}', 'score': s} for i, s in enumerate([0.9, 0.4, 0.8, 0.2])]
print(arrange_prompt('Answer only from the context.', chunks, 'refund window?'))

# ---------------------------------------------------------------------
# Remember: Order matters. Best evidence first and last; filler in the middle is where attention thins out.
# Common mistake: Stuffing 100 retrieved chunks in retrieval order and assuming the model reads them all equally.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
