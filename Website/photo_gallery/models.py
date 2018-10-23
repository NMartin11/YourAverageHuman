from __future__ import unicode_literals
# from cloudinary.models import CloudinaryField
from django.db import models


# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=200)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(null=False, blank=False, width_field="width", height_field="height") 
    timestamp =  models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-timestamp"]


# class CloudinaryPhoto(models.Model):
#     create_time = models.DateTimeField(auto_now=False, auto_now_add=True)
#     title = models.CharField(max_length=200, blank=True)

#     image = CloudinaryField('stage')

#     def __unicode__(self):
#         try:
#             public_id = self.image.public_id
#         except AttributeError:
#             public_id = ''
#         return "Photo <%s:%s>" % (self.title, public_id)
