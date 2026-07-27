"""Day 170 — Code-focused AI
Concept 8: Security of generated code

Run:  python 08_security_of_generated_code.py
"""

def generate_until_passing(generate, run_tests, max_attempts=3):
    feedback = None
    for attempt in range(1, max_attempts + 1):
        code = generate(feedback)
        ok, output = run_tests(code)
        print(f'attempt {attempt}: {"PASS" if ok else "FAIL"} — {output}')
        if ok:
            return code
        feedback = output          # the failure IS the next prompt
    return None

state = {'n': 0}
def fake_gen(fb):
    state['n'] += 1
    return f'version{state["n"]}'
def fake_tests(code):
    return (code == 'version2', 'assertion failed on empty input' if code != 'version2' else 'all green')

print('final:', generate_until_passing(fake_gen, fake_tests))

# ---------------------------------------------------------------------
# Remember: Feed the test failure text straight back as context — it is the highest-signal prompt you have.
# Common mistake: Accepting generated code that imports a package name nobody verified exists (a real supply-chain vector).
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
