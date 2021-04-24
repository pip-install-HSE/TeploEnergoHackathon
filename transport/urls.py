from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('/root/TeploEnergoHackathon/transport-web/dist/', views.file, name='file1'),
    path('<str:file_name>/', views.file, name='file'),
]
