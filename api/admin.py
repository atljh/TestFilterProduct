from django.contrib import admin
from .models import Product, FilterNumbers

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'productCode', 'price', 'currency', 'qty')
    search_fields = ['name', 'productCode']

@admin.register(FilterNumbers)
class FilterNumbersAdmin(admin.ModelAdmin):
    list_display = ('number',)
    search_fields = ['number']
