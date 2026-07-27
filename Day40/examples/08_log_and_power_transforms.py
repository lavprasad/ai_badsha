"""Day 40 — Encoding and scaling
Concept 8: Log and power transforms

Run:  python 08_log_and_power_transforms.py
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
