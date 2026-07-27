"""Day 198 — Interview preparation
Concept 10: A four-week preparation plan

Run:  python 10_a_four_week_preparation_plan.py
"""

PAPER_CHECKLIST = [
    'What problem, and what was the previous best?',
    'What is the single new idea? (usually one sentence)',
    'What is the evidence? Which baselines, which datasets?',
    'What did they NOT test? (the limitations section is the honest part)',
    'Could I implement the core idea in 50 lines?',
]
for q in PAPER_CHECKLIST:
    print('-', q)

# ---------------------------------------------------------------------
# Remember: If you cannot explain why your validation split is honest, you do not own the project yet.
# Common mistake: Listing twenty frameworks on a CV and being unable to debug a shape error in any of them.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
