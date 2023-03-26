from django import forms
from django.forms import TextInput, ModelForm, SelectMultiple, CheckboxInput, Select, NullBooleanSelect, RadioSelect, \
    MultipleHiddenInput, SelectDateWidget, MultiWidget

from .models import *


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Продукт',
                'style': 'width:50ch',
            }),
            "price": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена',
                'style': 'width:50ch',
            }),
        }


class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        # fields = ['title', 'products']

        fields = '__all__'
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Продукт',
                'style': 'width:50ch',
            }),
            "products": SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': 'Продукт',
                'style': 'width:40ch',
                'size': 20
            }),
        }
