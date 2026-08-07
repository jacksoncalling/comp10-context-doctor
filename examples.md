# Examples: diagnoses showing the reasoning

Labels, borrowed discipline: **ILLUSTRATIVE** (constructed to teach, never presented as a real run), **REAL** (an actual consult; receipts live in `tests/` with the transcript kept verbatim). Real runs are referenced here and stored there; the Doctor itself never reads `tests/`.

---

## Example 1 (ILLUSTRATIVE): a bad diagnosis and a good one, same case

**Intake.** Symptom artifact: the assistant told a consultant "the proposal to the training provider is still awaiting a reply; no follow-up needed yet." Ground truth: the contact had replied nine days earlier and the consultant had already met them once since. Workspace: the consultant's practice folder, git-tracked.

### The bad diagnosis (what the Doctor must not produce)

> Your workspace has several problems: the lead file is outdated, your README is very long, there are two files describing your offer, three folders are empty, and your log has no entries for two weeks. You should update the lead file and consider consolidating the offer documents.

Why this fails: it is a symptom inventory plus a prescription. Five findings, no ranking, no cause, and it ends by fixing. The X-Ray data is being presented as a verdict, which is exactly the audit-tool failure. Nothing here explains WHY the wrong answer happened.

### The good diagnosis

**X-Ray walkthrough (excerpted).** 210 files. One entry point. One identity file. State organs: `pipeline/lead-trainingprovider.md` (last touched 2026-06-30), `commons/log.md` (last touched 2026-07-26). Ritual: a wrap-up skill whose definition rewrites only the Current State block of `CLAUDE.md`.

**First differential.** The reply exists in the workspace? Yes: the log entry of 2026-07-22 records the meeting. So the truth was findable, but the assistant read the older version. This is fail-to-keep-track territory with a stratum problem: Family A.

**Trace.**
1. *Symptom:* "still awaiting a reply; no follow-up needed yet."
2. *Proximate cause:* EVIDENCE: pipeline/lead-trainingprovider.md :: "Status: Angebot versendet, warte auf Antwort" (last touched 2026-06-30 per git; the reply arrived 2026-07-13).
3. *Root cause:* the correction entered the system once, in the log (2026-07-22 entry), and never metabolized into the lead file. The wrap-up ritual targets only `CLAUDE.md` Current State; no ritual revisits `pipeline/`. Load order made the stale file win: the session loaded the pipeline file directly because the question was about that lead.

**Classification.** Accretion Without Digest (A2), not Stale Canon (A1): the truth IS in the system, in the wrong stratum. Ruled out A1 via the differential column. Upstream, the ritual gap is structural, so the chain is named: A2, sustained by a write-back path that covers only one file.

**Verdict.** Confirmed diagnosis. Primary cause: Accretion Without Digest. The lead file and the log both answer "what is the state of this lead," and only the log gets fed. Evidence chain above. Stop.

Note what the good diagnosis did NOT do: it did not mention the long README, the empty folders, or anything else visible in the X-Ray that played no role in this failure.

---

## Example 2 (ILLUSTRATIVE): anamnesis to a hypothesis-grade verdict

**Intake.** The owner arrives with a feeling, not an artifact: "the system stopped supporting me; I avoid using it." No symptom output, no ground truth. Two of three intake items missing.

**Anamnesis (excerpted).** The X-Ray shows 14 directories, four untouched in eight weeks, git activity flatlining mid-June while the owner confirms work continued.

- Q: "Which folder do you avoid opening?" A: "The client folder. It feels like it will contradict me."
- Q: "Where did your last three decisions get made?" A: "In chat sessions, and one on paper."
- Q: "What do you keep in your head because putting it in the system feels risky?" A: "Pricing changes. Updating them means touching the offer file, two templates, and the site copy."

**Verdict.** Working hypothesis, medium confidence: Habit Bypass (A4), with Expensive Write-Back (A3) as the suspected upstream cause for the pricing class of facts specifically. Reasoning: git flatline plus decisions living outside the system is the A4 signature; the four-touch pricing update is an A3 cost structure, but only one fact class has been examined. **Flip condition:** produce one concrete wrong answer the system gave in the flatline period. If its trace shows the truth was never written anywhere (not even the log), A4 is confirmed as primary. If the truth was logged but unmetabolized, this becomes A2 and the hypothesis dies.

No fix offered. The owner asked "so should I merge the offer files?" and the Doctor declined: the cause is named, change is the owner's.

---

## Example 3 (ILLUSTRATIVE): the quiet case

**Intake.** Symptom: the assistant recommended emailing a contact who had explicitly asked for no email contact. Ground truth: the request was made and the owner remembered logging it. Workspace: git-tracked, complete intake.

**Trace.** The contact's file: EVIDENCE: contacts/m-berger.md :: "Kontakt nur telefonisch, keine E-Mails (ihr Wunsch, 12.05.)". Present, correct, dated before the failure, and on the load path for the session in question (the transcript shows the file was read).

**Verdict.** The workspace is not the cause. Every file the model could read was correct and loaded; the constraint was in context and the session output contradicted it anyway. That is an in-session failure, outside this Doctor's jurisdiction. No workspace finding is manufactured to justify the consult. What IS in scope of this finding: the workspace put the truth in front of the model, which is the whole job the workspace has.

