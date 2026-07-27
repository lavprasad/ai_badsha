"""Day 184 — Scaling training
Concept 7: Mixed precision at scale

Run:  python 07_mixed_precision_at_scale.py
"""

from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=2000, weights=[0.95, 0.05], random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, stratify=y, random_state=0)
m = LogisticRegression(max_iter=1000).fit(Xtr, ytr)
print(confusion_matrix(yte, m.predict(Xte)))
print(classification_report(yte, m.predict(Xte), digits=3))
print('roc auc', round(roc_auc_score(yte, m.predict_proba(Xte)[:, 1]), 4))

# ---------------------------------------------------------------------
# Remember: Tune the decision threshold on validation data; 0.5 is a default, not a decision.
# Common mistake: Optimising ROC-AUC on a heavily imbalanced problem where precision-recall AUC is the honest metric.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
