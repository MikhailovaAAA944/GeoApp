from django.shortcuts import render
from .models import LaunchVehicle, CalculationRequest
from .forms import CalculationRequestFrom

def list_rocket(request):
    """Вывод списка rocket"""

    rockets = LaunchVehicle.objects.all()
 
    return render(request, "rocket/rocket_list.html", context={"rockets": rockets})

def my_calculation(request):
    """Вывод списка заявок"""

    calculations = CalculationRequest.objects.all()
 
    return render(request, "rocket/my_calculation.html", context={"calculations": calculations})


def playload_calculation(request):

    if request.method == 'POST':
        print(request.POST)
        form = CalculationRequestFrom(request.POST)
        if form.is_valid():
            calculation_request = form.save(commit=False)
            calculation_request.user = request.user
            calculation_request.result = 1111
            calculation_request.save()

    form = CalculationRequestFrom()

    return render(request, "rocket/payload_calculation.html", context={"form": form})
