from django.contrib import admin

from . import models


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'url_name', 'item_id', 'quantity', 'ducats', 'total_ducats']
    exclude = ('item_id',)

    def total_ducats(self, item):
        return item.quantity * item.ducats

