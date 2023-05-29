from django.db import models
from django.contrib.auth.models import User

# Modelo de Categoría
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
class Meta:
     db_table = 'categories' 

# Modelo de Producto
class Product(models.Model):
    category=models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    description = models.TextField()
    img=models.ImageField(upload_to="products", null=True)
    price = models.IntegerField()
    availableCant = models.IntegerField()
    def __str__(self):
        return self.name
class Meta:
     db_table = 'products' 

# Modelo de Factura
class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

class Meta:
     db_table = 'invoices'   