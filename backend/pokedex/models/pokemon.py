from django.contrib.postgres.fields import ArrayField
from django.db import models

from .classification import Classification


class Pokemon(models.Model):
    name = models.CharField(max_length=255)
    japanese_name = models.CharField(max_length=255)
    pokedex_number = models.IntegerField()
    classification = models.ForeignKey(
        Classification, on_delete=models.CASCADE
    )
    attack = models.IntegerField()
    defense = models.IntegerField()
    height_m = models.FloatField(blank=True, null=True)
    weight_kg = models.FloatField(blank=True, null=True)
    hp = models.IntegerField()
    sp_attack = models.IntegerField()
    sp_defense = models.IntegerField()
    speed = models.IntegerField()
    type = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    generation = models.IntegerField()
    is_legendary = models.BooleanField()

    def __str__(self):
        return self.name
