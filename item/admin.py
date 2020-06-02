from django.contrib import admin
from item.models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'item_image']


admin.site.register(Item, ItemAdmin)

