import csv
import os

from django.conf import settings
from django.db import migrations


def populate_data(apps, schema_editor):
    Classification = apps.get_model("pokedex", "Classification")
    Pokemon = apps.get_model("pokedex", "Pokemon")

    csv_file_path = os.path.join(settings.BASE_DIR, "pokedex/data/pokemon.csv")

    with open(csv_file_path, "r", encoding="utf-8-sig") as file:
        csv_reader = csv.DictReader(file, delimiter=";")
        for row in csv_reader:
            classification, _ = Classification.objects.get_or_create(
                name=row["classfication"]
            )
            type_list = set([row["type1"], row["type2"]])
            height = float(row["height_m"]) if row["height_m"] else None
            weight = float(row["weight_kg"]) if row["weight_kg"] else None
            Pokemon.objects.create(
                classification=classification,
                attack=int(row["attack"]),
                defense=int(row["defense"]),
                hp=int(row["hp"]),
                japanese_name=row["japanese_name"],
                name=row["name"],
                pokedex_number=int(row["pokedex_number"]),
                sp_attack=int(row["sp_attack"]),
                sp_defense=int(row["sp_defense"]),
                speed=int(row["speed"]),
                type=[type_str for type_str in type_list if type_str],
                weight_kg=weight,
                height_m=height,
                generation=int(row["generation"]),
                is_legendary=bool(int(row["is_legendary"])),
            )


class Migration(migrations.Migration):
    dependencies = [
        ("pokedex", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(populate_data),
    ]
