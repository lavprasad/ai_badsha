# Day 151 — Structured output

Today's goal: work through **Structured output** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Why free text is hard to use |
| 2 | JSON schemas for outputs |
| 3 | Tool/function calling |
| 4 | Validation and repair loops |
| 5 | Pydantic models for responses |
| 6 | Enums to constrain choices |
| 7 | Handling partial and malformed output |
| 8 | Streaming structured output |
| 9 | Confidence fields and their honesty |
| 10 | A robust extraction service |

---

## 1. Why free text is hard to use

Free text is hard to parse; ask for JSON against a schema instead. Tool/function calling formalises this: you describe callable functions, the model returns a structured call, your code executes it and returns the result. Always validate before you act on the output.

```python
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
```

**Remember:** Validate every model-produced payload against the schema before it reaches your database.

**Common mistake:** Passing model output straight into `eval`, a shell command, or an SQL string.

Practice: open `examples/01_why_free_text_is_hard_to_use.py`, predict the output, change one line, predict again.

## 2. JSON schemas for outputs

Free text is hard to parse; ask for JSON against a schema instead. Tool/function calling formalises this: you describe callable functions, the model returns a structured call, your code executes it and returns the result. Always validate before you act on the output.

```python
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
```

**Remember:** Validate every model-produced payload against the schema before it reaches your database.

**Common mistake:** Passing model output straight into `eval`, a shell command, or an SQL string.

Practice: open `examples/02_json_schemas_for_outputs.py`, predict the output, change one line, predict again.

## 3. Tool/function calling

Free text is hard to parse; ask for JSON against a schema instead. Tool/function calling formalises this: you describe callable functions, the model returns a structured call, your code executes it and returns the result. Always validate before you act on the output.

```python
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
```

**Remember:** Validate every model-produced payload against the schema before it reaches your database.

**Common mistake:** Passing model output straight into `eval`, a shell command, or an SQL string.

Practice: open `examples/03_tool_function_calling.py`, predict the output, change one line, predict again.

## 4. Validation and repair loops

Free text is hard to parse; ask for JSON against a schema instead. Tool/function calling formalises this: you describe callable functions, the model returns a structured call, your code executes it and returns the result. Always validate before you act on the output.

```python
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
```

**Remember:** Validate every model-produced payload against the schema before it reaches your database.

**Common mistake:** Passing model output straight into `eval`, a shell command, or an SQL string.

Practice: open `examples/04_validation_and_repair_loops.py`, predict the output, change one line, predict again.

## 5. Pydantic models for responses

Free text is hard to parse; ask for JSON against a schema instead. Tool/function calling formalises this: you describe callable functions, the model returns a structured call, your code executes it and returns the result. Always validate before you act on the output.

```python
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
```

**Remember:** Validate every model-produced payload against the schema before it reaches your database.

**Common mistake:** Passing model output straight into `eval`, a shell command, or an SQL string.

Practice: open `examples/05_pydantic_models_for_responses.py`, predict the output, change one line, predict again.

## 6. Enums to constrain choices

Free text is hard to parse; ask for JSON against a schema instead. Tool/function calling formalises this: you describe callable functions, the model returns a structured call, your code executes it and returns the result. Always validate before you act on the output.

```python
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
```

**Remember:** Validate every model-produced payload against the schema before it reaches your database.

**Common mistake:** Passing model output straight into `eval`, a shell command, or an SQL string.

Practice: open `examples/06_enums_to_constrain_choices.py`, predict the output, change one line, predict again.

## 7. Handling partial and malformed output

Free text is hard to parse; ask for JSON against a schema instead. Tool/function calling formalises this: you describe callable functions, the model returns a structured call, your code executes it and returns the result. Always validate before you act on the output.

```python
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
```

**Remember:** Validate every model-produced payload against the schema before it reaches your database.

**Common mistake:** Passing model output straight into `eval`, a shell command, or an SQL string.

Practice: open `examples/07_handling_partial_and_malformed_output.py`, predict the output, change one line, predict again.

## 8. Streaming structured output

Free text is hard to parse; ask for JSON against a schema instead. Tool/function calling formalises this: you describe callable functions, the model returns a structured call, your code executes it and returns the result. Always validate before you act on the output.

```python
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
```

**Remember:** Validate every model-produced payload against the schema before it reaches your database.

**Common mistake:** Passing model output straight into `eval`, a shell command, or an SQL string.

Practice: open `examples/08_streaming_structured_output.py`, predict the output, change one line, predict again.

## 9. Confidence fields and their honesty

Free text is hard to parse; ask for JSON against a schema instead. Tool/function calling formalises this: you describe callable functions, the model returns a structured call, your code executes it and returns the result. Always validate before you act on the output.

```python
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
```

**Remember:** Validate every model-produced payload against the schema before it reaches your database.

**Common mistake:** Passing model output straight into `eval`, a shell command, or an SQL string.

Practice: open `examples/09_confidence_fields_and_their_honesty.py`, predict the output, change one line, predict again.

## 10. A robust extraction service

Free text is hard to parse; ask for JSON against a schema instead. Tool/function calling formalises this: you describe callable functions, the model returns a structured call, your code executes it and returns the result. Always validate before you act on the output.

```python
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
```

**Remember:** Validate every model-produced payload against the schema before it reaches your database.

**Common mistake:** Passing model output straight into `eval`, a shell command, or an SQL string.

Practice: open `examples/10_a_robust_extraction_service.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 151

- Explain **Why free text is hard to use** to someone else without notes.
- Explain **JSON schemas for outputs** to someone else without notes.
- Explain **Tool/function calling** to someone else without notes.
- Explain **Validation and repair loops** to someone else without notes.
- Explain **Pydantic models for responses** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
