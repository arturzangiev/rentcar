from django import forms
from .models import Car, Booking


class BookingCreateForm(forms.Form):
    car = forms.ModelChoiceField(queryset=Car.objects.all(), empty_label=1)
    start_date = forms.DateTimeField()
    end_date = forms.DateTimeField()