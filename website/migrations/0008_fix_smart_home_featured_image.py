from django.db import migrations

# photo-1558002038-bb4237ef3e66 returns 404 from Unsplash/imgix; replaced with a working interior image.
NEW_URL = "https://images.unsplash.com/photo-1565538810643-b5bdb714032a?w=1200&q=80"
OLD_URL = "https://images.unsplash.com/photo-1558002038-bb4237ef3e66?w=1200&q=80"
SLUG = "smart-home-tech-and-resale"


def fix_image_url(apps, schema_editor):
    BlogPost = apps.get_model("website", "BlogPost")
    BlogPost.objects.filter(slug=SLUG, featured_image_url=OLD_URL).update(featured_image_url=NEW_URL)
    # Also update if URL was stored without query string or matches broken id only
    BlogPost.objects.filter(slug=SLUG, featured_image_url__contains="1558002038").update(
        featured_image_url=NEW_URL
    )


def revert_image_url(apps, schema_editor):
    BlogPost = apps.get_model("website", "BlogPost")
    BlogPost.objects.filter(slug=SLUG, featured_image_url=NEW_URL).update(featured_image_url=OLD_URL)


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0007_format_blog_post_bodies"),
    ]

    operations = [
        migrations.RunPython(fix_image_url, revert_image_url),
    ]
