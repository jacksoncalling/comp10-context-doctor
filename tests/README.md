# Test method

**Written 2026-08-04, before any run was executed.** This file declares the method first so the receipts are evidence, not a highlight reel.

## The split

Everything outside `tests/` is the product. Everything inside `tests/` is evidence about the product. The Doctor is instructed (rules.md step 10) never to read this folder, so it never sees its own test material.

## Method

1. **Runtime.** Each run is a fresh Claude session loaded with only the product files (README, identity, rules, examples, reference/, scripts/). No `tests/` content, no conversation history, and no persistent-memory features: the run executes in a context that receives no auto-memory injection (a spawned subagent, or a session with memory off). Auto-memory is prior context, and prior context contaminates a cold run.
2. **Inputs.** Each run gets a real intake: symptom artifact, ground truth as the owner states it, and workspace access. Constructed inputs are labeled CONSTRUCTED and are used only to demonstrate mechanics, never presented as consults.
3. **Preservation.** Transcripts are pasted verbatim and never edited. Errors, dead ends and wrong turns stay in. A cleaned receipt proves nothing.
4. **Assumption.** The Doctor made at least one mistake per run. Part of each run's writeup is looking for it and naming it, or stating that we looked and did not find it.
5. **Verification.** Every diagnosis produced in a run is checked with `python scripts/verify.py <diagnosis> <workspace>` and the checker output is committed beside the transcript.
6. **Answer keys.** Where an independent ground truth exists for the correct diagnosis, it is committed to the run folder BEFORE the run executes, so the run is falsifiable.

## Planned runs

| Run | Input | Status | Answer key |
|---|---|---|---|
| run-1 | The builder's own comp 9 competition repo (`comp9-editor`), symptom: "judges could not tell what the entry point was; the build read as three specialists where one was asked for" | **executed 2026-08-04, passed** (see `run-1/findings.md`) | The official judge feedback, committed before the run. It names the causes independently; the run tests whether the Doctor finds them without seeing it. |
| run-2 | The builder's live HQ (`step-into-more`), symptom: "I can't find certain projects; some have multiple saved locations; I open the home folder usually" | **executed 2026-08-05, passed** (see `run-2/findings.md`) | None (real consult). Falsifiability via a pre-committed builder hypothesis; the cold run diverged from it and named a better-argued primary (B3 over B1). Real names retained locally per owner; redaction gate before any public push. |
| run-3 | The builder's job-application system (an ordinary non-meta domain), symptom: "my internal HR and team-lead reviewers approve the package, but real applications get rejected at the first round" | **executed 2026-08-07, passed** (see `run-3/findings.md`) | None (real consult). Pre-committed builder hypothesis; the cold run converged and sharpened it (A3 Expensive Write-Back, not "no organ"). 11/11 verified. Anonymized to roles before commit. |

## Labels

- **REAL**: an actual consult on a workspace with a failure that actually happened.
- **CONSTRUCTED**: built to demonstrate a mechanism, labeled as such.
- **ILLUSTRATIVE**: teaching material in `examples.md`, never presented as a run.
