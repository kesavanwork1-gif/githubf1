from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


# Home Page
def home(request):
    return render(request, "home.html")

# Events List Page
def events_list(request):
    events = Event.objects.all()
    return render(request, "event.html", {"events": events})

# Event Detail Page
def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, "event_detail.html", {"event": event})