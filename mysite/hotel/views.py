from django.shortcuts import render

# Create your views here.
class Hotel:
    def __init__(self, name, location, price):
        self.name = name
        self.location = location
        self.price = price

    def rooms(request):
        room1 = Hotel("Deluxe Room", "1st Floor", 200)
        room2 = Hotel("Super Deluxe Room", "2nd Floor", 300)
        room3 = Hotel("Presidential Suite", "3rd Floor", 500)
        context = {
            'rooms': [room1, room2, room3]
        }
        return render(request, 'hotel/hotel.html', context)

    def room_detail(request, room_id):
        # For simplicity, we're not fetching real data from a database
        room = Hotel("Deluxe Room", "1st Floor", 200)
        context = {
            'room': room
        }
        return render(request, 'hotel/room_detail.html', context)
