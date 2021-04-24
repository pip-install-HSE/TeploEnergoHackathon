from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


def static(request, **kwargs):
    html = open("transport-web/dist/index.html").read()
    print(kwargs)
    return HttpResponse(html)


def file(request, **kwargs):
    body = open('transport-web/dist/' + kwargs['file_name']).read()
    print(body, '\n\n\n\n')
    print(kwargs)
    return HttpResponse(body)

