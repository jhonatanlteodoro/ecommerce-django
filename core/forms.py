from django import forms

class ContactForm(forms.Form):
    """
    Classe para modelagem do formulario de contato
    """
    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Menssagem', widget=forms.Textarea)
