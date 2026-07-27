"""Day 159 — Agents: planning and reliability
Concept 1: Explicit planning steps

Run:  python 01_explicit_planning_steps.py
"""

def calculator(expr):
    return eval(expr, {'__builtins__': {}}, {})   # locked-down namespace only

TOOLS = {'calc': calculator}

def agent_loop(plan, max_steps=5):
    """`plan` stands in for the model's tool choices."""
    history = []
    for step, (tool, arg) in enumerate(plan[:max_steps], 1):
        result = TOOLS[tool](arg)
        history.append((step, tool, arg, result))
        print(f'step {step}: {tool}({arg!r}) -> {result}')
    return history

agent_loop([('calc', '2 + 2'), ('calc', '(2 + 2) * 10')])

# ---------------------------------------------------------------------
# Remember: Always bound the loop. An unbounded agent burns money and finds creative ways to fail.
# Common mistake: Giving an agent a shell tool with no allowlist and no confirmation step.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
