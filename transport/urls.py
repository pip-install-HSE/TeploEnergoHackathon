from django.urls import path

from . import views


urlpatterns = [
    # path('/root/TeploEnergoHackathon/transport-web/dist/', views.file, name='file1'),
    # path('js/<str:file_name>', views.file, name='file'),
    # path('', views.index, name='index'),
    path('', views.TransportForm.as_view(), name='transport_form'),
    path('form_valid/', views.TransportFormHandle.as_view(), name='transport_form_handle'),
]
