from django.db import models
# from django.db.models.fields import IntegerField

# Create your models here.

class Settings(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    age = models.IntegerField(max_length=10, blank=False)