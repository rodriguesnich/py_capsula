from django import forms
from .models import *
  
class Upload_image(forms.ModelForm):
  
    class Meta:
        model = Photo
        fields = ['photo']