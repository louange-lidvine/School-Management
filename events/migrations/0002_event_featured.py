# Generated by Django 5.1.2 on 2024-10-28 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
