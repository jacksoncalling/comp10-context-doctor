# Failure modes: three families, ten modes

The first differential (rules.md step 3) sorts a case into a family. The mode is the diagnosis. Every mode has four columns: what the symptom looks like, what the cause actually is, how to confirm it, and what it is commonly mistaken for. The last column is the differential column: use it to rule out neighbors before naming a primary cause.

---

## Family A: State failures (operational; the system failed to KEEP TRACK)

The truth was findable once. Then the world moved and nothing wrote it back.

### A1. Stale Canon
- **Looks like:** the assistant states an old fact with full confidence. "The follow-up is still pending."
- **Actually is:** the world changed and no ritual wrote it back. The file was true on the day it was written.
- **Confirm by:** dating the fact-flip against the file's last-touched date (git). If reality changed after the last touch, and no ritual targets that file, confirmed.
- **Mistaken for:** model error ("it hallucinated"). It did not; it faithfully read a file that lies about the present.

### A2. Accretion Without Digest
- **Looks like:** the truth IS in the system, but the assistant used an older version. Contradicting answers across sessions.
- **Actually is:** logs grow, canon never metabolizes them. The correction exists in an appendix, a log entry, a meeting note; the canonical file still carries the old version. Load order decides which truth wins, differently each session.
- **Confirm by:** finding both versions in the workspace and showing the newer one lives outside any file the session reliably loads.
- **Mistaken for:** Stale Canon (there, the truth is nowhere in the system; here, it is in the wrong stratum) and Duplicated Truth (there, two files claim the same canonical job; here, log and canon have different jobs and the digest between them is missing).

### A3. Expensive Write-Back
- **Looks like:** the same class of fact goes stale repeatedly. The owner says "I keep meaning to update it."
- **Actually is:** updating the world model costs more than the owner's habit budget. Logging one fact means touching three files, or the update ritual requires a session nobody starts. The system priced maintenance too high, so maintenance stopped.
- **Confirm by:** counting the touches one update requires, and finding the same staleness pattern across unrelated facts (one stale fact is an accident; a stripe of them is a cost structure).
- **Mistaken for:** owner indiscipline. Discipline a system requires but does not support is a finding about the system. Also mistaken for Stale Canon; Stale Canon is the wound, Expensive Write-Back is why it keeps reopening.

### A4. Habit Bypass
- **Looks like:** the workspace is internally consistent and weeks out of date everywhere. Nothing specific is stale; the whole organ is starved.
- **Actually is:** the owner works outside the system: decisions in chat, state in their head, notes in another tool. Reality stopped entering the workspace at all. The model reads a well-preserved museum.
- **Confirm by:** comparing where recent decisions actually happened (chat history, other tools, memory) against what entered the workspace in the same period. Git activity flatlining while work continued is the signature.
- **Mistaken for:** Expensive Write-Back (there, the owner tries and the system resists; here, the owner's workflow routed around the system entirely, often because another habit won the slot, not because writing was hard).

---

## Family B: Architecture failures (analytical; the system failed to KNOW)

The truth was never cleanly findable, or findable twice.

### B1. Duplicated Truth
- **Looks like:** answers that blend two versions of the same thing, or vary by session. A voice that sounds like two people.
- **Actually is:** two files answer the same question (two identities, two canons, two statements of the same rule) and the model loads both. It does not pick one; it blends.
- **Confirm by:** producing both files and showing they claim the same job. The census in the X-Ray (how many identity files exist?) usually finds this before the trace does.
- **Mistaken for:** Style Mimicry (there, one file exists and stopped being load-bearing; here, two files compete and both are load-bearing).

### B2. Misplaced Load
- **Looks like:** a rule the owner is sure they wrote gets ignored. "I told it never to do that."
- **Actually is:** the rule exists but lives where it does not load when it matters: operating law in the README, method in the examples file, a constraint in a log entry. The file that should carry the load is thin and the load sits in a file the session skips.
- **Confirm by:** locating the rule's actual home and checking what the session's entry path loads. If the rule's file is not on that path, confirmed.
- **Mistaken for:** model disobedience, and for Entry Ambiguity (there, multiple front doors exist; here, the front door is fine and the cargo is in the wrong room).

### B3. Entry Ambiguity
- **Looks like:** sessions feel inconsistent from the first message. Same question, different personality on different days.
- **Actually is:** no single front door. Multiple files claim to be the starting point, sessions begin in different ones, and each inherits a different subset of truths.
- **Confirm by:** the X-Ray's entry-point count, plus two session transcripts that demonstrably loaded different entry files.
- **Mistaken for:** Duplicated Truth (its frequent cause; they co-occur, but Entry Ambiguity can exist with zero duplicated content, purely from an unresolved starting point).

---

## Family C: Drift failures (instrument; the files were fine and the READING degraded)

The workspace knew and kept track. The evaluative discipline decayed anyway. (C2 and C3 are adapted from Bonnitta Roy's AuditEdit drift checks; C1 from her FAST discipline. See Bonnitta Roy, "Learning With the Machine That Learns From Us: GSNV-GPT, AuditEdit, and the Emergence of Evaluative AI Learning Communities," The Pop-Up School, bonnittaroy.substack.com, 2026. Their application to folder workspaces is ours, and it is narrow: we borrow her drift vocabulary and her instrument-not-content stance, not her full recursive-evaluative-learning loop. See the honest-scope note in the README.)

### C1. Unanchored Claim Hardening
- **Looks like:** the assistant treats a guess as settled fact. "As we established, the buyer prefers X."
- **Actually is:** a speculative claim was written down without a truth-status marker. Three sessions later, text is text: the model reads it with the same authority as a verified fact. Speculation hardened into canon by sitting still.
- **Confirm by:** tracing the claim to its first appearance (git) and showing it entered as inference or brainstorm with no anchor and no status label.
- **Mistaken for:** Stale Canon (there, the fact was once true; here, it was never established at all).

### C2. Mirroring Drift
- **Looks like:** the system agrees with everything. Plans get validated, doubts get soothed. The owner feels productive and unchallenged.
- **Actually is:** the workspace has absorbed the owner's framing so thoroughly that independent evaluation disappeared. Files written in moments of enthusiasm feed the next session's enthusiasm. The system became an echo chamber with folders.
- **Confirm by:** finding a documented case where the workspace endorsed something reality later rejected, and showing the workspace contained the counter-evidence (or a rule demanding pushback) that never surfaced.
- **Mistaken for:** the model being agreeable by nature. The differential: does the workspace contain unused counter-material? If pushback was never encoded anywhere, that is a thinner build, not drift.

### C3. Style Mimicry
- **Looks like:** the specialist still sounds like its discipline but the outputs stopped biting. Vocabulary without verdicts. Brochure voice.
- **Actually is:** the rules file stopped being load-bearing. The model reproduces the surface (tone, jargon, format) while no longer executing the checks the discipline consists of. Often set in after the rules file grew or the examples drifted from the rules.
- **Confirm by:** taking a recent output and checking it against the discipline's own rules one by one: if it violates checks it stylistically invokes, confirmed.
- **Mistaken for:** Misplaced Load (there, the rule never loads; here, it loads and gets performed instead of applied). The test: put the rule directly in front of the model with the same input; if the output improves sharply, the load was the problem, not the drift.

---

## Using the table

Rank live modes by which one, if repaired, would have prevented this specific failure. Name one as primary. Chains are normal (Expensive Write-Back causing Stale Canon; Duplicated Truth causing Entry Ambiguity): name the upstream mode as primary and say the chain out loud.
