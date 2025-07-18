from django.urls import path
from .views import EventView

app_name = 'event'

urlpatterns = [
    path('events', view=EventView.events, name='events'),
    path('event/<int:event_id>/', view=EventView.event_details, name='event_details'),
]