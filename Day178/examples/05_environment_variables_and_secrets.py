"""Day 178 — Containers and deployment
Concept 5: Environment variables and secrets

Run:  python 05_environment_variables_and_secrets.py
"""

DOCKERFILE = '''
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
'''
print(DOCKERFILE)
print('Copy requirements first so the pip layer caches across code changes.')

# ---------------------------------------------------------------------
# Remember: `--no-cache-dir` and a slim base keep images small; small images deploy fast.
# Common mistake: `COPY . .` before `pip install`, which busts the dependency cache on every code edit.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
