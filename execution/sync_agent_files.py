#!/usr/bin/env python3
"""Mantiene CLAUDE.md, AGENTS.md y GEMINI.md idénticos.

Uso:
    python3 execution/sync_agent_files.py            # copia el más reciente a los demás
    python3 execution/sync_agent_files.py --source AGENTS.md
    python3 execution/sync_agent_files.py --check    # sale con código 1 si difieren
"""
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = ["CLAUDE.md", "AGENTS.md", "GEMINI.md"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--source", choices=FILES, help="Archivo fuente (por defecto, el modificado más recientemente)")
    parser.add_argument("--check", action="store_true", help="Solo verificar; no escribir nada")
    args = parser.parse_args()

    paths = [ROOT / name for name in FILES]
    existing = [p for p in paths if p.exists()]
    if not existing:
        print("ERROR: no existe ninguno de " + ", ".join(FILES), file=sys.stderr)
        return 1

    if args.check:
        contents = {p.name: p.read_bytes() if p.exists() else None for p in paths}
        if len(set(contents.values())) == 1:
            print("OK: los tres archivos son idénticos.")
            return 0
        print("DIFIEREN: " + ", ".join(f"{n}={'falta' if c is None else len(c)}" for n, c in contents.items()), file=sys.stderr)
        return 1

    source = ROOT / args.source if args.source else max(existing, key=lambda p: p.stat().st_mtime)
    if not source.exists():
        print(f"ERROR: {source.name} no existe", file=sys.stderr)
        return 1
    data = source.read_bytes()
    for p in paths:
        if p != source and (not p.exists() or p.read_bytes() != data):
            p.write_bytes(data)
            print(f"Actualizado {p.name} desde {source.name}")
    print("OK: sincronizado.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
