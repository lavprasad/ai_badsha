"""Day 54 — Boosting
Concept 9: Handling categorical features natively

Run:  python 09_handling_categorical_features_natively.py
"""

from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=3000, n_informative=8, random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=0)

model = HistGradientBoostingClassifier(
    learning_rate=0.1, max_iter=400, early_stopping=True,
    validation_fraction=0.15, random_state=0,
).fit(Xtr, ytr)
print('stopped at iteration', model.n_iter_, 'test acc', round(model.score(Xte, yte), 4))

# ---------------------------------------------------------------------
# Remember: Low learning rate + many trees + early stopping beats high learning rate + few trees.
# Common mistake: Running a fixed 1000 rounds with no early stopping and shipping an overfit ensemble.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
