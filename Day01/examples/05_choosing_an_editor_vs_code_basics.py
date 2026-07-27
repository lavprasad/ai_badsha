"""Day 01 — Setting up your AI workbench
Concept 5: Choosing an editor: VS Code basics

Run:  python 05_choosing_an_editor_vs_code_basics.py
"""

# The debugger you already have, no editor required:
def normalise(values):
    total = sum(values)
    # breakpoint()      # <- uncomment: drops you into an interactive prompt here
    return [v / total for v in values]

print(normalise([1, 2, 3]))
print('''
At a breakpoint:  n = next line   s = step into   c = continue
                  p expr = print   l = list source  q = quit
''')

# ---------------------------------------------------------------------
# Remember: `breakpoint()` is built in. You never need to add print statements to inspect a value again.
# Common mistake: Debugging a nested pipeline with print statements you then forget to remove.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
