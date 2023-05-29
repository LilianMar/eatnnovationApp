from django.contrib import admin
from .models import Category, Product

# Creación de administrador con Django Admin

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "category","availableCant"]
    list_editable=["price","availableCant"]
    list_filter=["category","price"]
    search_fields=["name"]

admin.site.register(Category)
admin.site.register(Product,ProductAdmin)