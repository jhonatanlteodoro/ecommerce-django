from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import generic

from .models import Product
from .models import Category



class ProductListView(generic.ListView):

    model = Product
    template_name = 'catalog/product_list.html'
    paginate_by = 3


class CategoryListView(generic.ListView):

    template_name = 'catalog/product_category_list.html'
    context_object_name = 'product_list'
    paginate_by = 3

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category,
                                                        slug=self.kwargs['slug']
                                                        )
        return context


class ProductView(generic.TemplateView):
    
    template_name = 'catalog/product.html'

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context['product'] = get_object_or_404(Product, slug=self.kwargs['slug'])
        return context
