from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


def static(request, **kwargs):
    html = open("transport-web/dist/index.html").read()
    print(kwargs)
    return HttpResponse(html)


def js(request, **kwargs):
    body = open('transport-web/dist/js/app.3224fe33.js').read()
    print(body, '\n\n\n\n')
    return HttpResponse(body)


class MainView(TemplateView):
    template_name = 'transport-web/dist/index.html'
