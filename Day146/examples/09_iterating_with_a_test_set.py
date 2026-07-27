"""Day 146 — Prompt engineering foundations
Concept 9: Iterating with a test set

Run:  python 09_iterating_with_a_test_set.py
"""

prompt = '''You are a support triage assistant.

Classify the ticket into exactly one of: BILLING, BUG, FEATURE, OTHER.
Return JSON only: {"label": ..., "confidence": 0.0-1.0}

Examples:
Ticket: "charged twice this month" -> {"label": "BILLING", "confidence": 0.95}
Ticket: "app crashes on upload"    -> {"label": "BUG", "confidence": 0.92}

Ticket: "can you add dark mode?"
'''
print(prompt)
print('Structure: role -> task -> allowed outputs -> format -> examples -> input.')

# ---------------------------------------------------------------------
# Remember: Put the output format last and show it as an example — models copy the nearest pattern.
# Common mistake: Writing a vague prompt, getting vague output, and blaming the model.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
