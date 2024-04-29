from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Category)
class Category_ModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date', 'updated_date']
    list_filter = ['created_date', 'updated_date']
    search_fields = ['title']


@admin.register(Sub_Category)
class SubCategory_ModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_date', 'updated_date']
    list_filter = ['created_date', 'updated_date']
    search_fields = ['title']


@admin.register(Product)
class Product_ModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'discount_price', 'created_date', 'updated_date']
    list_filter = ['discount_price', 'created_date', 'updated_date']
    search_fields = ['title']

