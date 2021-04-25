from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
import os

from .forms import TransportCustomerForm


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
    print(f'\n\n{request}\n{kwargs}\n\n')
    return HttpResponse(body)


#######################


class TransportForm(TemplateView):
    template_name = 'transport_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TransportCustomerForm
        return context


class TransportFormHandle(FormView):

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
