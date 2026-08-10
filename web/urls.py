from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, {"lang": "es"}, name="index"),
    path("en/", views.index, {"lang": "en"}, name="index_en"),
]
