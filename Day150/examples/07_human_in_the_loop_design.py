"""Day 150 — Designing with LLMs
Concept 7: Human-in-the-loop design

Run:  python 07_human_in_the_loop_design.py
"""

def extract_and_act(text, model_call, db):
    raw = model_call(text)                       # 1. fuzzy: model reads language
    try:                                          # 2. deterministic: validate
        amount = float(raw['amount'])
        account = str(raw['account'])
    except (KeyError, ValueError, TypeError):
        return {'status': 'rejected', 'reason': 'unparseable model output'}
    if not 0 < amount <= 10_000:                  # 3. deterministic: business rules
        return {'status': 'escalate', 'reason': 'amount outside auto-approve band'}
    return {'status': 'approved', 'account': account, 'amount': amount}

print(extract_and_act('refund 500', lambda t: {'amount': '500', 'account': 'A-1'}, db=None))
print(extract_and_act('refund lots', lambda t: {'amount': '99000', 'account': 'A-1'}, db=None))

# ---------------------------------------------------------------------
# Remember: The model proposes; your code disposes. Never let model output be the last check before an action.
# Common mistake: Trusting a model's own 'confidence: 0.98' field as if it were a calibrated probability.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
