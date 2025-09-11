from django.urls import path
from rocket import views

urlpatterns = [
    path("", views.list_rocket, name="list_rocket"),
]