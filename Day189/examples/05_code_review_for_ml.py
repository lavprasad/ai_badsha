"""Day 189 — Working on an AI team
Concept 5: Code review for ML

Run:  python 05_code_review_for_ml.py
"""

PLAN = [
    ('Phase 0: feasibility', '1 week',  'Does a baseline beat the current rule at all?'),
    ('Phase 1: baseline',    '2 weeks', 'Honest CV score + error analysis'),
    ('Phase 2: productionise','3 weeks', 'Serving, monitoring, fallback path'),
    ('Phase 3: iterate',     'ongoing', 'Flywheel from real feedback'),
]
for name, dur, gate in PLAN:
    print(f'{name:<24} {dur:<9} kill criterion: {gate}')
print('\nEach phase can end the project. That is the point.')

# ---------------------------------------------------------------------
# Remember: Give ranges and kill criteria, never a single date for work whose feasibility is unknown.
# Common mistake: Promising 95% accuracy in a planning meeting before anyone has looked at the data.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
