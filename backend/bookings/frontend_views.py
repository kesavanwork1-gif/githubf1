from django.shortcuts import render, get_object_or_404
from .models import Booking
from events.models import Event
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import BookingSerializer
from django.contrib.auth.decorators import login_required

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


@login_required
def book_event(request, id):
    event = get_object_or_404(Event, id=id)

    if request.method == "POST":
        tickets = int(request.POST["tickets"])
        name = request.POST["your_name"]
        mobile = request.POST["mobile_no"]
        email = request.POST["email"]

        # Check seat availability
        if tickets > event.seats_available:
            return render(request, "booking_form.html", {
                "event": event,
                "error": "Not enough seats available!"
            })

        # Save Booking
        booking = Booking.objects.create(
            user=request.user,
            event=event,
            tickets=tickets,
            your_name=name,
            mobile_no=mobile,
            email=email
        )

        # Reduce seats
        event.seats_available -= tickets
        event.save()

        return render(request, "booking_success.html", {"booking": booking})

    return render(request, "booking_form.html", {"event": event})


@login_required
def dashboard(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, "dashboard.html", {"bookings": bookings})

def destroy(self, request, *args, **kwargs):
        booking = self.get_object()

        # restore seats
        event = booking.event
        event.seats_available += booking.tickets
        event.save()

        booking.delete()

        return Response({"message": "Booking cancelled"}, status=status.HTTP_204_NO_CONTENT)
