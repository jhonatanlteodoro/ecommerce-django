from django.urls import path
from django.urls import include
from django.contrib import admin

from core import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contato/', views.contact, name='contact'),
    path('catalogo/', include('catalog.urls')),
    path('admin/', admin.site.urls),
]
