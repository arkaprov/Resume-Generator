from django.urls import path
from . import views

from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("index", views.index, name="index"),
]