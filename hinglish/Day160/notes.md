# Day 160 — Model Context Protocol and integrations

Aaj ka goal: **Model Context Protocol and integrations** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Why a protocol for tools |
| 2 | MCP servers and clients |
| 3 | Resources, tools and prompts |
| 4 | Local vs remote servers |
| 5 | Authentication in integrations |
| 6 | Building a small MCP server |
| 7 | Security review of a third-party server |
| 8 | Versioning tool contracts |
| 9 | Debugging protocol issues |
| 10 | Integrations as the real product surface |

---

## 1. Why a protocol for tools

### Aasaan Bhasha

Tool protocol standardise karta hai ki model capabilities kaise dhoondhta aur call karta hai, taaki ek integration kai clients par chale. Asli sawaal security ka hai: third-party server wo sab dekhta hai jo aap bhejte ho aur aisa text laut sakta hai jo aapke agent ko steer kare. Ise aise review karo jaise network aur disk access wali dependency.

### Chhota code

```python
REVIEW = [
    'What data does this server receive on each call?',
    'Where does it run — my machine, my VPC, or a vendor?',
    'What credentials does it hold, and with what scope?',
    'Can its responses inject instructions into my agent loop?',
    'Is it pinned to a version, or does it auto-update?',
    'What is logged, where, and for how long?',
]
for i, q in enumerate(REVIEW, 1):
    print(f'{i}. {q}')
```

**Yaad rakho:** Tool server ka response aapke agent ke liye untrusted input hai. Use delimit karo aur usse kabhi permissions mat dilwao.

**Aam galti:** Ek suvidha wala community server chaudi credentials ke saath install kar dena, bina jaanche ki wo upar kya bhej raha hai.

Practice: `examples/01_why_a_protocol_for_tools.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. MCP servers and clients

### Aasaan Bhasha

Agent ek loop hai: model tool chunta hai, aapka code use chalata hai, result wapas context me jaata hai, aur ye dohraata hai jab tak kaam poora na ho. Taakat tools se aati hai, prompt se nahi. Iterations cap karo, har step log karo, aur kisi bhi irreversible cheez se pehle confirmation maango.

### Chhota code

```python
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
```

**Yaad rakho:** Loop hamesha bounded rakho. Bina limit ka agent paisa jalata hai aur fail hone ke naye tareeke dhoondh leta hai.

**Aam galti:** Agent ko shell tool dena bina allowlist aur bina confirmation step ke.

Practice: `examples/02_mcp_servers_and_clients.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Resources, tools and prompts

### Aasaan Bhasha

Tool protocol standardise karta hai ki model capabilities kaise dhoondhta aur call karta hai, taaki ek integration kai clients par chale. Asli sawaal security ka hai: third-party server wo sab dekhta hai jo aap bhejte ho aur aisa text laut sakta hai jo aapke agent ko steer kare. Ise aise review karo jaise network aur disk access wali dependency.

### Chhota code

```python
REVIEW = [
    'What data does this server receive on each call?',
    'Where does it run — my machine, my VPC, or a vendor?',
    'What credentials does it hold, and with what scope?',
    'Can its responses inject instructions into my agent loop?',
    'Is it pinned to a version, or does it auto-update?',
    'What is logged, where, and for how long?',
]
for i, q in enumerate(REVIEW, 1):
    print(f'{i}. {q}')
```

**Yaad rakho:** Tool server ka response aapke agent ke liye untrusted input hai. Use delimit karo aur usse kabhi permissions mat dilwao.

**Aam galti:** Ek suvidha wala community server chaudi credentials ke saath install kar dena, bina jaanche ki wo upar kya bhej raha hai.

