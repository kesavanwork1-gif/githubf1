from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['Your_name', 'mobile_no', 'Email', 'tickets']