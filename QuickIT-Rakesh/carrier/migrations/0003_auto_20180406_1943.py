# Generated by Django 2.0.3 on 2018-04-06 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrier', '0002_auto_20180406_1928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='Dropoff_place',
            new_name='dropoff_place',
        ),
    ]
