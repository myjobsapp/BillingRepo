from django import forms
from .models import Category,Vendor,Product_info

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product_info
        fields = '__all__'



