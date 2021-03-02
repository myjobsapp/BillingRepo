from django.urls import path
from . import views

urlpatterns = [

## For category model
    # path('list/', views.VendorListView.as_view(), name='list'),
    # path('detail/<int:pk>', views.VendorDetailView.as_view(), name='detail'),
    # path('create/', views.CreateVendorView.as_view(), name='create'),
    path('allcategory/', views.allcategory, name='allcategory'),
    path('addcategory/', views.addcategory, name='addcategory'),

## For Vendor model
    # path('list/', views.VendorListView.as_view(), name='list'),
    # path('detail/<int:pk>', views.VendorDetailView.as_view(), name='detail'),
    # path('create/', views.CreateVendorView.as_view(), name='create'),
    # path('update/<int:pk>/', views.UpdateVendorView.as_view(), name='update'),
    # path('delete/<int:pk>/', views.DeleteVendorView.as_view(), name='delete'),

    path('allvendor/', views.allvendor, name='allvendor'),
    path('addvendor/', views.addvendor, name='addvendor'),
    path('updatevendor/<int:vid>/', views.updatevendor, name='updatevendor'),
    path('deletevendor/<int:vid>/', views.deletevendor, name='deletevendor'),

## For Product model
    path('allproduct/', views.allproduct, name='allproduct'),
    path('addproduct/', views.addproduct, name='addproduct'),
    path('updateproduct/<int:pid>/', views.updateproduct, name='updateproduct'),
    path('deleteproduct/<int:pid>/', views.deleteproduct, name='deleteproduct')



]