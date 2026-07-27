"""Day 35 — The machine learning problem framing
Concept 8: Feasibility: is the signal even there

Run:  python 08_feasibility_is_the_signal_even_there.py
"""

BRIEF = {
    'decision': 'Which support tickets get routed to the billing team',
    'unit': 'one ticket at creation time',
    'target': 'team that eventually resolved it',
    'metric': 'macro F1, because small teams matter as much as big ones',
    'baseline': 'keyword rules -> 0.61 macro F1',
    'available_at_predict_time': ['subject', 'body', 'customer_plan'],
    'not_available': ['resolution_time', 'agent_notes'],
}
for k, v in BRIEF.items():
    print(f'{k:>26}: {v}')

# ---------------------------------------------------------------------
# Remember: List what data exists *at prediction time* before you list features. That list kills most leaks.
# Common mistake: Building a model for six weeks before discovering the decision it supports is already automated.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
