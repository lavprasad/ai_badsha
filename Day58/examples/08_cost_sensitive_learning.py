"""Day 58 — Handling imbalanced data
Concept 8: Cost-sensitive learning

Run:  python 08_cost_sensitive_learning.py
"""

from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import recall_score

X, y = make_classification(n_samples=3000, weights=[0.97, 0.03], random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, stratify=y, test_size=0.3, random_state=0)

plain = LogisticRegression(max_iter=1000).fit(Xtr, ytr)
weighted = LogisticRegression(max_iter=1000, class_weight='balanced').fit(Xtr, ytr)
print('recall plain   ', round(recall_score(yte, plain.predict(Xte)), 3))
print('recall balanced', round(recall_score(yte, weighted.predict(Xte)), 3))

# ---------------------------------------------------------------------
# Remember: Try `class_weight='balanced'` before installing anything.
# Common mistake: Applying SMOTE before the split so synthetic copies of test rows appear in training.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
