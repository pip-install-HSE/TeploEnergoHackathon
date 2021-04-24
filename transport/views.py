from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


def static(req):
    html = open("transport-web/dist/index.html").read()
    print('Hello world\n\n\n\n\n')
    return HttpResponse(html)


class MainView(TemplateView):
    template_name = 'transport-web/dist/index.html'
