from django.db import models
from django.core.files.storage import FileSystemStorage


class Photo(models.Model):
    photo = models.ImageField(upload_to='images/')
