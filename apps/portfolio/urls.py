from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path("", views.home, name="home"),
    path("services/", views.services, name="services"),
    path("about/", views.about, name="about"),
]
