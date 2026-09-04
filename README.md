# Why is there still no agentic enterprise? Yet.

A working paper on why enterprises deployed agents everywhere and no enterprise
became agentic, and what would have to exist for that to change.

**Read it:** [`agentic-enterprise.md`](agentic-enterprise.md)
**Landing page:** https://ragnarpitla.github.io/Agentic-Enterprise/

## The argument in one paragraph

An agent is scoped to a session. Enterprise work is scoped to a commitment. A
purchase commitment made on a call in March is fulfilled by four systems over
eleven weeks, and the only durable record of it is a sentence in someone's
inbox. Every generation of this craft so far, prompt engineering through context
engineering, has assumed the unit of work fits inside a session. Enterprise
obligations outlive every session that touches them, so the next unit is not a
better session. It is a durable decision.

## What is in here

| File | What it is |
|---|---|
| `agentic-enterprise.md` | The paper. Nine hypotheses, each with a stated kill condition. |
| `census.py` | The measurement behind every number in section 5 and on the landing page. |
| `evidence-census.txt` | Output of the run cited in the paper, 4 September 2026. |
| `site/` | The landing page, served by GitHub Pages. |

## Reproducing the numbers

```
pip install tiktoken
python3 census.py
```

The script measures two agent skill libraries on the machine it runs on, so your
counts will differ. What should not differ is that it refuses to print anything
if any of its six controls fail. Two of those controls exist because earlier
versions of this measurement were wrong:

- **Control 1** catches a YAML parser that truncates multi-line descriptions to
  their first line. The truncating version passed a non-emptiness check while
  silently cutting 187 of them, which is the general lesson that a non-emptiness
  guard detects total blindness and never partial blindness.
- **Control 5** closes the set algebra. An earlier draft reported 274 shared
  names between a set of 308 and a set of 249, which is impossible. It survived
  three frontier-model reviews because all three read the reasoning and none
  re-ran the arithmetic.

Control 3 asserts a substring that was read out of the file by hand before the
assertion was written. The version before it asserted that the `de-slop`
description contains the word "slop". It does not.

## How the paper is written

As a disputation. A proposition seat states each claim at full strength and an
objection seat attacks it at full strength. Where the objection wins, the claim
is cut rather than softened; six claims from the first draft were killed
outright. Three disagreements are left unresolved because neither seat could
close them, and the strongest objection to the whole paper is stated in the
conclusion rather than buried: the economics may simply not justify any of this.

Every claim carries one of five epistemic labels, so a reader can tell a
measurement from a citation from an argument. Appendix D logs 31 corrections
with what was claimed, what was wrong, and who caught it.

## Licence and standing

Nothing here is a Microsoft position. The census covers one developer machine
and generalises only as far as the argument it supports.

---

Ragnar Pitla - [LinkedIn](https://www.linkedin.com/in/ragnarpitla) - [rbuild.ai](https://rbuild.ai)
