from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .form import *
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

# ## For Category Model
# class CategoryListView(ListView):
#     model = Category
#     template_name = 'inventory_App/list.html'
#     context_object_name = 'category'
#
# class CategoryDetailview(DetailView):
#     model = Category
#
# class CategoryCreateView(CreateView):
#     model = Category
#     fields = '__all__'
#     success_url = reverse_lazy('list')
#
#
# ##For Vendor List Model
# class VendorListView(ListView):
#     model = Vendor
#     template_name = 'inventory_App/list.html'
#     context_object_name = 'vendor'
#
# class VendorDetailView(DetailView):
#     model = Vendor
#
# class CreateVendorView(CreateView):
#     model = Vendor
#     fields = '__all__'
#     success_url = reverse_lazy('list')
#
# class UpdateVendorView(UpdateView):
#     model = Vendor
#     fields = '__all__'
#     success_url = reverse_lazy('list')
#
# class DeleteVendorView(DeleteView):
#     model = Vendor
#     success_url = reverse_lazy('list')


## for Category Model
def allcategory(request):
    category = Category.objects.all()
    template_name = 'inventory_App/allcategory.html'
    context = {'category':category}
    return render(request,template_name, context)

def addcategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            furniture, created = Category.objects.get_or_create(**form.cleaned_data)
            furniture.save()
            return redirect('allcategory')
    else:
        form = CategoryForm()
        template_name = 'inventory_App/addcategory.html'
        context = {'form':form}
        return render(request,template_name,context)


##For Vendor model

def allvendor(request):
    vendor = Vendor.objects.all()
    context = {'vendor': vendor}
    template_name = "inventory_App/allvendor.html"
    return render(request, template_name, context)

def addvendor(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            ven, created = Vendor.objects.get_or_create(**form.cleaned_data)
            ven.save()
            return redirect('allvendor')
    else:
        form = VendorForm()
        template_name = "inventory_App/addvendor.html"
        context = {'form':form}
        return render(request, template_name, context)

def updatevendor(request,vid):
    vendor = Vendor.objects.get(pk=vid)
    if request.method == 'GET':
        form = VendorForm(instance=vendor)
    elif request.method == 'POST':
        form = VendorForm(request.POST, instance=vendor)
        if form.is_valid():
            form.save()
            return redirect('allvendor')
    context = {'form': form}
    template_name = 'inventory_App/updatevendor.html'
    return render(request, template_name, context)

def deletevendor(request,vid):
    vendor = Vendor.objects.get(pk=vid)
    if request.method == 'GET':
        context = {'vendor':vendor}
        template_name = 'inventory_App/deletevendor.html'
        return render(request, template_name, context)
    elif request.method == 'POST':
        vendor = Vendor.objects.get(pk=vid)
        vendor.delete()
        return redirect('allvendor')


## For Product Model
def allproduct(request):
    product = Product_info.objects.all()
    template_name = 'inventory_App/allproduct.html'
    context = {'product':product}
    return render(request,template_name,context)

def addproduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            pro, created = Product_info.objects.get_or_create(**form.cleaned_data)
            pro.save()
            return redirect('allproduct')
        return HttpResponse("This error")
    else:
        form = ProductForm()
        template_name = "inventory_App/addproduct.html"
        context = {'form':form}
        return render(request, template_name, context)

def updateproduct(request,pid):
    product = Product_info.objects.filter(pk = pid)
    if request.method == 'GET':
        form = ProductForm(instance = product)
    elif request.method == 'POST':
        form = ProductForm(request.POST, instance = product)
        if form.is_valid():
            form.save()
            return redirect('allproduct')
    context = {'form':form}
    template_name = 'inventory_App/updateproduct.html'
    return render(request,template_name,context)

def deleteproduct(request,pid):
    product = Product_info.objects.get(pk = pid)
    if request.method == 'GET':
        context = {'product': product}
        template_name = 'inventory_App/deleteproduct.html'
        return render(request, template_name, context)
    elif request.method == 'POST':
        product = Product_info.objects.get(pk = pid)
        product.delete()
        return redirect('allproduct')














