import math
from django.conf import settings


def calculate_payload(launch_vehicle, port):
    """
    Расчет полезной нагрузки на ГСО по упрощенной формуле
    """
    try:
        k = settings.PAYLOAD_COEFFICIENT
        payload_gto = launch_vehicle.gto_playload
        latitude_degrees = port.location
        
        # Конвертируем градусы в радианы
        latitude_radians = math.radians(latitude_degrees)
        
        # Расчет по формуле: payload_gso = payload_gto * (1 - k * (1 - cos(latitude)))
        payload_gso = payload_gto * (1 - k * (1 - math.cos(latitude_radians)))
        
        return max(0, round(payload_gso, 2))  # Не может быть отрицательной
    except Exception as e:
        raise ValueError(f"Ошибка расчета полезной нагрузки: {str(e)}")