# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic import TemplateView
from django.views.generic import CreateView

from catalog.models import Category
from .forms import ContactForm

#def index(request):
#    context = {
#        'categories': Category.objects.all()
#    }
#    return render(request, 'index.html', context)

class IndexView(TemplateView):

    template_name = 'index.html'



def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    context = {
        'form': form,
        'success': success,
    }
    return render(request, 'contact.html', context)
