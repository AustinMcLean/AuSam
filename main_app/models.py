from django.db import models

# Create your models here.

class RsvpEntry(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    invite = models.IntegerField(null=True)
    is_child = models.BooleanField(default=False)
    attending = models.CharField(max_length=20, null=True, blank=True)
    meal = models.CharField(max_length=100, null=True, blank=True)
    dietary_restrictions = models.CharField(max_length=100, null=True, blank=True)
    song_request = models.CharField(max_length=200, null=True, blank=True)
    babysitter = models.CharField(max_length=20, null=True, blank=True)
    welcome_dinner = models.CharField(max_length=20, null=True, blank=True)
    welcome_meal = models.CharField(max_length=50, null=True, blank=True)
    pizza = models.CharField(max_length=20, null=True, blank=True)
    pizza_meal = models.CharField(max_length=50, null=True, blank=True)
    stay = models.CharField(max_length=20, null=True, blank=True)

