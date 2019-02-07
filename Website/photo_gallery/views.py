from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo 
from django.conf import settings
from django.views.decorators.cache import cache_page
from flickr_pony.storage import FlickrStorage
from el_pagination.decorators import page_template


@cache_page(60*30)
@page_template('photo_gallery/photo.html')
def flickr_photos(request, template='photo_gallery/photo.html'):
    storage = FlickrStorage(**settings.FLICKR_STORAGE_OPTIONS)
    user_id = request.GET.get('user_id', '') or storage.user_id
    # paginator = ''
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
            # paginator = Paginator(pictures_urls, 3)
            # page = request.GET.get('page')
            # page_numbers = paginator.get_page(page)

        except Exception as err:
            pictures = []
            error = 'Error: %s' % err.args[0]
    else:
        pictures = []

    context = {
        'entries' : pictures_urls,
    }

    return render(request, 'photo.html',context)


# @page_template('photo_gallery/photo.html')
# def flickr_photos(request, template='photo_gallery/photo.html', extra_context=None):
#     storage = FlickrStorage(**settings.FLICKR_STORAGE_OPTIONS)
#     user_id = request.GET.get('user_id', '') or storage.user_id
#     # paginator = ''
#     error = ''

#     if user_id:
#         try:
#             pictures = storage.listdir(user_id, size='L', original=False)
#             print("This is a list of pictures " + str(pictures))
#             pictures_urls = [] 
#             for pic in pictures[1]:
#                 print('pic => ' + str(pic))
#                 if len(pic) > 0:
#                     pictures_urls.append(pic)
#             # paginator = Paginator(pictures_urls, 3)
#             # page = request.GET.get('page')
#             # page_numbers = paginator.get_page(page)

#         except Exception as err:
#             pictures = []
#             error = 'Error: %s' % err.args[0]
#     else:
#         pictures = []

#     return render(request, 'photo.html', {
#         'entries': pictures_urls,
#         'user_id': user_id,
#         'error': error,
#         })