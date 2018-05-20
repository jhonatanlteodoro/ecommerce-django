from django.urls import path
from django.urls import include
from django.contrib import admin
from django.contrib.auth.views import login
from django.contrib.auth.views import logout

from django.conf.urls.static import static
from django.conf import settings

from core import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contato/', views.contact, name='contact'),
    path('catalogo/', include('catalog.urls')),
    path('conta/', include('accounts.urls')),
    path('compras/', include('checkout.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('entrar/', login, {'template_name': 'login.html'}, name='login'),
    path('sair/', logout, {'next_page': 'index'}, name='logout'),

    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
        )
