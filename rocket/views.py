from django.shortcuts import render
from .models import LaunchVehicle

def list_rocket(request):
    """Вывод списка rocket"""

    rockets = LaunchVehicle.objects.all()
 
    return render(request, "rocket/rocket_list.html", context={"rockets": rockets})