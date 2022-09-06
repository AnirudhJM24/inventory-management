from django.contrib import admin
from .models import Product, Order
from django.contrib.auth.models import Group

admin.site.site_header = 'Inventory dashboard'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','category','quantity')
    list_filter = ('category',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['product','order_quantity', 'date', 'staff']
    list_filter = ['date', 'product', 'staff']
# Register your models here.

admin.site.register(Product, ProductAdmin)
admin.site.unregister(Group)
admin.site.register(Order, OrderAdmin)
