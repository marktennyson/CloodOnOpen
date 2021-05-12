from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.

class Display(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    age = models.IntegerField(blank=False)