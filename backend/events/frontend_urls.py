from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .frontend_views import home, events_list, event_detail,EventViewSet

router = DefaultRouter()
router.register("events", EventViewSet)


urlpatterns = [
    path("dapi/", include(router.urls)),
     path("", home, name="home"),
    path("events/", events_list, name="events_list"),
    path("events/<int:id>/", event_detail, name="event_detail"),
]
