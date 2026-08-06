# Run 2 findings

Written after the run, against the pre-committed declaration in `README.md`. Transcript untouched in `transcript.md`; verifier receipt in `verify-output.txt` (13 evidence spans checked, 0 failed, exit 0).

## Did the cold run converge on the builder's pre-registered hypothesis?

**No. It diverged, and the divergence looks like the Doctor being more correct than the builder.**

| Pre-run hypothesis (builder, committed before the run) | Doctor (cold, no access to the hypothesis) |
|---|---|
| Primary: Duplicated Truth (B1). The same project resolves to two paths; identical identity files hide the switch. | Primary: **Entry Ambiguity (B3)**, Family B. Two project roots both claim to be the front door; the owner's habit lands on the stale one. |
| Neighbor (fail-to-keep-track) ranked below B1. | **Ruled B1 out explicitly**: B1 needs one reader to load both copies and blend them into a contradiction; here the owner opens one root exclusively and gets one self-consistent but stale version. Named **Stale Canon (A1)** as the downstream consequence, chained under B3. |

The Doctor's differential is sound, and it is consistent with run-1 rather than in tension with it. Run-1 was three `identity.md` files inside one repo that a model loads together, so the copies blend: that is B1. Run-2 is two separate folder-roots the owner opens one at a time, so nothing blends: that is B3, with staleness (A1) as what you read once you open the wrong root. Same taxonomy, correctly split on the "does a single reader load both at once" test. The builder's B1 was the looser call; the cold run applied the differential column the builder skipped.

This is the result the keyless method exists to produce: the run is not a mirror. Given the same intake and workspace, a cold Doctor reached a different, better-argued primary cause than the person who built it, and backed it with 13 verified spans.

## What the Doctor got wrong or weak (method item 4)

1. **It over-generalized `first-client-coach` into the pattern, then graded Confirmed anyway.** In its own Step 6 the Doctor noted that this home copy "was explicitly built and framed as a frozen competition submission... which reads as a deliberate snapshot rather than an accidental duplicate," which directly contradicts the owner's ground truth that "the split happened by accident." A deliberate archived snapshot is a different animal from an unmarked stale root; it may not belong in the B3 navigation-failure pattern at all. The Doctor spotted the fork and still folded all three pairs into one confirmed verdict without resolving it. Either it should have carved `first-client-coach` out as a possible non-instance, or held the grade until the owner answered. Naming the tension in an anamnesis question does not discharge it if the verdict then ignores the answer it does not have.

2. **The grade rounds up slightly.** It called the verdict a **Confirmed diagnosis** while its Step 6 Q1 leaves an load-bearing fact open: whether the owner's "open the home folder" habit means scanning file names in a file explorer (where the `partner-l` tombstone inside `CLAUDE.md` is invisible) or opening `CLAUDE.md` directly (where it is not). Whether the one existing write-back "works" depends on that answer, and it feeds the root-cause claim that markers must live at folder level. A very-high-confidence working hypothesis would have been the more honest grade for a diagnosis resting on an unconfirmed navigation mechanic. This mirrors run-1's weakness: over-trusting a reading the instrument did not fully settle.

## Instrument note (product tooling, not the patient)

`verify.py` crashed with `UnicodeEncodeError` on the first run because it prints spans through Windows' default cp1252 stdout, and the evidence quotes contain German umlauts, a middle dot, and the ⚠️ emoji. The span matching itself was unaffected (the crash is in `print`, after the match); re-running with `PYTHONUTF8=1` gave 13/0, exit 0. Recorded as a real weakness of the verifier on non-latin1 workspaces. Every span verified once the output could be encoded. **Fixed 2026-08-05:** both `verify.py` and `xray.py` now reconfigure stdout to UTF-8 at startup; `verify.py` returns 13/0 exit 0 with no environment variable, and `verify-output.txt` here was regenerated clean under the fix.

## Scope note

The run-2 intake named the home directory as a place to check for twins, so this run tested classification, evidence discipline, and the stop rule more than detection-from-scratch. Worth stating plainly so nobody reads run-2 as "it found the duplication unaided." That said, the Doctor did three things the intake did not hand it: it extended the census by hand and built the HQ-versus-home table itself, it found the `partner-l` tombstone and correctly read it as deferring rather than competing, and it surfaced the `first-client-coach` deliberate-snapshot tension against the owner's ground truth.

## Verdict on the run

Passes as a receipt: cold, memory-clean, 13/13 verified, one defensible primary cause with neighbors ruled out by their differential columns, and the stop rule held. The material openly invited a restructure (the owner had asked for one in the same session) and the Doctor named the cause and stopped. Most usefully, it did not converge on the builder's pre-registered hypothesis; it corrected it. One instrument weakness and two verdict weaknesses found and named.
