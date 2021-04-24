from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
import os


# def static(request, **kwargs):
#     html = open("transport-web/dist/index.html").read()
#     print(kwargs)
#     return HttpResponse(html)


def index(request, **kwargs):
    html = open("transport-web/dist/index.html").read()
    print(kwargs)
    return HttpResponse(html)


def file(request, **kwargs):
    body = open(os.path.join('transport-web/dist/', kwargs['file_name'])).read()
    print(body, '\n\n\n\n')
    print(kwargs)
    return HttpResponse(body)
