#!/usr/bin/env python3
"""Build js/location-pages.js from scraped location page text."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRAPE = ROOT / "tools" / "locations-scrape.txt"
OUT = ROOT / "js" / "location-pages.js"

CITIES = {
    "sun-prairie": "Sun Prairie",
    "middleton": "Middleton",
    "verona": "Verona",
    "fitchburg": "Fitchburg",
    "waunakee": "Waunakee",
    "stoughton": "Stoughton",
    "deforest": "DeForest",
    "cottage-grove": "Cottage Grove",
    "mcfarland": "McFarland",
    "monona": "Monona",
}

TITLES = {
    "sun-prairie": "House Cleaning Sun Prairie MA — Serving the North Shore's Largest Suburb | Marble Head Maids",
    "middleton": "House Cleaning Middleton MA — Quality Cleaning for Middleton Homes | Marble Head Maids",
    "verona": "House Cleaning Verona MA — Trusted Local Cleaners | Marble Head Maids",
    "fitchburg": "House Cleaning Fitchburg MA — Homes & Apartments | Marble Head Maids",
    "waunakee": "House Cleaning Waunakee MA — Family Homes & New Builds | Marble Head Maids",
    "stoughton": "House Cleaning Stoughton MA — Professional Cleaners Near You | Marble Head Maids",
    "deforest": "House Cleaning DeForest MA — Growing Community, Reliable Cleaning | Marble Head Maids",
    "cottage-grove": "House Cleaning Cottage Grove MA — Fast-Growing, Fully Served | Marble Head Maids",
    "mcfarland": "House Cleaning McFarland MA — Lakeside Community, Local Cleaners | Marble Head Maids",
    "monona": "House Cleaning Monona MA — Local Cleaning for a Local Community | Marble Head Maids",
}


def find_index(lines, prefix):
    for i, line in enumerate(lines):
        if line.startswith(prefix):
            return i
    return -1


def parse_location(slug, lines):
    city = CITIES[slug]
    h1_idx = find_index(lines, f"House Cleaning in {city}")
    about_idx = find_index(lines, f"About {city}")
    services_idx = find_index(lines, f"Cleaning Services Available in {city}")
    recurring_idx = find_index(lines, f"Recurring Cleaning Services in {city}")
    why_idx = find_index(lines, f"Why {city} Homeowners Choose Marble Head Maids")
    faq_idx = find_index(lines, f"{city} Cleaning FAQs")
    cta_idx = find_index(lines, f"Get a Quote for Your {city} Home")

    hero_subtitle = lines[h1_idx + 1] if h1_idx >= 0 else ""

    about_paragraphs = []
    if about_idx >= 0:
        i = about_idx + 1
        while i < len(lines) and not lines[i].startswith("Cleaning Services"):
            line = lines[i]
            if line == "Population:" and i + 3 < len(lines):
                about_paragraphs.append(
                    f"Population: {lines[i + 1].replace('|', '').strip()} | Distance: {lines[i + 3]}"
                )
                i += 4
                continue
            if line == "Neighborhoods we serve:" and i + 1 < len(lines):
                about_paragraphs.append(f"Neighborhoods we serve: {lines[i + 1]}")
                i += 2
                continue
            if line not in ("Population:", "Distance:", "Neighborhoods we serve:", "−") and not line.startswith("Get a Quote"):
                if "|" not in line or "Population" in (lines[i - 1] if i > 0 else ""):
                    about_paragraphs.append(line)
            i += 1

    services_intro = ""
    if services_idx >= 0 and services_idx + 1 < len(lines):
        services_intro = lines[services_idx + 1]

    recurring_subtitle = ""
    recurring_text = ""
    if recurring_idx >= 0:
        recurring_subtitle = lines[recurring_idx + 1] if recurring_idx + 1 < len(lines) else ""
        for j in range(recurring_idx, min(recurring_idx + 30, len(lines))):
            if lines[j].startswith("Life in ") or lines[j].startswith("Between the "):
                recurring_text = lines[j]
                break

    faq_items = []
    if faq_idx >= 0:
        i = faq_idx + 1
        while i < len(lines) and not lines[i].startswith("Get a Quote for Your"):
            if lines[i] != "−" and i + 2 < len(lines) and lines[i + 1] == "−":
                faq_items.append({"question": lines[i], "answer": lines[i + 2]})
                i += 3
            else:
                i += 1

    cta_title = lines[cta_idx] if cta_idx >= 0 else f"Get a Quote for Your {city} Home"
    cta_text = lines[cta_idx + 1] if cta_idx >= 0 and cta_idx + 1 < len(lines) else ""

    why_items = [
        {
            "title": "You're Not an Afterthought",
            "description": f"{city} is part of our regular weekly route — not a 'we'll get to it when we can' add-on.",
        },
        {
            "title": "Same Teams, Same Quality",
            "description": f"Your {city} home gets the same trained team, the same checklist, and the same quality standard as a home on the North Shore's near west side.",
        },
        {
            "title": "Transparent Pricing",
            "description": f"Flat-rate quotes based on your home's specifics. No hourly billing, no distance surcharges for {city} addresses.",
        },
        {
            "title": "No Contracts",
            "description": "All plans are month-to-month. Pause, adjust, or cancel anytime.",
        },
    ]

    return {
        "slug": slug,
        "city": city,
        "pageTitle": TITLES[slug],
        "metaDescription": f"House cleaning in {city}, MA. Recurring, deep cleaning, move-in/out and more from Marble Head Maids. Background-checked teams, transparent pricing.",
        "h1": f"House Cleaning in {city}, MA",
        "heroSubtitle": hero_subtitle,
        "about": {
            "heading": f"About {city}",
            "paragraphs": about_paragraphs[:4],
        },
        "servicesIntro": services_intro,
        "recurringTitle": f"Recurring Cleaning Services in {city}",
        "recurringSubtitle": recurring_subtitle,
        "recurringText": recurring_text,
        "whyChoose": {
            "heading": f"Why {city} Homeowners Choose Marble Head Maids",
            "items": why_items,
        },
        "faq": {
            "heading": f"{city} Cleaning FAQs",
            "items": faq_items,
        },
        "cta": {"title": cta_title, "description": cta_text},
    }


def main():
    scrape = json.loads(SCRAPE.read_text(encoding="utf-8"))
    pages = {slug: parse_location(slug, lines) for slug, lines in scrape.items()}
    OUT.write_text(
        "window.LOCATION_PAGES = " + json.dumps(pages, indent=2, ensure_ascii=False) + ";\n",
        encoding="utf-8",
    )
    print(f"Wrote {OUT} ({len(pages)} locations)")


if __name__ == "__main__":
    main()
