from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from menu.models import *


def index(request):
    return render(request, 'menu/homemenu.html')

class Product(ListView):
    model = Product
    template_name = 'menu/product.html'