from django.urls import path

from . import views

urlpatterns = [
    path("", views.validation_view, name="validation_view"),
]