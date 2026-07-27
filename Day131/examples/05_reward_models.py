"""Day 131 — Post-training: SFT and alignment
Concept 5: Reward models

Run:  python 05_reward_models.py
"""

# Typical SFT record: the model learns the assistant turn only.
example = {
    'messages': [
        {'role': 'system', 'content': 'You extract invoice fields as JSON.'},
        {'role': 'user', 'content': 'Invoice 4471, dated 2024-03-02, total Rs 15,300.'},
        {'role': 'assistant', 'content': '{"id": "4471", "date": "2024-03-02", "total": 15300}'},
    ]
}
import json
print(json.dumps(example, indent=2))
print('\\nRule: mask the loss on system+user tokens; train only on the assistant response.')

# ---------------------------------------------------------------------
# Remember: Fine-tune for behaviour and format. Use RAG for knowledge that changes.
# Common mistake: Fine-tuning to inject company facts, then re-training every time a policy document changes.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
