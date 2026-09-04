#!/usr/bin/env python3
"""
Census of the agent skill libraries on one developer machine.

This is the script behind every number on the landing page and in section 5
of the paper. It exists because the first two versions of this measurement
were wrong in ways that a careful reader of the prose could not have caught,
so the controls below are the point of the file rather than decoration.

Control 3 asserts a substring that was read out of the file by hand before
the assertion was written. An earlier version asserted that the "de-slop"
description contains the word "slop". It does not, and that control failed
for the right reason only by accident.

Control 5 closes the set algebra. An earlier draft reported 274 shared names
between a set of 308 and a set of 249, which is impossible, and it survived
three model reviews because all three read the reasoning and none re-ran the
arithmetic.

Usage:  python3 census.py
Needs:  tiktoken  (pip install tiktoken)
"""

import os
import re
import glob
import sys

COPILOT = os.path.expanduser("~/.copilot/skills")
CLAUDE = os.path.expanduser("~/.claude/skills")
STALE_DAYS = 90


def load(root):
    """Parse every SKILL.md under root into name, description, body length."""
    out = {}
    for path in glob.glob(os.path.join(root, "*", "SKILL.md")):
        try:
            text = open(path, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        name = os.path.basename(os.path.dirname(path))
        desc = ""
        m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
        frontmatter, body = (m.group(1), m.group(2)) if m else ("", text)
        if frontmatter:
            # Capture through to the next top-level key, so a description
            # wrapped over several lines is not silently truncated to its
            # first line. The truncating version passed a non-emptiness
            # check while cutting 187 of them.
            d = re.search(r"^description:\s*(.*?)(?=^\w[\w-]*:|\Z)", frontmatter, re.S | re.M)
            if d:
                desc = " ".join(d.group(1).split())
            n = re.search(r"^name:\s*(.+)$", frontmatter, re.M)
            if n:
                name = n.group(1).strip()
        out[path] = {
            "dir": os.path.basename(os.path.dirname(path)),
            "name": name,
            "desc": desc,
            "body": len(body),
            "mtime": os.path.getmtime(path),
        }
    return out


def symlinks(root):
    total = broken = 0
    for entry in os.scandir(root):
        if entry.is_symlink():
            total += 1
            if not os.path.exists(entry.path):
                broken += 1
    return total, broken


def main():
    try:
        import tiktoken
    except ImportError:
        sys.exit("error: tiktoken is required. pip install tiktoken")

    for root in (COPILOT, CLAUDE):
        if not os.path.isdir(root):
            sys.exit(f"error: {root} does not exist. A recursive scan of a missing "
                     f"path returns nothing and reads as a proven negative.")

    cop = load(COPILOT)
    cla = load(CLAUDE)

    cop_names = {v["name"] for v in cop.values()}
    cla_names = {v["name"] for v in cla.values()}
    shared = cop_names & cla_names
    only_cop = cop_names - cla_names
    only_cla = cla_names - cop_names

    enc = tiktoken.get_encoding("cl100k_base")
    meta = "".join(f"{v['name']}: {v['desc']}\n" for v in cop.values())
    meta_tokens = len(enc.encode(meta))
    body_chars = sum(v["body"] for v in cop.values())

    now = __import__("time").time()
    stale = sum(1 for v in cop.values() if (now - v["mtime"]) > STALE_DAYS * 86400)

    cop_sym = symlinks(COPILOT)
    cla_sym = symlinks(CLAUDE)

    # ------------------------------------------------------------- CONTROLS
    long_descs = [v for v in cop.values() if len(v["desc"]) > 200]
    assert len(long_descs) >= 5, (
        f"control 1 FAILED: only {len(long_descs)} descriptions over 200 chars. "
        "The parser is truncating multi-line YAML again.")

    assert len(cop) > 200 and len(cla) > 200, (
        f"control 2 FAILED: counts look wrong ({len(cop)}, {len(cla)}).")

    probe = [v for v in cop.values() if v["dir"] == "deep-research"]
    assert probe and "firecrawl" in probe[0]["desc"].lower(), (
        "control 3 FAILED: the deep-research description does not contain "
        "'firecrawl'. Either the parser broke or the skill changed.")

    assert not [v for v in cop.values() if v["dir"] == "zzz-skill-that-does-not-exist"], (
        "control 4 FAILED: a name that cannot exist returned a match, so the "
        "matcher matches everything and proves nothing.")

    assert len(shared) + len(only_cop) == len(cop_names), "control 5 FAILED: copilot set algebra"
    assert len(shared) + len(only_cla) == len(cla_names), "control 5 FAILED: claude set algebra"
    assert len(cop_names | cla_names) == len(shared) + len(only_cop) + len(only_cla), (
        "control 5 FAILED: union does not equal shared plus both exclusives.")

    assert len(enc.encode("hello world")) == 2, (
        "control 6 FAILED: tiktoken is not returning the known cl100k count.")

    print("all 6 controls passed")
    print()
    print(f"copilot SKILL.md files   : {len(cop)}    unique names: {len(cop_names)}")
    print(f"claude  SKILL.md files   : {len(cla)}    unique names: {len(cla_names)}")
    print(f"shared names             : {len(shared)}")
    print(f"only in copilot          : {len(only_cop)}")
    print(f"only in claude           : {len(only_cla)}")
    print(f"always-loaded metadata   : {len(meta)} chars = {meta_tokens} tokens (cl100k)")
    print(f"skill bodies             : {body_chars} chars")
    print(f"body-to-index ratio      : {body_chars / len(meta):.1f}x")
    print(f"untouched {STALE_DAYS}d           : {stale} of {len(cop)} = {100 * stale / len(cop):.1f}%")
    print(f"copilot symlinks         : {cop_sym[0]} total, {cop_sym[1]} broken")
    print(f"claude  symlinks         : {cla_sym[0]} total, {cla_sym[1]} broken")


if __name__ == "__main__":
    main()
