from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('product/', product, name='product'),
    path('update-product/<int:pk>', update_product, name='update_product'),
    path('delete-product/<int:pk>', delete_product, name='delete_product'),
]
