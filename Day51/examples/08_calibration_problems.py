"""Day 51 — Naive Bayes
Concept 8: Calibration problems

Run:  python 08_calibration_problems.py
"""

prior = 1 / 10_000          # base rate of the disease
sensitivity = 0.99          # P(positive | sick)
false_positive = 0.01       # P(positive | healthy)

evidence = sensitivity * prior + false_positive * (1 - prior)
posterior = sensitivity * prior / evidence
print(f'P(sick | positive) = {posterior:.4f}')   # ~0.0098

# ---------------------------------------------------------------------
# Remember: Rare events make precision collapse no matter how good the classifier looks on accuracy.
# Common mistake: Reporting accuracy on an imbalanced problem where predicting 'no' always scores 99%.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
