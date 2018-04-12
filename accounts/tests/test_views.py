from django.test import Client
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


User = get_user_model()
class RegisterViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('accounts:register')

    def test_register_ok(self):
        data  = {
            'username': 'jhowuserteste', 'email': 'uhuuu@gmail.com',
            'password1': 'teste123','password2': 'teste123',
        }
        response = self.client.post(self.register_url, data)
        login_url = reverse('login')
        self.assertRedirects(response, login_url)
        self.assertEquals(User.objects.count(), 1)

    def test_register_fail(self):
        data  = {
            'username': 'jhowuserteste', 'password1': 'teste123',
            'password2': 'teste123',
        }
        response = self.client.post(self.register_url, data)
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')
