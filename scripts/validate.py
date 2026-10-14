#!/usr/bin/env python3
"""Validate ASCII wireframes.

Usage:
  python validate.py FILE [FILE ...]
  python validate.py -            (read one drawing from stdin)

A markdown file is checked block by block: only fenced blocks labelled `wire`.
Any other file (or stdin) is treated as one drawing.

Checks per drawing:
  1. Printable ASCII only, no tabs.
  2. Every row has the same width.
  3. First and last character of every row is + or |.
  4. Every | has a | or + directly above or below.
  5. Every + that touches a - has a | or + directly above or below.
"""
import sys


def split_blocks(text, is_md):
    lines = text.replace("\r", "").split("\n")
    if not is_md:
        while lines and lines[-1] == "":
            lines.pop()
        return [(1, lines)]
    out, i = [], 0
    while i < len(lines):
        s = lines[i].strip()
        if s.startswith("```"):
            info = s[3:].strip()
            start = i + 2
            body = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                body.append(lines[i])
                i += 1
            if info == "wire":
                out.append((start, body))
        i += 1
    return out


def check(body, start):
    errs = []
    if not body:
        return errs
    widths = {len(r) for r in body}
    target = len(body[0])
    for k, row in enumerate(body):
        ln = start + k
        for c in row:
            if not (32 <= ord(c) <= 126):
                errs.append(f"line {ln}: non ASCII or tab character {c!r}")
                break
        if len(row) != target:
            errs.append(f"line {ln}: width {len(row)}, expected {target}")
        if row and (row[0] not in "+|" or row[-1] not in "+|"):
            errs.append(f"line {ln}: row must start and end with + or |")

    def at(r, c):
        if 0 <= r < len(body) and 0 <= c < len(body[r]):
            return body[r][c]
        return " "

    for r, row in enumerate(body):
        for c, ch in enumerate(row):
            ln = start + r
            if ch == "|":
                if at(r - 1, c) not in "|+" and at(r + 1, c) not in "|+":
                    errs.append(f"line {ln}, col {c + 1}: | has no border above or below")
            elif ch == "+":
                touches = at(r, c - 1) in "-+" or at(r, c + 1) in "-+"
                if touches and at(r - 1, c) not in "|+" and at(r + 1, c) not in "|+":
                    errs.append(f"line {ln}, col {c + 1}: + is not a junction (no | or + above or below)")
    return errs


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    bad = 0
    for path in argv[1:]:
        if path == "-":
            text, is_md, name = sys.stdin.read(), False, "stdin"
        else:
            with open(path, encoding="utf-8") as f:
                text = f.read()
            is_md, name = path.endswith(".md"), path
        blocks = split_blocks(text, is_md)
        n_err = 0
        for start, body in blocks:
            e = check(body, start)
            for m in e:
                print(f"{name}: {m}")
            n_err += len(e)
        status = "OK" if n_err == 0 else f"{n_err} problem(s)"
        print(f"{name}: {len(blocks)} drawing(s) checked, {status}")
        bad += n_err
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
