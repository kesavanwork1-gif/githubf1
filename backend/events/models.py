from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Event(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date = models.DateTimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    seats_available = models.IntegerField()
    image = models.ImageField(upload_to="event_images/", blank=True, null=True)


    def __str__(self):
        return self.title
