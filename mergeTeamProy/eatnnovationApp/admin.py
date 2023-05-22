from django.contrib import admin
from .models import Category, Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "category","availableCant"]
    list_editable=["price","availableCant"]
    list_filter=["category","price"]
    search_fields=["name"]


admin.site.register(Category)
admin.site.register(Product,ProductAdmin)