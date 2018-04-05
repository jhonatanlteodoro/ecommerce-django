from django.urls import path

from . import views

app_name = 'catalog'
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<str:slug>/', views.product_category_list,
         name='product_category_list'),
    path('produto/<str:slug>/', views.product, name='product'),
]
