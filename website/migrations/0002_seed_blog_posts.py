from datetime import timedelta

from django.db import migrations
from django.utils import timezone


def seed_blog_posts(apps, schema_editor):
    BlogPost = apps.get_model("website", "BlogPost")
    User = apps.get_model("auth", "User")
    author = User.objects.filter(is_superuser=True).first()
    author_id = author.pk if author else None

    base_date = timezone.now()
    posts = [
        {
            "slug": "luxury-buyers-checklist-2026",
            "title": "A Smart Checklist for Luxury Home Buyers in 2026",
            "excerpt": "From inspections to title review, the high-end market rewards buyers who stay organized and patient.",
            "body": """Buying a luxury home is as much about process as it is about the property itself. Start with a clear budget that includes closing costs, insurance, and any planned renovations.

Work with a lender who understands jumbo and portfolio loans, and get pre-underwritten early so your offer carries real weight. On the tour side, look beyond staging: ask about systems (HVAC, roof, smart home), association rules if applicable, and any recent capital projects.

Always invest in a thorough inspection—even new construction benefits from a second set of eyes. Finally, review title and easements carefully; waterfront, hillside, and estate parcels often carry surprises that are easier to resolve before you close.""",
        },
        {
            "slug": "staging-that-sells-high-end-homes",
            "title": "Staging Strategies That Help High-End Homes Sell Faster",
            "excerpt": "Thoughtful staging highlights architecture and flow without distracting from the space.",
            "body": """In luxury real estate, buyers are imagining a lifestyle. Staging should feel aspirational but believable—neutral palettes, quality textiles, and art that complements sight lines rather than competing with them.

Prioritize the primary suite, kitchen, and main living areas; these photos drive online engagement. Remove personal photos and excess clutter so rooms feel larger and calmer.

Lighting matters enormously: layer ambient, task, and accent light, and ensure every bulb matches in temperature. Outside, refresh landscaping, power-wash hardscapes, and define outdoor “rooms” with seating.

Small investment in styling often shortens days on market and can support a stronger negotiated outcome.""",
        },
        {
            "slug": "interest-rates-and-luxury-market",
            "title": "How Interest Rates Shape the Luxury Property Market",
            "excerpt": "Cash-heavy segments react differently than the broader market—here is what to watch.",
            "body": """Luxury markets are not monolithic. In city condos and second-home destinations, all-cash or low-leverage buyers may barely feel rate changes. In suburban move-up segments, financing sensitivity is higher.

When rates rise, inventory can grow slightly as buyers pause—but quality listings in prime locations often still attract competition. When rates ease, well-priced properties can see renewed bidding activity.

If you are financing, compare fixed versus adjustable structures with your advisor, especially if you plan to hold short term or expect liquidity events. For sellers, the lesson is timeless: prepare the home, price with current comps, and market globally where appropriate.""",
        },
        {
            "slug": "investing-in-vacation-rentals",
            "title": "What to Know Before Investing in a Vacation Rental",
            "excerpt": "Regulations, seasonality, and operating costs can make or break the numbers.",
            "body": """Vacation rentals can diversify a portfolio, but underwriting must be realistic. Research local short-term rental regulations; some cities cap nights, require licenses, or restrict non-owner operators.

Model revenue with conservative occupancy and compare peak versus shoulder seasons. Budget for property management, turnover cleaning, maintenance, insurance specific to rentals, and furniture replacement.

Tax treatment and depreciation differ from long-term rentals—consult a CPA familiar with hospitality real estate. If the property doubles as your retreat, plan how personal use interacts with income reporting.

The best opportunities combine strong tourism or business travel demand with sensible local rules and a floor plan guests actually want to book.""",
        },
        {
            "slug": "choosing-the-right-neighborhood",
            "title": "Choosing the Right Neighborhood for Your Next Move",
            "excerpt": "Schools, commute, amenities, and future development all belong on your scorecard.",
            "body": """House hunting should start with neighborhood fit. List non-negotiables: commute time, school districts, walkability, noise tolerance, and proximity to family or work.

Visit at different times of day. Morning traffic, evening light, and weekend foot traffic tell a fuller story than a single open house. Check municipal plans for upcoming construction that could affect views or access.

Talk to neighbors when appropriate; they often share insights agents cannot. For condos and townhomes, read resale minutes and reserve studies if available—the health of the association matters as much as the unit.

A great home in the wrong location rarely feels like a win long term.""",
        },
        {
            "slug": "selling-your-home-winter-guide",
            "title": "Selling Your Home in Winter: Myths and Opportunities",
            "excerpt": "Fewer listings can mean more serious buyers—if you present the home well.",
            "body": """Many sellers wait for spring, but winter buyers are often motivated—job relocations, tax planning, or life changes do not follow the weather.

Keep entries clear of snow and ice, maintain warm and bright lighting, and emphasize cozy, efficient systems (newer furnace, smart thermostat, insulation upgrades). Professional photos still matter; capture evergreen exterior if snow is patchy.

Price in line with recent closed sales, not aspirational spring numbers from years past. Be flexible on showings within reason; limited daylight means scheduling matters.

With the right presentation and realistic pricing, winter can be an excellent time to stand out with less competition.""",
        },
        {
            "slug": "new-construction-vs-resale",
            "title": "New Construction vs. Resale: Which Fits Your Goals?",
            "excerpt": "Warranties and customization compete with character and established neighborhoods.",
            "body": """New construction offers modern floor plans, energy efficiency, and builder warranties. You may wait months for completion and should scrutinize contracts, upgrade pricing, and punch-list processes.

Resale homes deliver mature landscaping, established neighbors, and often superior locations where land is scarce. Updates and maintenance are part of the tradeoff.

Ask how long you plan to stay. If you need to move quickly, resale may win. If you want every finish your way and can tolerate build timelines, new homes shine.

Either path benefits from independent representation—your advisor should review documents and compare net costs apples to apples.""",
        },
        {
            "slug": "eco-friendly-upgrades-value",
            "title": "Eco-Friendly Upgrades That Can Add Real Value",
            "excerpt": "Efficiency improvements increasingly influence both appraisals and buyer perception.",
            "body": """High-performance windows, improved insulation, and modern heat pumps can reduce operating costs while improving comfort—especially in climates with hot summers or cold winters.

Solar paired with storage may appeal in regions with favorable net metering, but evaluate roof age, orientation, and local incentives before committing. Smart irrigation, native landscaping, and rainwater capture support curb appeal with lower upkeep.

Document upgrades with receipts and model numbers; they help appraisers and future buyers understand quality. Not every green project pays back equally, so prioritize measures your market rewards and that align with your hold period.""",
        },
        {
            "slug": "global-buyers-us-luxury-real-estate",
            "title": "A Primer for Global Buyers in U.S. Luxury Real Estate",
            "excerpt": "Tax, titling, and FIRPTA considerations deserve a specialized team.",
            "body": """International clients are drawn to U.S. stability, educational options, and diverse luxury inventory. Early planning prevents friction: engage a real estate attorney, lender familiar with foreign national programs, and a CPA who understands cross-border rules.

Understand how you will hold title—individual, entity, or trust—and implications for financing and future sale. FIRPTA withholding may apply on disposition; structure and withholding certificates can matter.

Currency timing and repatriation plans should align with your overall wealth strategy. On the ground, focus on markets with transparent data, strong property rights, and professional representation.

With the right advisors, a U.S. luxury purchase can be efficient and secure.""",
        },
        {
            "slug": "preparing-for-the-home-inspection",
            "title": "Preparing for the Home Inspection: A Seller’s Playbook",
            "excerpt": "Small fixes now reduce renegotiation later and keep momentum to closing.",
            "body": """Before the inspector arrives, service major systems—HVAC tune-up, gutter cleaning, and testing of smoke and CO detectors. Replace obvious burned-out bulbs; they otherwise get flagged as potential electrical issues.

Provide attic and crawlspace access, and clear the electrical panel. Disclose known defects honestly; transparency builds trust and reduces legal risk.

Leave utilities on and leave a note if any systems are winterized. If you have recent receipts for roof, pest, or foundation work, leave copies for the buyer side.

A smooth inspection supports the emotional arc of the sale: confidence on both sides makes for cleaner amendments and an on-time close.""",
        },
    ]

    for i, row in enumerate(posts):
        published_at = base_date - timedelta(days=(len(posts) - i) * 5)
        BlogPost.objects.update_or_create(
            slug=row["slug"],
            defaults={
                "title": row["title"],
                "excerpt": row["excerpt"],
                "body": row["body"],
                "is_published": True,
                "published_at": published_at,
                "author_id": author_id,
            },
        )


def unseed_blog_posts(apps, schema_editor):
    BlogPost = apps.get_model("website", "BlogPost")
    slugs = [
        "luxury-buyers-checklist-2026",
        "staging-that-sells-high-end-homes",
        "interest-rates-and-luxury-market",
        "investing-in-vacation-rentals",
        "choosing-the-right-neighborhood",
        "selling-your-home-winter-guide",
        "new-construction-vs-resale",
        "eco-friendly-upgrades-value",
        "global-buyers-us-luxury-real-estate",
        "preparing-for-the-home-inspection",
    ]
    BlogPost.objects.filter(slug__in=slugs).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_blog_posts, unseed_blog_posts),
    ]
