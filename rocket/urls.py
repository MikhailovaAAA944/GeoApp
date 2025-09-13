from django.urls import path
from rocket import views

urlpatterns = [
    path("", views.list_rocket, name="list_rocket"),
    path("calculation/", views.playload_calculation, name="playload_calculation"),
    path("mycalculation/", views.my_calculation, name="my_calculation")
]
