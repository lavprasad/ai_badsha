"""Day 164 — Evaluation for LLM applications
Concept 5: Pairwise preference evaluation

Run:  python 05_pairwise_preference_evaluation.py
"""

import numpy as np

# DPO intuition: raise logprob of the chosen reply relative to the rejected one,
# while a KL term keeps you near the reference model.
policy = {'chosen': -2.0, 'rejected': -2.5}     # log-probs under the trained model
ref = {'chosen': -2.4, 'rejected': -2.3}        # log-probs under the frozen reference
beta = 0.1

margin = beta * ((policy['chosen'] - ref['chosen']) - (policy['rejected'] - ref['rejected']))
loss = -np.log(1 / (1 + np.exp(-margin)))
print(f'margin {margin:.4f}  dpo loss {loss:.4f}')

# ---------------------------------------------------------------------
# Remember: Alignment optimises a proxy for what humans want; the proxy can always be gamed.
# Common mistake: Over-optimising the reward model until outputs are sycophantic and useless — classic reward hacking.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
