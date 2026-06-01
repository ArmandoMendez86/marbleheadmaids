#!/usr/bin/env python3
"""Generate js/location-pages.js for Marblehead Maids (North Shore & North Suburbs, MA)."""

import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "js" / "location-pages.js"
HEROES = ROOT / "images" / "heroes"

BRAND = "Marblehead Maids"
BASE = "Marblehead"

NORTH_SHORE = [
    ("beverly", "Beverly"),
    ("danvers", "Danvers"),
    ("essex", "Essex"),
    ("gloucester", "Gloucester"),
    ("hamilton", "Hamilton"),
    ("ipswich", "Ipswich"),
    ("marblehead", "Marblehead"),
    ("nahant", "Nahant"),
    ("newbury", "Newbury"),
    ("newburyport", "Newburyport"),
    ("rockport", "Rockport"),
    ("rowley", "Rowley"),
    ("salem", "Salem"),
    ("salisbury", "Salisbury"),
    ("swampscott", "Swampscott"),
]

NORTH_SUBURBS = [
    ("andover", "Andover"),
    ("boxford", "Boxford"),
    ("georgetown", "Georgetown"),
    ("groveland", "Groveland"),
    ("haverhill", "Haverhill"),
    ("lawrence", "Lawrence"),
    ("lynn", "Lynn"),
    ("lynnfield", "Lynnfield"),
    ("methuen", "Methuen"),
    ("middleton", "Middleton"),
    ("north-andover", "North Andover"),
    ("peabody", "Peabody"),
    ("saugus", "Saugus"),
    ("topsfield", "Topsfield"),
    ("west-newbury", "West Newbury"),
]

COASTAL = {
    "beverly", "gloucester", "marblehead", "nahant", "newburyport",
    "rockport", "rowley", "salem", "salisbury", "swampscott", "lynn",
}


def region_label(region: str) -> str:
    return "the North Shore" if region == "north_shore" else "the North Suburbs"


def city_hook(city: str, slug: str, region: str) -> str:
    if slug in COASTAL:
        return (
            f"{city} sits on {region_label(region)} with a mix of coastal properties, "
            f"established neighborhoods, and year-round residents who expect their homes to stay fresh."
        )
    if region == "north_suburbs":
        return (
            f"{city} is a thriving community in {region_label(region)} — "
            f"with family homes, busy schedules, and the kind of day-to-day life that makes professional cleaning a real relief."
        )
    return (
        f"{city} is a well-loved town on {region_label(region)} — "
        f"with residential neighborhoods, local shops, and homes that deserve reliable, professional care."
    )


