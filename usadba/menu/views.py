from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .forms import *


def index(request):
    return render(request, 'menu/homemenu.html')


class ProductCreateView(CreateView):
    model = Product
    template_name = 'menu/product.html'
    form_class = AddProductForm
    success_url = reverse_lazy('product')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


# # Добавление продукта
# def product(request):
#     success = False
#     # Проверка на данные
#     if request.method == 'POST':
#         form = AddProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             success = True
#
#     context = {
#         'products': Product.objects.all(),
#         'form': AddProductForm(),
#         'success': success,
#     }
#
#     return render(request, 'menu/product.html', context=context)


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'menu/product.html'
    form_class = AddProductForm
    success_url = reverse_lazy('product')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_product'] = True
        return context

# # Обновление продукта
# def update_product(request, pk):
#     get_product = Product.objects.get(pk=pk)
#
#     # Обновляет данные в форме
#     if request.method == 'POST':
#         form = AddProductForm(request.POST, instance=get_product)
#         if form.is_valid():
#             form.save()
#             return redirect('/product')
#
#     context = {
#         'get_product': get_product,
#         'update_product': True,
#         'form': AddProductForm(instance=get_product),
#
#     }
#     return render(request, 'menu/product.html', context=context)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'menu/product.html'
    success_url = reverse_lazy('product')

# # Удаление продукта
# def delete_product(request, pk):
#     get_product = Product.objects.get(pk=pk)
#     get_product.delete()
#     return redirect('/product')
