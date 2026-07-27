"""Day 52 — Decision trees
Concept 10: Visualising and exporting a tree

Run:  python 10_visualising_and_exporting_a_tree.py
"""

from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
tree = DecisionTreeClassifier(max_depth=3, min_samples_leaf=5, random_state=0).fit(X, y)
print(export_text(tree, feature_names=load_iris().feature_names))

# ---------------------------------------------------------------------
# Remember: A single unpruned tree is almost always worse than a small forest — but it is readable, which sometimes wins.
# Common mistake: Trusting a deep tree's feature importances; they are unstable and biased toward high-cardinality columns.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
