from rest_framework import serializers
from .models import Booking
from django import forms

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
        read_only_fields = ['user', 'event', 'booked_on']        
