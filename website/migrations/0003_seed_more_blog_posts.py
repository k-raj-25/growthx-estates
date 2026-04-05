from datetime import timedelta

from django.db import migrations
from django.utils import timezone


def seed_more_blog_posts(apps, schema_editor):
    BlogPost = apps.get_model("website", "BlogPost")
    User = apps.get_model("auth", "User")
    author = User.objects.filter(is_superuser=True).first()
    author_id = author.pk if author else None

    base_date = timezone.now()
    posts = [
        {
            "slug": "condo-vs-coop-urban-buying",
            "title": "Condo vs. Co-op: What Urban Buyers Should Know",
            "excerpt": "Board approvals, financing rules, and monthly fees differ more than you might expect.",
            "body": """In many cities, co-ops dominate certain neighborhoods while condos offer a more familiar ownership structure. Co-ops are technically shares in a corporation; boards often interview buyers and can turn down offers for reasons condos cannot.

Financing can be trickier for co-ops—higher down payments and fewer lender options are common. Condos usually allow more flexibility and may be easier to rent out later, but association docs still matter.

Compare monthly charges apples to apples: what covers taxes, insurance, reserves, and utilities? Ask for recent assessments and planned projects. Your attorney should review minutes and financials before you waive contingencies.

Neither is universally “better”; fit depends on your timeline, liquidity, privacy tolerance, and long-term plans.""",
        },
        {
            "slug": "multiple-offers-winning-strategy",
            "title": "Multiple Offers: How to Compete Without Regret",
            "excerpt": "Strong terms and clarity beat guessing at an arbitrary ceiling.",
            "body": """In competitive markets, price is only one lever. Sellers often favor certainty: shorter contingencies when responsible, reputable inspectors, and lenders with a track record of closing on time.

A personal letter can help—or hurt—depending on local norms and fair housing sensitivities; follow your agent’s guidance. Escalation clauses require careful drafting so you do not overexpose your max unintentionally.

Earnest money and down payment percentages signal seriousness. If you can shorten the rent-back or flex on closing date to match the seller’s move, do it when it is low risk for you.

Decide your walk-away number in advance so decisions under pressure align with your plan, not panic.""",
        },
        {
            "slug": "downsizing-after-empty-nest",
            "title": "Downsizing After the Empty Nest: A Calm, Practical Plan",
            "excerpt": "Rightsizing space can free time and budget—if you edit possessions and expectations together.",
            "body": """Start with how you want to live day to day: hosting frequency, hobbies, work-from-home needs, and travel. That drives square footage and layout more than nostalgia for every old room.

Audit furniture and storage early; donate, sell, or digitize before you list your current home. If you are moving to a condo, measure elevators and door swings—large pieces do not always make the trip.

Tax and timing can matter when proceeds fund the next purchase; coordinate with your accountant. Emotional drift is normal; give yourselves milestones and celebrate progress.

The goal is a home that fits today’s life, not yesterday’s headcount.""",
        },
        {
            "slug": "waterfront-home-essentials",
            "title": "Buying Waterfront: Docks, Flood Zones, and Insurance Reality",
            "excerpt": "Riparian rights and storm risk belong in the same conversation as the view.",
            "body": """Waterfront property is desirable—and complex. Confirm what you actually own: shoreline, dock permits, shared access, and any leasehold interests. Environmental rules can limit expansions or repairs.

Flood insurance and elevation certificates affect costs and sometimes financing. Ask about historical flooding, bulkheads, seawalls, and maintenance obligations.

Inspections should include moisture, foundations, and exterior systems battered by weather. If the home is a vacation asset, plan for off-season checks and reliable local vendors.

When diligence matches the romance of the setting, waterfront living stays a pleasure instead of a surprise.""",
        },
        {
            "slug": "historic-home-renovations-permits",
            "title": "Renovating a Historic Home: Permits, Commissions, and Patience",
            "excerpt": "Character adds value; altering facades without approval can cost far more than time.",
            "body": """Designated historic districts and landmark properties often require review before windows, roofing, siding, or additions change. Start with the local preservation office or commission—rules vary block by block.

Your architect and contractor should have prior wins in similar zones. Build extra weeks into the schedule for approvals and neighbor comment periods.

Materials may cost more when you match period profiles or efficiency without visible compromise. Document approved plans for future buyers; they appreciate lawful, insurable work.

The payoff is authenticity preserved—and typically strong resale in neighborhoods where charm is the product.""",
        },
        {
            "slug": "hoa-red-flags-buyers",
            "title": "HOA Red Flags Buyers Should Not Ignore",
            "excerpt": "Thin reserves and enforcement drama surface in the documents—if you read them.",
            "body": """Association health shows up in budgets, reserve studies, and meeting minutes. Special assessments for roofs, siding, or elevators are not failures if planned; repeated emergencies are a warning.

Check litigation involving the association or builder. Lenders may hesitate if lawsuits are unresolved. Rental caps and pet rules should match your plans for the next few years.

Compare fee growth over several years and ask what it covers. Underfunded reserves today mean bigger bills tomorrow.

Spend time on the property at weekends and evenings: noise, parking, and guest policies affect daily life as much as amenities on paper.""",
        },
        {
            "slug": "pricing-your-home-to-move",
            "title": "Pricing Your Home to Move (Without Leaving Money on the Table)",
            "excerpt": "The right launch price sparks showings; chasing the tape can stall the story.",
            "body": """Buyers search in bands set by portals; pricing just above a common threshold can hide you from results. Anchor to current pending and closed comps, not peak headlines from a year ago.

Condition and presentation justify premiums; overpricing without either invites lowballs later. Track showing feedback weekly and adjust if traffic is weak early—stale listings train buyers to wait.

In many markets, minor strategic reductions beat one large panic cut later. Metrics like days on market and cost of carry should inform timing as much as ego.

A disciplined launch paired with great marketing often yields stronger net proceeds than fishing high and chasing down.""",
        },
        {
            "slug": "1031-exchange-basics-investors",
            "title": "1031 Exchanges: A Straightforward Intro for Property Investors",
            "excerpt": "Deferral is powerful when timelines and qualified intermediaries are handled correctly.",
            "body": """A like-kind exchange under Section 1031 can defer capital gains when you reinvest proceeds into another investment property. The rules are strict: timelines for identification and closing, use of a qualified intermediary, and qualified property types.

Personal-use homes generally do not qualify; syndications and certain interests may have limits. Boot and debt replacement can trigger partial tax.

Engage a specialist before you close the sale—retrofitting an exchange after the fact often fails. Your CPA should model the long-term picture; deferral is not forgiveness.

Used wisely, 1031 strategies support scaling a portfolio without an immediate tax hit on each step up.""",
        },
        {
            "slug": "smart-home-tech-and-resale",
            "title": "Smart Home Tech: What Actually Helps at Resale?",
            "excerpt": "Reliable basics beat flashy gadgets that confuse the next owner.",
            "body": """Thermostats, doorbells, locks, and well-placed lighting controls are mainstream now—when they are brands people recognize and accounts transfer cleanly. Document logins and reset procedures in a welcome binder.

Avoid irreversible installs that lock you into one ecosystem if you plan to sell soon. Hardwired access points and robust Wi-Fi foundations age better than brittle hub-and-spoke experiments.

Security cameras and sensors can help or alarm buyers worried about privacy; disclose what stays and what conveys.

The winning pattern is simple, dependable automation that makes daily life easier—not a science fair on the wall.""",
        },
        {
            "slug": "moving-with-pets-smooth-transition",
            "title": "Moving With Pets: A Low-Stress Transition Checklist",
            "excerpt": "Routine, containment, and one calm room go a long way on moving day.",
            "body": """Update IDs, microchips, and vet records before transport. Pack a travel kit with food, meds, water, bedding, and favorite toys so essentials are never at the back of the truck.

On moving day, secure pets in a quiet room or trusted boarding to prevent door dashes and anxiety around strangers. Introduce them to the new home gradually—one safe zone first, then expand.

Scout local vets, parks, and ordinances early. For renters and buyers alike, confirm breed and weight rules if applicable.

Pets adjust faster when their people project calm consistency; the house becomes home one sniff at a time.""",
        },
    ]

    for i, row in enumerate(posts):
        published_at = base_date - timedelta(hours=i * 4)
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


def unseed_more_blog_posts(apps, schema_editor):
    BlogPost = apps.get_model("website", "BlogPost")
    slugs = [
        "condo-vs-coop-urban-buying",
        "multiple-offers-winning-strategy",
        "downsizing-after-empty-nest",
        "waterfront-home-essentials",
        "historic-home-renovations-permits",
        "hoa-red-flags-buyers",
        "pricing-your-home-to-move",
        "1031-exchange-basics-investors",
        "smart-home-tech-and-resale",
        "moving-with-pets-smooth-transition",
    ]
    BlogPost.objects.filter(slug__in=slugs).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0002_seed_blog_posts"),
    ]

    operations = [
        migrations.RunPython(seed_more_blog_posts, unseed_more_blog_posts),
    ]
