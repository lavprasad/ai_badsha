"""Day 116 — Edge and mobile vision
Concept 8: On-device privacy advantages

Run:  python 08_on_device_privacy_advantages.py
"""

import torch

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print('using', device)

x = torch.randn(1000, 1000, device=device)
y = x @ x.T
print(y.shape, y.device)

if device == 'cuda':
    print('allocated MB', round(torch.cuda.memory_allocated() / 1e6, 1))

# ---------------------------------------------------------------------
# Remember: Reduce batch size first when you hit CUDA OOM; use gradient accumulation to keep the effective batch.
# Common mistake: Keeping the full loss tensor in a list each step — it holds the whole graph and leaks memory.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
