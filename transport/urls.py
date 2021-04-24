from django.urls import path

from . import views


urlpatterns = [
    path('/root/TeploEnergoHackathon/transport-web/dist/', views.file, name='file1'),
    path('/js/<str:file_name>', views.file, name='file'),
    path('/root/TeploEnergoHackathon/transport-web/dist/', views.index, name='index'),
]
