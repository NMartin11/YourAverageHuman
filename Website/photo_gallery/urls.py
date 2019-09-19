from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = "photo_gallery"

urlpatterns = [
    url(r'^$', views.flickr_photos, name='photo_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

