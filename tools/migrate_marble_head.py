#!/usr/bin/env python3
"""Rebrand site to Marble Head Maids and update MA location references."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

from build_ma_locations import NORTH_SHORE, NORTH_SUBURBS  # noqa: E402

REPLACEMENTS = [
    ("Marble Head Maids", "Marble Head Maids"),
    ("Madtown <span class=\"text-primary\">Maids</span>", "Marble Head <span class=\"text-primary\">Maids</span>"),
    ("Madtown <span class=\"text-primary\">Maids</span>", "Marble Head <span class=\"text-primary\">Maids</span>"),
    ("marbleheadmaids.com", "marbleheadmaids.com"),
    ("Marble Head Maids - Clone Styles", "Marble Head Maids - Styles"),
    ("Serving the North Shore & North Suburbs", "Serving the North Shore & North Suburbs"),
    ("Serving the North Shore &amp; North Suburbs", "Serving the North Shore &amp; North Suburbs"),
    ("Recurring Cleaning Services You Can Count On", "Recurring Cleaning Services You Can Count On"),
    ("Why the North Shore Trusts Marble Head Maids", "Why the North Shore Trusts Marble Head Maids"),
    ("Book Your Cleaning in 3 Simple Steps", "Book Your Cleaning in 3 Simple Steps"),
    ("Trusted by North Shore Residents", "Trusted by North Shore Residents"),
    ("Common Questions About Our Cleaning Services", "Common Questions About Our Cleaning Services"),
    ("Cleaning Services on the North Shore, MA", "Cleaning Services on the North Shore, MA"),
    ("Cleaning Services North Shore MA", "Cleaning Services North Shore MA"),
    ("The North Shore's trusted local cleaning company", "The North Shore's trusted local cleaning company"),
    ("across the North Shore and North Suburbs", "across the North Shore and North Suburbs"),
    ("the North Shore and North Suburbs, MA", "the North Shore and North Suburbs, MA"),
    ("the North Shore, North Suburbs & greater Essex County", "the North Shore, North Suburbs & greater Essex County"),
    ("the North Shore, North Suburbs &amp; greater Essex County", "the North Shore, North Suburbs &amp; greater Essex County"),
    ("the North Shore and North Suburbs", "the North Shore and North Suburbs"),
    ("the North Shore, North Suburbs, and greater Essex County", "the North Shore, North Suburbs, and greater Essex County"),
    ("North Shore and North Suburbs", "North Shore and North Suburbs"),
    ("North Shore homeowners and renters", "North Shore homeowners and renters"),
    ("North Shore and North Suburbs residents actually live", "North Shore and North Suburbs residents actually live"),
    ("Life on the North Shore is busy enough", "Life on the North Shore is busy enough"),
    ("Life on the North Shore moves fast", "Life on the North Shore moves fast"),
    ("weekend plans, coastal living, and busy schedules", "weekend plans, coastal living, and busy schedules"),
    ("North Shore, MA", "North Shore, MA"),
    ("Marblehead, Massachusetts", "Marblehead, Massachusetts"),
    ("on the North Shore", "on the North Shore"),
    ("North Shore ", "North Shore "),
    ("the North Shore.", "the North Shore."),
    ("the North Shore,", "the North Shore,"),
    ("the North Shore's", "the North Shore's"),
    ("Essex County", "Essex County"),
    (" Massachusetts", " Massachusetts"),
    (", MA", ", MA"),
    (" MA ", " MA "),
    (" MA—", " MA—"),
    (" MA |", " MA |"),
    ("studios to multi-bedroom units", "studios to multi-bedroom units"),
    ("along the Route 128 corridor", "along the Route 128 corridor"),
    ("North Shore property managers", "local property managers"),
    ("the North Shore's near west side", "Marblehead"),
    ("North Shore proper", "Marblehead"),
    ("North Shore metro", "North Shore"),
    ("Marblehead", "Marblehead"),
    ("Beverly, Salem, Peabody, Andover, Swampscott, and more", "Beverly, Salem, Peabody, Andover, Swampscott, and more"),
    ("How much does house cleaning cost on the North Shore?", "How much does house cleaning cost on the North Shore?"),
    ("Marble Head Maids was built on the North Shore, for Madison", "Marble Head Maids was built on the North Shore, for the North Shore"),
    ("We live on the North Shore", "We live on the North Shore"),
    ("from Marblehead to the North Suburbs", "from Marblehead to the North Suburbs"),
    ("North Shore cleaning market", "North Shore cleaning market"),
    ("apartments across the North Shore", "apartments across the North Shore"),
    ("cleaned apartments across the North Shore", "cleaned apartments across the North Shore"),
    ("North Shore renters", "North Shore renters"),
    ("North Shore apartments", "North Shore apartments"),
    ("House cleaning on the North Shore", "House cleaning on the North Shore"),
    ("Cleaning Checklist North Shore", "Cleaning Checklist North Shore"),
    ("our North Shore cleaning services", "our North Shore cleaning services"),
    ("Careers at Marble Head Maids — Join Our Cleaning Team in North Shore, MA", "Careers at Marble Head Maids — Join Our Cleaning Team on the North Shore, MA"),
    ("Join the Marble Head Maids team! We're hiring reliable, detail-oriented cleaners in the North Shore and North Suburbs, MA.", "Join the Marble Head Maids team! We're hiring reliable, detail-oriented cleaners on the North Shore and North Suburbs, MA."),
    ("About Marble Head Maids", "About Marble Head Maids"),
    ("About Marble Head Maids — Locally Owned Cleaning Company in North Shore, MA", "About Marble Head Maids — Locally Owned Cleaning Company on the North Shore, MA"),
    ("A North Shore cleaning company built on trust", "A North Shore cleaning company built on trust"),
    ("Why We Started Marble Head Maids", "Why We Started Marble Head Maids"),
    ("Join the Marble Head Maids Team", "Join the Marble Head Maids Team"),
    ("Contact Marble Head Maids", "Contact Marble Head Maids"),
    ("Marble Head Maids is a locally owned cleaning company based in Marblehead, Massachusetts", "Marble Head Maids is a locally owned cleaning company based in Marblehead, Massachusetts"),
    ("Marble Head Maids is a locally owned cleaning company based on the North Shore", "Marble Head Maids is a locally owned cleaning company based in Marblehead"),
    ("Marble Head Maids is a locally owned and operated cleaning company based in Marblehead, Massachusetts", "Marble Head Maids is a locally owned and operated cleaning company based in Marblehead, Massachusetts"),
    ("Marble Head Maids serves homes and businesses across North Shore, MA and the surrounding Essex County communities", "Marble Head Maids serves homes and businesses across the North Shore, North Suburbs, and greater Essex County"),
    ("Marble Head Maids is ready when you are", "Marble Head Maids is ready when you are"),
    ("from Marble Head Maids", "from Marble Head Maids"),
    ("Marble Head Maids did an incredible job", "Marble Head Maids did an incredible job"),
    ("Marble Head Maids — the North Shore's Largest Suburb", "Marble Head Maids"),
    ("Privacy Policy for Marble Head Maids", "Privacy Policy for Marble Head Maids"),
    ("Terms and Conditions for Marble Head Maids", "Terms and Conditions for Marble Head Maids"),
    ("SMS messages from Marble Head Maids", "SMS messages from Marble Head Maids"),
    ("Marble Head Maids. All rights reserved.", "Marble Head Maids. All rights reserved."),
    ("Marble Head Maids - Service Area", "Marble Head Maids - Service Area"),
    ("Generate internal HTML pages for Marble Head Maids clone.", "Generate internal HTML pages for Marble Head Maids."),
]

TEXT_GLOBS = ["**/*.js", "**/*.html", "**/*.py", "**/*.css"]
SKIP_DIRS = {"node_modules", ".git", "images"}


def locations_js_array() -> str:
    lines = ["  locations: ["]
    for slug, city in NORTH_SHORE + NORTH_SUBURBS:
        lines.append(f'    {{ label: "{city}", href: "locations/{slug}.html" }},')
    lines.append("  ],")
    return "\n".join(lines)


def patch_data_locations(content: str) -> str:
    pattern = r"  locations: \[\s*\n(?:.*?\n)*?  \],"
    replacement = locations_js_array()
    if not re.search(pattern, content, re.DOTALL):
        raise SystemExit("Could not find locations array in data.js")
    return re.sub(pattern, replacement, content, count=1)


def apply_replacements(text: str) -> str:
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    return text


def iter_files():
    for glob in TEXT_GLOBS:
        for path in ROOT.glob(glob):
            if any(part in SKIP_DIRS for part in path.parts):
                continue
            if path.suffix not in {".js", ".html", ".py", ".css"}:
                continue
            yield path


def cleanup_old_locations(valid_slugs: set[str]) -> None:
    loc_dir = ROOT / "locations"
    if not loc_dir.exists():
        return
    for path in loc_dir.glob("*.html"):
        if path.stem not in valid_slugs:
            path.unlink()
            print(f"Removed old location page {path.name}")


def main():
    updated = 0
    for path in iter_files():
        if path.name == "location-pages.js":
            continue
        original = path.read_text(encoding="utf-8")
        text = apply_replacements(original)
        if path.name == "data.js" and "locations:" in text:
            text = patch_data_locations(text)
        if text != original:
            path.write_text(text, encoding="utf-8")
            updated += 1
            print(f"Updated {path.relative_to(ROOT)}")

    valid_slugs = {slug for slug, _ in NORTH_SHORE + NORTH_SUBURBS}
    cleanup_old_locations(valid_slugs)
    print(f"Done. Updated {updated} files.")


if __name__ == "__main__":
    main()
