from django.urls import path,include
from .frontend_views import book_event, dashboard



urlpatterns = [
    path("book/<int:id>/", book_event, name="book_event"),
    path("dashboard/", dashboard, name="dashboard"),
]
