from django.db import migrations
from django.utils import timezone


NEWS_UPDATES = [
    {
        "title": "GrowthX expands advisory footprint in three new metros",
        "summary": "Press coverage of our regional hiring wave and new partner-developer relationships.",
        "image_url": "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=800&q=80",
        "link_url": "",
        "sort_order": 0,
    },
    {
        "title": "Q1 luxury market brief: inventory, rates, and buyer sentiment",
        "summary": "Our quarterly note to clients on what moved the needle in the first quarter.",
        "image_url": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=800&q=80",
        "link_url": "",
        "sort_order": 1,
    },
    {
        "title": "Featured: how we closed a landmark off-market estate sale",
        "summary": "Case study pick-up in a regional business journal.",
        "image_url": "https://images.unsplash.com/photo-1600585154526-990dced4db0d?auto=format&fit=crop&w=800&q=80",
        "link_url": "",
        "sort_order": 2,
    },
]

EVENTS_HIGHLIGHTS = [
    {
        "title": "Annual client appreciation evening — skyline terrace",
        "summary": "Invite-only sunset reception thanking top clients and referral partners.",
        "image_url": "https://images.unsplash.com/photo-1511795409834-ef04bbd61622?auto=format&fit=crop&w=800&q=80",
        "link_url": "",
        "sort_order": 0,
    },
    {
        "title": "Luxury development preview brunch",
        "summary": "First look at a waterfront tower with the developer and design team.",
        "image_url": "https://images.unsplash.com/photo-1540575467063-178a50c2df87?auto=format&fit=crop&w=800&q=80",
        "link_url": "",
        "sort_order": 1,
    },
    {
        "title": "Broker open house — historic district showcase",
        "summary": "Co-hosted tour across three curated listings with local tastemakers.",
        "image_url": "https://images.unsplash.com/photo-1505373877841-8d25f7d46678?auto=format&fit=crop&w=800&q=80",
        "link_url": "",
        "sort_order": 2,
    },
    {
        "title": "Panel: the future of urban mixed-use",
        "summary": "Our principals moderated a city forum on housing, retail, and transit.",
        "image_url": "https://images.unsplash.com/photo-1475721027785-f74eccf877e2?auto=format&fit=crop&w=800&q=80",
        "link_url": "",
        "sort_order": 3,
    },
    {
        "title": "Charity gala — keys to stable housing fundraiser",
        "summary": "Team table sponsorship and live auction for a housing nonprofit partner.",
        "image_url": "https://images.unsplash.com/photo-1511578314322-379afb476865?auto=format&fit=crop&w=800&q=80",
        "link_url": "",
        "sort_order": 4,
    },
    {
        "title": "Wine & architecture walk — private portfolio homes",
        "summary": "Curated weekend walkthrough pairing winemakers with signature residential architecture.",
        "image_url": "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?auto=format&fit=crop&w=800&q=80",
        "link_url": "",
        "sort_order": 5,
    },
]

SECTION_NEWS = "news"
SECTION_EVENTS = "events"

SEED_TITLES = tuple(
    n["title"] for n in NEWS_UPDATES
) + tuple(e["title"] for e in EVENTS_HIGHLIGHTS)


def seed_news_events(apps, schema_editor):
    NewsEventsItem = apps.get_model("website", "NewsEventsItem")
    now = timezone.now()
    for row in NEWS_UPDATES:
        NewsEventsItem.objects.create(
            section=SECTION_NEWS,
            title=row["title"],
            summary=row["summary"],
            image_url=row["image_url"],
            link_url=row["link_url"] or "",
            is_published=True,
            sort_order=row["sort_order"],
            created_at=now,
            updated_at=now,
        )
    for row in EVENTS_HIGHLIGHTS:
        NewsEventsItem.objects.create(
            section=SECTION_EVENTS,
            title=row["title"],
            summary=row["summary"],
            image_url=row["image_url"],
            link_url=row["link_url"] or "",
            is_published=True,
            sort_order=row["sort_order"],
            created_at=now,
            updated_at=now,
        )


def unseed_news_events(apps, schema_editor):
    NewsEventsItem = apps.get_model("website", "NewsEventsItem")
    NewsEventsItem.objects.filter(title__in=SEED_TITLES).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0017_news_events_item"),
    ]

    operations = [
        migrations.RunPython(seed_news_events, unseed_news_events),
    ]
