"""Day 01 — Setting up your AI workbench
Concept 7: Google Colab and free GPUs

Run:  python 07_google_colab_and_free_gpus.py
"""

import os

def on_colab():
    return 'COLAB_GPU' in os.environ or os.path.exists('/content')

print('running on Colab:', on_colab())
print('''
Colab survival rules:
  1. Save checkpoints to Drive, not /content — /content is wiped.
  2. Re-run the pip install cell after every reconnect.
  3. Check the GPU you were given: !nvidia-smi
  4. Long jobs get disconnected. Checkpoint every epoch.
''')

# ---------------------------------------------------------------------
# Remember: Anything not saved outside /content is gone when the runtime recycles. Checkpoint every epoch.
# Common mistake: Training for four hours in Colab with no checkpointing and losing everything to a disconnect.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
