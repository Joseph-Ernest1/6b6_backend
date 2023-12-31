from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    decription = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="product_image")
    category = models.TextField(blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1)


    def __str__(self):
        return self.name
      


