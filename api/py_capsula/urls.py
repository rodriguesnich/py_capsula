from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('store', views.post, name='image_upload'),
    path('', views.index, name='index_images')
    # path('sucess', views.sucess, name='sucess'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
