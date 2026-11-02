#!/usr/bin/env python3
"""Manutenzione del Second Brain.

Uso:
    python tools/brain.py           rigenera gli _index.md e controlla le note
    python tools/brain.py --check   controlla soltanto, senza scrivere nulla

Solo libreria standard: nessuna dipendenza da installare.
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEXED = ["10-me", "20-knowledge", "30-playbooks", "40-progetti", "50-esempi"]
SKIP_DIRS = {".git", ".obsidian", ".trash", "tools", "__pycache__"}
NOT_NOTES = {"_index.md", "memory.md", "AGENTS.md", "CLAUDE.md"}
MAX_LINES = 150
REQUIRED = ["summary", "tags", "related", "fonte", "aggiornato"]
HEADER = "<!-- generato da tools/brain.py: non modificare a mano -->"

WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
CODE = re.compile(r"```.*?```|`[^`\n]*`", re.S)  # esempi nel codice: non sono link
RELATED_OK = re.compile(r'^\[\s*"\[\[[^\]]+\]\]"(\s*,\s*"\[\[[^\]]+\]\]")*\s*\]$')


def skipped(path: Path) -> bool:
    """Cartelle escluse: di sistema, nascoste o che iniziano con '_' (template)."""
    rel = path.relative_to(ROOT).parts
    return any(p in SKIP_DIRS or p.startswith((".", "_")) for p in rel[:-1] if p)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def frontmatter(text: str):
    """Restituisce il dizionario dell'intestazione YAML (una chiave per riga) o None."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    fm = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return fm
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            fm[m.group(1)] = m.group(2).strip()
    return None  # intestazione mai chiusa


def is_note(path: Path) -> bool:
    return (
        path.suffix == ".md"
        and path.name not in NOT_NOTES
        and not path.name.startswith(("_", "."))
        and path.relative_to(ROOT).parts[0] in INDEXED
        and not skipped(path)
    )


def all_md():
    for p in ROOT.rglob("*.md"):
        rel = p.relative_to(ROOT).parts
        if not any(part in {".git", ".obsidian", ".trash"} for part in rel):
            yield p


def summary_of(path: Path) -> str:
    fm = frontmatter(read(path)) if path.exists() else None
    return (fm or {}).get("summary", "").strip('"\' ')


def build_index(folder: Path) -> str:
    rel = folder.relative_to(ROOT).as_posix()
    subdirs = sorted(
        d for d in folder.iterdir()
        if d.is_dir() and not d.name.startswith((".", "_")) and d.name not in SKIP_DIRS
    )
    notes = sorted(p for p in folder.glob("*.md") if is_note(p))
    others = sorted(
        p for p in folder.iterdir()
        if p.is_file() and p.suffix != ".md" and not p.name.startswith(".")
    )
    out = [HEADER, f"# Indice — {rel}", ""]
    if subdirs:
        out.append("## Sottocartelle")
        for d in subdirs:
            n = sum(1 for p in d.rglob("*.md") if is_note(p))
            desc = summary_of(d / "AGENTS.md") or f"{n} note"
            out.append(f"- [[{rel}/{d.name}/_index|{d.name}/]] — {desc}")
        out.append("")
    out.append("## Note")
    if notes:
        for p in notes:
            out.append(f"- [[{p.stem}]] — {summary_of(p) or '(manca summary)'}")
    else:
        out.append("- (vuota)")
    if others:
        out += ["", "## Altri file"] + [f"- `{p.name}`" for p in others]
    return "\n".join(out) + "\n"


def main() -> int:
    check_only = "--check" in sys.argv
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    # 1. indici
    written = 0
    if not check_only:
        for top in INDEXED:
            base = ROOT / top
            if not base.is_dir():
                continue
            folders = [base] + [
                d for d in base.rglob("*")
                if d.is_dir() and not skipped(d / "x")
            ]
            for folder in folders:
                target = folder / "_index.md"
                content = build_index(folder)
                if not target.exists() or read(target) != content:
                    target.write_text(content, encoding="utf-8", newline="\n")
                    written += 1

    # 2. controlli
    stems = defaultdict(list)
    paths = set()
    for p in all_md():
        stems[p.stem].append(p)
        paths.add(p.relative_to(ROOT).with_suffix("").as_posix())

    errors = defaultdict(list)
    notes = [p for p in all_md() if is_note(p)]
    hubs = [p for p in (ROOT / "40-progetti").glob("*/AGENTS.md") if not skipped(p)]

    for p in notes + hubs:
        rel = p.relative_to(ROOT).as_posix()
        text = read(p)
        fm = frontmatter(text)
        if fm is None:
            errors["Intestazione YAML mancante o non chiusa"].append(rel)
        else:
            missing = [k for k in REQUIRED if not fm.get(k)]
            if missing:
                errors["Campi mancanti nell'intestazione"].append(f"{rel}: {', '.join(missing)}")
            rel_val = fm.get("related", "")
            if rel_val and not RELATED_OK.match(rel_val):
                errors['Formato "related" non valido (usa ["[[a]]", "[[b]]"])'].append(rel)
        n = len(text.splitlines())
        if n > MAX_LINES:
            errors[f"Nota troppo lunga (> {MAX_LINES} righe): spezzala"].append(f"{rel}: {n} righe")
        if p in notes and p.stem in stems and len(stems[p.stem]) > 1:
            others = [q.relative_to(ROOT).as_posix() for q in stems[p.stem] if q != p]
            errors["Nome di nota duplicato"].append(f"{rel} (anche {', '.join(others)})")

    for p in all_md():
        if skipped(p):
            continue  # tools/ e _template/: segnaposto ammessi
        rel = p.relative_to(ROOT).as_posix()
        for target in WIKILINK.findall(CODE.sub("", read(p))):
            t = target.strip()
            ok = t in paths if "/" in t else t in stems
            if not ok:
                errors["Link rotti"].append(f"{rel} → [[{t}]]")

    if not errors:
        msg = f"OK — {len(notes)} note, 0 errori"
        if not check_only:
            msg += f", {written} indici aggiornati"
        print(msg)
        return 0
    total = sum(len(v) for v in errors.values())
    print(f"{total} errori su {len(notes)} note")
    for rule, items in errors.items():
        print(f"\n## {rule}")
        for item in items:
            print(f"- {item}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
