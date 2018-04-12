from django.shortcuts import render
from django.urls import reverse_lazy
from .models import User
from .forms import UserAdminCreationForm
from django.views.generic import CreateView



class RegisterView(CreateView):

    model = User
    template_name = 'accounts/register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('login')
