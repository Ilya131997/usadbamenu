from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('product/', ProductCreateView.as_view(), name='product'),
    path('update-product/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('delete-product/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
    path('recipe/', RecipeCreateView.as_view(), name='recipe'),
    path('update-recipe/<int:pk>', RecipeUpdateView.as_view(), name='update_recipe'),
    path('delete-recipe/<int:pk>', RecipeDeleteView.as_view(), name='delete_recipe'),
    path('mainmenu/', MainMenuCreateView.as_view(), name='mainmenu'),
]
