from django.contrib import admin
from django.urls import path
from home.views import *
from home import views
urlpatterns = [
 path('',views.home,name='home'),
 path('product/',CreateProductView.as_view(),name='addproduct'),
 path('productList/', ListProductView.as_view(),name='productlist'),
 path('deleteProduct/<int:pk>',DeleteProductView.as_view(),name='deleteproduct'),
 path('updateProduct/<int:pk>',UpdateProductView.as_view(),name='updateproduct'),
 path('searchproduct/', views.searchProduct,name='searchproduct'),
 path('sold/', views.soldProduct,name='soldproduct')
]
