from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

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


@receiver(post_save, sender=RsvpEntry)
def send_notification(sender, instance, **kwargs):
    message = f"{instance.name}\n\n Attending: {instance.attending}\n\n Wedding Meal: {instance.meal}\n\n Dietary Restrictions: {instance.dietary_restrictions}\n\n Song Request: {instance.song_request}\n\n Babysitter: {instance.babysitter}\n\n Welcome Dinner: {instance.welcome_dinner}\n\n Welcome Meal: {instance.welcome_meal}\n\n Pizza: {instance.pizza}\n\n Pizza Meal: {instance.pizza_meal}\n\n Staying: {instance.stay} days"
    send_mail(
        f"RSVP submitted for {instance.name}",
        message,
        'austinmclean148@gmail.com',
        ['austin_mclean@hotmail.com', 'fulginiti.samantha@gmail.com'],
        fail_silently=False,
    )