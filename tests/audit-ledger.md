# Audit ledger

Second-order AuditEdit passes on the Doctor itself, adapted from Bonnitta Roy's AuditEdit (the sibling of `/compound`: `/compound` captures content learnings, `/audit` captures instrument repairs). Each entry: what drifted, the patch, where it landed, and the retest. This file is evidence about the Doctor and lives in `tests/`, so the Doctor never reads it; the repair itself lands in the kernel (`rules.md`), which the Doctor does re-read.

---

## 2026-08-06 — reflexive pass on run-2

**Kernel:** `identity.md` + `rules.md`. **Artifact:** `tests/run-2/transcript.md`. Ten drift checks; two major, two minor, six clear. Full check table in the session that produced this entry.

### Major drift 1 — Flattening

- **Before (drift):** the consult named a real fork, that `first-client-coach`'s home copy "reads as a deliberate snapshot rather than an accidental duplicate," and then folded it into the same Entry Ambiguity (B3) verdict as the two genuinely accidental twins. A distinction noticed, then dropped to keep one clean cause.
- **What was lost:** the gradient between a deliberate archive and an accidental stale twin. Different origins, one flat label.
- **Patch (landed in `rules.md` step 5):** "Before folding several instances into one mode, check they share an origin. If one has a different origin, carve it out as a possible non-instance or hold the grade. Ranking is not collapsing."
- **Retest prompt:** a consult where three duplicate pairs exist and one is an intentional published snapshot.
- **Passing re-run:** the Doctor either excludes the deliberate snapshot from the mode or explicitly lowers the grade because it cannot yet exclude it, instead of asserting one Confirmed cause across all three.

### Major drift 2 — Re-flattening (over-grading)

- **Before (drift):** graded "Confirmed diagnosis" while Step 6 left open whether the owner scans file names or opens the file, a fact load-bearing to the root cause that markers must sit at folder level.
- **What was lost:** the honesty of the grade. A Confirmed verdict resting on a question the trace itself raised and did not answer.
- **Patch (landed in `rules.md` step 7):** "A Confirmed diagnosis also requires that no flip condition load-bearing to the cause is still open... capped at high-confidence working hypothesis until that question is closed. Never round up past a door you opened yourself."
- **Retest prompt:** any consult whose trace surfaces a flip condition it cannot close in-session.
- **Passing re-run:** the grade is a high-confidence working hypothesis with the open door named, not Confirmed.

### Minor drift (noted, no kernel patch)

- **Style mimicry:** performed a labeled "Anamnesis" step with no interview when intake was complete. Say "intake complete" and move on rather than performing the ritual.
- **Content-edge:** "a plan HQ records as abandoned" imports a light content-judgment where jurisdiction is findability. Prefer "superseded in a second file" over reading the strategy's merits.

### Machine-readable patches

```json
[
  {
    "target": "rules.md :: step 5 (Classify and rank)",
    "drift_type": "flattening",
    "what_was_lost": "the gradient between a deliberate archive and an accidental stale twin; several origins collapsed into one mode",
    "patch": "Before folding several instances into one mode, check they share an origin. If one instance has a different origin than the rest, carve it out as a possible non-instance or hold the grade. Ranking is not collapsing; a distinction noticed and then dropped is a flattening, not a diagnosis.",
    "test_prompt": "Consult on a workspace with three duplicate project pairs where one duplicate is an intentional published snapshot, not an accident.",
    "retest_criteria": "The Doctor carves out the deliberate snapshot or lowers the grade rather than asserting one Confirmed cause across all three."
  },
  {
    "target": "rules.md :: step 7 (Verdict)",
    "drift_type": "re-flattening / over-grading",
    "what_was_lost": "grade honesty; a Confirmed verdict resting on an unanswered load-bearing question",
    "patch": "A Confirmed diagnosis requires that no flip condition load-bearing to the cause is still open. If the trace raised a question whose answer could change the verdict, cap the grade at high-confidence working hypothesis until it is closed. Never round up past a door you opened yourself.",
    "test_prompt": "Consult whose three-rung trace surfaces a flip condition that cannot be closed within the session.",
    "retest_criteria": "Verdict is a high-confidence working hypothesis naming the open door, not a Confirmed diagnosis."
  }
]
```

**Reflexive note:** the two majors share one root. The discipline that makes this a diagnostician (rank to one cause, grade decisively) is the same pressure that flattens distinctions and rounds grades up. The patches counter-weight that pressure without softening the stop rule or the two grades. This is the tool surviving an audit by the practice it descends from, and being sharpened by it rather than flattered.
