from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView

from .models import *
from .forms import *


def index(request):
    return render(request, 'menu/homemenu.html')


def product(request):
    success = False
    #Проверка на данные
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            form.save()
            success = True

    context = {
        'products': Product.objects.all(),
        'form': AddProductForm(),
        'success': success
    }

    return render(request, 'menu/product.html', context=context)

