# Generated by Django 5.0.7 on 2024-08-21 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0002_room_name_alter_amenity_scription"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="amenity",
            options={"verbose_name_plural": "Amenities"},
        ),
        migrations.RenameField(
            model_name="amenity",
            old_name="scription",
            new_name="description",
        ),
    ]
