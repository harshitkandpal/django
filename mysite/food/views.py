from django.shortcuts import render
from .models import Item

# Create your views here.
def items(request):
    if request.method == 'GET':    
        items = Item.objects.all()
        print(items)
        context = {'items': items}
        return render(request, 'food/items.html', context)

def item_detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item
    }
    return render(request, 'food/item_detail.html', context)
