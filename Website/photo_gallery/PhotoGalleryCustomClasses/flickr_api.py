from django.conf import settings
from flickr_pony.storage import FlickrStorage

class FlickrAPI():
    
    
    def __init__(self,request):
        self.storage = FlickrStorage(**settings.FLICKR_STORAGE_OPTIONS) 
        if self.storage.user_id:
            self.user_id = self.storage.user_id
        else:
            self.user_id = request.GET.get('user_id', '')
        self.template = 'base.html'
        self.page_template = 'photo.html'

    def get_pictures_as_list(self, size, original): 
        if self.user_id:
            try:
                pictures = self.storage.listdir(self.user_id, size='L', original=False)
                print("This is a list of pictures " + str(pictures))
                pictures_urls = [] 
                for pic in pictures[1]:
                    print('pic => ' + str(pic))
                    if len(pic) > 0:
                        pictures_urls.append(pic)
                return pictures_urls

            except Exception as err:
                pictures = []
                error = 'Error: %s' % err.args[0]
        else:
            pictures = []