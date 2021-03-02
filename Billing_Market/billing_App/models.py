from django.db import models
from inventory_App.models import Product_info

# Create your models here.

class Customer(models.Model):
    customer_id = models.IntegerField(unique=True)
    customer_name = models.CharField(max_length=50)
    customer_addr = models.CharField(max_length=50)
    customer_contact = models.IntegerField()
    customer_email = models.EmailField()

    def __str__(self):
        return self.customer_name

class Gst(models.Model):
    gst_code = models.CharField(max_length=50)
    sgst = models.DecimalField(decimal_places=2, max_digits=10)
    cgst = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.gst_code

class Offer(models.Model):
    offer_name = models.CharField(max_length=80)
    offer_id = models.IntegerField()
    offer_percentage = models.DecimalField(decimal_places=2, max_digits=10)
    offer_date_time = models.DateTimeField()
    category_type = models.CharField(max_length=80)

    def __str__(self):
        return self.offer_name

class Product(models.Model):
    product_info = models.ForeignKey(Product_info, on_delete=models.CASCADE)
    product_qty = models.PositiveIntegerField()
    gst = models.ForeignKey(Gst, on_delete=models.CASCADE)
    product_price_with_gst = models.DecimalField(decimal_places=2, max_digits=10)
    product_price_without_gst = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.product_name


class Invoice(models.Model):
    receipt_no = models.CharField(max_length=50,unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    invoice_date_time = models.DateTimeField(auto_now_add=True)
    total_cost = models.DecimalField(decimal_places=2, max_digits=10)

