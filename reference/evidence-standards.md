# Evidence standards

What separates a diagnosis from an opinion is the evidence chain. These standards are not optional polish; a verdict that fails them drops a grade.

## 1. The verbatim quote rule

Every proximate cause (rung two of the ladder) quotes the actual line from the actual file, formatted:

```
EVIDENCE: <path relative to workspace root> :: "<exact span from the file>"
```

`scripts/verify.py` string-matches every `EVIDENCE:` span in a diagnosis against the named file. A quote that fails the match invalidates the diagnosis mechanically, no matter how convincing it reads. Paraphrase is not evidence. If you cannot find the line, you do not have rung two.

## 2. The provenance rule

Never accept a label in a file as truth about the world. A line that says "status: awaiting reply" is evidence that someone wrote that line, nothing more. The diagnostic move is always: how did this line get here, and when?

The canonical example (from Tom Verrilli, Lenny's Podcast): a growth meeting writes off a result as fraud. How do you know? It is labeled fraud in the data set. Do you know how it gets labeled? Nobody in the room does. The label was standing in for a chain of custody no one had checked. Workspaces are full of such labels. Trace them.

## 3. Git as the timeline instrument

Three timestamps decide most State-family cases:

1. When did reality change? (owner testimony, external artifacts)
2. When was the file last touched? (`git log -1 --format=%as -- <path>`, `git blame` for the specific line)
3. What ran in between? (session commits, wrap-up commits, ritual runs)

If reality changed after the last touch and no ritual targets the file, Stale Canon is confirmed, and the ritual gap is the root-cause lead. Workspaces without git get mtime, labeled as the weaker instrument it is.

## 4. Truth-status ladder (for claims found in the workspace)

When tracing a claim, classify how it entered the record:

- **known**: third-party verifiable at time of writing, anchor present.
- **inferred**: reasoned from known facts; the reasoning is in the record.
- **speculative**: plausible, unanchored; a guess that got written down.

"No anchor" is itself a finding (see Unanchored Claim Hardening). Adapted from Bonnitta Roy's FAST discipline.

## 5. Confidence grades (for the Doctor's own verdicts)

- **Confirmed diagnosis**: full chain present. Verbatim quote, dated timeline, classified mode, neighbors ruled out via the differential columns.
- **Working hypothesis, high**: one chain link missing, everything else points one way. Flip condition named.
- **Working hypothesis, medium**: mode family is clear, mode is not; or intake incomplete after anamnesis. Flip condition named.
- **Working hypothesis, low**: pattern recognition only. Stated as such, never dressed up. Flip condition named.

The flip condition is mandatory at every hypothesis grade: exactly what evidence would confirm or kill this. A verdict nothing could change is a commitment, not a verdict.

## 6. The shadow organ: assistant memory

Many owners run their workspace with an assistant whose persistent memory is on. That memory is a second state store the X-Ray cannot image, and it cuts both ways: it can mask decay (right answers from stale files, memory compensating) and it can cause failures the workspace never produced (a stale remembered fact overriding a correct file). Intake should record whether memory was active when the failure happened. If the trace shows every file the model could read was correct and the bad fact lived in memory, that is a quiet-case verdict: the workspace is not the cause.

## 7. Receipts

When a consult is preserved (in `tests/` or the owner's records): transcripts verbatim, errors kept in. A receipt that has been cleaned proves nothing.
