# Day 74 PROJECT — tabular ML competition

A project is not a bigger exercise. It is the part where nobody tells you the
shape of the answer. Build the thinnest end-to-end version first, then thicken it.

## Milestones

1. **Goal: beat a strong baseline honestly**
2. **Framing and metric selection**
3. **EDA and leakage audit**
4. **Baseline: dummy then logistic regression**
5. **Feature engineering iterations**
6. **Gradient boosting with early stopping**
7. **Cross-validated model comparison**
8. **Error analysis and targeted fixes**
9. **Final model, calibrated and saved**
10. **Writing the results as a report**

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
