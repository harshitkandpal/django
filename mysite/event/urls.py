from django.urls import path
from .views import Event

app_name = 'event'

urlpatterns = [
    path('', view=Event.events, name='events'),
]