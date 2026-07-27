"""Day 139 — Multilingual and Indic NLP
Concept 6: Transliteration

Run:  python 06_transliteration.py
"""

def rough_tokens(text, chars_per_token):
    return round(len(text) / chars_per_token)

samples = [
    ('english', 'Please refund my order from last week.', 4.0),
    ('hinglish', 'Mera last week ka order refund kar do please.', 3.5),
    ('devanagari', 'कृपया मेरा पिछले सप्ताह का ऑर्डर वापस करें।', 1.5),
]
for name, text, cpt in samples:
    print(f'{name:<12} {len(text):>3} chars -> ~{rough_tokens(text, cpt):>3} tokens')
print('\nSame meaning, very different bills and context usage.')

# ---------------------------------------------------------------------
# Remember: Measure tokens per request in your users' actual language, not in English.
# Common mistake: Sizing a context window and a budget from English samples, then launching in a script that costs 4x.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
