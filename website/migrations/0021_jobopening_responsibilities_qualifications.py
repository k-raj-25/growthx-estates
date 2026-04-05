from django.db import migrations, models


ROLE_COPY = {
    "senior luxury sales advisor": {
        "responsibilities": """- Represent buyers and sellers in luxury residential transactions end-to-end
- Prepare pricing opinions, tour strategies, and negotiation plans grounded in live comps
- Coordinate discreet off-market previews and maintain immaculate client files
- Partner with marketing, transactions, and research on listings and bespoke buyer searches
- Mentor junior advisors through shadowing and structured deal reviews""",
        "qualifications": """- 5+ years in high-end residential sales or comparable advisory experience
- Track record of closed volume and strong references from clients and peers
- Exceptional written and verbal communication; calm under pressure
- Licensed real estate salesperson (or equivalent for your market), in good standing
- Fluency with CRM, MLS, and presentation tools; willingness to travel locally for tours""",
    },
    "marketing coordinator": {
        "responsibilities": """- Produce listing sheets, email campaigns, and social assets aligned with brand guidelines
- Maintain content calendars and coordinate shoots, open houses, and partner events
- Update the website and internal templates with accurate copy and imagery
- Track campaign performance and share concise insights with leadership
- Support PR and award submissions with timelines and asset packages""",
        "qualifications": """- 2+ years in marketing, communications, or creative operations (real estate a plus)
- Strong writing and editing skills; comfort with design tools (Figma, Canva, or similar)
- Organized, detail-oriented, and able to juggle multiple deadlines
- Experience with email platforms and basic analytics (GA, Meta, or comparable)
- Bachelor’s degree or equivalent experience""",
    },
    "summer analyst — market intelligence": {
        "responsibilities": """- Assist with comp gathering, data cleaning, and charting for internal memos
- Support senior analysts on market snapshots and investment summaries
- Maintain spreadsheets and light research on macro and local drivers
- Document sources and assumptions so work is easy to audit and reuse
- Present a short capstone on one submarket at the end of the program""",
        "qualifications": """- Currently enrolled in undergraduate or graduate studies (economics, finance, real estate, or related)
- Strong Excel / Sheets skills; interest in Python or BI tools is a plus
- Curious, meticulous, and comfortable asking clarifying questions
- Available for the full 10-week summer schedule in-office
- Prior internship or coursework in analysis or research preferred""",
    },
}


def fill_role_details(apps, schema_editor):
    JobOpening = apps.get_model("website", "JobOpening")
    for job in JobOpening.objects.all():
        key = (job.title or "").strip().lower()
        block = ROLE_COPY.get(key)
        if not block:
            continue
        JobOpening.objects.filter(pk=job.pk).update(
            responsibilities=block["responsibilities"],
            qualifications=block["qualifications"],
        )


def noop_reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0020_careers_job_openings"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobopening",
            name="qualifications",
            field=models.TextField(
                blank=True,
                help_text="Shown in the role detail popup. One bullet per line (optional leading “- ”).",
            ),
        ),
        migrations.AddField(
            model_name="jobopening",
            name="responsibilities",
            field=models.TextField(
                blank=True,
                help_text="Shown in the role detail popup. One bullet per line (optional leading “- ”).",
            ),
        ),
        migrations.RunPython(fill_role_details, noop_reverse),
    ]
