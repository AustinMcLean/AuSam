from django.db import models

# Create your models here.


class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class RsvpEntry(models.Model):
    name = models.CharField(max_length=200)
    attending = models.CharField(max_length=20)