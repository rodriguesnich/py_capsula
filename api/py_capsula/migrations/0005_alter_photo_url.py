# Generated by Django 3.2 on 2021-04-10 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('py_capsula', '0004_photo_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='url',
            field=models.URLField(default=''),
        ),
    ]
