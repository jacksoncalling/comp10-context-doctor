# Run 3: the job-application system

**Declared 2026-08-07, before execution.** Method per `tests/README.md`.

- **Label:** REAL. A live job-application package system the builder actually uses. The failure is real and ongoing: the system's internal reviewers approve packages that reality rejects at the first round. This is the first run on an ordinary, non-meta domain (not an AI-about-AI system).
- **Runtime:** a fresh spawned subagent, no prior context, no auto-memory injection. Product files only; barred from `tests/`. The patient is a private folder. It has **no git history**, so the timeline instrument is filesystem mtimes (weaker), which the Doctor is told to note.
- **Intake given to the Doctor:**
  - Symptom (owner, verbatim): "The HR Screener and Team Lead specialists approve my application package, but in reality my applications rarely get past the first-round screen. Also, the cover letters often do not match my own writing tone."
  - Ground truth (owner): across roughly June to August 2026, most real applications were rejected at or before the first round, despite the internal reviewers approving them. The owner writes in German.
  - Workspace: the job-application folder, no git.
- **No answer key.** Real consult. Falsifiability via the pre-registered builder hypothesis below.
- **Pre-run hypothesis (builder, committed before the run, never shown to the Doctor):** a fail-to-keep-track failure. The system has no organ that captures real outcomes; rejections never re-enter the folder, so the reviewers grade against a calibration (`winning-patterns.md`, `evaluative-field.md`) that real results never correct. Not the reviewers being lenient (the HR Screener has real teeth). Primary candidate: the missing outcome feedback loop.
- **Anonymization gate.** The patient contains the owner's real name and real company names. The transcript and verify output are anonymized to roles **before anything is committed**, per the owner's instruction. `verify.py` is run against the real workspace first for a true receipt, then names are mapped for the committed version, with a header noting the order.
- **Preservation:** the Doctor's output is preserved verbatim (then name-mapped, no other edits). `verify.py` output committed beside it. The scoring writeup names at least one Doctor mistake and scores convergence against the hypothesis.
