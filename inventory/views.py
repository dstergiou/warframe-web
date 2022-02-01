from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import Item


def index(request):
    items = Item.objects.all()
    
    return render(request, 'index.html', {'items': items})

@require_http_methods(['POST'])
def search(request):
    search_item = request.POST['search']
    if len(search_item) == 0:
        return render(request, 'item.html', {'items': []})
    
    db_items = Item.objects.all()
    
    items = []
    for item in db_items:
        if search_item.lower() in item.name.lower():
            items.append(item)
            
    return render(request, 'item.html', {'items': items})
    

def card(request):
    return render(request, 'card.html', {'items': []})