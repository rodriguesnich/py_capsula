from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *

# Create your views here.


def image_upload(request):

    if request.method == 'POST':
        form = Upload_image(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = Upload_image()
    return render(request, 'index.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')
