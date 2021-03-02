from django.contrib import admin
from .models import Category,Vendor,Product_info

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_type']
admin.site.register(Category, CategoryAdmin)

class VenderAdmin(admin.ModelAdmin):
    list_display = ['vendor_name', 'company_name', 'vendor_contact', 'vendor_email', 'vendor_address']
admin.site.register(Vendor, VenderAdmin)

class Product_infoAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_description', 'product_expiry_date', 'product_weight', 'product_qty',
                    'product_price']
admin.site.register(Product_info, Product_infoAdmin)


