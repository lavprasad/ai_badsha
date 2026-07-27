"""Day 196 — Reading research
Concept 2: The three-pass reading method

Run:  python 02_the_three_pass_reading_method.py
"""

PASS_1 = ['title', 'abstract', 'figures and captions', 'conclusion']
PASS_2 = ['method section', 'experimental setup', 'baselines used', 'results tables']
PASS_3 = ['every equation', 'appendix', 'reimplement the core idea']

for i, (name, items) in enumerate([('5 min', PASS_1), ('30 min', PASS_2), ('hours', PASS_3)], 1):
    print(f'Pass {i} ({name}): ' + ', '.join(items))
print('\nStop after pass 1 for 90% of papers. That is not laziness, that is triage.')

# ---------------------------------------------------------------------
# Remember: Check which baselines they compared against. A weak baseline makes any method look strong.
# Common mistake: Reading twenty papers and implementing none — understanding without building fades in a week.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
