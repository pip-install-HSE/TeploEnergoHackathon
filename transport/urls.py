from django.urls import path

from . import views


urlpatterns = [
    path('<str:file_name>/', views.file, name='file'),
]
