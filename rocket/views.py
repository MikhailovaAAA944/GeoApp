from django.shortcuts import render, redirect, get_object_or_404
from .models import LaunchVehicle, CalculationRequest
from .forms import CalculationRequestFrom
from rocket.services import calculate_payload

def list_rocket(request):
    """Вывод списка rocket"""

    rockets = LaunchVehicle.objects.all()
 
    return render(request, "rocket/rocket_list.html", context={"rockets": rockets})

def rocket_detail(request, pk):
    """Вывод детального описания rocket"""

    rocket = get_object_or_404(LaunchVehicle, pk = pk )
 
    return render(request, "rocket/rocket_detail.html", context={"rocket": rocket})

def my_calculation(request):
    """Вывод списка заявок"""

    calculations = CalculationRequest.objects.all()
 
    return render(request, "rocket/my_calculation.html", context={"calculations": calculations})


def playload_calculation(request):

    if request.method == 'POST':
        form = CalculationRequestFrom(request.POST)
        if form.is_valid():
            # Выполняем расчет
            calculation_request = form.save(commit=False)
            payload = calculate_payload(
                calculation_request.rocket,
                calculation_request.port
            )

            calculation_request.user = request.user
            calculation_request.result = payload
            calculation_request.save()
            return redirect("my_calculation")

    form = CalculationRequestFrom()

    return render(request, "rocket/payload_calculation.html", context={"form": form})


