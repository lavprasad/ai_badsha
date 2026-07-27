"""Day 145 — Small models and local AI
Concept 4: Running models on a laptop

Run:  python 04_running_models_on_a_laptop.py
"""

# Memory footprint by precision, for a 7B parameter model
params = 7e9
for name, bits in [('fp32', 32), ('fp16/bf16', 16), ('int8', 8), ('int4', 4)]:
    gb = params * bits / 8 / 1e9
    print(f'{name:<10} {bits:>2} bits -> {gb:6.1f} GB of weights')
print('\nPlus KV cache and activations at runtime — budget roughly 20-30% more.')

# ---------------------------------------------------------------------
# Remember: Quantise, measure quality on your own eval set, then decide. Published benchmarks are not your task.
# Common mistake: Shipping an int4 model because it fits, without ever measuring what accuracy it cost you.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
