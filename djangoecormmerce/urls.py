from django.urls import path
from django.urls import include
from django.contrib import admin

from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contact, name='contact'),
    path('produto/', views.product, name='product'),
    path('produtos/', include('catalog.urls')),
    path('admin/', admin.site.urls),
]
