from django import forms
from django.forms import TextInput, ModelForm

from .models import *


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Продукт'
            }),
            "price": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена'
            }),
        }
