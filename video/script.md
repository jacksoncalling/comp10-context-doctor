# Demo script — The Context Doctor

**Target length: about 1:45.** No voiceover, text on screen only. Companion to `brief-for-lovable.md`: the brief is what Lovable builds; this is the beat sheet, the real-content sources, and the capture-and-production notes.

**Tone:** plain, clinical, unhurried. The pace of someone reading a scan carefully, not a product launch. The tool is a careful diagnostician; a frantic demo would contradict its own subject.

**The spine (say it in one line):** here is your system as an image, here is the lens I read it through, here is the exact line that caused the wrong answer, here is the one cause, and I stop without fixing it.

---

## Beat sheet

| # | Time | Beat | The point |
|---|---|---|---|
| 1 | 0:00–0:10 | The problem | Your system lied to you, confidently, and you could not see why. |
| 2 | 0:10–0:20 | The intake | Three inputs: the wrong answer, the ground truth, the workspace. |
| 3 | 0:20–0:42 | The X-Ray | A descriptive image of the workspace. Counts, dates, duplications. **No judgments.** |
| 4 | 0:42–1:02 | The mental model | The lens, shown in full: the KNOW / KEEP-TRACK / drift fork, the three families and ten modes, the three-rung ladder. No black box. |
| 5 | 1:02–1:24 | The trace | The ladder walked on real evidence. Every proximate cause is a quoted line, checked against the file. |
| 6 | 1:24–1:40 | The turn | One primary cause, graded honestly (a working hypothesis, not a certainty). Then a "fix" types itself and deletes itself. It names the cause and stops. |
| 7 | 1:40–1:52 | Close | Folder tree, one real receipt line, the ICM tagline, the repo. |

The exact on-screen text for every beat lives in `brief-for-lovable.md`. Do not paraphrase it; the wording is load-bearing (especially the "no judgments" line in beat 3 and "would confirm it" in beat 6).

---

## What is real vs. animated

The comp 9 rule was "screen-record the real tool, do not rebuild a prettier fake." Same spirit here, adapted to a tool whose surfaces are a terminal and a document:

- **Beat 3, the X-Ray:** use the **real** `xray.py` output. It is already the demo's strongest asset because it is genuine and unglamorous. Generate it and paste the actual text into Lovable so the frame shows real structure, not lorem ipsum:
  ```bash
  python scripts/xray.py ./path/to/an/anonymized/workspace
  ```
- **Beat 4, the mental model:** drawn from `reference/failure-modes.md` (the three families and ten modes) and `rules.md` (the fork and the ladder). This is a diagram of the method, animated. It is the one beat that is a designed surface, and that is fine, because it is showing a map, not faking a UI.
- **Beat 5, the trace:** use **real** `EVIDENCE` lines and their green checks from a real `verify.py` run. The "not found" strike-through line is invented on purpose, to show what failing the check looks like; label it clearly in your own notes so no one thinks it is a real miss.

---

## Anonymization check (do this before exporting)

Every legible frame must show **roles only**: `prospect-a`, `partner-l`, "the owner", "the workspace". Never a real person or company. The run-2 material is already anonymized, so pull on-screen content from the committed, anonymized files, not from the live HQ. Pause on every frame where text is readable and read it before you export. One real name on screen fails the confidentiality bar the whole entry is built on.

---

## Two production notes

**Descriptive before evaluative, on screen too.** Beat 3 must contain zero judgment words. The amber underline on `identity.md x7` is the only foreshadow allowed, and it carries no label. All judgment waits for beat 6. This is not a style choice; it is the tool's own imaging rule, applied to its own trailer. If the trailer breaks the rule the tool enforces, the entry undercuts itself.

**The turn is the whole thing. Give it room.** The self-deleting "fix" in beat 6 is the single strongest moment, the same slot the comp 9 video used for its self-deleting rewrite. Do not cut away early. The empty line after the deletion sits for a full second before "It names one cause. It does not fix it." A diagnostician that refuses to prescribe is the entire idea; the pause is where a viewer feels the discipline instead of being told about it.
