# Generated by Django 3.2 on 2021-04-10 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('py_capsula', '0005_alter_photo_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='url',
        ),
    ]