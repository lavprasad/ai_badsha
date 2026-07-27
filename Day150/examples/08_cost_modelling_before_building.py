"""Day 150 — Designing with LLMs
Concept 8: Cost modelling before building

Run:  python 08_cost_modelling_before_building.py
"""

STEPS = [
    '1. Define the decision the model supports and the metric that measures it',
    '2. Get the data; write the loader; assert the schema',
    '3. Dumb baseline (mean / majority class) -> this is the bar',
    '4. Simple model + honest validation split',
    '5. Error analysis: look at 30 wrong predictions by hand',
    '6. Improve the biggest error bucket, not the leaderboard',
    '7. Serve it, log inputs and outputs, monitor drift',
]
for s in STEPS:
    print(s)

# ---------------------------------------------------------------------
# Remember: Spend an hour looking at wrong predictions before you spend a day tuning hyperparameters.
# Common mistake: Six weeks of feature engineering with no baseline to prove any of it helped.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
