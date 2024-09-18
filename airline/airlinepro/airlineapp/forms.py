from django import forms
from .models import Flight

class FlightForm(forms.ModelForm):
    dep_date = forms.DateField(
        input_formats=['%Y-%m-%d'],  # Accepts date in YYYY-MM-DD format
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    dep_time = forms.TimeField(
        input_formats=['%H:%M'],  # Accepts time in HH:MM format
        widget=forms.TimeInput(attrs={'type': 'time'})
    )
    arr_date = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    arr_time = forms.TimeField(
        input_formats=['%H:%M'],
        widget=forms.TimeInput(attrs={'type': 'time'})
    )

    class Meta:
        model = Flight
        fields = ['flight_id', 'dep_airport', 'dep_date', 'dep_time', 'arr_airport', 'arr_date', 'arr_time']
