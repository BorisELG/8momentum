# Generated by Django 5.0.2 on 2024-02-19 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NavigationSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github_url', models.URLField(blank=True, verbose_name='GitHub URL')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
