import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORT = []

SEMANTIC_BLACKLIST = [
    "note that",
    "you may",
    "we believe",
    "in this conversation",
    "for example",
    "it seems",
]

HEADER_ORDER = [
    "Document ID:",
    "Version:",
    "Status:",
    "Effective Date:",
    "Last Updated:",
    "Owner:",
    "Maintained By:",
    "Applies To:",
    "Scope:",
    "Authority:",
]

def normalize_spacing(lines):
    fixed = []
    prev_blank = False

    for line in lines:
        is_blank = line.strip() == ""

        if is_blank and prev_blank:
            continue

        fixed.append(line.rstrip())
        prev_blank = is_blank

    return fixed

def normalize_numbered_lists(lines):
    fixed = []
    for i, line in enumerate(lines):
        fixed.append(line)
        if re.match(r"^\d+\.\s+", line.strip()):
            if i + 1 < len(lines) and lines[i + 1].strip() != "":
                fixed.append("")
    return fixed

def check_semantic_pollution(text, path):
    for phrase in SEMANTIC_BLACKLIST:
        if phrase in text.lower():
            REPORT.append(f"[SEMANTIC] {path}: '{phrase}'")

def check_header_order(lines, path):
    found = [l for l in lines if any(l.startswith(h) for h in HEADER_ORDER)]
    if found != sorted(found, key=lambda x: HEADER_ORDER.index(next(h for h in HEADER_ORDER if x.startswith(h)))):
        REPORT.append(f"[HEADER_ORDER] {path}")

def process_file(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    original = lines[:]

    lines = normalize_spacing(lines)
    lines = normalize_numbered_lists(lines)

    text = "\n".join(lines)
    check_semantic_pollution(text, path)
    check_header_order(lines, path)

    if lines != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
        REPORT.append(f"[FIXED] {path}")

def main():
    for md in ROOT.rglob("*.md"):
        if "/.git/" in str(md):
            continue
        process_file(md)

    report_path = ROOT / "system" / "audits" / "FORMAT_NORMALIZATION_REPORT.txt"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as r:
        r.write("\n".join(REPORT))

    print("Scan complete. Report written to:", report_path)

if __name__ == "__main__":
    main()
