"""Day 136 — Text generation quality
Concept 1: Fluency versus factuality

Run:  python 01_fluency_versus_factuality.py
"""

def answer_with_guard(question, chunks, threshold=0.35):
    if not chunks or max(c['score'] for c in chunks) < threshold:
        return "I don't have information about that in the provided documents."
    best = max(chunks, key=lambda c: c['score'])
    return f"{best['text']}  [source: {best['id']}]"

print(answer_with_guard('refund policy?', [{'id': 'policy.pdf#3', 'text': 'Refunds take 5 days.', 'score': 0.81}]))
print(answer_with_guard('CEO home address?', [{'id': 'policy.pdf#3', 'text': 'Refunds take 5 days.', 'score': 0.11}]))

# ---------------------------------------------------------------------
# Remember: An explicit 'not in my sources' path is worth more than any confidence score.
# Common mistake: Shipping a chatbot with no abstain path, so it invents a policy under pressure.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
