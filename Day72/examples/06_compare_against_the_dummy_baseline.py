"""Day 72 — Debugging a model that will not learn
Concept 6: Compare against the dummy baseline

Run:  python 06_compare_against_the_dummy_baseline.py
"""

from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, stratify=y, random_state=0)

baseline = DummyClassifier(strategy='most_frequent').fit(Xtr, ytr)
model = RandomForestClassifier(n_estimators=200, random_state=0).fit(Xtr, ytr)
print(f'dummy {baseline.score(Xte, yte):.3f}   model {model.score(Xte, yte):.3f}')

# ---------------------------------------------------------------------
# Remember: Report your model's score next to the dummy's. A number alone means nothing.
# Common mistake: Celebrating 92% accuracy on data where 91% of rows are one class.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