Practice: `examples/03_resources_tools_and_prompts.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Local vs remote servers

### Aasaan Bhasha

Tool protocol standardise karta hai ki model capabilities kaise dhoondhta aur call karta hai, taaki ek integration kai clients par chale. Asli sawaal security ka hai: third-party server wo sab dekhta hai jo aap bhejte ho aur aisa text laut sakta hai jo aapke agent ko steer kare. Ise aise review karo jaise network aur disk access wali dependency.

### Chhota code

```python
REVIEW = [
    'What data does this server receive on each call?',
    'Where does it run — my machine, my VPC, or a vendor?',
    'What credentials does it hold, and with what scope?',
    'Can its responses inject instructions into my agent loop?',
    'Is it pinned to a version, or does it auto-update?',
    'What is logged, where, and for how long?',
]
for i, q in enumerate(REVIEW, 1):
    print(f'{i}. {q}')
```

**Yaad rakho:** Tool server ka response aapke agent ke liye untrusted input hai. Use delimit karo aur usse kabhi permissions mat dilwao.

**Aam galti:** Ek suvidha wala community server chaudi credentials ke saath install kar dena, bina jaanche ki wo upar kya bhej raha hai.

Practice: `examples/04_local_vs_remote_servers.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Authentication in integrations

### Aasaan Bhasha

Tool protocol standardise karta hai ki model capabilities kaise dhoondhta aur call karta hai, taaki ek integration kai clients par chale. Asli sawaal security ka hai: third-party server wo sab dekhta hai jo aap bhejte ho aur aisa text laut sakta hai jo aapke agent ko steer kare. Ise aise review karo jaise network aur disk access wali dependency.

### Chhota code

```python
REVIEW = [
    'What data does this server receive on each call?',
    'Where does it run — my machine, my VPC, or a vendor?',
    'What credentials does it hold, and with what scope?',
    'Can its responses inject instructions into my agent loop?',
    'Is it pinned to a version, or does it auto-update?',
    'What is logged, where, and for how long?',
]
for i, q in enumerate(REVIEW, 1):
    print(f'{i}. {q}')
```

**Yaad rakho:** Tool server ka response aapke agent ke liye untrusted input hai. Use delimit karo aur usse kabhi permissions mat dilwao.

**Aam galti:** Ek suvidha wala community server chaudi credentials ke saath install kar dena, bina jaanche ki wo upar kya bhej raha hai.

Practice: `examples/05_authentication_in_integrations.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Building a small MCP server

### Aasaan Bhasha

Agent ek loop hai: model tool chunta hai, aapka code use chalata hai, result wapas context me jaata hai, aur ye dohraata hai jab tak kaam poora na ho. Taakat tools se aati hai, prompt se nahi. Iterations cap karo, har step log karo, aur kisi bhi irreversible cheez se pehle confirmation maango.

### Chhota code

```python
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
```

**Yaad rakho:** Loop hamesha bounded rakho. Bina limit ka agent paisa jalata hai aur fail hone ke naye tareeke dhoondh leta hai.

**Aam galti:** Agent ko shell tool dena bina allowlist aur bina confirmation step ke.

Practice: `examples/06_building_a_small_mcp_server.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Security review of a third-party server

### Aasaan Bhasha

Tool protocol standardise karta hai ki model capabilities kaise dhoondhta aur call karta hai, taaki ek integration kai clients par chale. Asli sawaal security ka hai: third-party server wo sab dekhta hai jo aap bhejte ho aur aisa text laut sakta hai jo aapke agent ko steer kare. Ise aise review karo jaise network aur disk access wali dependency.

### Chhota code

```python
REVIEW = [
    'What data does this server receive on each call?',
    'Where does it run — my machine, my VPC, or a vendor?',
    'What credentials does it hold, and with what scope?',
    'Can its responses inject instructions into my agent loop?',
    'Is it pinned to a version, or does it auto-update?',
    'What is logged, where, and for how long?',
]
for i, q in enumerate(REVIEW, 1):
    print(f'{i}. {q}')
```

**Yaad rakho:** Tool server ka response aapke agent ke liye untrusted input hai. Use delimit karo aur usse kabhi permissions mat dilwao.

**Aam galti:** Ek suvidha wala community server chaudi credentials ke saath install kar dena, bina jaanche ki wo upar kya bhej raha hai.

