from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo 
from django.conf import settings
from django.views.decorators.cache import cache_page
from flickr_pony.storage import FlickrStorage
from el_pagination.decorators import page_template
from el_pagination.views import AjaxListView
import photo_gallery.PhotoGalleryCustomClasses.flickr_api as FlickApi


@cache_page(60*30)
def flickr_photos(request, template='base.html', page_template='photo.html'):
    flickr = FlickApi.FlickrAPI(request)
    flickr_photos = flickr.get_pictures_as_list('L', False)

    context = {
        'entry_list': flickr_photos,
        'page_template': page_template,
    }

    if request.is_ajax():
        template = page_template

    return render(request, template, context)