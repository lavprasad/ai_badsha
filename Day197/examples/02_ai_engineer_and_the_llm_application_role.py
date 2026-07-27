"""Day 197 — The AI job landscape
Concept 2: AI engineer and the LLM application role

Run:  python 02_ai_engineer_and_the_llm_application_role.py
"""

ROLES = {
    'Research scientist': 'novel methods, papers, experiments — mostly large labs',
    'ML engineer':        'training pipelines, serving, monitoring, scale',
    'AI engineer':        'LLM apps: prompts, RAG, agents, evals, product surface',
    'Data engineer':      'ingestion, warehouses, contracts — the foundation',
    'Data scientist':     'analysis, experiments, decisions — often no deployed model',
}
for role, day in ROLES.items():
    print(f'{role:<20} {day}')

# ---------------------------------------------------------------------
# Remember: One project you can defend end to end beats ten tutorials on your CV.
# Common mistake: Chasing the title with the highest salary into work you find tedious every single day.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
