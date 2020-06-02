from django.shortcuts import render
from item.models import Item


def welcome(request):
    items = Item.objects.filter(active='Y')
    return render(request, 'item/welcome.html', {'items': items})


def add_item(request):
    add_item = True
    msg = None
    if request.method == 'POST':
        image_path = request.FILES.get('img', None)
        item_obj = Item(name=request.POST['name'], description=request.POST['desc'],
                        price=request.POST['price'], item_image=image_path)
        item_obj.save()
        msg = f'Item - "{item_obj.name}" Added Successfully...'
        add_item = False
    items = Item.objects.filter(active='Y')
    return render(request, 'item/welcome.html', {'items': items,
                                                 'add': add_item, 'msg': msg})


def remove_item(request, id=None):
    item_obj = Item.objects.get(id=id)
    if item_obj:
        item_obj.active = 'N'
        item_obj.save()
        msg = f'Item - "{item_obj.name}"  Removed Successfully...'
    items = Item.objects.filter(active='Y')
    return render(request, 'item/welcome.html', {'items': items, 'msg': msg})


def item_details(request, id=None):
    return render(request, 'item/item_details.html', {'item': Item.objects.get(id=id)})


