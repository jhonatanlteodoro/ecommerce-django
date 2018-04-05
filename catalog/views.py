from django.shortcuts import render

from .models import Product
from .models import Category

def product_list(request):
    context = {
        'product_list': Product.objects.all()
    }
    return render(request, 'catalog/product_list.html', context)


def product_category_list(request, slug):
    category = Category.objects.get(slug=slug)
    context = {
        'current_category': category,
        'product_list': Product.objects.filter(category=category),
    }
    return render(request, 'catalog/product_category_list.html', context)
