# Generated by Django 5.0.1 on 2024-05-05 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_rsvpentry_babysitter_rsvpentry_dietary_restrictions_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rsvpentry',
            name='is_child',
            field=models.BooleanField(default=False),
        ),
    ]
