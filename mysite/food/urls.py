from django.urls import path
from .views import items, item_detail

app_name = 'food'

urlpatterns =[
    path('', view=items, name='items'),
    path('<int:item_id>/', view=item_detail, name='item_detail'),
]




















