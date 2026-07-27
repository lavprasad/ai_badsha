"""Day 04 — Files, JSON and the filesystem
Concept 5: pathlib for portable paths

Run:  python 05_pathlib_for_portable_paths.py
"""

import json, os
from pathlib import Path

config = {'model': 'small', 'epochs': 3, 'tags': ['demo']}
p = Path('config.json')
p.write_text(json.dumps(config, indent=2), encoding='utf-8')
print(json.loads(p.read_text(encoding='utf-8')))
p.unlink()

api_key = os.environ.get('MY_API_KEY')
print('key loaded from env:', bool(api_key))   # never print the key itself

# ---------------------------------------------------------------------
# Remember: Use `Path` division (`root / 'data' / 'x.csv'`) instead of string concatenation with slashes.
# Common mistake: Committing an API key, then 'removing' it in a later commit where it still lives in history.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
