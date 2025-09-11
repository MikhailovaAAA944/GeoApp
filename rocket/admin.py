from django.contrib import admin
from rocket.models import LaunchVehicle
from rocket.models import SpacePort
from rocket.models import CalculationRequest


admin.site.register(LaunchVehicle)
admin.site.register(SpacePort)
admin.site.register(CalculationRequest)

# makemigrations
# migrate
