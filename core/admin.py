from django.contrib import admin
from .models import Item,Category

class ItemAdmin(admin.ModelAdmin):
    list_display = ['name','category','author','created_by','price']

admin.site.register(Item,ItemAdmin)
admin.site.register(Category)
