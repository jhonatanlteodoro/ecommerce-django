from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('registro/', views.RegisterView.as_view(),
        {'template_name': 'register.html'}, name='register'),
    path('', views.IndexView.as_view(), name='index'),
    path('alterar-dados/', views.UpdateUserView.as_view(), name='update_user'),
    path('alterar-senha/', views.UpdatePasswordView.as_view(), name='update_password')
]
