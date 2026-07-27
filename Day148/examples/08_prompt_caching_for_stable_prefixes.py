"""Day 148 — LLM APIs in code
Concept 8: Prompt caching for stable prefixes

Run:  python 08_prompt_caching_for_stable_prefixes.py
"""

# pip install anthropic ; export ANTHROPIC_API_KEY=...
# import anthropic
# client = anthropic.Anthropic()
# resp = client.messages.create(
#     model='claude-sonnet-5',
#     max_tokens=1024,
#     system=[{'type': 'text', 'text': LONG_STABLE_INSTRUCTIONS,
#              'cache_control': {'type': 'ephemeral'}}],
#     messages=[{'role': 'user', 'content': 'Summarise the attached policy.'}],
# )
# print(resp.content[0].text)
print('Stable prefix first + cache_control -> cheaper, faster repeat calls.')

# ---------------------------------------------------------------------
# Remember: Never hard-code an API key. Read it from the environment and keep it out of git.
# Common mistake: Rebuilding the prompt in a different order each call, so nothing ever hits the cache.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
