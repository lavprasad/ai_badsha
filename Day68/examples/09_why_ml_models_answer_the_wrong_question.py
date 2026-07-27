"""Day 68 — Causal inference basics
Concept 9: Why ML models answer the wrong question

Run:  python 09_why_ml_models_answer_the_wrong_question.py
"""

import numpy as np

rng = np.random.default_rng(0)
n = 5000
severe = rng.random(n) < 0.3                  # confounder: severity
treated = rng.random(n) < np.where(severe, 0.8, 0.2)   # sick people get treated
outcome = 0.6 * severe - 0.3 * treated + rng.normal(0, 0.1, n)

naive = outcome[treated].mean() - outcome[~treated].mean()
adjusted = np.mean([
    outcome[(treated) & (severe == s)].mean() - outcome[(~treated) & (severe == s)].mean()
    for s in (0, 1)
])
print(f'naive difference   {naive:+.3f}   (treatment looks harmful)')
print(f'adjusted for severity {adjusted:+.3f}   (true effect is -0.3)')

# ---------------------------------------------------------------------
# Remember: Name the confounders before you interpret any observational effect. If you cannot, do not claim causality.
# Common mistake: Telling a business to change X because the model gave X a high feature importance.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
