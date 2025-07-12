from django.urls import path
from .views import Hotel

app_name = 'hotel'

urlpatterns = [
    path('', view=Hotel.rooms, name='rooms'),
]