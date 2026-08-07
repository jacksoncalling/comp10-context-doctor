# The Context Doctor

**This folder is the diagnostician. Drop it into a Claude project and it becomes The Context Doctor.**

It diagnoses one thing: why a folder-based AI workspace that used to give good answers has started giving wrong, stale, or generic ones.

**Watch the demo:** https://youtu.be/3X9Ed_CMAPs

## Folder systems are grown, not built

A folder system is alive. You start with a need and a rough idea of how to meet it, you build the folders, and then reality shows you where the thinking was thin. So you adapt. It grows with the work, organically, the way real systems in real organizations grow. Nobody gets to stand outside their own system and one-shot a perfect one.

So the real work was never the first build. It is keeping the system in tune with the need and the world as both keep moving. That is the job this tool exists to support.

## The failure it works backward from

You built a folder system (a Claude project, an ICM workspace, a "second brain") so an AI assistant could work inside your world. It worked. Then one day:

- It confidently told you something that stopped being true three weeks ago.
- Its plan ignored a decision you already made and logged.
- Your specialist used to sound like a discipline and now sounds like a brochure.
- Two sessions gave two contradicting answers to the same question.

Something already broke in the real world. The Context Doctor tells you why it broke. Not how to fix it. Why it failed.

## What to feed it

Three things make a complete intake:

1. **The symptom artifact.** The wrong output, verbatim. A transcript excerpt or the quoted answer.
2. **The ground truth.** What was actually true, and roughly since when.
3. **The workspace.** The folder the assistant was reading. Git history included if it exists.

Missing one or two? Bring what you have. The Doctor does not turn patients away; it takes a history (see "anamnesis" in `rules.md`) and tells you honestly what grade of verdict the evidence supports.

It also helps to say what the workspace was meant to do. Before sorting the failure, the Doctor establishes the system's purpose, and it follows Stafford Beer here: the purpose of a system is what it does. So it reads the purpose from how the workspace actually behaves, then measures that against what you set it up to do. Often the failure lives in that gap, a structure quietly doing something other than the job it was built for, and naming the gap is the first real move of the diagnosis.

## How to use it

1. Create a Claude project (or Claude Code session) and add this folder.
2. Instruction string: `Read identity.md and rules.md, then follow them. You are The Context Doctor.`
3. Give it the intake (above). Point it at your workspace folder.
4. Optionally run the imaging script yourself first and paste the result:

```bash
python scripts/xray.py /path/to/your/workspace
```

5. You get back: a Topological X-Ray of your workspace (descriptive imaging, shown to you like a doctor shows a patient the scan), then ONE named primary cause with the evidence chain that led there, graded either **confirmed diagnosis** or **working hypothesis** with a confidence level and the evidence that would settle it.

Then it stops. No fixes, no rewrites, no "try this instead."

## What is in the folder

| File | Job |
|---|---|
| `identity.md` | Who the Doctor is, what it diagnoses, what it refuses |
| `rules.md` | The method: intake, imaging, differential, evidence chain, verdict grades |
| `examples.md` | Worked diagnoses showing the reasoning, including a bad-vs-good pair and a quiet case |
| `reference/failure-modes.md` | Ten named failure modes in three families, with differential columns |
| `reference/evidence-standards.md` | Quote rule, provenance rule, git timeline, truth-status and confidence grades |
| `reference/analytical-vs-operational.md` | The first differential question and where it comes from |
| `scripts/xray.py` | Mechanical imaging: a descriptive census of the workspace |
| `scripts/verify.py` | Checks every quoted evidence span in a diagnosis against the workspace files |
| `tests/` | **Evidence about the product, not the product.** Cold-run receipts. The Doctor never reads this folder. |

The product/tests split matters: the files above the line are what you load; `tests/` exists so a stranger can check the Doctor rather than believe it.

## Who it is for

Anyone running a folder-based AI workspace: Claude projects, ICM builds, CLAUDE.md-driven repos, agent teams coordinating through shared files. If you have ever asked "why did my system just lie to me," this is for you.

## Why maintenance, not rescue

As AI systems get more entangled in producing the next version of themselves, the human role can quietly shrink to consumption, reaction, and governance after the fact. Bonnitta Roy calls the answer a human-recursion loop: the disciplined habit of watching how your own instruments are shaping what you believe, testing that against reality, and repairing them when they drift. This tool is one small instrument of that loop. It treats maintenance not as a failure to have built the thing right the first time, but as the attentive attunement that any living system needs to stay in contact with the world. It diagnoses and then stops, precisely so the repair, and the understanding that comes with it, stay yours. You stay in the loop.

## Sources and honest scope

Three lineages, cited where they are used rather than decoratively:

- **Kyle Bird** (Platform Designer, Dotwork) for the analytical vs operational context distinction, which drives the Doctor's first differential (`reference/analytical-vs-operational.md`).
- **Bonnitta Roy** for the drift checks in Family C and the contact discipline behind `verify.py`, adapted from her AuditEdit and FAST practices (see `reference/failure-modes.md`, and her essay "Learning With the Machine That Learns From Us," bonnittaroy.substack.com, 2026).
- **Stafford Beer** for the purpose test in step 2b: the purpose of a system is what it does. The Doctor reads a workspace's purpose from how it behaves and measures that against what it was set up to do (`rules.md`).

What we took from Roy is deliberately narrow, and saying so is part of the discipline she teaches (she names decorative borrowing of a framework's vocabulary as a failure mode in its own right). The Context Doctor is an instrument-not-content auditor, like AuditEdit, and it keeps FAST's demand for contact with evidence (every claim carries a verifiable quote). Of her three practices we carry FAST (that quote discipline) and AuditEdit (the Family C drift checks, and the reflexive audit logged in `tests/audit-ledger.md`); OntoEdit we carry only in its minimal form, the level calibration in `rules.md` step 2b that asks what a workspace is for and whether its trouble is mechanical or an altitude mismatch, not her full first-order analysis across levels. It does **not** implement her full recursive-evaluative-learning loop: it stops at the diagnosis and refuses the repair, so the human stays the one who changes the system; there is no repair script, no retest cycle, and no community evaluative field here. That is a choice, not an oversight. It also foregrounds architectural drift (duplicated truth, entry ambiguity, stale canon) over the purely interpretive drift (mirroring, flattery, metaphor-as-explanation) that is Roy's signature concern; those interpretive modes live in Family C but have not yet driven a run.

## Where a judge should push

- The X-Ray could drift into an audit checklist. Check that every X-Ray in `tests/` is purely descriptive and every verdict names exactly one primary cause.
- The quote discipline is only as good as `verify.py`. Run it against any receipt in `tests/` and try to sneak a fabricated quote past it.
- Hypothesis-grade verdicts could be used to dodge rigor. Check that every one names its flip condition: the evidence that would confirm or kill it.
