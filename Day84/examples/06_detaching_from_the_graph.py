"""Day 84 — PyTorch fundamentals
Concept 6: Detaching from the graph

Run:  python 06_detaching_from_the_graph.py
"""

# Requires: pip install torch  (does not run inside the browser sandbox)
import torch
import torch.nn as nn

model = nn.Sequential(nn.Linear(4, 16), nn.ReLU(), nn.Linear(16, 1))
opt = torch.optim.AdamW(model.parameters(), lr=1e-3)
loss_fn = nn.MSELoss()

X = torch.randn(64, 4)
y = torch.randn(64, 1)
for step in range(50):
    opt.zero_grad()                # 1. clear old gradients
    pred = model(X)                # 2. forward
    loss = loss_fn(pred, y)        # 3. loss
    loss.backward()                # 4. backward
    opt.step()                     # 5. update
print('final loss', round(loss.item(), 4))

# ---------------------------------------------------------------------
# Remember: `opt.zero_grad()` first, every step. PyTorch accumulates gradients by design.
# Common mistake: Calling `loss.backward()` twice without `retain_graph` and getting a confusing runtime error.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
