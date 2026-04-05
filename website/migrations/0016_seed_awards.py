from django.db import migrations
from django.utils import timezone


AWARDS = [
    {
        "title": "Excellence in Client Service",
        "issuer": "National Association of Realtors",
        "year_label": "2025",
        "summary": "Recognized for consistent five-star client satisfaction scores and ethical transaction standards across luxury listings.",
        "image_url": "https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=800&q=80",
        "link_url": "",
        "sort_order": 0,
    },
    {
        "title": "Top Luxury Brokerage — Northeast",
        "issuer": "Real Estate Executive Magazine",
        "year_label": "2024",
        "summary": "Named among the leading boutique advisory firms for high-net-worth residential and new-development sales.",
        "image_url": "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=800&q=80",
        "link_url": "",
        "sort_order": 1,
    },
    {
        "title": "Best Marketing Campaign — Estate Portfolio",
        "issuer": "Luxury Portfolio International",
        "year_label": "2024",
        "summary": "Honored for integrated digital and private-tour campaigns that achieved record engagement on signature listings.",
        "image_url": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=800&q=80",
        "link_url": "",
        "sort_order": 2,
    },
    {
        "title": "Five Star Professional — Real Estate Agent",
        "issuer": "Five Star Professional / Forbes partner survey",
        "year_label": "2023–2025",
        "summary": "Selected by clients and peers for trust, communication, and market knowledge three years running.",
        "image_url": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=800&q=80",
        "link_url": "",
        "sort_order": 3,
    },
    {
        "title": "Community Impact Award",
        "issuer": "Metro Housing Alliance",
        "year_label": "2023",
        "summary": "Acknowledged for pro-bono advisory and fundraising support connecting families with stable housing resources.",
        "image_url": "https://images.unsplash.com/photo-1523217582562-09d0def993a6?auto=format&fit=crop&w=800&q=80",
        "link_url": "",
        "sort_order": 4,
    },
    {
        "title": "Deal of the Year — Mixed-Use Development",
        "issuer": "Commercial Property Awards",
        "year_label": "2023",
        "summary": "Awarded for structuring a complex joint venture and rezoning path for a landmark urban residential tower.",
        "image_url": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=800&q=80",
        "link_url": "",
        "sort_order": 5,
    },
    {
        "title": "Platinum Club — Top 1% Production",
        "issuer": "Regional MLS Circle of Excellence",
        "year_label": "2022–2025",
        "summary": "Sustained placement in the top tier for closed volume and units in the luxury price band.",
        "image_url": "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=800&q=80",
        "link_url": "",
        "sort_order": 6,
    },
    {
        "title": "Innovation in Virtual Showings",
        "issuer": "PropTech Review Summit",
        "year_label": "2022",
        "summary": "Highlighted for cinematic remote tours and secure off-market preview workflows adopted industry-wide.",
        "image_url": "https://images.unsplash.com/photo-1558036117-15d82a90b9b1?auto=format&fit=crop&w=800&q=80",
        "link_url": "",
        "sort_order": 7,
    },
    {
        "title": "Readers’ Choice — Best Buyer Representation",
        "issuer": "City Lifestyle Journal",
        "year_label": "2022",
        "summary": "Voted by readers for negotiation skill, disclosure diligence, and calm guidance in competitive bidding environments.",
        "image_url": "https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?auto=format&fit=crop&w=800&q=80",
        "link_url": "",
        "sort_order": 8,
    },
    {
        "title": "Rising Star — Luxury Advisory",
        "issuer": "International Property Forum",
        "year_label": "2021",
        "summary": "Early-career recognition for cross-border referrals and white-glove service to relocating executives.",
        "image_url": "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?auto=format&fit=crop&w=800&q=80",
        "link_url": "",
        "sort_order": 9,
    },
]

SEED_TITLES = tuple(a["title"] for a in AWARDS)


def seed_awards(apps, schema_editor):
    AwardRecognition = apps.get_model("website", "AwardRecognition")
    now = timezone.now()
    for row in AWARDS:
        AwardRecognition.objects.create(
            title=row["title"],
            issuer=row["issuer"],
            year_label=row["year_label"],
            summary=row["summary"],
            image_url=row["image_url"],
            link_url=row["link_url"] or "",
            is_published=True,
            sort_order=row["sort_order"],
            created_at=now,
            updated_at=now,
        )


def unseed_awards(apps, schema_editor):
    AwardRecognition = apps.get_model("website", "AwardRecognition")
    AwardRecognition.objects.filter(title__in=SEED_TITLES).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0015_award_recognition"),
    ]

    operations = [
        migrations.RunPython(seed_awards, unseed_awards),
    ]
