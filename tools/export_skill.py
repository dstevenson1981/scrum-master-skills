#!/usr/bin/env python3
"""Export a SKILL.md skill folder to formats other AI tools can use.

Usage:
    python3 export_skill.py path/to/skill-folder [--out out] [--no-inline-refs]

Writes, under --out/<skill-name>/:
    copilot/.github/instructions/<name>.instructions.md   (applyTo: "**")
    copilot/.github/prompts/<name>.prompt.md              (reusable prompt)
    agents/AGENTS.md                                      (AGENTS.md convention)
    plain/<name>.txt                                      (paste into any chat)

Other tools don't load references/ on demand, so by default the reference
files are appended to the body. Standard library only.
"""
import argparse
import re
import sys
from pathlib import Path


def parse_skill(skill_dir: Path):
    text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        sys.exit("SKILL.md must start with --- frontmatter ---")
    front, body = m.group(1), m.group(2).lstrip("\n")
    meta = {}
    key = None
    for line in front.splitlines():
        km = re.match(r"^([A-Za-z_-]+):\s*(.*)$", line)
        if km and not line.startswith(" "):
            key, val = km.group(1), km.group(2).strip()
            if val in (">", "|", ">-", "|-"):
                val = ""
            meta[key] = val
        elif key and line.strip():
            meta[key] = (meta[key] + " " + line.strip()).strip()
    for k in ("name", "description"):
        meta[k] = meta.get(k, "").strip().strip("\"'")
    if not meta["name"] or not meta["description"]:
        sys.exit("frontmatter needs name and description")
    return meta, body


def collect_refs(skill_dir: Path):
    refs = skill_dir / "references"
    if not refs.is_dir():
        return []
    return [(p.relative_to(skill_dir).as_posix(), p.read_text(encoding="utf-8"))
            for p in sorted(refs.rglob("*.md"))]


def build_body(body, refs, inline):
    if not inline or not refs:
        return body.rstrip() + "\n"
    out = [body.rstrip(), "", "---", "",
           "# Reference material",
           "",
           "Where the instructions above say to read a `references/` file, use "
           "the matching section below."]
    for rel, content in refs:
        out += ["", f"## {rel}", "", content.strip()]
    return "\n".join(out) + "\n"


def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print("wrote", path)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("skill_dir", type=Path)
    ap.add_argument("--out", type=Path, default=Path("out"))
    ap.add_argument("--no-inline-refs", action="store_true")
    a = ap.parse_args()

    meta, body = parse_skill(a.skill_dir)
    name, desc = meta["name"], meta["description"]
    full = build_body(body, collect_refs(a.skill_dir), not a.no_inline_refs)
    root = a.out / name

    write(root / "copilot/.github/instructions" / f"{name}.instructions.md",
          f'---\napplyTo: "**"\ndescription: "{desc.replace(chr(34), chr(39))}"\n---\n\n{full}')
    write(root / "copilot/.github/prompts" / f"{name}.prompt.md",
          f'---\ndescription: "{desc.replace(chr(34), chr(39))}"\n---\n\n{full}')
    write(root / "agents/AGENTS.md", f"# {name}\n\n> {desc}\n\n{full}")
    write(root / "plain" / f"{name}.txt",
          f"Use these instructions for this whole conversation.\n"
          f"Apply them when: {desc}\n\n{full}")


if __name__ == "__main__":
    main()
