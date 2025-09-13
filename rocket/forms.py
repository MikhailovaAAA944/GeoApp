from django.forms import ModelForm
from rocket.models import CalculationRequest


class CalculationRequestFrom(ModelForm):
    class Meta:
        model = CalculationRequest
        fields = ("rocket", "port", "comment")