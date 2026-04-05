from django.db import migrations
from django.utils.html import escape


def _looks_like_html(body):
    if not body or not str(body).strip():
        return False
    lower = str(body).lower()
    return (
        "<p" in lower
        or "<h1" in lower
        or "<h2" in lower
        or "<h3" in lower
        or "<div" in lower
        or "<ul" in lower
        or "<ol" in lower
        or "<blockquote" in lower
    )


def _plain_to_html(text):
    blocks = [b.strip() for b in str(text).split("\n\n") if b.strip()]
    if not blocks:
        return str(text)
    parts = []
    for block in blocks:
        inner = "<br>\n".join(
            escape(line.strip()) for line in block.split("\n") if line.strip()
        )
        parts.append(f"<p>{inner}</p>")
    return "\n".join(parts)


def format_blog_bodies(apps, schema_editor):
    BlogPost = apps.get_model("website", "BlogPost")
    for post in BlogPost.objects.iterator():
        body = post.body or ""
        if _looks_like_html(body):
            continue
        if not body.strip():
            continue
        new_body = _plain_to_html(body)
        BlogPost.objects.filter(pk=post.pk).update(body=new_body)


def noop_reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0006_ckeditor5_body"),
    ]

    operations = [
        migrations.RunPython(format_blog_bodies, noop_reverse),
    ]
