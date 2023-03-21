from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView

from .models import *
from .forms import *


def index(request):
    return render(request, 'menu/homemenu.html')


# Добавление продукта
def product(request):
    success = False
    # Проверка на данные
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            form.save()
            success = True

    context = {
        'products': Product.objects.all(),
        'form': AddProductForm(),
        'success': success,
    }

    return render(request, 'menu/product.html', context=context)


# Обновление продукта
def update_product(request, pk):
    get_product = Product.objects.get(pk=pk)

    # Обновляет данные в форме
    if request.method == 'POST':
        form = AddProductForm(request.POST, instance=get_product)
        if form.is_valid():
            form.save()
            return redirect('/product')

    context = {
        'get_product': get_product,
        'update_product': True,
        'form': AddProductForm(instance=get_product),

    }
    return render(request, 'menu/product.html', context=context)


# Обновление продукта
def delete_product(request, pk):
    get_product = Product.objects.get(pk=pk)
    get_product.delete()
    return redirect('/product')
