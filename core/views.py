# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse

from catalog.models import Category
from .forms import ContactForm

def index(request):
    context = {
        'categories': Category.objects.all()
    }
    return render(request, 'index.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
    else:
        form = ContactForm()

    context = {
        'form': form
    }
    return render(request, 'contact.html', context)


def product(request):
    return render(request, 'product.html')
