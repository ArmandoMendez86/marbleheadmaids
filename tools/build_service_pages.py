#!/usr/bin/env python3
"""Build js/service-pages.js from tools/service-pages-source.json.

To regenerate source data from Python dicts, run first:
  python tools/gen_service_source.py
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = Path(__file__).resolve().parent / "service-pages-source.json"
OUTPUT = ROOT / "js" / "service-pages.js"


def main() -> None:
    if not SOURCE.exists():
        raise SystemExit(f"Missing source file: {SOURCE}")

    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    payload = json.dumps(data, indent=2, ensure_ascii=False)
    OUTPUT.write_text(f"window.SERVICE_PAGES = {payload};\n", encoding="utf-8")
    print(f"Wrote {OUTPUT} ({len(data)} services)")


if __name__ == "__main__":
    main()
