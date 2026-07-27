"""Day 151 — Structured output
Concept 6: Enums to constrain choices

Run:  python 06_enums_to_constrain_choices.py
"""

import json

TOOL = {
    'name': 'get_weather',
    'description': 'Current weather for a city',
    'input_schema': {
        'type': 'object',
        'properties': {'city': {'type': 'string'}, 'unit': {'type': 'string', 'enum': ['c', 'f']}},
        'required': ['city'],
    },
}

model_output = '{"city": "Pune", "unit": "c"}'
try:
    args = json.loads(model_output)
    assert 'city' in args, 'missing required field: city'
    print('validated call ->', TOOL['name'], args)
except (json.JSONDecodeError, AssertionError) as e:
    print('reject and retry:', e)

# ---------------------------------------------------------------------
# Remember: Validate every model-produced payload against the schema before it reaches your database.
# Common mistake: Passing model output straight into `eval`, a shell command, or an SQL string.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
