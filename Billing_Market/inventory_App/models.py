from django.db import models

# Create your models here.

class Category(models.Model):
    category_type = models.CharField(max_length=50)

    def __str__(self):
        return self.category_type

class Vendor(models.Model):
    vendor_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    vendor_contact = models.IntegerField()
    vendor_email = models.EmailField()
    vendor_address = models.CharField(max_length=100)

    def __str__(self):
        return self.vendor_name


class Product_info(models.Model):
    product_name = models.CharField(max_length=50)
    product_description = models.TextField()
    product_expiry_date = models.DateField()
    product_weight = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    product_qty = models.IntegerField(null=True)
    product_price = models.DecimalField(decimal_places=2, max_digits=10)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # def get_total_price(self):
    #     return self.product_qty * self.product_price

    def __str__(self):
        return self.product_name


