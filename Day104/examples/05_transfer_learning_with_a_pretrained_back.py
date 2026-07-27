"""Day 104 — PROJECT: deep learning image classifier
Concept 5: Transfer learning with a pretrained backbone

Run:  python 05_transfer_learning_with_a_pretrained_back.py
"""

# Requires torch + torchvision
# import torchvision.models as models, torch.nn as nn
#
# model = models.resnet18(weights='IMAGENET1K_V1')
# for p in model.parameters():
#     p.requires_grad = False          # freeze the backbone
# model.fc = nn.Linear(model.fc.in_features, 3)   # 3 of your classes
# # only model.fc trains -> works with a few hundred images
print('Transfer learning: freeze backbone, replace head, train head, then unfreeze at low LR.')

# ---------------------------------------------------------------------
# Remember: Use the exact normalisation statistics the pretrained model was trained with.
# Common mistake: Fine-tuning the whole network at 1e-3 and washing away everything ImageNet taught it.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
