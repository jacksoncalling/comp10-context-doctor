# Run 1 answer key (committed BEFORE the run)

**Provenance.** Run 1 was scored against the official judge feedback for the builder's Comp 9 entry (`jacksoncalling/comp9-editor`, judged at commit `afc5574`), received by the builder in August 2026. That feedback is the independent ground truth for what was actually wrong with that workspace. The Doctor never sees this file; the run tests whether it reaches the same causes on its own.

**Redaction note.** The judges' feedback is intentionally not reproduced here. It is their writing, and the owner chose not to republish their words in a public repo. What follows is the owner's own summary of the causes that feedback named, stated in the Doctor's taxonomy so the run stays falsifiable. The verbatim feedback remains in the owner's private records; a judge who wants to check convergence can compare against the original they wrote.

**The causes the feedback named (owner's summary, for scoring):**

1. **Entry unresolved.** Nothing in the repo settled which folder a stranger should open first.
2. **Truth duplicated.** The editor's identity was defined in more than one place at once (`identity.md`, `rules.md`, and `examples.md` recurring across `commons/`, `commons/ranger/`, and `editor/`), so a model reading the repo loads several competing definitions instead of one.
3. **The one-tier fix.** The correction was to collapse to a single folder with a single identity file. The underlying mechanism was sound; the structure had scattered it into what read as multiple specialists where the brief asked for one.

In the Doctor's taxonomy, the expected findings are Entry Ambiguity (B3) and Duplicated Truth (B1), with the run's open question being which the Doctor names primary and how it justifies the ranking.
