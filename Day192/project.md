# Day 192 PROJECT — predictive system

A project is not a bigger exercise. It is the part where nobody tells you the
shape of the answer. Build the thinnest end-to-end version first, then thicken it.

## Milestones

1. **Problem framing and metric**
2. **Data acquisition and validation**
3. **EDA and leakage audit**
4. **Baseline and iteration log**
5. **Model selection with honest CV**
6. **Error analysis and targeted improvement**
7. **Calibration and threshold choice**
8. **Packaging and serving**
9. **Monitoring plan**
10. **Write-up with results and limitations**

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
