from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/home/dash/Pictures/py_capsula')

class Photo(models.Model):
    photo = models.ImageField(upload_to='images/')