def build_page(slug: str, city: str, region: str) -> dict:
    region_name = region_label(region)
    return {
        "slug": slug,
        "city": city,
        "pageTitle": f"House Cleaning {city} MA — Trusted Local Cleaners | {BRAND}",
        "metaDescription": (
            f"House cleaning in {city}, MA. Recurring, deep cleaning, move-in/out and more "
            f"from {BRAND}. Background-checked teams, transparent pricing."
        ),
        "h1": f"House Cleaning in {city}, MA",
        "heroSubtitle": (
            f"{BRAND} is a locally owned cleaning company based in {BASE}, and {city} is one of our "
            f"core service areas on {region_name}. Trained, background-checked teams clean homes in "
            f"{city} every week — same scheduling, same quality, same flat-rate pricing."
        ),
        "about": {
            "heading": f"About {city}",
            "paragraphs": [
                city_hook(city, slug, region),
                f"Service area: {city}, MA and surrounding neighborhoods on {region_name}.",
                (
                    f"Neighborhoods we serve: residential streets throughout {city}, downtown areas, "
                    f"and nearby developments — if you're in {city}, we're your local cleaning team."
                ),
                (
                    f"{city} is part of our regular weekly routes. We have teams cleaning in {city} "
                    f"multiple days per week."
                ),
            ],
        },
        "servicesIntro": f"All of our residential and commercial cleaning services are available in {city}.",
        "recurringTitle": f"Recurring Cleaning Services in {city}",
        "recurringSubtitle": (
            f"Keep your {city} home spotless with flexible weekly, biweekly, or monthly cleaning plans"
        ),
        "recurringText": (
            f"Life in {city} moves fast — between work, family commitments, and everything {region_name} "
            f"has going on, who has time to clean? Our flexible scheduling lets you choose the frequency "
            f"that fits your lifestyle. Need to skip a week or reschedule? No problem — just give us 24 hours notice."
        ),
        "whyChoose": {
            "heading": f"Why {city} Homeowners Choose {BRAND}",
            "items": [
                {
                    "title": "You're Not an Afterthought",
                    "description": (
                        f"{city} is part of our regular weekly route — not a "
                        f"\"we'll get to it when we can\" add-on."
                    ),
                },
                {
                    "title": "Same Teams, Same Quality",
                    "description": (
                        f"Your {city} home gets the same trained team, the same checklist, and the same "
                        f"quality standard as homes across {region_name}."
                    ),
                },
                {
                    "title": "Transparent Pricing",
                    "description": (
                        f"Flat-rate quotes based on your home's specifics. No hourly billing, "
                        f"no distance surcharges for {city} addresses."
                    ),
                },
                {
                    "title": "No Contracts",
                    "description": "All plans are month-to-month. Pause, adjust, or cancel anytime.",
                },
            ],
        },
        "faq": {
            "heading": f"{city} Cleaning FAQs",
            "items": [
                {
                    "question": f"Do you really serve {city} regularly?",
                    "answer": (
                        f"Yes. {city} is part of our weekly routes — we have teams there multiple days "
                        f"per week. You're not an afterthought."
                    ),
                },
                {
                    "question": f"Is there a distance surcharge for {city}?",
                    "answer": (
                        f"No. Our flat-rate pricing is the same regardless of whether you're in "
                        f"{BASE} or {city}."
                    ),
                },
                {
                    "question": f"Can I get same-week service in {city}?",
                    "answer": "Often, yes. Contact us with your preferred date and we'll do our best to accommodate.",
                },
                {
                    "question": "What if I need to reschedule?",
                    "answer": (
                        "Just give us 24 hours' notice and we'll find a new time that works. "
                        "No cancellation fees with proper notice."
                    ),
                },
                {
                    "question": f"Do you service all neighborhoods in {city}?",
                    "answer": (
                        f"Yes. We clean throughout {city} — residential streets, downtown areas, "
                        f"and surrounding neighborhoods on {region_name}."
                    ),
                },
                {
                    "question": f"Do you bring your own cleaning supplies to {city}?",
                    "answer": (
                        "Yes. Our teams arrive fully equipped with all supplies and equipment — "
                        "you don't need to provide anything."
                    ),
                },
            ],
        },
        "cta": {
            "title": f"Get a Quote for Your {city} Home",
            "description": (
                f"Tell us about your {city} home — size, service type, preferred frequency — "
                f"and we'll send you a clear, no-obligation quote."
            ),
        },
    }


def all_locations():
    pages = {}
    for slug, city in NORTH_SHORE:
        pages[slug] = build_page(slug, city, "north_shore")
    for slug, city in NORTH_SUBURBS:
        pages[slug] = build_page(slug, city, "north_suburbs")
    return pages


def sync_hero_images(pages: dict) -> None:
    HEROES.mkdir(parents=True, exist_ok=True)
    fallback = HEROES / "home.jpg"
    if not fallback.exists():
        return
    for slug in pages:
        dest = HEROES / f"{slug}.jpg"
        if not dest.exists() or dest.stat().st_size != fallback.stat().st_size:
            shutil.copy2(fallback, dest)


def main():
    pages = all_locations()
    OUT.write_text(
        "window.LOCATION_PAGES = " + json.dumps(pages, indent=2, ensure_ascii=False) + ";\n",
        encoding="utf-8",
    )
    sync_hero_images(pages)
    print(f"Wrote {OUT} ({len(pages)} locations)")


if __name__ == "__main__":
    main()
