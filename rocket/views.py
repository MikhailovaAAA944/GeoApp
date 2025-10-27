from django.shortcuts import render, redirect, get_object_or_404
from .models import LaunchVehicle, CalculationRequest, Order
from .forms import CalculationRequestFrom
from rocket.services import calculate_payload

def list_rocket(request):
    """Вывод списка rocket"""

    rockets = LaunchVehicle.objects.all()
    rockets_reserv_pk = list(CalculationRequest.objects.filter(
        order__client=request.user, order__status="Черновик"
        ).values_list('rocket', flat=True))
    print(rockets_reserv_pk)
    query = request.GET.get('q')
    if query : 
        rockets = rockets.filter(name__icontains = query)
    from django.conf import settings
    return render(request, "rocket/rocket_list.html", context={"rockets": rockets, 
                                                               "rockets_reserv_pk":rockets_reserv_pk,
                                                                'STATIC_URL': settings.STATIC_URL,
        'DEBUG': settings.DEBUG,
        'STATIC_ROOT': settings.STATIC_ROOT,})


def request_form(request, rocket_pk):
    """Добавление ракеты в расчет"""
    
    # get_or_create возвращает кортеж (object, created)
    order, created = Order.objects.get_or_create(
        status="Черновик", 
        client=request.user
    )
    
    CalculationRequest.objects.create(
        order=order,  # передаем объект order, а не order.pk
        rocket_id=rocket_pk,  # используем rocket_id для явного указания внешнего ключа
        result=-1
    )
    
    return redirect("list_rocket")

 


def rocket_detail(request, pk):
    """Вывод детального описания rocket"""

    rocket = get_object_or_404(LaunchVehicle, pk = pk )
 
    return render(request, "rocket/rocket_detail.html", context={"rocket": rocket})

def my_calculation(request):
    """Вывод списка заявок"""

    calculations = CalculationRequest.objects.filter(order__status=Order.OrderStatus.COMPLETED)
 
    return render(request, "rocket/my_calculation.html", context={"calculations": calculations})

def remove_rocket(request, rocket_pk):
    if request.method != "POST":
        return redirect('list_rocket')
    try:
        rocket = LaunchVehicle.objects.get(id=rocket_pk)
        rocket.is_active = False
        rocket.save()
        return redirect('list_rocket')
    except rocket.DoesNotExist:
        return redirect('list_rocket')
    
def delete_from_calc(request, rocket_pk):
    """Удаление ракеты из рсчета"""

    calculations = CalculationRequest.objects.filter(
        order__client=request.user, order__status=Order.OrderStatus.DRAFT, rocket = rocket_pk 
    )
    calculations.delete()
 
    return redirect("playload_calculation")
from django.db import connection

def delete_calc(request, order_pk):
    if request.method != "POST":
        return redirect('list_rocket')
     # Выполняем SQL запрос
    with connection.cursor() as cursor:
        cursor.execute(
                "UPDATE public.rocket_order SET status = %s WHERE id = %s",
                ['Удален', order_pk]
            )
    return redirect('list_rocket')

def playload_calculation(request):
    r = CalculationRequest.objects.select_related('rocket').filter(
        order__client=request.user, order__status=Order.OrderStatus.DRAFT
        )
    if r:
        order_pk = r.first().order.pk
    else:
        order_pk = ''
    if request.method == 'POST':
        form = CalculationRequestFrom(request.POST)
        if form.is_valid():
            # Выполняем расчет
            port = form.cleaned_data['port']
            for obj in r:
                payload = calculate_payload(
                    obj.rocket,
                    port
                )
                CalculationRequest.objects.filter(
                    order__client=request.user, order__status="Черновик", rocket=obj.rocket
                ).update(result = payload)

                Order.objects.filter(pk = obj.order.pk).update(status="Расчет завершен")
                
                
            return redirect("my_calculation")

    form = CalculationRequestFrom()
    
    return render(request, "rocket/payload_calculation.html", context={"form": form,
                                                                       "rockets": r, "order_pk": order_pk})


