from django.db import models

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
