"""Day 186 — Privacy, security and compliance
Concept 10: Working with a compliance team

Run:  python 10_working_with_a_compliance_team.py
"""

import numpy as np
import pandas as pd

df = pd.DataFrame({
    'group': ['a'] * 100 + ['b'] * 100,
    'y':     [1] * 50 + [0] * 50 + [1] * 50 + [0] * 50,
    'pred':  [1] * 45 + [0] * 55 + [1] * 30 + [0] * 70,
})
for g, sub in df.groupby('group'):
    tpr = ((sub.pred == 1) & (sub.y == 1)).sum() / max((sub.y == 1).sum(), 1)
    rate = (sub.pred == 1).mean()
    print(f'group {g}: selection rate {rate:.2f}  recall {tpr:.2f}')
print('Large gaps here are the finding — investigate before shipping.')

# ---------------------------------------------------------------------
# Remember: Dropping the sensitive attribute does not remove bias; proxies (pincode, name) carry it right back in.
# Common mistake: Auditing fairness once at launch and never again as the data drifts.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
