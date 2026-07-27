"""Day 166 — Cost engineering
Concept 4: Model routing by difficulty

Run:  python 04_model_routing_by_difficulty.py
"""

def cost_per_resolved(price_per_call, success_rate, escalation_price):
    return price_per_call + (1 - success_rate) * escalation_price

options = [
    ('small model',  0.001, 0.62),
    ('large model',  0.020, 0.94),
    ('small->large', 0.001 + 0.38 * 0.020, 0.96),
]
for name, price, success in options:
    print(f'{name:<14} cost/resolved = {cost_per_resolved(price, success, 2.00):.4f}')
print('\n(escalation to a human costed at 2.00)')

# ---------------------------------------------------------------------
# Remember: Always price the failure path. Human escalation usually dominates every model cost in the table.
# Common mistake: Switching to the cheapest model, watching token spend drop, and never noticing support load doubled.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
