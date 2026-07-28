# Day 151 — Structured output

Aaj ka goal: **Structured output** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

### Aasaan Bhasha

Free text parse karna mushkil hai; iske bajaye schema ke against JSON maango. Tool/function calling ise formal bana deta hai: aap callable functions batate ho, model structured call lautata hai, aapka code use chalata hai aur result wapas deta hai. Output par act karne se pehle hamesha validate karo.

### Chhota code

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

**Yaad rakho:** Model se aaye har payload ko schema ke against validate karo, tab hi wo aapke database tak pahuche.

**Aam galti:** Model output ko seedha `eval`, shell command, ya SQL string me daal dena.

Practice: `examples/01_why_free_text_is_hard_to_use.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. JSON schemas for outputs

### Aasaan Bhasha

Free text parse karna mushkil hai; iske bajaye schema ke against JSON maango. Tool/function calling ise formal bana deta hai: aap callable functions batate ho, model structured call lautata hai, aapka code use chalata hai aur result wapas deta hai. Output par act karne se pehle hamesha validate karo.

### Chhota code

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

**Yaad rakho:** Model se aaye har payload ko schema ke against validate karo, tab hi wo aapke database tak pahuche.

**Aam galti:** Model output ko seedha `eval`, shell command, ya SQL string me daal dena.

Practice: `examples/02_json_schemas_for_outputs.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Tool/function calling

### Aasaan Bhasha

Free text parse karna mushkil hai; iske bajaye schema ke against JSON maango. Tool/function calling ise formal bana deta hai: aap callable functions batate ho, model structured call lautata hai, aapka code use chalata hai aur result wapas deta hai. Output par act karne se pehle hamesha validate karo.

### Chhota code

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

**Yaad rakho:** Model se aaye har payload ko schema ke against validate karo, tab hi wo aapke database tak pahuche.

**Aam galti:** Model output ko seedha `eval`, shell command, ya SQL string me daal dena.

Practice: `examples/03_tool_function_calling.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Validation and repair loops

### Aasaan Bhasha

Free text parse karna mushkil hai; iske bajaye schema ke against JSON maango. Tool/function calling ise formal bana deta hai: aap callable functions batate ho, model structured call lautata hai, aapka code use chalata hai aur result wapas deta hai. Output par act karne se pehle hamesha validate karo.

### Chhota code

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

**Yaad rakho:** Model se aaye har payload ko schema ke against validate karo, tab hi wo aapke database tak pahuche.

**Aam galti:** Model output ko seedha `eval`, shell command, ya SQL string me daal dena.

Practice: `examples/04_validation_and_repair_loops.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Pydantic models for responses

### Aasaan Bhasha

Free text parse karna mushkil hai; iske bajaye schema ke against JSON maango. Tool/function calling ise formal bana deta hai: aap callable functions batate ho, model structured call lautata hai, aapka code use chalata hai aur result wapas deta hai. Output par act karne se pehle hamesha validate karo.

### Chhota code

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

**Yaad rakho:** Model se aaye har payload ko schema ke against validate karo, tab hi wo aapke database tak pahuche.

**Aam galti:** Model output ko seedha `eval`, shell command, ya SQL string me daal dena.

Practice: `examples/05_pydantic_models_for_responses.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Enums to constrain choices

### Aasaan Bhasha

Free text parse karna mushkil hai; iske bajaye schema ke against JSON maango. Tool/function calling ise formal bana deta hai: aap callable functions batate ho, model structured call lautata hai, aapka code use chalata hai aur result wapas deta hai. Output par act karne se pehle hamesha validate karo.

### Chhota code

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

**Yaad rakho:** Model se aaye har payload ko schema ke against validate karo, tab hi wo aapke database tak pahuche.

**Aam galti:** Model output ko seedha `eval`, shell command, ya SQL string me daal dena.

Practice: `examples/06_enums_to_constrain_choices.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Handling partial and malformed output

### Aasaan Bhasha

Free text parse karna mushkil hai; iske bajaye schema ke against JSON maango. Tool/function calling ise formal bana deta hai: aap callable functions batate ho, model structured call lautata hai, aapka code use chalata hai aur result wapas deta hai. Output par act karne se pehle hamesha validate karo.

### Chhota code

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

**Yaad rakho:** Model se aaye har payload ko schema ke against validate karo, tab hi wo aapke database tak pahuche.

**Aam galti:** Model output ko seedha `eval`, shell command, ya SQL string me daal dena.

Practice: `examples/07_handling_partial_and_malformed_output.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Streaming structured output

### Aasaan Bhasha

Free text parse karna mushkil hai; iske bajaye schema ke against JSON maango. Tool/function calling ise formal bana deta hai: aap callable functions batate ho, model structured call lautata hai, aapka code use chalata hai aur result wapas deta hai. Output par act karne se pehle hamesha validate karo.

### Chhota code

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

**Yaad rakho:** Model se aaye har payload ko schema ke against validate karo, tab hi wo aapke database tak pahuche.

**Aam galti:** Model output ko seedha `eval`, shell command, ya SQL string me daal dena.

Practice: `examples/08_streaming_structured_output.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Confidence fields and their honesty

### Aasaan Bhasha

Free text parse karna mushkil hai; iske bajaye schema ke against JSON maango. Tool/function calling ise formal bana deta hai: aap callable functions batate ho, model structured call lautata hai, aapka code use chalata hai aur result wapas deta hai. Output par act karne se pehle hamesha validate karo.

### Chhota code

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

**Yaad rakho:** Model se aaye har payload ko schema ke against validate karo, tab hi wo aapke database tak pahuche.

**Aam galti:** Model output ko seedha `eval`, shell command, ya SQL string me daal dena.

Practice: `examples/09_confidence_fields_and_their_honesty.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. A robust extraction service

### Aasaan Bhasha

Free text parse karna mushkil hai; iske bajaye schema ke against JSON maango. Tool/function calling ise formal bana deta hai: aap callable functions batate ho, model structured call lautata hai, aapka code use chalata hai aur result wapas deta hai. Output par act karne se pehle hamesha validate karo.

### Chhota code

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

**Yaad rakho:** Model se aaye har payload ko schema ke against validate karo, tab hi wo aapke database tak pahuche.

**Aam galti:** Model output ko seedha `eval`, shell command, ya SQL string me daal dena.

Practice: `examples/10_a_robust_extraction_service.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 151 ke baad aapko ye aana chahiye

- **Why free text is hard to use** ko bina notes dekhe kisi dost ko samjha sakna.
- **JSON schemas for outputs** ko bina notes dekhe kisi dost ko samjha sakna.
- **Tool/function calling** ko bina notes dekhe kisi dost ko samjha sakna.
- **Validation and repair loops** ko bina notes dekhe kisi dost ko samjha sakna.
- **Pydantic models for responses** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
