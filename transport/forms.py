from django import forms

from .models import CustomerChoice, VehicleChoice


class TransportCustomerForm(forms.Form):
    customer = forms.ChoiceField(choices=CustomerChoice.choices)
    vehicle = forms.MultipleChoiceField(
        choices=VehicleChoice.choices,
        widget=forms.CheckboxSelectMultiple,
    )
