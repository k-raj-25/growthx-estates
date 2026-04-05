# Re-apply image URLs from properties_data after replacing broken Unsplash links.

from django.db import migrations


def sync_property_images(apps, schema_editor):
    Property = apps.get_model("website", "Property")
    from website import properties_data

    for row in properties_data._RAW_PROPERTIES:
        Property.objects.filter(slug=row["slug"]).update(images=row["images"])


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0012_resync_property_seed"),
    ]

    operations = [
        migrations.RunPython(sync_property_images, migrations.RunPython.noop),
    ]
