from django.db import models
from inventory_App.models import Product_info

# Create your models here.

class Order(models.Model):
    order_id = models.PositiveIntegerField()
    order_date = models.DateTimeField()
    total_amount = models.DecimalField(decimal_places=2, max_digits=10)
    total_products = models.PositiveIntegerField()

    def __str__(self):
        return self.order_id

class Product(models.Model):
    product_info = models.ForeignKey(Product_info, related_name='product_info', on_delete=models.CASCADE)##relationship with product_info model from Inventory App
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    order_qty = models.PositiveIntegerField()

    def __str__(self):
        return self.order

class Order_summary(models.Model):
    order_delievery_date = models.DateTimeField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
