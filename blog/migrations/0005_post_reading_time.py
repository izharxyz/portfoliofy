# Generated by Django 5.0 on 2025-01-01 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_alter_postcontent_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="reading_time",
            field=models.PositiveIntegerField(default=5),
        ),
    ]
