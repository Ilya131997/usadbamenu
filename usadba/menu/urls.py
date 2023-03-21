from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('product/', product, name='product'),
    path('update-product/', updateproduct, name='updateproduct'),
]
