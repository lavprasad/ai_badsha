"""Day 164 — Evaluation for LLM applications
Concept 1: Defining success for a fuzzy task

Run:  python 01_defining_success_for_a_fuzzy_task.py
"""

GOLDEN = [
    {'input': 'charged twice', 'expect': 'BILLING'},
    {'input': 'crashes on upload', 'expect': 'BUG'},
    {'input': 'please add dark mode', 'expect': 'FEATURE'},
]

def classify(text):                      # stand-in for the real model call
    t = text.lower()
    if 'charg' in t or 'bill' in t:
        return 'BILLING'
    if 'crash' in t or 'error' in t:
        return 'BUG'
    return 'FEATURE'

hits = sum(classify(c['input']) == c['expect'] for c in GOLDEN)
print(f'eval score {hits}/{len(GOLDEN)}')
assert hits == len(GOLDEN), 'regression: fix before shipping'

# ---------------------------------------------------------------------
# Remember: 50 real examples you curated beat 5000 synthetic ones nobody checked.
# Common mistake: Changing the prompt on Friday with no eval and finding out from customers on Monday.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
