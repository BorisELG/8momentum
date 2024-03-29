# Generated by Django 5.0.2 on 2024-02-19 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_footertext_delete_navigationsettings"),
    ]

    operations = [
        migrations.CreateModel(
            name="NavigationSettings",
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
                ("github_url", models.URLField(blank=True, verbose_name="GitHub URL")),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
