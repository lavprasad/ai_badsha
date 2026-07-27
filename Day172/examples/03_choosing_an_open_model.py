"""Day 172 — Open source and self-hosting
Concept 3: Choosing an open model

Run:  python 03_choosing_an_open_model.py
"""

def monthly_comparison(requests, tokens_per_req, api_price_per_mtok, gpu_hourly, gpu_util):
    api = requests * tokens_per_req / 1e6 * api_price_per_mtok
    self_host = gpu_hourly * 24 * 30 / max(gpu_util, 0.01)
    return {'api': round(api), 'self_hosted': round(self_host)}

for reqs in (50_000, 2_000_000, 20_000_000):
    print(f'{reqs:>10,} req/mo ->', monthly_comparison(reqs, 1200, 3.0, 2.5, 1.0))

# ---------------------------------------------------------------------
# Remember: Self-hosting costs run whether or not traffic does. Spiky workloads almost always favour an API.
# Common mistake: Renting a GPU 24/7 for a workload that peaks for two hours a day at 8% utilisation.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
