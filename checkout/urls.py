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
    path('meus_pedidos/', views.OrderListView.as_view(), name='order_list'),
    path('meus_pedidos/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
]
