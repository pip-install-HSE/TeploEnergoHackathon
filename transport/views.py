from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, FormView, DetailView
import os

from .forms import TransportCustomerForm
from .models import StaticAnalytics


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


class TransportForm(TemplateView, FormView):
    template_name = 'transport_form.html'
    form_class = TransportCustomerForm


class MainPageView(TemplateView):
    template_name = 'main_page.html'


class ViewAnalytics(DetailView):
    model = StaticAnalytics
    template_name = 'static_analytics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = get_object_or_404(StaticAnalytics, pk=1)
        return context


class TransportFormHandle(FormView):
    success_url = '/'
    form_class = TransportCustomerForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
