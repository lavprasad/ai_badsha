"""Day 167 — Latency engineering
Concept 9: Measuring p50, p95, p99

Run:  python 09_measuring_p50_p95_p99.py
"""

# Effective batch = per_device_batch * n_devices * grad_accum_steps
per_device, devices, accum = 8, 4, 4
print('effective batch size', per_device * devices * accum)
print('\\nGradient accumulation gives a large effective batch on small memory:')
print('  for i, batch in enumerate(loader):')
print('      loss = model(batch).loss / accum')
print('      loss.backward()')
print('      if (i + 1) % accum == 0:')
print('          opt.step(); opt.zero_grad()')

# ---------------------------------------------------------------------
# Remember: Profile first. GPU at 30% utilisation means the bottleneck is the data pipeline, not the GPU.
# Common mistake: Scaling the learning rate wrongly when you scale the batch — a larger batch usually needs a larger LR.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
