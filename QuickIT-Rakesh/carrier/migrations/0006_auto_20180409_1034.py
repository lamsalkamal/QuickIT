# Generated by Django 2.0.3 on 2018-04-09 07:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrier', '0005_auto_20180409_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='receiver_no',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
