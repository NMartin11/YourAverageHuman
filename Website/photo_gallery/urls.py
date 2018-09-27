from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'', views.index, name='index'),
]

<<<<<<< HEAD
=======
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

>>>>>>> e8a4e69b0deb2fe769697a46b6e165c88774a4fc
