# Generated by Django 5.1.7 on 2025-03-29 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_one', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='isDeleted',
            field=models.BooleanField(default=False),
        ),
    ]
