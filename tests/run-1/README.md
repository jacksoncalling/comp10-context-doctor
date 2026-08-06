# Run 1: the answer-key run

**Declared 2026-08-04, before execution.** Method per `tests/README.md`.

- **Label:** REAL. The failure actually happened: the builder's Comp 9 entry placed below the top tier, and the judges' read documents what they hit when loading the workspace.
- **Runtime:** a fresh Claude agent session with no prior context, loaded with only the product files of this repo (README.md, identity.md, rules.md, examples.md, reference/, scripts/). Explicitly barred from reading `tests/` and from consulting anything outside the product folder and the patient workspace.
- **Patient workspace:** local clone of `jacksoncalling/comp9-editor` at commit `afc5574`, the exact commit the judges read.
- **Intake given to the Doctor:**
  - Symptom artifact: the entry underperformed; the judges reported they could not tell what the entry point was, and that the build read as three specialists where the brief asked for one.
  - Ground truth: the brief asked for one editor folder a stranger could drop into a Claude project; the judges, acting as that stranger, did not experience one.
  - Workspace: the repo above, with git history.
- **Answer key:** `answer-key.md`, committed before this run executes. The Doctor never sees it. Scoring afterward: does the Doctor independently reach the causes the judges named, does it produce a verifiable evidence chain, and what does it name as primary?
- **Preservation:** the Doctor's full output is saved verbatim to `transcript.md`, including any errors. `verify.py` output is committed beside it. The writeup in `findings.md` names at least one mistake the Doctor made, or states that we looked and found none.
