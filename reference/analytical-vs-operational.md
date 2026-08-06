# The first differential: analytical vs operational context

The Doctor's first question after imaging is: **did the system fail to KNOW, or fail to KEEP TRACK?** This file explains why that question sorts almost every case.

## Two jobs that look like one

"Context" gets used as one word for two different jobs.

**Analytical context** exists so a system can understand: reference material, canon, explanations, the organized knowledge needed to answer questions well. Its quality is measured by whether the right information is findable, singular, and trustworthy at read time. This is retrieval territory, and it is the part most folder builders think about.

**Operational context** exists so a system can act over time: state, memory, identities of the things being managed, an understanding of what changed since Tuesday. Its quality is measured by whether the representation still matches the world after the world moves. This is not better retrieval; it is a different job with different architecture, because it needs write-back, not just read.

(The analytical vs operational context distinction is adapted from Kyle Bird, Platform Designer at Dotwork, and his framing of the two jobs "context" is asked to do for AI systems. The application to folder workspaces is ours.)

## Why folder workspaces fail at the seam

Folder-based AI workspaces are almost always built as analytical context: canon files, reference layers, explanations. Then, because they work, they get trusted with operational jobs: lead statuses, open loops, current state, who promised what. A wrap-up ritual or a log file gets bolted on as the write-back path.

That seam, an analytical architecture carrying operational load, is where most real failures cluster:

- Facts that change (operational) stored in files designed for facts that hold (analytical): **Stale Canon**.
- A write-back path that exists but costs too much to use: **Expensive Write-Back**.
- Logs that receive state but never metabolize into canon: **Accretion Without Digest**.
- An owner whose operational life routed around the analytical building: **Habit Bypass**.

## Using the differential

- **Fail to know** → Family B (architecture): the truth was never cleanly findable, or findable twice. The repair surface is structure.
- **Fail to keep track** → Family A (state): the truth was findable once, then the world moved. The repair surface is the write-back path and its cost.
- **Neither** (the files were right and loaded) → Family C (drift): the reading degraded, not the record.

Answer it explicitly in every consult and record the answer before classifying the mode. Cases that seem to fit two families usually mean an upstream/downstream chain; the differential forces you to say which end you are treating as primary.