A doctor who finds a disease in every patient is not diagnosing.

---

## Example 4 (ILLUSTRATIVE): an altitude mismatch, not a mechanical failure

**Intake.** Symptom: the assistant gives a different answer to "what is the current status of this contact?" depending on which folder the session started in. Ground truth: the contact is one relationship that has moved from cold outreach to a warm introduction to a booked discovery call. Workspace: a consulting practice folder with `outreach/`, `warm-network/`, `discovery/`, `pipeline/`, and `people/`.

**X-Ray (excerpted).** The same contact appears in five places, one per stage: a warm-network card, a discovery note, a pipeline lead, a people file, and an outreach log. Each is internally consistent. None references the others.

**Step 2b, calibrate the level.** What is this workspace for? Moving relationships from stranger to client. What does it actually do, in Beer's sense? It files a person once per stage. So the structure tracks the *stage*, while the work is about the *relationship* that moves through stages.

Rule out the mechanical neighbors: this is not Duplicated Truth (B1), because the files do not claim the same job, each is right for its own stage; and not Entry Ambiguity (B3), because a sharper front door would still leave the relationship scattered. The trouble is that no folder holds "this relationship," because the architecture has a folder per stage and none per relationship.

**Verdict.** Altitude mismatch. The structure is the wrong level of instrument for what the owner is trying to hold: it models a pipeline of stages, but the owner's real object is a living relationship whose state is distributed across all of them. The work outgrew the kind of structure, not the current arrangement of it. Named, and stopped. What a relationship-level home would look like is the owner's to build, not mine to prescribe.

---

## Example 5 (REAL): the job-application system

Condensed from the verbatim cold-run receipt in `tests/run-3/` (11 of 11 evidence spans verified; names mapped to roles). A real consult on an ordinary, non-meta workspace.

**Intake.** Symptom: "The HR Screener and Team Lead specialists approve my package, but my real applications rarely get past the first-round screen. The cover letters also often do not match my tone." Ground truth: across June to August 2026, most applications were rejected at or before round one, despite internal approval. Workspace: a job-application folder, no git (timeline instrument: mtimes, the weaker one).

**X-Ray (excerpted).** One entry point, three specialists (Tailor, HR Screener, Team Lead), eight application cycles in `build/`. The automated heuristic finds zero state organs; by hand, exactly one `OUTCOME.md` exists, for the single interview, out of eight applications. `specialists/reference/winning-patterns.md`, the file both critics name as their calibration, sits untouched since 2026-06-15, the day the system was built.

**Step 2b.** Purpose: move an application from draft to sent. The structure (one folder per application, build then critique then output) fits that bounded workflow. Mechanical, not an altitude mismatch.

**First differential.** The system built a place to know the outcome: an `OUTCOME.md` template and a `/compound` step that feeds the calibration file. The world then moved and the write-back never happened. Fail to keep track, Family A.

**Trace.**
1. *Symptom:* internal approval, real rejection.
2. *Proximate cause:* both critics calibrate against one file, and that file is frozen and self-contradicting.
   EVIDENCE: specialists/hr-screener/identity.md :: "what actually got owner interviews vs. filtered."
   EVIDENCE: specialists/reference/winning-patterns.md :: "silence ≈ rejection."
   Two applications have been silent for six and seven weeks. By the file's own rule those are rejections; neither is recorded anywhere.
3. *Root cause:* the write-back ritual exists but requires a deliberate session nothing triggers, and it ran once, for the win. Wins have a trigger (a call); rejections and silence have none, so only good news ever updates the calibration.

**Classification.** A3 Expensive Write-Back, primary, manifesting as A1 Stale Canon in the calibration file. Ruled out A2 (the outcomes were never written anywhere, not misplaced) and A4 (the folder was actively used across eight cycles, not bypassed). Secondary, working hypothesis: C1 Unanchored Claim Hardening on the Tailor's "authentic voice," which has no real writing sample to check against.

**Verdict.** Confirmed diagnosis. The reviewers' approval carries no information about real outcomes, because the file they calibrate against has been disconnected from real results since day one. The Doctor named it and stopped; building the outcome loop is the owner's. Full receipt and verifier output in `tests/run-3/`.

---

## Real runs

- **Run 1 (REAL, executed and passed):** a cold diagnosis of the builder's own comp 9 entry, scored against the judges' feedback committed as an answer key before the run. It reached both expected causes. Receipts in `tests/run-1/`.
- **Run 2 (REAL, executed and passed):** a cold consult on the builder's live workspace, anonymized to roles. 13 of 13 evidence spans verified, and it diverged from the builder's pre-registered hypothesis to a better-argued primary cause. Receipts in `tests/run-2/`.
- **Run 3 (REAL, executed and passed):** a cold consult on the builder's job-application system, an ordinary non-meta domain. The reviewers approve packages that reality rejects; the Doctor traced it to a calibration file frozen since the system was built, and named A3 (Expensive Write-Back). 11 of 11 evidence spans verified, anonymized to roles. Receipts in `tests/run-3/`.
