from django.db import models

# Create your models here.

class RsvpEntry(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    invite = models.IntegerField(null=True)
    attending = models.CharField(max_length=20, null=True)
    meal = models.CharField(max_length=100, null=True)
    dietary_restrictions = models.CharField(max_length=200, null=True, blank=True)
    babysitter = models.CharField(max_length=20, null=True)
    welcome_dinner = models.CharField(max_length=20, null=True)
    welcome_meal = models.CharField(max_length=50, null=True, blank=True)
    pizza = models.CharField(max_length=20, null=True)
    pizza_meal = models.CharField(max_length=50, null=True, blank=True)
    stay = models.CharField(max_length=20, null=True)

