from django.db import models

# Create your models here.

class RsvpEntry(models.Model):
    name = models.CharField(max_length=200)
    attending = models.CharField(max_length=20)