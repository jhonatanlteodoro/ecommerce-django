from django.urls import path
from . import views

app_name = 'checkout'
urlpatterns = [
    path(
        'carrinho/adicionar/<str:slug>/', views.CreateCartItemView.as_view(),
         name='create_cartitem'
    ),
    path('carrinho/', views.CartItemView.as_view(), name='cart_item'),
    path('finalizando/', views.CheckoutView.as_view(), name='checkout'),

]