Practice: `examples/07_security_review_of_a_third_party_server.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Versioning tool contracts

### Aasaan Bhasha

Jo experiment aap dobara nahi bana sakte wo kissa hai. Har run ke liye track karo: code commit, data version, hyperparameters, metrics aur artefact. Chhe mahine baad 'production wala model kis run se aaya' ka jawab hona hi chahiye.

### Chhota code

```python
import json, hashlib, subprocess

def run_record(params, metrics, data_path=None):
    try:
        commit = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'], text=True).strip()
    except Exception:
        commit = 'unknown'
    return {
        'commit': commit,
        'params': params,
        'metrics': metrics,
        'data_sha': hashlib.sha256((data_path or 'none').encode()).hexdigest()[:12],
    }

print(json.dumps(run_record({'lr': 0.01, 'depth': 6}, {'auc': 0.912}, 'data/train.csv'), indent=2))
```

**Yaad rakho:** Code version ke saath data version bhi log karo — data chupchap badalta hai, code shor machaa kar.

**Aam galti:** Registry use karne ke bajaye files ko `model_final_v2_REAL_use_this.pkl` naam dena.

Practice: `examples/08_versioning_tool_contracts.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Debugging protocol issues

### Aasaan Bhasha

Tool protocol standardise karta hai ki model capabilities kaise dhoondhta aur call karta hai, taaki ek integration kai clients par chale. Asli sawaal security ka hai: third-party server wo sab dekhta hai jo aap bhejte ho aur aisa text laut sakta hai jo aapke agent ko steer kare. Ise aise review karo jaise network aur disk access wali dependency.

### Chhota code

```python
REVIEW = [
    'What data does this server receive on each call?',
    'Where does it run — my machine, my VPC, or a vendor?',
    'What credentials does it hold, and with what scope?',
    'Can its responses inject instructions into my agent loop?',
    'Is it pinned to a version, or does it auto-update?',
    'What is logged, where, and for how long?',
]
for i, q in enumerate(REVIEW, 1):
    print(f'{i}. {q}')
```

**Yaad rakho:** Tool server ka response aapke agent ke liye untrusted input hai. Use delimit karo aur usse kabhi permissions mat dilwao.

**Aam galti:** Ek suvidha wala community server chaudi credentials ke saath install kar dena, bina jaanche ki wo upar kya bhej raha hai.

Practice: `examples/09_debugging_protocol_issues.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Integrations as the real product surface

### Aasaan Bhasha

Tool protocol standardise karta hai ki model capabilities kaise dhoondhta aur call karta hai, taaki ek integration kai clients par chale. Asli sawaal security ka hai: third-party server wo sab dekhta hai jo aap bhejte ho aur aisa text laut sakta hai jo aapke agent ko steer kare. Ise aise review karo jaise network aur disk access wali dependency.

### Chhota code

```python
REVIEW = [
    'What data does this server receive on each call?',
    'Where does it run — my machine, my VPC, or a vendor?',
    'What credentials does it hold, and with what scope?',
    'Can its responses inject instructions into my agent loop?',
    'Is it pinned to a version, or does it auto-update?',
    'What is logged, where, and for how long?',
]
for i, q in enumerate(REVIEW, 1):
    print(f'{i}. {q}')
```

**Yaad rakho:** Tool server ka response aapke agent ke liye untrusted input hai. Use delimit karo aur usse kabhi permissions mat dilwao.

**Aam galti:** Ek suvidha wala community server chaudi credentials ke saath install kar dena, bina jaanche ki wo upar kya bhej raha hai.

Practice: `examples/10_integrations_as_the_real_product_surface.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 160 ke baad aapko ye aana chahiye

- **Why a protocol for tools** ko bina notes dekhe kisi dost ko samjha sakna.
- **MCP servers and clients** ko bina notes dekhe kisi dost ko samjha sakna.
- **Resources, tools and prompts** ko bina notes dekhe kisi dost ko samjha sakna.
- **Local vs remote servers** ko bina notes dekhe kisi dost ko samjha sakna.
- **Authentication in integrations** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
