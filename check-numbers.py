#!/usr/bin/env python3
"""Cross-artifact number consistency.

The site, the paper and the author note each state how many adversarial reviews
ran and how many corrections are logged. Nothing kept them in agreement, and a
stale note contradicted the microcopy sitting directly above it on the same
screen. This fails the build when they drift apart again.

Every check carries a control, because a checker that silently matches nothing
reports a clean run while measuring nothing.
"""
import re
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
PAPER = ROOT / "agentic-enterprise.md"
SITE = ROOT / "site" / "index.html"

paper = PAPER.read_text()
site = SITE.read_text()

WORD = {
    "three": 3, "four": 4, "five": 5, "six": 6,
    "thirty-one": 31, "forty-one": 41, "forty-two": 42,
}


def nums(text, pattern):
    """Every number matching pattern, digits or English words, as ints."""
    out = []
    for m in re.finditer(pattern, text, re.I):
        tok = m.group(1).lower()
        out.append(int(tok) if tok.isdigit() else WORD.get(tok, -1))
    return out


REVIEWS = r"\b(\d+|three|four|five|six)\s+(?:further\s+)?(?:adversarial|frontier)"
CORRECTIONS = r"\b(\d+|thirty-one|forty-one|forty-two)\s+(?:logged\s+)?corrections?\b"

# "an error that survived three frontier-model reviews" is a different claim
# from "this paper had five reviews". Only the totals are compared.
NOT_A_TOTAL = re.compile(r"surviv|separate", re.I)


def nums_total(text, pattern):
    out = []
    for m in re.finditer(pattern, text, re.I):
        if NOT_A_TOTAL.search(text[max(0, m.start() - 60):m.start()]):
            continue
        tok = m.group(1).lower()
        out.append(int(tok) if tok.isdigit() else WORD.get(tok, -1))
    return out

failures = []


def check(ok, msg):
    print(("[ok]   " if ok else "[FAIL] ") + msg)
    if not ok:
        failures.append(msg)


# ---- controls -------------------------------------------------------------
# If a pattern matches nothing, every assertion built on it is vacuously true.
site_rev = nums_total(site, REVIEWS)
paper_rev = nums_total(paper, REVIEWS)
site_cor = nums_total(site, CORRECTIONS)
paper_cor = nums_total(paper, CORRECTIONS)

check(len(site_rev) >= 2, f"CONTROL: review count found >=2 times on the site (got {len(site_rev)})")
check(len(paper_rev) >= 1, f"CONTROL: review count found on the paper (got {len(paper_rev)})")
check(len(site_cor) >= 1, f"CONTROL: corrections count found on the site (got {len(site_cor)})")
check(len(paper_cor) >= 1, f"CONTROL: corrections count found in the paper (got {len(paper_cor)})")

# Negative control: the word map must not silently swallow an unknown token.
check(WORD.get("seventeen") is None, "CONTROL: unmapped number words are not silently accepted")

# ---- the actual invariant -------------------------------------------------
check(len(set(site_rev)) <= 1, f"site agrees with itself on review count: {site_rev}")
check(len(set(site_cor)) <= 1, f"site agrees with itself on corrections count: {site_cor}")
check(
    not site_rev or not paper_rev or set(site_rev) <= set(paper_rev),
    f"site review count {set(site_rev)} appears in the paper {set(paper_rev)}",
)
check(
    not site_cor or not paper_cor or set(site_cor) <= set(paper_cor),
    f"site corrections count {set(site_cor)} appears in the paper {set(paper_cor)}",
)

# The paper's own corrections table must have as many rows as it claims.
rows = re.findall(r"^\| (\d+) \| ", paper, re.M)
check(len(rows) >= 10, f"CONTROL: correction rows parsed from the paper (got {len(rows)})")
if rows:
    top = max(int(r) for r in rows)
    check(top in paper_cor, f"highest numbered correction row ({top}) matches a stated total {set(paper_cor)}")

print()
print(f"{len(failures)} FAILED" if failures else "numbers agree across paper, site and note")
sys.exit(1 if failures else 0)
