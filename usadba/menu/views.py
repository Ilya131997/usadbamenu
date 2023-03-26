from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .forms import *


def index(request):
    return render(request, 'menu/homemenu.html')


class CustomSuccessMessageMixin:
    @property
    def success_msg(self):
        return False

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)


class ProductCreateView(CustomSuccessMessageMixin, CreateView):
    model = Product
    template_name = 'menu/product.html'
    form_class = AddProductForm
    success_url = reverse_lazy('product')
    success_msg = 'Продукт добавлен'

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


class ProductUpdateView(CustomSuccessMessageMixin, UpdateView):
    model = Product
    template_name = 'menu/product.html'
    form_class = AddProductForm
    success_url = reverse_lazy('product')
    success_msg = 'Продукт обновлен'

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


class ProductDeleteView(CustomSuccessMessageMixin, DeleteView):
    model = Product
    template_name = 'menu/product.html'
    success_url = reverse_lazy('product')
    success_msg = 'Продукт удален'


# # Удаление продукта
# def delete_product(request, pk):
#     get_product = Product.objects.get(pk=pk)
#     get_product.delete()
#     return redirect('/product')

# ________________Рецепты
class RecipeCreateView(CustomSuccessMessageMixin, CreateView):
    model = Recipe
    template_name = 'menu/recipe.html'
    form_class = AddRecipeForm
    success_url = reverse_lazy('recipe')
    success_msg = 'Рецепт добавлен'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = Recipe.objects.all()
        # context['products'] = Product.objects.all()
        return context


class RecipeUpdateView(CustomSuccessMessageMixin, UpdateView):
    model = Recipe
    template_name = 'menu/recipe.html'
    form_class = AddRecipeForm
    success_url = reverse_lazy('recipe')
    success_msg = 'Рецепт обновлен'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_recipe'] = True
        return context


class RecipeDeleteView(CustomSuccessMessageMixin, DeleteView):
    model = Recipe
    template_name = 'menu/recipe.html'
    success_url = reverse_lazy('recipe')
    success_msg = 'Рецепт удален'


# _______________________Меню основное
class MainMenuCreateView(CustomSuccessMessageMixin, CreateView):
    model = Recipe
    template_name = 'menu/recipe.html'
    form_class = AddRecipeForm
    success_url = reverse_lazy('recipe')
    success_msg = 'Рецепт добавлен'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = Recipe.objects.all()
        # context['products'] = Product.objects.all()
        return context
