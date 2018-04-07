from django.urls import path
from django.urls import include
from django.contrib import admin
from django.contrib.auth.views import login
from django.contrib.auth.views import logout

from core import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contato/', views.contact, name='contact'),
    path('catalogo/', include('catalog.urls')),
    path('registro/', views.RegisterView.as_view(),
        {'template_name': 'register.html'}, name='register'),
    path('entrar/', login, {'template_name': 'login.html'}, name='login'),
    path('sair/', logout, {'next_page': 'index'}, name='logout'),
    path('admin/', admin.site.urls),
]
