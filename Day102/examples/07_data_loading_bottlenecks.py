"""Day 102 — Hardware and performance
Concept 7: Data loading bottlenecks

Run:  python 07_data_loading_bottlenecks.py
"""

def training_estimate(samples, epochs, samples_per_sec, gpu_cost_per_hour):
    steps = samples * epochs
    hours = steps / samples_per_sec / 3600
    return {'hours': round(hours, 2), 'cost': round(hours * gpu_cost_per_hour, 2)}

print(training_estimate(samples=1_200_000, epochs=3, samples_per_sec=850, gpu_cost_per_hour=2.5))
print('If GPU utilization < 60%, fix the data pipeline before scaling hardware.')

# ---------------------------------------------------------------------
# Remember: Profile before you scale. A slow `__getitem__` wastes more money than a small GPU.
# Common mistake: Renting four GPUs to fix a bottleneck that was a single-threaded JPEG decode.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
