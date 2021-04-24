from django.urls import path

from . import views

urlpatterns = [
    path(
        '/',
        views.static,
        'main-page',
    ),
    path(
        'main/',
        views.MainView.as_view(),
        'main-page-template',
    )
]
