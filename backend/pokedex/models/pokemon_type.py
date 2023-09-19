from django.db import models


class PokemonType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    icon_url = models.CharField(max_length=255)

    def __str__(self):
        return self.name
