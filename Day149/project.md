# Day 149 PROJECT — fine-tuned domain assistant

A project is not a bigger exercise. It is the part where nobody tells you the
shape of the answer. Build the thinnest end-to-end version first, then thicken it.

## Milestones

1. **Goal: a small model specialised to one task**
2. **Collecting and curating examples**
3. **Formatting an SFT dataset**
4. **Choosing base model and LoRA settings**
5. **Training run and monitoring**
6. **Evaluating against the base model**
7. **Comparing against a prompted large model**
8. **Cost and latency comparison**
9. **Deciding whether tuning was worth it**
10. **Packaging the adapter**

## Definition of done

- [ ] Runs end to end from a single command on a clean checkout.
- [ ] Has a README stating the problem, the metric, and the result.
- [ ] Beats a stated baseline — and the baseline number is written down.
- [ ] Every random source is seeded; a rerun reproduces the number.
- [ ] At least one test that fails if the core logic breaks.
- [ ] Limitations section that is honest about what it cannot do.

## How to avoid the usual trap

The usual trap is spending week one on infrastructure and week four discovering
the data cannot answer the question. Invert it: on day one, get the dumbest
possible version working end to end — hard-coded paths, one file, terrible
accuracy. That version tells you whether the project is possible at all.
Everything after that is improvement, and improvement is easy to schedule.

## Stretch goals

- Serve it behind an HTTP endpoint.
- Add a monitoring script that would catch it silently degrading.
- Write it up as a post someone outside your team could follow.
