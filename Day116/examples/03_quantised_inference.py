"""Day 116 — Edge and mobile vision
Concept 3: Quantised inference

Run:  python 03_quantised_inference.py
"""

BUDGET = {'latency_ms': 100, 'model_mb': 25, 'ram_mb': 150}

candidates = [
    {'name': 'resnet50-fp32',   'latency_ms': 340, 'model_mb': 98, 'ram_mb': 420},
    {'name': 'mobilenetv3-int8','latency_ms':  38, 'model_mb':  6, 'ram_mb':  90},
    {'name': 'efficientnet-b0', 'latency_ms': 120, 'model_mb': 21, 'ram_mb': 180},
]
for c in candidates:
    fits = all(c[k] <= v for k, v in BUDGET.items())
    print(f"{c['name']:<20} {'FITS' if fits else 'over budget'}")

# ---------------------------------------------------------------------
# Remember: Measure on the target device, warm and under load — not on your laptop, once, cold.
# Common mistake: Validating latency on a desktop GPU and discovering the phone throttles after 40 seconds.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
