from django.urls import path

from . import views


urlpatterns = [
    # path('/root/TeploEnergoHackathon/transport-web/dist/', views.file, name='file1'),
    # path('js/<str:file_name>', views.file, name='file'),
    path('', views.MainPageView.as_view(), name='main'),
    path('static_analytics/<int:pk>/', views.ViewAnalytics.as_view(), name='static_analytics'),
    path('make_analytics/', views.TransportForm.as_view(), name='make_analytics'),
    path('form_valid/', views.TransportFormHandle.as_view(), name='transport_form_handle'),
    path('result/<int:pk>', views.AnalyticsResultView.as_view(), name='result'),
]
