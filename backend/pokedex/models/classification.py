from django.db import models


class Classification(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
