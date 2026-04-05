from django.db import migrations
from django.utils import timezone


REMOVED_NEWS_TITLES = (
    "Sustainability pledge: greener tours and paperless closings",
    "New digital vault for clients: documents and milestones in one place",
)

RESTORE_NEWS_ROWS = [
    {
        "title": "Sustainability pledge: greener tours and paperless closings",
        "summary": "Company initiative announcement rolling out across all offices.",
        "image_url": "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?auto=format&fit=crop&w=800&q=80",
        "link_url": "",
        "sort_order": 3,
    },
    {
        "title": "New digital vault for clients: documents and milestones in one place",
        "summary": "Product update email and blog cross-post.",
        "image_url": "https://images.unsplash.com/photo-1551434678-e076c223a692?auto=format&fit=crop&w=800&q=80",
        "link_url": "",
        "sort_order": 4,
    },
]

NEW_EVENT = {
    "title": "Wine & architecture walk — private portfolio homes",
    "summary": "Curated weekend walkthrough pairing winemakers with signature residential architecture.",
    "image_url": "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?auto=format&fit=crop&w=800&q=80",
    "link_url": "",
    "sort_order": 5,
}

SECTION_NEWS = "news"
SECTION_EVENTS = "events"


def trim_news_add_event(apps, schema_editor):
    NewsEventsItem = apps.get_model("website", "NewsEventsItem")
    now = timezone.now()
    NewsEventsItem.objects.filter(
        section=SECTION_NEWS, title__in=REMOVED_NEWS_TITLES
    ).delete()
    if not NewsEventsItem.objects.filter(title=NEW_EVENT["title"]).exists():
        NewsEventsItem.objects.create(
            section=SECTION_EVENTS,
            title=NEW_EVENT["title"],
            summary=NEW_EVENT["summary"],
            image_url=NEW_EVENT["image_url"],
            link_url=NEW_EVENT["link_url"] or "",
            is_published=True,
            sort_order=NEW_EVENT["sort_order"],
            created_at=now,
            updated_at=now,
        )


def restore_news_remove_event(apps, schema_editor):
    NewsEventsItem = apps.get_model("website", "NewsEventsItem")
    now = timezone.now()
    NewsEventsItem.objects.filter(title=NEW_EVENT["title"]).delete()
    for row in RESTORE_NEWS_ROWS:
        if not NewsEventsItem.objects.filter(title=row["title"]).exists():
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


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0018_seed_news_events"),
    ]

    operations = [
        migrations.RunPython(trim_news_add_event, restore_news_remove_event),
    ]
