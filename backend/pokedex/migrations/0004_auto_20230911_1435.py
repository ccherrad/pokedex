# Generated by Django 4.2.5 on 2023-09-11 14:35
import json
import os

from django.db import migrations
from django.conf import settings

def load_pokemon_types_data(apps, schema_editor):
    PokemonType = apps.get_model('pokedex', 'PokemonType')

    json_file_path = os.path.join(settings.BASE_DIR, 'pokedex/data/types.json')
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        
        for item in data['types']:
            PokemonType.objects.create(
                name=item['name'],
                icon_url=item['icon_url']
            )

class Migration(migrations.Migration):
    dependencies = [
        ("pokedex", "0003_type"),
    ]

    operations = [
        migrations.RunPython(load_pokemon_types_data),
    ]