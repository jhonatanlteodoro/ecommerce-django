from django.shortcuts import render
from django.urls import reverse_lazy
from .models import User
from .forms import UserAdminCreationForm
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.views.generic import UpdateView
from django.views.generic import FormView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(LoginRequiredMixin, TemplateView):

    template_name = 'accounts/index.html'



class RegisterView(CreateView):

    model = User
    template_name = 'accounts/register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('login')



class UpdateUserView(LoginRequiredMixin, UpdateView):

    model = User
    template_name = 'accounts/update_user.html'
    fields = ['name', 'email']
    success_url = reverse_lazy('accounts:index')

    def get_object(self):
        return self.request.user


class UpdatePasswordView(LoginRequiredMixin, FormView):

    template_name = 'accounts/update_password.html'
    success_url = reverse_lazy('accounts:index')
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
