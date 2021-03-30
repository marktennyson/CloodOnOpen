from django.db import models

class CountryInfo(models.Model):
    name = models.CharField(max_length=600, unique=True)
    region = models.CharField(max_length=600)
    subRegion = models.CharField(max_length=600)
    population = models.IntegerField()
    currency = models.CharField(max_length=600)
    languages = models.CharField(max_length=600)

    def __str__(self):
        return self.name