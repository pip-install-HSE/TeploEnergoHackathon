from django.urls import path

from . import views

urlpatterns = [
    path('',
         views.static,
         name='main-page', ),
    path('main/',
         views.MainView.as_view(),
         name='main-page-template', ),
    path('<str:something>/', views.static, name='all'),
]
