from django import forms
from django.forms import ModelForm
from rocket.models import CalculationRequest


class CalculationRequestFrom(ModelForm):
    SPACEPORTS = [
        (45,'Байконур',),
        (51,'Восточный'),
        (28,'Мыс Канаверал'),
        (5,'Куру'),
        (40,'Цзюцюань'),
    ]
    
    port = forms.ChoiceField(
        choices=SPACEPORTS,
        label="Космодром",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = CalculationRequest
        fields = ("port",)
