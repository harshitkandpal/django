from django.shortcuts import render

# Create your views here.
class Event:
    def __init__(self, name, date, location):
        self.name = name
        self.date = date
        self.location = location

    @staticmethod
    def events(request):
        event1 = Event("Music Concert", "2023-12-01", "City Hall")
        event2 = Event("Art Exhibition", "2023-12-15", "Art Gallery")
        event3 = Event("Food Festival", "2023-12-20", "Central Park")
        context = {
            'events': [event1, event2, event3]
        }
        return render(request, 'event/events.html', context)