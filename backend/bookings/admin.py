from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    # Columns in the list page
    list_display = (
        "user",
        "event",
        "get_location",
        "get_event_date",
        "your_name",
        "email",
        "mobile_no",
        "tickets",
        "booked_on",
    )

    # Fields to show in the detail/edit page
    fields = (
        "user",
        "event",
        "get_location",
        "get_event_date",
        "your_name",
        "email",
        "mobile_no",
        "tickets",
        "booked_on",
    )

    # Make location/date read-only because they come from Event
    readonly_fields = ("get_location", "get_event_date", "booked_on")

    # Custom methods to show event info
    def get_location(self, obj):
        return obj.event.location
    get_location.short_description = "Location"

    def get_event_date(self, obj):
        return obj.event.date
    get_event_date.short_description = "Event Date"