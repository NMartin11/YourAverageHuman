from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo 
from django.conf import settings
from django.views.decorators.cache import cache_page
from flickr_pony.storage import FlickrStorage


def photo_list(request):
    queryset = Photo.objects.all()
    return render(request, "photo.html", {'photos': queryset})

@cache_page(60*30)
def flickr_photos(request):
    storage = FlickrStorage(**settings.FLICKR_STORAGE_OPTIONS)
    user_id = request.GET.get('user_id', '') or storage.user_id
    error = ''

    if user_id:
        try:
            pictures = storage.listdir(user_id, size='L', original=False)
            print("This is a list of pictures " + str(pictures))
            pictures_urls = [] 
            for pic in pictures[1]:
                print('pic => ' + str(pic))
                if len(pic) > 0:
                    pictures_urls.append(pic)

        except Exception as err:
            pictures = []
            error = 'Error: %s' % err.args[0]
    else:
        pictures = []

    return render(request, 'photo.html', {
        'pictures': pictures_urls,
        'user_id': user_id,
        'error': error
        })

