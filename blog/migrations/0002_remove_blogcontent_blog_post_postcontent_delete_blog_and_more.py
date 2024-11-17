# Generated by Django 5.0 on 2024-11-17 09:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blogcontent",
            name="blog",
        ),
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=100)),
                ("slug", models.SlugField(unique=True)),
                ("description", models.CharField(max_length=255)),
                ("image", models.ImageField(upload_to="post/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "categories",
                    models.ManyToManyField(related_name="posts", to="blog.category"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PostContent",
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
                ("image", models.ImageField(upload_to="post/content/")),
                ("content", models.TextField()),
                (
                    "blog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="content",
                        to="blog.post",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Blog",
        ),
        migrations.DeleteModel(
            name="BlogContent",
        ),
    ]