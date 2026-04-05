from django.db import migrations, models


def seed_careers(apps, schema_editor):
    CareersSettings = apps.get_model("website", "CareersSettings")
    JobOpening = apps.get_model("website", "JobOpening")
    CareersSettings.objects.get_or_create(
        pk=1,
        defaults={"hr_email": "careers@growthestates.com"},
    )
    if not JobOpening.objects.exists():
        JobOpening.objects.bulk_create(
            [
                JobOpening(
                    title="Senior luxury sales advisor",
                    department="Sales & advisory",
                    location="New York, NY (hybrid)",
                    employment_type="full_time",
                    description=(
                        "Represent buyers and sellers in the tri-state luxury market. "
                        "You bring 5+ years of high-end residential experience, a calm client presence, "
                        "and a track record of discreet, well-prepared transactions."
                    ),
                    is_published=True,
                    sort_order=0,
                ),
                JobOpening(
                    title="Marketing coordinator",
                    department="Marketing",
                    location="Hybrid",
                    employment_type="full_time",
                    description=(
                        "Support campaigns, listings collateral, and events across digital and print. "
                        "Strong writing skills, comfort with CRM and analytics, and an eye for brand consistency."
                    ),
                    is_published=True,
                    sort_order=1,
                ),
                JobOpening(
                    title="Summer analyst — market intelligence",
                    department="Research",
                    location="New York, NY",
                    employment_type="internship",
                    description=(
                        "10-week program assisting the market intelligence team with comps, memos, and data quality. "
                        "Ideal for students pursuing finance, economics, or real estate."
                    ),
                    is_published=True,
                    sort_order=2,
                ),
            ]
        )


def noop_reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0019_trim_news_add_event_seed"),
    ]

    operations = [
        migrations.CreateModel(
            name="CareersSettings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "hr_email",
                    models.EmailField(
                        help_text="Address where candidates should email résumés (shown on the site).",
                        max_length=254,
                    ),
                ),
            ],
            options={
                "verbose_name": "Careers / HR contact",
                "verbose_name_plural": "Careers / HR contact",
            },
        ),
        migrations.CreateModel(
            name="JobOpening",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("department", models.CharField(blank=True, max_length=120)),
                (
                    "location",
                    models.CharField(
                        blank=True,
                        help_text="E.g. city, hybrid, or remote.",
                        max_length=200,
                    ),
                ),
                (
                    "employment_type",
                    models.CharField(
                        choices=[
                            ("full_time", "Full-time"),
                            ("part_time", "Part-time"),
                            ("contract", "Contract"),
                            ("internship", "Internship"),
                        ],
                        default="full_time",
                        max_length=20,
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Role summary and requirements (plain text on the site).",
                    ),
                ),
                ("is_published", models.BooleanField(db_index=True, default=True)),
                (
                    "sort_order",
                    models.PositiveIntegerField(
                        default=0,
                        help_text="Lower numbers appear first.",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Job opening",
                "verbose_name_plural": "Job openings",
                "ordering": ["sort_order", "-created_at"],
            },
        ),
        migrations.RunPython(seed_careers, noop_reverse),
    ]
