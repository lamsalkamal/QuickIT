# Generated by Django 2.0.3 on 2018-04-08 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrier', '0003_auto_20180406_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/'),
        ),
    ]