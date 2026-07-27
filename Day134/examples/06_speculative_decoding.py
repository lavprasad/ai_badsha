"""Day 134 — Serving LLMs efficiently
Concept 6: Speculative decoding

Run:  python 06_speculative_decoding.py
"""

# pip install fastapi uvicorn ; run: uvicorn app:app --reload
# from fastapi import FastAPI
# from pydantic import BaseModel
# import joblib
#
# app = FastAPI()
# model = joblib.load('model.joblib')      # once, at startup
#
# class Req(BaseModel):
#     features: list[float]
#
# @app.get('/health')
# def health():
#     return {'ok': True}
#
# @app.post('/predict')
# def predict(req: Req):
#     return {'prediction': float(model.predict([req.features])[0])}
print('Load once at startup; validate with a schema; expose /health for the load balancer.')

# ---------------------------------------------------------------------
# Remember: Batch requests where latency allows — GPU throughput collapses on batch size 1.
# Common mistake: Reloading the model per request and wondering why p99 latency is four seconds.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
