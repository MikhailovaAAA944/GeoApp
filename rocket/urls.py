from django.urls import path
from rocket import views

urlpatterns = [
    path("", views.list_rocket, name="list_rocket"),
    path("calculation/", views.playload_calculation, name="playload_calculation"),
    path("mycalculation/", views.my_calculation, name="my_calculation"),
    path("rocketdetail/<int:pk>/", views.rocket_detail, name="rocket_detail"),
    path("request_form/<int:rocket_pk>/", views.request_form, name="request_form"),
    path("delete_from_calc/<int:rocket_pk>/", views.delete_from_calc, name="delete_from_calc"),
    path("remove_rocket/<int:rocket_pk>/", views.remove_rocket, name="remove_rocket"),
    path("delete_calc/<int:order_pk>/", views.delete_calc, name="delete_calc")

    
]
