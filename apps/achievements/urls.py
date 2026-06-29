from django.urls import path
from . import views

app_name = "achievements"

urlpatterns = [
    path("", views.achievements, name="achievements"),
]
