import math
from django.conf import settings
from django.contrib.auth import get_user_model
from rocket.models import CalculationRequest


User = get_user_model()

@property
def get_user_calc_request_count(self):
    try:
        result = CalculationRequest.objects.filter(user=self).count()
    except:
        result = 0
    return result


User.add_to_class("get_request_count", get_user_calc_request_count)


def calculate_payload(launch_vehicle, port):
    """
    Расчет полезной нагрузки на ГСО по упрощенной формуле
    """
    try:
        k = settings.PAYLOAD_COEFFICIENT
        payload_gto = launch_vehicle.gto_playload
        latitude_degrees = int(port)
        
        # Конвертируем градусы в радианы
        latitude_radians = math.radians(latitude_degrees)
        
        # Расчет по формуле: payload_gso = payload_gto * (1 - k * (1 - cos(latitude)))
        payload_gso = payload_gto * (1 - k * (1 - math.cos(latitude_radians)))
        
        return max(0, round(payload_gso, 2))  # Не может быть отрицательной
    except Exception as e:
        raise ValueError(f"Ошибка расчета полезной нагрузки: {str(e)}")