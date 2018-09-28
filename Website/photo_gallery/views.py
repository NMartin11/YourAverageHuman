from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo


def photo_list(request):
    queryset = Photo.objects.all()
    context = {
        "photos": queryset,
    }
    return render(request, "photo.html", {'photos': queryset})
