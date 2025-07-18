from django.shortcuts import render
from .models import Room

# Create your views here.
class HotelView:

    def rooms(request):
        rooms = Room.objects.all()
        context = {
            'rooms': rooms
        }
        return render(request, 'hotel/hotel.html', context)

    def room_detail(request, room_id):
        room = Room.objects.get(id=room_id)
        context = {
            'room': room
        }
        return render(request, 'hotel/room_details.html', context)
