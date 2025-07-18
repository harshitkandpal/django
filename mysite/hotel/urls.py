from django.urls import path
from .views import HotelView

app_name = 'hotel'

urlpatterns = [
    path('', view=HotelView.rooms, name='rooms'),
    path('room/<int:room_id>/', view=HotelView.room_detail, name='room_detail'),
]