# coding=utf-8
from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy

from .forms import ContactForm

class IndexView(generic.TemplateView):

    template_name = 'index.html'


class ContactView(generic.FormView):

    template_name =  'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def post(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)
        if form.is_valid():
            messages.success(request, 'Menssagem Enviada!')
            form.send_mail()
            return self.form_valid(form)
        else:
            messages.error(request, 'Formulário inválido')
            return self.form_invalid(form)
