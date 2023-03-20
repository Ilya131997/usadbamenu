from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import *


def index(request):
    return render(request, 'menu/homemenu.html')


class Product(ListView):
    model = Product
    template_name = 'menu/product.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Продукты'
        return context
