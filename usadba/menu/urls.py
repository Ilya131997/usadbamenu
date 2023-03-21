from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('product/', ProductCreateView.as_view(), name='product'),
    path('update-product/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('delete-product/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
    path('dish/', dish, name='dish')
]

# urlpatterns = [
#     path('', index, name='home'),
#     path('product/', product, name='product'),
#     path('update-product/<int:pk>', update_product, name='update_product'),
#     path('delete-product/<int:pk>', delete_product, name='delete_product'),
# ]