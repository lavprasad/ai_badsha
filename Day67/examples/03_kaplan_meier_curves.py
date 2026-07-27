"""Day 67 — Survival and duration models
Concept 3: Kaplan-Meier curves

Run:  python 03_kaplan_meier_curves.py
"""

import numpy as np

# Kaplan-Meier estimator, by hand
times = np.array([2, 3, 3, 5, 8, 9, 12])
event = np.array([1, 1, 0, 1, 0, 1, 0])   # 0 = still alive at last contact (censored)

surv, n_at_risk, s = [], len(times), 1.0
for t in np.unique(times):
    at_risk = int((times >= t).sum())
    died = int(((times == t) & (event == 1)).sum())
    if died:
        s *= (1 - died / at_risk)
    surv.append((int(t), at_risk, died, round(s, 3)))

print('time  at_risk  events  S(t)')
for row in surv:
    print('%4d %8d %7d %6.3f' % row)

# ---------------------------------------------------------------------
# Remember: A censored row still carries information: it survived at least that long. Never drop it.
# Common mistake: Modelling churn as 'churned in 30 days yes/no' and silently discarding everyone who joined last week.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
