from django.shortcuts import render
from django.http import HttpResponse

def resume(request, template="base.html", page_template='resume.html'):
    context = {
        'page_template': page_template,
    }

    if request.is_ajax():
        template = page_template

    return render(request, template, context)