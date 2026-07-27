"""Day 04 — Files, JSON and the filesystem
Concept 4: JSON serialisation and parsing

Run:  python 04_json_serialisation_and_parsing.py
"""

import joblib, sklearn, json
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
model = LogisticRegression(max_iter=500).fit(X, y)
joblib.dump(model, 'model.joblib')
json.dump({'sklearn': sklearn.__version__, 'features': X.shape[1]}, open('model_meta.json', 'w'))

loaded = joblib.load('model.joblib')
print('reloaded score', round(loaded.score(X, y), 4))

# ---------------------------------------------------------------------
# Remember: Never unpickle a model file you did not produce — pickle executes arbitrary code on load.
# Common mistake: Shipping a pickle with no version metadata and discovering the drift six months later.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
