# Day 15 PROJECT — dataset explorer CLI

A project is not a bigger exercise. It is the part where nobody tells you the
shape of the answer. Build the thinnest end-to-end version first, then thicken it.

## Milestones

1. **Framing the tool: what question does it answer**
2. **Loading any CSV robustly**
3. **Auto-detecting column types**
4. **Null and cardinality report**
5. **Summary statistics per column type**
6. **Correlation with the target column**
7. **Generating plots to a folder**
8. **Command-line arguments with argparse**
9. **Writing a markdown report file**
10. **Packaging and reusing the tool**

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
