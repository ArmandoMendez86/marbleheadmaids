#!/usr/bin/env python3
"""Download location hero images from madtownmaids.com."""

import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "images" / "heroes"

SLUGS = [
    "sun-prairie",
    "middleton",
    "verona",
    "fitchburg",
    "waunakee",
    "stoughton",
    "deforest",
    "cottage-grove",
    "mcfarland",
    "monona",
    "about",
    "checklist",
    "contact",
    "home",
]

BASE = "https://madtownmaids.com/images/heroes/"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for slug in SLUGS:
        url = f"{BASE}{slug}.jpg"
        dest = OUT / f"{slug}.jpg"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            data = urllib.request.urlopen(req, timeout=30).read()
            dest.write_bytes(data)
            print(f"Downloaded {dest} ({len(data)} bytes)")
        except Exception as exc:
            print(f"FAILED {slug}: {exc}")


if __name__ == "__main__":
    main()
