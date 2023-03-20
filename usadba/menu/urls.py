from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('product/', Product.as_view(), name='product')
]
