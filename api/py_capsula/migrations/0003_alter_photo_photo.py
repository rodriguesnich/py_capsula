# Generated by Django 3.2 on 2021-04-10 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('py_capsula', '0002_alter_photo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
