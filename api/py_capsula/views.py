from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import *

# Create your views here.

@csrf_exempt
def post(request):
    if request.method == 'POST':
        form = Upload_image(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('successfully uploaded')
    else:
        form = Upload_image()
        return HttpResponse('error while recing file')


def index(request):

    if request.method == 'GET':
        Photos = Photo.objects.all()
        # getting all the objects of hotel.
        response = []
        for photo in Photos:
            response.append(f'{request.get_host()}{photo.photo.url}')

		
		
        # return render(request, 'store.html',
        #               {'photos': Photos})
        return JsonResponse(response, safe=False)
