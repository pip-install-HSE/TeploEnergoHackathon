from django.urls import path

from . import views


urlpatterns = [
    path('',
         views.static,
         name='main-page', ),
    path('main/',
         views.MainView.as_view(),
         name='main-page-template', ),
    path('<str:file_name>/', views.file, name='file'),
    path('<str:something>/', views.static, name='all'),
]
