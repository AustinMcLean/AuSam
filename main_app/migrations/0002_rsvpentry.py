# Generated by Django 5.0.1 on 2024-03-17 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [

    ]

    operations = [
        migrations.CreateModel(
            name='RsvpEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('attending', models.CharField(max_length=20)),
            ],
        ),
    ]
