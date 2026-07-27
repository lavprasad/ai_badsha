"""Day 01 — Setting up your AI workbench
Concept 3: Virtual environments with venv

Run:  python 03_virtual_environments_with_venv.py
"""

# python -m venv .venv
# .venv\\Scripts\\activate      (Windows)
# source .venv/bin/activate     (macOS/Linux)
# pip install numpy pandas scikit-learn
# pip freeze > requirements.txt
import sys
print(sys.executable)  # proves which Python you are actually using

# ---------------------------------------------------------------------
# Remember: If `pip install` worked but the import fails, you installed into a different interpreter.
# Common mistake: Installing globally, then wondering why a colleague's machine gets different results.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
