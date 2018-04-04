from django.contrib import admin

from .models import Product
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    """
    Classe para edição de listagem das categorias no admin do django
    """
    list_display = ['name', 'slug', 'created', 'modified']
    search_fields = ['name', 'slug']
    list_filter = ['created', 'modified']

class ProductAdmin(admin.ModelAdmin):
    """
    Classe para edição de listagem dos produtos no admin do django
    """
    list_display = ['name', 'slug', 'category', 'created', 'modified']
    search_fields = ['name', 'slug', 'category__name']
    list_filter = ['created', 'modified']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
