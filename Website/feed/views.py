from django.shortcuts import render, HttpResponse
from django.http import  JsonResponse
from pusher import Pusher
import json
import os.path
from .models import Feed
from ..feed.forms import *



# get pusher creds
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../Website/secrets/pusher_keys.json")
with open(path) as f:
    data = json.load(f)

#instantiate pusher
pusher = Pusher(app_id=data["pusher"]["app_id"], key=data["pusher"]["key"], secret=data["pusher"]["secret"],
                cluster=data["pusher"]["cluster"])


# Create your views here.
def index(request):
    # get all current photos ordered by the latest
    all_documents = Feed.objects.all().order_by('-id')

    # return the index.html template, passing in all the feeds
    return render(request, 'index.html', {'all_documents': all_documents})

# function that authenticates the private channel
def pusher_authentication(request):
    channel = request.GET.get('channel_name', None)
    socket_id = request.GET.get('socket_id', None)
    auth = pusher.authenticate(
        channel = channel,
        socket_id = socket_id
    )

    return JsonResponse(json.dumps(auth), safe=False)

# function that triggers the pusher request
def push_feed(request):
    # check if the method is post
    if request.method == 'POST':
        #try form validation
        form = DocumentForm


