from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


def static(request):
    html = open("transport-web/dist/index.html").read()
    print(html)
    return HttpResponse(html)


class MainView(TemplateView):
    template_name = 'transport-web/dist/index.html'
