from django.urls import path

from . import views


urlpatterns = [
    path('', views.file, name='file'),
]
