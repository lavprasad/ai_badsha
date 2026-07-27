"""Day 95 — Generative adversarial networks
Concept 10: Reading GAN samples, not GAN losses

Run:  python 10_reading_gan_samples_not_gan_losses.py
"""

# Minimax intuition, no framework needed
# generator loss  : make D(fake) high
# discriminator   : D(real) high, D(fake) low
real_score, fake_score = 0.9, 0.2
d_loss = -(0.5 * (real_score) + 0.5 * (1 - fake_score))
g_loss = -(fake_score)
print(f'discriminator loss {d_loss:.3f}  generator loss {g_loss:.3f}')
print('Balance is everything: if D wins outright, G gets no usable gradient.')

# ---------------------------------------------------------------------
# Remember: Watch samples, not the loss curves — GAN losses are not a progress signal.
# Common mistake: Letting the discriminator get too strong too early, which starves the generator of gradient.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
