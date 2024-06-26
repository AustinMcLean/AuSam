# Generated by Django 5.0.1 on 2024-05-08 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_rsvpentry_attending_alter_rsvpentry_babysitter_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rsvpentry',
            name='song_request',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='rsvpentry',
            name='dietary_restrictions',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='rsvpentry',
            name='name',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]
