from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, FormView, DetailView
import os

import psycopg2

from .forms import TransportCustomerForm
from .models import StaticAnalytics, AnalyticsResult

from django.core.files.images import ImageFile


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


class ViewAnalytics(TemplateView):
    model = StaticAnalytics
    template_name = 'static_analytics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = get_object_or_404(StaticAnalytics, pk=1)
        return context


class TransportFormHandle(FormView):
    # success_url = '/'

    def get_success_url(self):
        return reverse('result', kwargs={'pk': AnalyticsResult.objects.count()})

    form_class = TransportCustomerForm

    def form_valid(self, form):
        # print(form.cleaned_data)

        customer = form.cleaned_data['customer']
        vehicle = form.cleaned_data['vehicle']

        conn = psycopg2.connect(dbname='main', user='postgres',
                                password='fnvjYUbf63nv', host='193.162.143.45')
        cursor = conn.cursor()
        r = '''select l.name, o.date, "order".predict_time, o.real_time, customer.name, v.name from "order"
inner join customer on customer.id = "order".customer_id
inner join vehicle v on v.id = "order".vehicle_id
inner join license l on l.id = "order".license_id
inner join "ride" o on l.id = o.license_id and "order".date = o.date'''
        print(r)
        cursor.execute(r)
        records = cursor.fetchall()

        print(records)

        m = AnalyticsResult.objects.create()
        m.image = ImageFile(open("images/dynamic.jpg", "rb"))
        m.save()

        return super().form_valid(form)


class AnalyticsResultView(DetailView):
    model = AnalyticsResult
    template_name = 'result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = AnalyticsResult.objects.get(pk=AnalyticsResult.objects.count())
        return context
