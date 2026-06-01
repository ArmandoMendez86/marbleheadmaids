#!/usr/bin/env python3
"""One-time generator for tools/service-pages-source.json — run to regenerate source data."""

import json
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "service-pages-source.json"


def cat(title, items):
    return {"title": title, "items": items}


PAGES = {
    "apartment-cleaning": {
        "slug": "apartment-cleaning",
        "pageTitle": "Apartment Cleaning North Shore MA — Renter-Friendly Pricing | Marblehead Maids",
        "metaDescription": "Apartment cleaning across North Shore — from studios to multi-bedroom units. Priced for your unit size, not a 4-bedroom house.",
        "h1": "Apartment Cleaning in North Shore, MA — Sized for Your Space, Priced for Renters",
        "heroSubtitle": "You shouldn't have to pay house-cleaning prices for a one-bedroom apartment. Marblehead Maids offers apartment cleaning across North Shore — from studios to multi-bedroom units and everything in between. Our pricing scales to your actual unit size, and there's zero long-term commitment required.",
        "intro": {
            "heading": "Apartment Cleaning Built for North Shore Renters",
            "paragraphs": [
                "North Shore apartments aren't like houses — they're different animals entirely. Smaller spaces that show dirt immediately. Campus-area units with high turnover. You need cleaners who understand all of this.",
                "At Marblehead Maids, we've cleaned apartments across North Shore — from high-rises downtown to duplexes on Williamson Street, from complexes off Mineral Point to garden-level units near campus. We know the layouts, the challenges, and exactly how to get your apartment sparkling.",
                "We respect that you're renting. We're careful with walls and fixtures, mindful of neighbors, and focused on keeping your space in top condition — whether that's for your own sanity or your landlord's next inspection.",
            ],
        },
        "checklist": {
            "heading": "What's Included in Our Apartment Cleaning",
            "intro": "Every apartment cleaning covers all the essentials to keep your space fresh and comfortable. We focus on the areas that matter most in apartment living.",
            "categories": [
                cat("Kitchen", ["Countertops wiped and sanitized", "Stovetop and exterior of appliances cleaned", "Sink scrubbed and polished", "Cabinet fronts wiped down", "Floor swept and mopped", "Trash emptied and new liner placed"]),
                cat("Bathroom(s)", ["Toilet thoroughly cleaned and sanitized inside and out", "Shower and tub scrubbed", "Sink and vanity cleaned", "Mirror polished streak-free", "Floor mopped", "Towels neatly arranged or folded"]),
                cat("Bedrooms & Living Areas", ["All surfaces dusted", "Furniture wiped down", "Floors vacuumed and/or mopped", "Ceiling fans dusted (within reach)", "Light switches and door handles sanitized", "Bed made or linens changed if left out"]),
                cat("Throughout", ["Baseboards wiped in main areas", "Cobwebs removed", "Trash emptied from all rooms", "General tidying and straightening", "Entry area cleaned"]),
            ],
        },
        "whenToBook": {
            "heading": "When to Book Apartment Cleaning",
            "options": [
                {"title": "Weekly Cleaning", "description": "Best for busy professionals, pet owners, or anyone who wants to come home to a fresh apartment every week. North Shore apartments get dirty fast — this keeps them under control."},
                {"title": "Biweekly Cleaning", "description": "The sweet spot for most North Shore renters. Keeps your apartment consistently clean without weekly visits. Great for smaller units or those who tidy between visits."},
                {"title": "Monthly Cleaning", "description": "Good for studios, single-person households, or as a supplement to your own routine. Maintains standards without the weekly commitment."},
                {"title": "One-Time Cleaning", "description": "Not ready for recurring service? Perfect for a reset, pre-party prep, or when life just got ahead of you. Many recurring clients started with a single visit."},
                {"title": "Move-In or Move-Out", "description": "Starting a new lease or ending one? Our move-in and move-out cleaning services are designed specifically for apartment transitions."},
            ],
        },
        "recurringTitle": "Save with Recurring Apartment Cleaning",
        "recurringSubtitle": "Set it and forget it — we'll keep your apartment spotless on your schedule",
        "pricing": {
            "heading": "Apartment Cleaning Prices on the North Shore",
            "paragraphs": [
                "We price based on your apartment's size and condition — not a one-size-fits-all rate designed for houses. You pay for what you actually need cleaned.",
                "Studio (0 BR / 1 BA): Standard Clean $110–$140, Deep Clean $160–$200.",
                "1 Bedroom (1 BR / 1 BA): Standard Clean $130–$170, Deep Clean $190–$250.",
                "2 Bedroom (2 BR / 1 BA): Standard Clean $170–$220, Deep Clean $250–$320.",
                "3+ Bedroom (3+ BR / 2+ BA): Standard Clean $220+, Deep Clean $320+.",
                "Prices vary based on condition, specific requests, and location withon the North Shore.",
            ],
        },
        "whyChoose": {
            "heading": "Why North Shore Renters Choose Marblehead Maids",
            "items": [
                {"title": "We Respect Your Space", "description": "You don't own your apartment, but it's still your home. We treat it that way—careful with surfaces, mindful of walls and fixtures, respectful of your belongings."},
                {"title": "We Work Efficiently", "description": "Thin walls? Neighbors who work nights? Small space where everything echoes? Our teams clean quickly and quietly. We're in, we're thorough, and we're out."},
                {"title": "Flexible, No Contracts", "description": "North Shore renters move frequently — lease cycles, job changes, graduating. We don't require contracts or recurring commitments. Book when you need us."},
                {"title": "We Help Protect Your Deposit", "description": "Regular cleaning prevents buildup that leads to deductions when you move out. And when you're ready to leave, our move-out cleaning helps you get that deposit back."},
            ],
        },
        "locations": {"heading": "Apartment Cleaning Throughout Madison", "intro": "We proudly serve apartments across the North Shore and North Suburbs."},
        "faq": {
            "heading": "Apartment Cleaning FAQs",
            "items": [
                {"question": "How long does apartment cleaning take?", "answer": "It depends on your apartment's size and condition. A standard clean for a 1-bedroom typically takes 1.5-2.5 hours. Deep cleans or larger apartments take longer. We'll give you a time estimate with your quote."},
                {"question": "Do you bring your own supplies?", "answer": "Yes, we bring everything needed for a complete clean. If your building has rules about certain products or you have preferences (fragrance-free, eco-friendly), just let us know."},
                {"question": "How do you handle building access?", "answer": "However works best — lockbox, door code, or you can let us in. We're experienced with all types of North Shore buildings."},
                {"question": "Can you clean apartments with pets?", "answer": "Absolutely. We love pets. Just give us a heads up so we know to expect your furry friend—and any extra fur to vacuum."},
                {"question": "How do I prepare for my apartment cleaning?", "answer": "A quick pickup of personal items and clutter helps us clean more thoroughly. We can clean around things, but the clearer the surfaces, the better."},
                {"question": "Do I need to be home during the cleaning?", "answer": "Not at all. Many apartment clients give us a door code or leave a key. We're fully insured and background-checked."},
            ],
        },
        "cta": {"title": "Get Your North Shore Apartment Cleaned This Week", "description": "Stop spending your free time scrubbing floors. Book a professional apartment cleaning and come home to a space that actually feels relaxing."},
    },
    "house-cleaning": {
        "slug": "house-cleaning",
        "pageTitle": "House Cleaning North Shore MA — Weekly, Biweekly & Monthly Plans | Marblehead Maids",
        "metaDescription": "Recurring weekly, biweekly, or monthly cleaning that keeps your North Shore home consistently fresh.",
        "h1": "House Cleaning in North Shore, MA — Recurring Plans That Actually Keep Your Home Clean",
        "heroSubtitle": "You told yourself you'd keep up with it this week. Then Wednesday turned into a twelve-hour day, the kids had practice, the dog tracked mud through the kitchen, and suddenly it's Sunday night and the bathroom still hasn't been touched. Marblehead Maids provides professional house cleaning across North Shore — on a schedule that works for your life.",
        "intro": {
            "heading": "How Our House Cleaning Works",
            "paragraphs": [
                "Every house is different. A Nakoma bungalow has different needs than a Fitchburg colonial or a Middleton ranch. That's why we don't do cookie-cutter cleaning.",
                "When you book with Marblehead Maids, we learn about your home — the layout, the high-traffic areas, the spots that always need extra attention. Then we create a cleaning plan that actually makes sense for how you live.",
                "The result? A home that's consistently clean, week after week. No more marathon cleaning sessions before guests arrive. No more guilt about the dust bunnies under the couch. Just a clean home you can actually relax in.",
            ],
        },
        "checklist": {
            "heading": "What's Included in Our House Cleaning",
            "intro": "Our standard house cleaning covers everything you need to maintain a fresh, comfortable home. We clean every room thoroughly, focusing on the surfaces and areas that matter most.",
            "categories": [
                cat("Kitchen", ["Countertops cleaned and sanitized", "Stovetop and range hood wiped down", "Exterior of all appliances cleaned", "Sink and faucet scrubbed", "Cabinet fronts wiped", "Floor swept and mopped", "Trash emptied"]),
                cat("Bathroom(s)", ["Toilets thoroughly cleaned inside and out", "Showers and tubs scrubbed and sanitized", "Sinks and counters cleaned", "Mirrors polished", "Floors mopped", "Towels folded or hung neatly"]),
                cat("Bedrooms & Living Areas", ["All surfaces dusted", "Furniture wiped", "Floors vacuumed and mopped", "Beds made (or linens changed if you leave clean sheets out)", "Ceiling fans dusted", "Light switches and door handles sanitized"]),
                cat("Throughout", ["Baseboards wiped in main areas", "Windowsills dusted", "Air vents dusted (reachable ones)", "Stairs vacuumed", "Trash emptied from all rooms", "Cobwebs removed"]),
            ],
        },
        "whenToBook": {
            "heading": "When to Book House Cleaning",
            "options": [
                {"title": "Weekly Cleaning", "description": "Best for busy households, families with kids or pets, or anyone who wants to come home to a clean house every single week. Your home never has time to build up grime between visits."},
                {"title": "Biweekly Cleaning", "description": "Our most popular plan. Every two weeks, your team resets your home from top to bottom. Enough frequency to stay ahead of dust and mess without feeling like overkill."},
                {"title": "Monthly Cleaning", "description": "A good fit for smaller households, minimalists, or people who maintain their home between visits but want a professional-grade clean once a month to handle what they miss."},
                {"title": "One-Time Cleaning", "description": "Not ready for recurring service? Book a one-time clean to see the difference professional cleaning makes. Many of our recurring clients started this way."},
                {"title": "Seasonal Deep Clean", "description": "Pair your regular service with a deep clean once or twice a year to tackle the areas regular cleaning doesn't reach — inside appliances, behind furniture, and more."},
            ],
        },
        "recurringTitle": "Save with Recurring House Cleaning",
        "recurringSubtitle": "Set it and forget it — we'll keep your home spotless on your schedule",
        "pricing": {
            "heading": "House Cleaning Prices on the North Shore",
            "paragraphs": [
                "We price based on your home's size, the number of bathrooms, and the type of cleaning you need. You get a flat rate per visit — no hidden fees, no surprise charges.",
                "Small (1-2 BR / 1 BA): Recurring $150–$190, Deep Clean $350–$450.",
                "Medium (2-3 BR / 2 BA): Recurring $190–$250, Deep Clean $450–$550.",
                "Large (3-4 BR / 2-3 BA): Recurring $250–$320, Deep Clean $550+.",
                "Extra Large (4+ BR / 3+ BA): Recurring $320+, Deep Clean $650+.",
                "First-time cleanings may cost more if your home needs extra attention to reach a maintainable baseline. Recurring clients receive preferred pricing.",
            ],
        },
        "whyChoose": {
            "heading": "Why North Shore Homeowners Choose Marblehead Maids",
            "items": [
                {"title": "Consistent Teams", "description": "You'll see the same familiar faces each visit. Our cleaners get to know your home, your preferences, and exactly how you like things done."},
                {"title": "Background-Checked & Insured", "description": "Every cleaner passes a comprehensive background check. We're fully insured, so your home and belongings are protected."},
                {"title": "Real Communication", "description": "Need to reschedule? Have a special request? Want feedback on your last clean? We respond quickly and actually listen."},
                {"title": "Satisfaction Guaranteed", "description": "If something isn't right, tell us within 24 hours and we'll come back to fix it — no questions, no hassle."},
            ],
        },
        "locations": {"heading": "House Cleaning Throughout North Shore & Essex County", "intro": "We proudly serve homes across North Shore and the surrounding communities."},
        "faq": {
            "heading": "House Cleaning FAQs",
            "items": [
                {"question": "How long does a house cleaning take?", "answer": "It depends on your home's size and condition. A standard clean for a 3-bedroom home typically takes 2.5-3.5 hours. First-time cleans or deep cleans take longer. We'll give you a time estimate with your quote."},
                {"question": "Do I need to be home during the cleaning?", "answer": "Not at all. Many clients give us a key, garage code, or door code. We're fully insured and background-checked, so you can feel confident whether you're home or not."},
                {"question": "Will I have the same cleaner each time?", "answer": "We do our best to send consistent teams to each home. You'll get to know your cleaners and they'll get to know your home's specific needs."},
                {"question": "What if I have pets?", "answer": "We love pets! Just let us know about any animals in the home so we can plan accordingly. We'll be careful with doors and gates."},
                {"question": "What should I do before the cleaning?", "answer": "Picking up clutter—toys, clothes, dishes—helps us clean more thoroughly. The clearer the surfaces, the better we can clean them. But if you don't have time, we'll work around what's there."},
                {"question": "What if I need to skip or reschedule?", "answer": "No problem. Just give us 24 hours' notice and we'll reschedule at no charge. Life happens—we get it."},
            ],
        },
        "cta": {"title": "Ready to Stop Spending Your Weekends Cleaning?", "description": "Join the North Shore homeowners who've taken cleaning off their to-do list for good. Get a free quote today and see how affordable regular house cleaning can be."},
    },
    "deep-cleaning": {
        "slug": "deep-cleaning",
        "pageTitle": "Deep Cleaning Services North Shore MA — Top-to-Bottom Reset | Marblehead Maids",
        "metaDescription": "When surface-level isn't cutting it. We go behind appliances, inside cabinets, into grout lines, and across every baseboard.",
        "h1": "Deep Cleaning Services on the North Shore, MA — A Complete Reset for Your Home",
        "heroSubtitle": "When regular cleaning isn't enough. Our deep cleaning service reaches the spots you forgot existed — behind appliances, inside cabinets, under furniture, and everywhere in between. The reset your home deserves.",
        "intro": {
            "heading": "More Than Surface Clean — A Complete Home Reset",
            "paragraphs": [
                "There's a point where wiping down the countertops and running the vacuum isn't enough anymore. The grout's discolored. There's dust behind the fridge you haven't moved in two years. The baseboards have a film you keep meaning to deal with.",
                "That's what deep cleaning is for. It's a comprehensive, top-to-bottom clean that reaches every surface regular cleaning skips — behind, beneath, and inside. Marblehead Maids provides professional deep cleaning across the North Shore and North Suburbs, with trained teams who follow a structured process to reset your home to its cleanest possible state.",
                "Most homes benefit from a deep clean once or twice a year, or as a starting point before beginning regular cleaning service. If it's been a while since your home had serious attention, this is where we start.",
            ],
        },
        "checklist": {
            "heading": "What's Included in Our Deep Cleaning",
            "intro": "Our deep cleaning service covers everything in a standard clean plus extensive detail work throughout your home. Here's what we tackle:",
            "categories": [
                cat("Kitchen", ["All standard cleaning PLUS:", "Inside oven cleaned", "Inside microwave", "Inside refrigerator (shelves, drawers, walls)", "Behind and under appliances (where movable)", "Inside cabinet fronts wiped", "Range hood degreased", "Backsplash scrubbed", "Light fixtures cleaned", "Baseboards hand-wiped"]),
                cat("Bathroom(s)", ["All standard cleaning PLUS:", "Grout scrubbed and treated", "Tile walls wiped completely", "Shower door tracks cleaned", "Inside vanity cabinets and drawers wiped", "Exhaust fan vent cleaned", "Light fixtures cleaned", "Behind toilet thoroughly cleaned", "Baseboards hand-wiped"]),
                cat("Bedrooms & Living Areas", ["All standard cleaning PLUS:", "Under beds cleaned (moved if possible)", "Behind and under furniture", "Inside closet shelving dusted", "Ceiling fan blades detailed", "Light fixtures cleaned", "Window sills and tracks cleaned", "Baseboards hand-wiped", "Door frames and tops of doors wiped"]),
                cat("Throughout", ["Interior windows cleaned", "All baseboards hand-wiped", "All door frames wiped", "Light switches and outlets wiped", "Blinds dusted or wiped", "Cobwebs removed from all corners", "Air vents removed and cleaned", "Stairs thoroughly cleaned including railings"]),
            ],
        },
        "whenToBook": {
            "heading": "When to Book Deep Cleaning",
            "options": [
                {"title": "Before Starting Regular Service", "description": "If you're new to professional cleaning, we recommend starting with a deep clean. This brings your home to a clean baseline that's much easier (and less expensive) to maintain with regular visits."},
                {"title": "Seasonal Reset", "description": "Spring cleaning is a tradition for a reason. A deep clean once or twice a year keeps the hidden buildup from getting out of control. Many North Shore clients book in spring and fall."},
                {"title": "Before Major Events", "description": "Hosting Thanksgiving? Throwing a party? Having family stay for the holidays? A deep clean ensures your home is guest-ready down to the last detail."},
                {"title": "After Extended Absence", "description": "Been traveling? Finally back home after a long project? Dust settles while you're gone. A deep clean gets everything fresh again."},
                {"title": "Allergy Relief", "description": "Deep cleaning removes dust, pet dander, and allergens from places regular cleaning doesn't reach. If allergies are flaring up, a deep clean can make a real difference."},
            ],
        },
        "recurringTitle": "Save with Recurring Deep Cleaning",
        "recurringSubtitle": "Maintain that fresh-start feeling with regular cleaning service",
        "pricing": {
            "heading": "Deep Cleaning Prices on the North Shore",
            "paragraphs": [
                "Deep cleaning takes significantly more time and effort than standard cleaning, so it's priced accordingly. The investment is worth it — you're getting every corner of your home addressed.",
                "Studio/1BR Apartment (0-1 BR / 1 BA): $200–$280.",
                "2BR Apartment (2 BR / 1 BA): $280–$380.",
                "Small House (2-3 BR / 1-2 BA): $350–$450.",
                "Medium House (3-4 BR / 2 BA): $450–$550.",
                "Large House (4+ BR / 3+ BA): $550+.",
                "Prices vary based on home condition, specific requests, and how long it's been since the last deep clean. Homes in extreme condition may require a custom quote.",
            ],
        },
        "whyChoose": {
            "heading": "Why North Shore Homeowners Choose Marblehead Maids for Deep Cleaning",
            "items": [
                {"title": "We Don't Cut Corners", "description": "Our deep cleaning checklist is comprehensive, and we follow it completely. Every item gets addressed—no skipping, no shortcuts."},
                {"title": "Experienced Teams", "description": "Deep cleaning requires skill. Our teams know how to clean inside appliances without damage, how to treat different surfaces, and where hidden grime accumulates."},
                {"title": "Clear Communication", "description": "We'll walk you through exactly what's included before we start. No surprises about scope or pricing."},
                {"title": "Satisfaction Guaranteed", "description": "If you're not happy with any area, let us know within 24 hours and we'll come back to address it."},
            ],
        },
        "locations": {"heading": "Deep Cleaning Throughout North Shore & Essex County", "intro": "We proudly serve homes across North Shore and the surrounding communities."},
        "faq": {
            "heading": "Deep Cleaning FAQs",
            "items": [
                {"question": "How long does deep cleaning take?", "answer": "Most deep cleans take 4-6 hours depending on home size and condition. Larger homes or those that haven't been deep cleaned in years may take longer. We'll give you a time estimate with your quote."},
                {"question": "How often should I deep clean my home?", "answer": "For most North Shore homes, once or twice a year is sufficient — typically spring and fall. If you have pets, allergies, or a high-traffic household, you might benefit from quarterly deep cleans."},
                {"question": "Is deep cleaning worth the cost?", "answer": "If your home hasn't had professional attention in a while, absolutely. Deep cleaning addresses months or years of buildup that regular cleaning can't tackle. Most clients are amazed at the difference."},
                {"question": "Can you deep clean just certain rooms?", "answer": "Yes. If you only need the kitchen and bathrooms deep cleaned, or want to focus on specific areas, we can customize your service."},
                {"question": "Do I need to prepare anything?", "answer": "Clearing clutter and personal items from surfaces helps us work more efficiently. If you have specific areas of concern, let us know in advance."},
                {"question": "Can I add deep cleaning items to my regular service?", "answer": "Yes. Recurring clients can add deep cleaning extras (inside oven, inside fridge, etc.) to any regular visit. Many rotate through these items over time."},
            ],
        },
        "cta": {"title": "Give Your Home the Deep Clean It Deserves", "description": "There's nothing quite like walking into a truly clean home. Every surface gleaming, every corner addressed, every neglected spot finally taken care of. Book your deep clean today."},
    },
    "move-in-cleaning": {
        "slug": "move-in-cleaning",
        "pageTitle": "Move-In Cleaning North Shore MA — Start Fresh in Your New Place | Marblehead Maids",
        "metaDescription": "Start fresh. We'll clean every surface, drawer, and fixture in your new place before you unpack a single box.",
        "h1": "Move-In Cleaning in North Shore, MA — Walk Into a Home That's Actually Clean",
        "heroSubtitle": "The previous tenant said they cleaned. The landlord said it was 'move-in ready.' But you open the cabinets and there are crumbs. A move-in clean from Marblehead Maids means you're not unpacking into someone else's leftover mess.",
        "intro": {
            "heading": "Why Clean Before You Move In?",
            "paragraphs": [
                "Moving is the perfect — and maybe only — time to get your new home truly clean. Once your furniture, boxes, and belongings are in place, you'll never see those baseboards again.",
                "Right now, while the space is empty, is your one chance to clean every surface before it gets occupied. The floors can be mopped without navigating furniture. The closets can be wiped without removing clothes. The kitchen can be deep cleaned without working around your dishes.",
                "And let's be honest — no matter what the previous tenant claims, there's always something left behind. Dust in the vents. Hair in the bathroom drains. Grease on the range hood. A professional move-in clean eliminates all of that.",
            ],
        },
        "checklist": {
            "heading": "What's Included in Our Move-In Cleaning",
            "intro": "Our move-in cleaning is a comprehensive deep clean designed for empty homes. With no furniture to work around, we can reach everything—and we do.",
            "categories": [
                cat("Kitchen", ["All countertops cleaned and sanitized", "Inside all cabinets and drawers wiped out", "Inside refrigerator cleaned (shelves, drawers, walls)", "Inside oven and microwave cleaned", "Inside dishwasher cleaned", "Stovetop and range hood degreased", "Sink and faucet scrubbed", "Backsplash cleaned", "Floor thoroughly mopped", "Light fixtures and switches cleaned"]),
                cat("Bathroom(s)", ["All toilets deep cleaned and sanitized", "Showers and tubs scrubbed thoroughly", "Grout cleaned", "Inside vanity cabinets wiped", "Sinks and faucets cleaned", "Mirrors polished", "Medicine cabinets wiped inside", "Exhaust fans cleaned", "Floors mopped", "All fixtures polished"]),
                cat("Bedrooms & Living Areas", ["All floors vacuumed and mopped", "Inside all closets cleaned (shelves, rods, floors)", "Ceiling fans cleaned", "All windowsills and tracks cleaned", "Blinds dusted or wiped", "Light fixtures cleaned", "Light switches and outlets wiped", "Baseboards hand-wiped throughout", "Door frames and doors wiped"]),
                cat("Throughout", ["All air vents and returns cleaned", "Interior windows cleaned", "All baseboards wiped", "Cobwebs removed everywhere", "Any visible leftover items or debris flagged/removed"]),
            ],
        },
        "whenToBook": {
            "heading": "When to Book Move-In Cleaning",
            "options": [
                {"title": "After Lease Starts, Before Movers Arrive", "description": "The ideal timing. You get the keys to your new place, we come in and clean, and your moving day starts with a fresh home. Schedule us for the day after you get keys."},
                {"title": "During Lease Overlap", "description": "If you have access to your new place before your official move-in date, book us for that window. Your first night will be in a truly clean space."},
                {"title": "Between Tenants", "description": "Taking over a lease or moving into a place that was just vacated? Don't trust the outgoing tenant's cleaning. Let us make it actually clean."},
                {"title": "New Construction", "description": "Developers clean for appearance, not livability. New construction leaves behind dust in the vents, paint overspray, construction debris. Our post-construction cleaning handles all of that."},
                {"title": "Same-Week or Last Minute", "description": "Moving timelines shift — we get it. We often have same-week availability. Give us a call and we'll do our best to fit you in."},
            ],
        },
        "recurringTitle": "Keep Your New Home Fresh with Recurring Service",
        "recurringSubtitle": "After your move-in clean, maintain that fresh feeling on your schedule",
        "pricing": {
            "heading": "Move-In Cleaning Prices on the North Shore",
            "paragraphs": [
                "Move-in cleaning is priced as a deep clean since we're working through an entire empty home. The good news: empty spaces are easier to clean thoroughly.",
                "Studio Apartment (0 BR / 1 BA): $180–$240.",
                "1 BR Apartment (1 BR / 1 BA): $220–$300.",
                "2 BR Apartment (2 BR / 1 BA): $280–$380.",
                "3+ BR Apartment/House (3+ BR / 2+ BA): $380–$500+.",
                "New construction cleaning may cost more due to additional detail work. Final pricing depends on home size and condition.",
            ],
        },
        "whyChoose": {
            "heading": "Why North Shore Movers Choose Marblehead Maids",
            "items": [
                {"title": "We Work With Your Timeline", "description": "Moving schedules are unpredictable. We're flexible with booking and can often accommodate last-minute changes if your lease start shifts."},
                {"title": "Empty Space Expertise", "description": "We know how to maximize an empty apartment—reaching every corner, cleaning inside every cabinet, and leaving nothing for you to clean later."},
                {"title": "One Less Thing to Worry About", "description": "Moving is stressful. Cross cleaning off your list completely and focus on unpacking into a home that's already spotless."},
                {"title": "We Know Madison", "description": "Apartment complexes, condos, houses across the isthmus and suburbs — we've cleaned them all. Just give us access details and we'll handle the rest."},
            ],
        },
        "locations": {"heading": "Move-In Cleaning Throughout North Shore & Essex County", "intro": "We proudly serve homes and apartments across North Shore and the surrounding communities."},
        "faq": {
            "heading": "Move-In Cleaning FAQs",
            "items": [
                {"question": "How soon should I book my move-in cleaning?", "answer": "As soon as you know your move-in date, reach out. We often have same-week availability, but end of month books quickly — especially during UW-the North Shore's lease turnover season. A week's notice is ideal."},
                {"question": "Can you clean if there's still some stuff in the apartment?", "answer": "We can work around some items, but the cleaner the space, the more thorough we can be. If the previous tenant left furniture or boxes, let us know—we can still help."},
                {"question": "What if the apartment is in really bad condition?", "answer": "Some move-in situations are worse than others. If the previous tenant left significant mess, we may need to adjust scope and price. Send us photos if you're concerned."},
                {"question": "How do I give you access to the apartment?", "answer": "However works best — meet us there, leave keys in a lockbox, provide a code, or coordinate with your property manager."},
                {"question": "Can you clean rental properties between tenants?", "answer": "Absolutely. Property managers and landlords on the North Shore trust us for tenant turnover cleaning. Contact us about recurring partnership rates."},
                {"question": "Do you clean new construction apartments?", "answer": "Yes. New builds have unique needs—construction dust, debris, adhesive residue. We're experienced with new construction and know what to look for."},
            ],
        },
        "cta": {"title": "Start Your New Home the Right Way", "description": "You're starting a new chapter — don't let someone else's mess be part of the story. Book a move-in clean and walk into a home that's truly fresh, truly clean, and truly yours."},
    },
    "move-out-cleaning": {
        "slug": "move-out-cleaning",
        "pageTitle": "Move-Out Cleaning North Shore MA — Get Your Full Deposit Back | Marblehead Maids",
        "metaDescription": "Leave your place landlord-ready. Designed around what North Shore property managers actually inspect — so you get your deposit back.",
        "h1": "Move-Out Cleaning in North Shore, MA — Leave It Landlord-Ready, Get Your Deposit Back",
        "heroSubtitle": "Your deposit is on the line — and you've got enough to worry about. Our move-out cleaning covers everything landlords look for, so you can walk away with your full deposit and zero cleaning stress.",
        "intro": {
            "heading": "Move-Out Cleaning That Gets Your Deposit Back",
            "paragraphs": [
                "You've packed the boxes, filed your forwarding address, and coordinated the movers. But there's one thing standing between you and your full security deposit: the condition of the apartment.",
                "North Shore landlords and property managers have 21 days to return your deposit — and they'll deduct for anything that's not up to their standard. A professional move-out clean from Marblehead Maids eliminates that risk. We clean your space based on what landlords actually look for during their walk-through.",
                "The oven that always gets checked? We clean inside it. The baseboards nobody notices until move-out? We wipe every one. The grout in the bathroom? Scrubbed. We're not just cleaning your old place — we're protecting your deposit.",
            ],
        },
        "checklist": {
            "heading": "What's Included in Our Move-Out Cleaning",
            "intro": "Our move-out clean is comprehensive, covering everything that typically appears on North Shore landlord and property management inspection checklists. Nothing gets overlooked.",
            "categories": [
                cat("Kitchen", ["Inside oven cleaned (removing all grease and residue)", "Inside refrigerator cleaned (shelves, drawers, walls, seals)", "Inside microwave and dishwasher cleaned", "Stovetop and drip pans cleaned", "Range hood degreased", "All countertops cleaned and sanitized", "Sink and faucet scrubbed until shining", "Inside all cabinets and drawers wiped out", "Backsplash cleaned", "Floor swept and mopped thoroughly", "Light fixtures and switches cleaned"]),
                cat("Bathroom(s)", ["Toilets deep cleaned inside, outside, around, and behind", "Showers and tubs scrubbed completely", "Grout cleaned and treated", "Shower doors and tracks cleaned", "Inside vanity cabinets and drawers wiped", "Sinks and faucets polished", "Mirrors streak-free", "Medicine cabinets cleaned inside", "Exhaust fans cleaned", "Floors mopped", "All chrome and fixtures polished"]),
                cat("Bedrooms & Living Areas", ["All floors vacuumed and mopped", "Inside all closets cleaned (shelves, rods, floors)", "Ceiling fans cleaned", "Windowsills and tracks cleaned", "Blinds dusted or wiped", "Light fixtures cleaned", "Light switches and outlet covers wiped", "Baseboards hand-wiped throughout", "Door frames and doors wiped", "Walls spot-cleaned (scuffs and marks)"]),
                cat("Throughout", ["All air vents and returns cleaned", "Interior windows cleaned", "Any debris or trash removed", "Final walk-through to check our work"]),
            ],
        },
        "whenToBook": {
            "heading": "When to Book Move-Out Cleaning",
            "options": [
                {"title": "After Furniture Out, Before Walk-Through", "description": "The perfect timing. Your furniture and boxes are out, we clean thoroughly, and you arrive to your inspection confident. Schedule us 1-2 days before your walk-through if possible."},
                {"title": "Same-Day as Move-Out", "description": "Moving and need us that same day? We can often accommodate tight timelines. You move out in the morning, we clean in the afternoon, inspection happens after."},
                {"title": "Last-Minute Bookings", "description": "We know moves rarely go perfectly to plan. If you need us in 24-48 hours, reach out—we'll do our best to fit you in."},
                {"title": "End of Month Rush", "description": "Most North Shore leases end at the end of the month. This is our busiest time — book early if your move-out falls then."},
                {"title": "Before Listing for Sale", "description": "Selling your condo or co-op? A thorough cleaning makes showings more impressive and helps buyers see the space without distraction."},
            ],
        },
        "recurringTitle": "Starting Fresh? Keep It That Way",
        "recurringSubtitle": "After your move, set up recurring service at your new place",
        "pricing": {
            "heading": "Move-Out Cleaning Prices on the North Shore",
            "paragraphs": [
                "Move-out cleaning is priced as a deep clean because we're cleaning to inspection standards. Think of it as the cost of protecting your deposit — which on the North Shore is often one to two months' rent.",
                "Studio Apartment (0 BR / 1 BA): $200–$260.",
                "1 BR Apartment (1 BR / 1 BA): $250–$340.",
                "2 BR Apartment (2 BR / 1-2 BA): $320–$420.",
                "3+ BR Apartment/House (3+ BR / 2+ BA): $420–$550+.",
                "Condition matters. If the property has significant buildup or hasn't been cleaned regularly, additional time and cost may be required. Send us photos for an accurate quote.",
            ],
        },
        "whyChoose": {
            "heading": "Why North Shore Renters Choose Marblehead Maids for Move-Out",
            "items": [
                {"title": "We Know What Landlords Check", "description": "We've cleaned thousands of move-outs across the North Shore. We know the inspection checklist — the oven, the grout, the baseboards, the refrigerator seals. We hit every spot."},
                {"title": "Deposit Protection Guarantee", "description": "If your landlord identifies a cleaning issue that we were responsible for, let us know within 24 hours and we'll come back to address it at no charge."},
                {"title": "Flexible Scheduling", "description": "Moving timelines shift constantly. We work with your schedule and can accommodate last-minute changes when possible."},
                {"title": "One Less Stress", "description": "You've got enough on your plate. Hand off the cleaning—we've got it covered."},
            ],
        },
        "locations": {"heading": "Move-Out Cleaning Throughout North Shore & Essex County", "intro": "We proudly serve apartments and homes across North Shore and the surrounding communities."},
        "faq": {
            "heading": "Move-Out Cleaning FAQs",
            "items": [
                {"question": "How soon before my move-out should I book?", "answer": "Ideally, give us a week's notice. We can often accommodate shorter timelines, but end-of-month dates book quickly. Once you know your move-out date, reach out."},
                {"question": "Do I need to be completely moved out?", "answer": "The more that's moved out, the better we can clean. We can work around some remaining items if your timeline is tight, but an empty space lets us reach every surface."},
                {"question": "What about carpet cleaning?", "answer": "Our service includes vacuuming, but professional carpet shampooing is separate. If your lease requires carpet cleaning, let us know and we can recommend providers or arrange it alongside our cleaning."},
                {"question": "What about the walls?", "answer": "We spot-clean scuffs and marks. If your walls need repainting or have significant damage, that's beyond cleaning scope—but basic spots, we handle."},
                {"question": "Can you help if the walk-through finds issues?", "answer": "Call us immediately. Depending on availability, we may be able to come back that same day to address concerns."},
                {"question": "Do you work with management companies?", "answer": "Yes. Many North Shore management companies and landlords use us for turnover cleaning between tenants. Contact us about partnerships."},
            ],
        },
        "cta": {"title": "Move Out Without the Cleaning Stress", "description": "You've got enough on your plate. Let us handle the cleaning — the right way, to inspection standards — so you can focus on your move and walk away with your deposit intact."},
    },
    "post-construction-cleaning": {
        "slug": "post-construction-cleaning",
        "pageTitle": "Post-Construction Cleaning North Shore MA — Dust & Debris Removal | Marblehead Maids",
        "metaDescription": "Renovation dust doesn't clean itself. We handle drywall dust, paint residue, adhesive removal, and construction debris.",
        "h1": "Post-Construction Cleaning in North Shore, MA — From Construction Zone to Move-In Ready",
        "heroSubtitle": "The renovation is done. The new kitchen looks incredible. But there's a fine layer of drywall dust on everything you own, paint flecks on the window frames, and adhesive residue on the new floors. Marblehead Maids provides multi-phase post-construction cleaning for homes across the North Shore.",
        "intro": {
            "heading": "Why Post-Construction Cleaning Requires Specialists",
            "paragraphs": [
                "Construction dust isn't normal dust. It's finer, it gets into everything, and it doesn't respond to a standard vacuum and microfiber cloth. The contractor's crew did a quick sweep and called it clean.",
                "Construction dust — from drywall, sawing, sanding — is incredibly fine. It becomes airborne easily and settles into places regular cleaning never touches. It gets into your HVAC system and redistributes throughout the home every time the air kicks on.",
                "Contractors often do a basic cleanup — sweep the floors, wipe the major surfaces — but they're not in the business of detailed cleaning. Post-construction cleaning requires specific techniques, multiple passes, and attention to the unique hiding spots of construction dust.",
            ],
        },
        "checklist": {
            "heading": "What's Included in Our Post-Construction Cleaning",
            "intro": "Our post-construction cleaning is a multi-phase process designed to remove construction dust and debris from every surface in your newly built or renovated space.",
            "categories": [
                cat("Kitchen", ["Inside all cabinets and drawers wiped (construction dust gets everywhere)", "All countertops thoroughly cleaned", "All appliances cleaned inside and out", "Sink and fixtures polished", "Backsplash cleaned", "Range hood cleaned", "Floors cleaned multiple times if needed", "Light fixtures and switches cleaned"]),
                cat("Bathroom(s)", ["All fixtures cleaned and polished", "Inside cabinets and drawers wiped", "Tile and grout cleaned", "Mirrors and glass cleaned (often multiple passes needed)", "Toilets, showers, and tubs sanitized", "Exhaust fans cleaned", "Floors mopped"]),
                cat("Bedrooms & Living Areas", ["All floors vacuumed and mopped (multiple times if needed)", "Inside all closets cleaned", "Ceiling fans cleaned", "All windowsills and tracks cleaned", "Blinds dusted or wiped", "Light fixtures cleaned", "Light switches and outlets wiped", "Baseboards hand-wiped throughout", "Door frames and doors wiped"]),
                cat("Throughout", ["All surfaces wiped to remove dust film", "Ceilings dusted", "Walls wiped or dusted", "All woodwork, trim, and molding wiped", "Air vents and returns removed and cleaned", "Interior windows cleaned", "Sticker and label removal from new surfaces", "Adhesive residue removal", "Paint drip spot-cleaning where possible"]),
            ],
        },
        "whenToBook": {
            "heading": "When to Book Post-Construction Cleaning",
            "options": [
                {"title": "After All Trades Are Complete", "description": "Schedule after all construction work is done, final inspections complete, and no more dust-generating work will happen. Cleaning before construction ends means the dust comes right back."},
                {"title": "Before Final Punch List Walk", "description": "If you have a final walk-through with your contractor, having the space cleaned makes it easier to identify actual defects vs. dust covering them."},
                {"title": "Before Moving In", "description": "Don't unpack into construction dust. Schedule cleaning after construction completes but before your belongings arrive. You'll enjoy your new space immediately."},
                {"title": "After a Renovation Project", "description": "Kitchen remodel, bathroom update, or room renovation complete? Renovation dust migrates throughout the home. We'll clean the renovated space plus any areas affected by dust."},
                {"title": "New Development Move-In", "description": "Moving into a newly built home or condo? Developer cleaning is notoriously minimal. We make it actually livable."},
            ],
        },
        "recurringTitle": "Maintain Your Renovated Space",
        "recurringSubtitle": "After the construction dust settles, keep it clean with regular service",
        "pricing": {
            "heading": "Post-Construction Cleaning Prices on the North Shore",
            "paragraphs": [
                "Post-construction cleaning is priced based on scope—full gut renovation vs. single-room remodel, apartment size, and current condition. Because it often requires multiple passes and specialized attention, it typically costs more than standard cleaning.",
                "Bathroom Renovation: $200–$350.",
                "Kitchen Remodel: $300–$450.",
                "Major Renovation: $500–$800.",
                "Full Gut Renovation (1BR): $450–$650.",
                "Full Gut Renovation (2BR): $650–$900.",
                "Full Gut Renovation (3BR+): $900+.",
                "These are estimates. Pricing depends heavily on condition. Heavy dust accumulation, debris, or extensive detail work will affect final price. We recommend photos or an on-site assessment for accurate quoting.",
            ],
        },
        "whyChoose": {
            "heading": "Why North Shore Contractors & Homeowners Choose Marblehead Maids",
            "items": [
                {"title": "We Understand Construction Dust", "description": "We know it's different from regular cleaning. We know it settles for days. We know it hides in vents, tracks, and crevices. We clean accordingly."},
                {"title": "Multiple-Pass Process", "description": "We don't do one wipe and call it done. Our process includes rough clean, detail clean, and touch-up as needed because construction dust keeps settling."},
                {"title": "Safe for New Surfaces", "description": "We know how to clean brand-new countertops, fresh paint, new flooring, and delicate fixtures without causing damage."},
                {"title": "Contractor Partnerships", "description": "We work with North Shore contractors and developers who need reliable cleaning before closings. Ask about our contractor rates."},
            ],
        },
        "locations": {"heading": "Post-Construction Cleaning Throughout North Shore & Essex County", "intro": "We proudly serve homes across North Shore and the surrounding communities."},
        "faq": {
            "heading": "Post-Construction Cleaning FAQs",
            "items": [
                {"question": "Is post-construction cleaning different from deep cleaning?", "answer": "Yes. Post-construction cleaning specifically addresses construction dust, adhesive residue, and new-build debris. It often requires multiple passes because construction dust continues to settle. Different mess, different approach."},
                {"question": "Why does dust keep appearing after cleaning?", "answer": "Fine construction dust becomes airborne and continues to settle for several days after construction. This is normal. Some homeowners schedule a touch-up cleaning a few days after the initial clean."},
                {"question": "Should I change my HVAC filter after construction?", "answer": "Absolutely—and again a week or two later. Construction dust fills filters quickly. You may also want professional duct cleaning if significant construction occurred with the HVAC running."},
                {"question": "Can you remove paint drips or caulk mess?", "answer": "We can carefully remove paint drips from hard surfaces if they'll come up without damage. Heavy paint or caulk issues may need to be addressed by your contractor."},
                {"question": "How long does post-construction cleaning take?", "answer": "It depends on scope and condition. A bathroom renovation might take 2-3 hours. A full gut renovation might take 6-10+ hours (sometimes across multiple visits)."},
                {"question": "Do you work with contractors directly?", "answer": "Yes. We work with North Shore contractors, developers, and property managers who need reliable cleaning before closings or move-ins. Contact us about partnership rates."},
            ],
        },
        "cta": {"title": "Turn Your Construction Zone Into a Home", "description": "You've waited through months of renovation. Don't spend another day living with dust. Let us finish what your contractor started and make your new space move-in ready."},
    },
    "airbnb-rental-cleaning": {
        "slug": "airbnb-rental-cleaning",
        "pageTitle": "Airbnb & Rental Cleaning North Shore MA — Fast Turnovers, 5-Star Reviews | Marblehead Maids",
        "metaDescription": "Same-day turnovers, linen changes, restocking, and damage reports. Reliable cleaning that protects your reviews — every guest, every time.",
        "h1": "Airbnb & Short-Term Rental Cleaning in North Shore, MA",
        "heroSubtitle": "Guest-ready, every time. Marblehead Maids provides fast, reliable turnover cleaning for Airbnb, VRBO, and short-term rental hosts across North Shore — with the speed, consistency, and reliability your reviews depend on.",
        "intro": {
            "heading": "Turnover Cleaning That Protects Your Reviews",
            "paragraphs": [
                "Your guest checks out at 11 AM. The next one checks in at 4 PM. In between, your rental needs to go from \"lived in for three days\" to \"looks like no one's ever touched it.\" Every. Single. Time.",
                "One missed hair in the bathtub. One sticky counter. One dusty nightstand. That's the difference between a 5-star review and a complaint. Marblehead Maids provides turnover cleaning for Airbnb, VRBO, and short-term rental hosts across North Shore — with the speed, consistency, and reliability your reviews depend on.",
            ],
        },
        "checklist": {
            "heading": "What's Included in Every Turnover Clean",
            "intro": "Our turnover cleaning goes beyond basic housekeeping. We handle everything needed to make your rental guest-ready — from sanitization to staging.",
            "categories": [
                cat("Full Guest-Ready Clean", ["Every surface a guest might see or touch cleaned and sanitized", "Countertops, appliances, sinks, toilets, showers, mirrors", "Floors vacuumed, swept, and mopped throughout", "Furniture surfaces dusted and wiped", "Door handles, light switches, and remotes sanitized", "Trash and recycling taken out"]),
                cat("Linen Service", ["Beds stripped and remade with fresh linens", "Towels replaced with clean sets", "Used linens collected for laundering", "On-site laundry available or coordination with your linen service"]),
                cat("Kitchen Reset", ["Dishes washed and put away (if guests left them)", "Counters cleared and wiped", "Coffee maker, microwave, and stovetop cleaned", "Inside refrigerator cleared and wiped", "Trash and recycling taken out"]),
                cat("Restocking & Staging", ["Toilet paper, paper towels, soap, and coffee checked and restocked", "Supplies restocked to your specifications", "Pillows fluffed, throws folded, welcome materials placed", "Toiletries arranged for a listing-photo finish", "Damage and issues flagged with photos before next guest arrives"]),
            ],
        },
        "whenToBook": {
            "heading": "Scheduling Options for Hosts",
            "options": [
                {"title": "Same-Day Turnovers", "description": "Guest checks out in the morning, next guest arrives in the afternoon. We schedule turnover cleans with specific arrival windows — your next guest is never waiting because we ran late."},
                {"title": "Back-to-Back Weekends", "description": "High season on the North Shore means constant bookings. We handle recurring weekend turnovers on a consistent schedule so you never have to scramble."},
                {"title": "Last-Minute & Flexible", "description": "Guest extended their stay? Early check-in request? Double booking? We handle schedule changes and last-minute requests because we know that's the reality of hosting."},
                {"title": "Seasonal Properties", "description": "Not every property is booked every weekend. We'll clean when you need us — three times a week in summer or once a month in winter."},
                {"title": "Multi-Property Management", "description": "Managing two, five, or twenty rental properties in the North Shore area? We can handle all of them with dedicated account management and volume pricing."},
            ],
        },
        "recurringTitle": None,
        "recurringSubtitle": None,
        "pricing": None,
        "whyChoose": {
            "heading": "Why North Shore Hosts Choose Marblehead Maids",
            "items": [
                {"title": "We Understand the Clock", "description": "Same-day turnovers leave no room for \"we'll be there sometime this afternoon.\" We schedule with specific arrival windows and communicate if anything changes."},
                {"title": "Consistency That Protects Your Reviews", "description": "Your listing depends on every single stay being clean. We use a standardized checklist for your property so the clean is identical regardless of which team member is there."},
                {"title": "We Think Like a Host", "description": "We don't just clean — we walk through as if we were the guest checking in. Is the bed perfectly made? Is there a weird smell? Did the last guest leave a mess in a spot a normal cleaner would miss?"},
                {"title": "Damage & Issue Reporting", "description": "We'll flag anything unusual — stains, damage, broken items, missing inventory — and send you a report with photos before the next guest arrives. This protects you on damage claims."},
            ],
        },
        "locations": {"heading": "Rental Turnover Cleaning Throughout North Shore & Essex County", "intro": "We serve short-term rental hosts across North Shore and the surrounding communities."},
        "faq": {
            "heading": "Common Questions for Hosts",
            "items": [
                {"question": "Can you handle back-to-back same-day turnovers?", "answer": "Yes. If you have a checkout at 11 AM and check-in at 3 PM, we plan accordingly. We'll let you know during setup if your window is too tight for the property size."},
                {"question": "Do you provide linens and supplies?", "answer": "We can work with your linens and supplies, source them for you, or integrate with a linen service. Whatever works for your operation."},
                {"question": "What if a guest leaves the place in terrible shape?", "answer": "We handle it. Heavily soiled turnovers may take longer and cost more, but we'll communicate that to you before the next guest arrives — along with photo documentation for any damage claims."},
                {"question": "Can you handle seasonal properties or irregular bookings?", "answer": "Absolutely. Not every property is booked every weekend. We'll clean when you need us, whether that's three times a week in summer or once a month in winter."},
                {"question": "I manage the property remotely — is that a problem?", "answer": "Not at all. Many of our host clients live outside the North Shore. We communicate everything via text, email, or app — including post-clean confirmation and damage reports."},
                {"question": "How is turnover cleaning priced?", "answer": "Pricing depends on property size, scope of work (laundry, restocking, staging), and volume. Hosts with consistent weekly bookings benefit from per-turnover rates that are more favorable than one-off cleanings. We price per turnover, not hourly."},
            ],
        },
        "cta": {"title": "Your Reviews Depend on Your Cleaning", "description": "One bad cleaning can mean one bad review. And one bad review can cost you bookings for months. Let's make sure that doesn't happen."},
    },
    "commercial-cleaning": {
        "slug": "commercial-cleaning",
        "pageTitle": "Commercial Cleaning North Shore MA — Offices, Retail & Business Spaces | Marblehead Maids",
        "metaDescription": "Offices, retail, medical, and business spaces cleaned on your schedule. Evening and weekend availability, dedicated teams, no long-term contracts.",
        "h1": "Commercial Cleaning in North Shore, MA — Clean Workspace, Zero Hassle",
        "heroSubtitle": "A clean workspace affects how your employees feel, how clients perceive your business, and how much sick time your team takes. Marblehead Maids provides commercial cleaning for offices, retail, medical facilities, and more — scheduled around your business hours.",
        "intro": {
            "heading": "Commercial Spaces We Clean",
            "paragraphs": [
                "A dirty office isn't just unpleasant — it affects how your employees feel, how clients perceive your business, and how much sick time your team takes. But managing a cleaning crew shouldn't be part of your job description.",
                "Marblehead Maids provides commercial cleaning across the North Shore and North Suburbs for offices, retail spaces, medical facilities, and more. Our teams are trained, insured, and scheduled around your business hours — so you walk in every morning to a clean space without lifting a finger.",
                "From single-suite offices on the Capitol Square to multi-floor spaces on the west side, retail stores and showrooms, medical and dental offices, restaurants and food service, and property management common areas — we customize our service to fit any commercial space.",
            ],
        },
        "checklist": {
            "heading": "What's Included in Commercial Cleaning",
            "intro": "Our commercial cleaning covers everything your business needs to maintain a professional, healthy environment — from daily maintenance to periodic deep services.",
            "categories": [
                cat("Standard Recurring Service", ["Trash removal and liner replacement", "Restroom cleaning and restocking", "Floor vacuuming, sweeping, and mopping", "Surface dusting and wiping", "Kitchen/break room cleaning and sanitization", "Glass and mirror cleaning", "Door handle and high-touch surface sanitization"]),
                cat("Offices & Coworking Spaces", ["Desks and workstation surfaces wiped", "Conference rooms cleaned and reset", "Break rooms and kitchenettes sanitized", "Lobby and reception areas maintained", "Common area restrooms cleaned daily"]),
                cat("Retail & Medical Spaces", ["Retail floors cleaned and displays dusted", "Fitting rooms and customer areas maintained", "Waiting rooms and exam rooms cleaned to higher standard", "Sanitization best practices for healthcare environments", "Restaurant kitchen deep cleaning and dining room maintenance"]),
                cat("Periodic Deep Services (Add-On)", ["Carpet extraction cleaning", "Hard floor stripping and waxing", "Window cleaning (interior)", "Upholstery and fabric cleaning", "HVAC vent and light fixture cleaning", "Post-event cleanup"]),
            ],
        },
        "whenToBook": {
            "heading": "Scheduling Options for Your Business",
            "options": [
                {"title": "Daily Cleaning", "description": "High-traffic offices, medical facilities, and retail spaces that need nightly or early-morning cleaning to start fresh every day."},
                {"title": "Weekly or Biweekly", "description": "Smaller offices, coworking spaces, or businesses that don't need daily service but want consistent upkeep on a regular schedule."},
                {"title": "After-Hours & Weekends", "description": "Most businesses don't want a cleaning crew around during work hours. We offer evening, overnight, and weekend scheduling so your space is clean before the first person walks in."},
                {"title": "One-Time or Event Cleanup", "description": "Post-event cleanup, pre-inspection cleaning, or one-time deep cleans for commercial spaces — available on demand."},
                {"title": "New Office Setup", "description": "Moving into a new commercial space? We'll get it clean before your team moves in and set up a recurring plan going forward."},
            ],
        },
        "recurringTitle": None,
        "recurringSubtitle": None,
        "pricing": None,
        "whyChoose": {
            "heading": "Why North Shore Businesses Choose Marblehead Maids",
            "items": [
                {"title": "Flexible Scheduling — Including After Hours", "description": "We offer evening, overnight, and weekend scheduling so your space is clean before the first person walks in. No disruption to your workday."},
                {"title": "Consistent Teams, Not Rotating Strangers", "description": "We assign dedicated teams to your account. They learn your space, your preferences, and your expectations. If something isn't right, the same people come back to fix it."},
                {"title": "No Long-Term Contracts", "description": "Our service agreements are month-to-month. We keep your business by earning it, not by trapping you in annual agreements with cancellation fees."},
                {"title": "Fully Insured & Background-Checked", "description": "Every team member is background-checked and our business carries full commercial general liability insurance. We'll provide a certificate of insurance on request."},
            ],
        },
        "locations": {"heading": "Commercial Cleaning Throughout North Shore & Essex County", "intro": "We serve businesses across downtown, the Capitol Square area, the west side tech corridor, east side commercial districts, and suburban business parks."},
        "faq": {
            "heading": "Common Questions About Commercial Cleaning",
            "items": [
                {"question": "How much does commercial cleaning cost on the North Shore?", "answer": "Pricing depends on square footage, scope of work, frequency, and scheduling requirements. We provide a flat monthly quote based on your specific needs — no hourly billing."},
                {"question": "Can you start this week?", "answer": "For smaller spaces, we can often begin within a week. Larger accounts typically require a walk-through and setup time. Contact us and we'll give you a realistic timeline."},
                {"question": "Do you provide cleaning supplies?", "answer": "Yes. We bring all supplies and equipment. If your facility requires specific products (e.g., green-certified, fragrance-free), we'll accommodate."},
                {"question": "What happens on holidays?", "answer": "We'll work out a holiday schedule with you in advance. Most clients skip major holidays and adjust the cleaning schedule around them."},
                {"question": "Can you handle one-time commercial cleaning?", "answer": "Yes — post-event cleanup, pre-inspection cleaning, or one-time deep cleans for commercial spaces are available."},
                {"question": "What types of businesses do you work with?", "answer": "Our clients include law firms, tech companies, medical practices, real estate offices, retail stores, restaurants, nonprofits, and property management companies across the North Shore and North Suburbs."},
            ],
        },
        "cta": {"title": "Ready for a Cleaner Workspace?", "description": "Tell us about your space and what you need. We'll schedule a walk-through and send you a detailed, no-obligation quote."},
    },
}

if __name__ == "__main__":
    SOURCE.write_text(json.dumps(PAGES, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {SOURCE} ({len(PAGES)} services)")
