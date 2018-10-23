import cloudinary
from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo 
# from .models import CloudinaryPhoto
import six


def photo_list(request):
    queryset = Photo.objects.all()
    context = {
        "photos": queryset,
    }
    return render(request, "photo.html", {'photos': queryset})


# def filter_nones(d):
#     return dict((k, v) for k, v in six.iteritems(d) if v is not None)

# def cloudinary_list(request):
#     defaults = dict(format="jpg", height=150, width=150)
#     defaults["class"] = "thumbnail inline"

#     #The different transformations to persent
#     samples = [
#         dict(crop="fill", radius=10),
#         dict(crop="scale"),
#         dict(crop="fit", format="png"),
#         dict(crop="thumb", gravity="face"),
#         dict(format="png", angle=20, height=None, width=None, transformation=[
#             dict(crop="fill", gravity="north", width=150, height=150, effect="sepia"),
#         ]),
#     ]
#     samples = [filter_nones(dict(defaults, **sample)) for sample in samples]
#     return render(request, 'photo.html', dict(cloudPhotos=CloudinaryPhoto.objects.all(), samples=samples))


