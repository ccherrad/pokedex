# Generated by Django 4.2.5 on 2023-09-11 14:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pokedex", "0002_auto_20230909_1518"),
    ]

    operations = [
        migrations.CreateModel(
            name="PokemonType",
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
                ("name", models.CharField(max_length=255, unique=True)),
                ("icon_url", models.CharField(max_length=255)),
            ],
        ),
    ]