"""Day 05 — Objects, errors and clean code
Concept 10: Writing code your future self can read

Run:  python 10_writing_code_your_future_self_can_read.py
"""

from dataclasses import dataclass, field

@dataclass
class TrainConfig:
    lr: float = 1e-3
    epochs: int = 10
    tags: list[str] = field(default_factory=list)   # never a bare []

    def __post_init__(self):
        assert self.lr > 0, 'learning rate must be positive'

cfg = TrainConfig(lr=3e-4, epochs=5)
print(cfg)

# ---------------------------------------------------------------------
# Remember: In a dataclass, mutable defaults need `field(default_factory=...)`, not a literal.
# Common mistake: Building a five-level inheritance hierarchy for what a dict and two functions would have solved.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
