from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
class Meta:
     db_table = 'categories' 


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

class Sale(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.total = self.amount * self.price
        super().save(*args, **kwargs)

class Meta:
     db_table = 'sales'     

class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def calculate_total(self):
        self.total = Sale.objects.filter(user=self.user).aggregate(total=models.Sum('total'))['total']
        self.save()

class Meta:
     db_table = 'invoices'     