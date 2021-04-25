from django import forms

from .models import CustomerChoice, VehicleChoice


class TransportCustomerForm(forms.Form):
    customer = forms.MultipleChoiceField(
        choices=CustomerChoice.choices,
        widget=forms.CheckboxSelectMultiple,
    )
    vehicle = forms.MultipleChoiceField(
        choices=VehicleChoice.choices,
        widget=forms.CheckboxSelectMultiple,
    )
