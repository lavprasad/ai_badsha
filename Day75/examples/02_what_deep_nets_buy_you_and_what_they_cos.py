"""Day 75 — Why deep learning
Concept 2: What deep nets buy you and what they cost

Run:  python 02_what_deep_nets_buy_you_and_what_they_cos.py
"""

CHOOSE = {
    'tabular, <100k rows':      'gradient boosting — almost always',
    'tabular, huge + embeddings': 'deep nets can win, measure both',
    'images / audio / video':   'deep nets, pretrained backbone',
    'text understanding':       'transformer, pretrained',
    'strict interpretability':  'linear or a small tree',
    'tiny data (<1000 rows)':   'simple model + strong regularization',
}
for k, v in CHOOSE.items():
    print(f'{k:<28} -> {v}')

# ---------------------------------------------------------------------
# Remember: Capacity is not the bottleneck in most projects — data quality and framing are.
# Common mistake: Reaching for a neural network on 3,000 tabular rows and losing to a random forest built in one line.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
