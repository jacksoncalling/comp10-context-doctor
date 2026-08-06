# Build brief — 90-second animated demo (The Context Doctor)

Paste this whole file into Lovable. It is self-contained: the on-screen content below is real output from the tool, use it verbatim rather than inventing placeholder text.

## What to build

A **~100-second silent animation** (target 1:40, the reference ran 1:50), 1920x1080, that explains one idea: a folder-based AI workspace started giving wrong answers, and this tool takes a descriptive image of the workspace, **shows the mental model it diagnoses with**, walks that model down to the exact line that caused the wrong answer, names one structural cause, and then **stops without fixing it**.

The demo shows three surfaces in order: the **image** (what your system is), the **model** (the lens it is read through), and the **trace** (the line that connects them). Showing the model is not optional. A diagnostician whose reasoning you cannot see is just another oracle; the whole claim is that this one is legible.

No voiceover. Text on screen only. It should feel unhurried and clinical, the pace of someone reading a scan carefully. The subject is a careful diagnostician; a frantic demo would contradict its own subject.

Output: an autoplaying, loopable web page to screen-record. No controls, no scroll. One fixed frame, scenes cross-fading in sequence.

## The visual system (do not invent a mood; the tool has one)

The Context Doctor has no dashboard. Its interface is two things: a **terminal census** (monospace, sectioned, deliberately plain) and a **written consult** (a document with quoted evidence). The animation should look like those two surfaces, nothing more. It should read as *the tool running*, not as a promo for it.

### Palette (clinical, restrained)

```
--bg-dark:  #0b0d10   the problem screen (near-black)
--bg:       #f7f8fa   clinical light background
--panel:    #ffffff   card / document surface
--text:     #14171c   body text
--muted:    #6b7280   dates, secondary, "no judgments"
--line:     #e3e6ea   hairlines
--mono:     #1b1e24   terminal / evidence text
--verify:   #047857   the green check for a verified quote (earned, used sparingly)
--flag:     #b45309   amber, the duplication highlight (foreshadow, never alarm)
--verdict:  #4f46e5   the one primary cause
```

**No red anywhere.** Red reads as alarm and audit. This tool images calmly, then delivers one quiet verdict. Amber is the strongest heat allowed, and only once.

### Type

System sans for prose captions. Monospace for the X-ray census, the `EVIDENCE` lines, and the folder tree. Generous line height. Nothing larger than it needs to be.

---

## The four hard rules (read before building)

1. **No literal medical imagery.** No skeletons, no glowing scans, no stethoscopes, no hospital, no heartbeat line. The words "X-ray", "diagnosis", "consult" are labels that do real work (a descriptive census, one named cause, a written finding). The moment they become decoration, the demo fails the exact discipline the tool is about. The "X-ray" on screen is *text*.
2. **Descriptive before evaluative.** Scene 3 (the X-ray) must contain **zero** judgment words: no "wrong", "bad", "error", "problem", "messy". It is counts, dates, and structure only. Judgment happens once, later, in Scene 6. If an evaluative word appears in Scene 3, that is a bug.
3. **Every name on screen is a role.** `prospect-a`, `partner-l`, "the owner". Never a real person or company. Pause on every legible frame and check.
4. **Motion is type, cards, highlights, and one self-deleting line.** No stock, no 3D, no particles, no gradients. Cards move ~20px with a 300 to 400ms ease-out. Small distances.

---

## Scenes

### 1 · 0:00–0:10 — The problem

Near-black (`--bg-dark`). Three lines, one at a time, fading in and holding. Nothing else moves.

```
Your folder system used to give good answers.
```
```
Then one day it told you something that stopped being true three weeks ago.
```
```
Confidently. In the right voice. And you could not see why.
```

### 2 · 0:10–0:20 — The intake

Cut to light (`--bg`). Three small cards settle in a row, plain:

```
the symptom          the wrong answer, word for word
the ground truth     what was actually true, and since when
the workspace        the folder it was reading
```

Caption, lower third:
```
You bring three things. The tool takes an image before it forms an opinion.
```

### 3 · 0:20–0:42 — The X-Ray (your system, as an image)

A command types itself at the top:
```
python scripts/xray.py  ./workspace
```

Then the census builds in **section by section**, ~2.5s apart, monospace, plain. This is real output; use it verbatim. Do not style it as a chart; it is a printout.

```
TOPOLOGICAL X-RAY   (descriptive imaging; contains no judgments)
files: 343   |   staleness horizon: 45 days

[entry point candidates at root]  2
[identity census]  identity.md files: 7   agent definitions: 5
[state organs]  12    oldest 2026-06-01   newest 2026-07-27
[duplicate filenames]
   readme.md     x19
   identity.md   x7
   claude.md     x9
   lead.md       x6

end of image. Interpretation happens in the consult, not here.
```

