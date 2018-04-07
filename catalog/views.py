from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import generic

from .models import Product
from .models import Category



class ProductListView(generic.ListView):

    model = Product
    template_name = 'catalog/product_list.html'
    paginate_by = 3

product_list = ProductListView.as_view()

#def product_list(request):
#    context = {
#        'product_list': Product.objects.all()
#    }
#    return render(request, 'catalog/product_list.html', context)


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

product_category_list = CategoryListView.as_view()

#def product_category_list(request, slug):
#    category = Category.objects.get(slug=slug)
#    context = {
#        'current_category': category,
#        'product_list': Product.objects.filter(category=category),
#    }
#    return render(request, 'catalog/product_category_list.html', context)

def product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product,
    }
    return render(request, 'catalog/product.html', context)
