from django.shortcuts import render
from .models import Event

# Create your views here.
class EventView:

    def events(request):
        events = Event.objects.all()
        context = {
            'events': events,
        }
        return render(request, 'event/events.html', context)

    def event_details(request, event_id):
        event = Event.objects.get(id=event_id)
        context = {
            'event': event,
        }
        return render(request, 'event/event_details.html', context)