from django.db import models
from django.contrib.auth import get_user_model
from events.models import Event

User = get_user_model()

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    booked_on = models.DateTimeField(auto_now_add=True)
    your_name = models.TextField()     # lowercase
    mobile_no = models.IntegerField()
    email = models.EmailField()        # lowercase
    tickets = models.IntegerField()

    def __str__(self):
        return f"{self.user} booked {self.event}"