As the `[duplicate filenames]` block lands, the `identity.md   x7` row gets a single soft **amber underline** (`--flag`). No label, no arrow, no words. Just a quiet mark that something recurs. This is the only heat in the whole census.

Caption after the census completes:
```
An image first. Descriptive, no judgments.
The inside of your own system, the way a scan is shown to a patient.
```

### 4 · 0:42–1:02 — The mental model (the lens)

The census dims to ~30% and holds behind, so the model reads as laid *over* the image. Three parts build in sequence. This is the beat that makes the tool interpretable: show the whole method, not a black box.

First, the question it always asks first, as a three-way fork:
```
one question first: why did the record and the world disagree?

  fail to KNOW         the truth was never findable, or findable twice    → architecture
  fail to KEEP TRACK   the truth was findable once, then the world moved  → state
  neither              the files were fine, the reading degraded          → drift
```

Then the map it sorts into, three families and ten named modes, as a compact list:
```
A · STATE          Stale Canon · Accretion Without Digest · Expensive Write-Back · Habit Bypass
B · ARCHITECTURE   Duplicated Truth · Misplaced Load · Entry Ambiguity
C · DRIFT          Unanchored Claim · Mirroring · Style Mimicry
```

The `fail to KNOW` branch and the `B · ARCHITECTURE` row light in `--verdict`; every other line stays muted. The lens has chosen a direction, not yet a single mode.

Then the ladder it will walk, three rungs, drawn as empty slots waiting to be filled:
```
symptom          the wrong answer, quoted
proximate cause  the exact line, in the exact file, with its date
root cause       the structural reason the system let that line exist
```

Caption:
```
This is the whole method, on screen. No black box. You can check every step it takes.
```

### 5 · 1:02–1:24 — The trace (the ladder, walked)

The three empty rungs from Scene 4 now fill, top down, from the real consult. The `proximate cause` rung is where the receipts land: three `EVIDENCE` lines appear one at a time, monospace, and as each lands a green check (`--verify`) snaps in at the right, like a stamp.

```
EVIDENCE  prospect-a/CLAUDE.md :: "Current State (2026-05-05)"              ✓
EVIDENCE  pipeline/prospect-a/lead.md :: "kein Produkt, kein CEO-Pitch"     ✓
EVIDENCE  partner-l/CLAUDE.md :: "AUFGELOEST (2026-07-20)"                  ✓
```

Then one more line tries to appear, a plausible-sounding quote, and instead of a green check it gets a quiet grey **strike-through** (no red):
```
EVIDENCE  prospect-a/CLAUDE.md :: "the client already signed"        (not found)
```

Caption:
```
Every claim is a real line, quoted, checked against the file.
A convincing quote that isn't there does not pass.
```

### 6 · 1:24–1:40 — The turn (strongest beat, give it room)

The verdict card resolves, centered, one primary cause only:
```
PRIMARY CAUSE
Entry Ambiguity
one project, two front doors, and no pointer to the live one

working hypothesis · high confidence
would confirm it: one answer served from the stale copy
```

Note the grade is a **working hypothesis, not a certainty**. It does not round up. Let "would confirm it" sit visibly; the honesty is part of the point.

Then, beneath it, a suggestion begins to type itself, the thing every other tool would do:
```
Fix: merge the two folders, add a canonical pointer, and archive the
```
…and it **deletes itself**, character by character, until the line is empty. Hold the empty line for a full second.

```
It names one cause. It does not fix it.
```

Held alone, centered:
```
A tool that hands you the rewrite
teaches you nothing about your own system.
```

### 7 · 1:40–1:50 — Close

The folder tree, monospace, drawn line by line:

```
context-doctor/
   identity.md    who it is
   rules.md       how it diagnoses
   examples.md    worked diagnoses
   reference/     the failure-mode taxonomy
   scripts/       the x-ray and the quote-checker
   README.md      how to use it
```

One quiet receipt line, then the final card:
```
Pointed at a real workspace, cold, it named a cause the owner had stopped seeing.
```
```
Interpretable Context Methodology.
Folders as architecture.
Drop it in. Claude becomes the Context Doctor.
```

Then the repo, monospace, held 3 seconds:
```
github.com/jacksoncalling/comp10-context-doctor
```
End, then loop.

---

## Rules recap

- The four hard rules above are not style preferences; they are the entry. Especially: no literal medical imagery, and the X-ray scene stays purely descriptive.
- Readability over cleverness. Any text on screen must be readable in one pass at 1080p.
- If a frame makes you want to add a decorative flourish, that instinct is the drift this tool diagnoses. Cut it.
