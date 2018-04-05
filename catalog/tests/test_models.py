from django.test import TestCase
from model_mommy import mommy

from django.urls import reverse

from catalog.models import Category
from catalog.models import Product


class CategoryTestCase(TestCase):

    def setUp(self):
        self.category = mommy.make(Category)

    def test_get_absolute_url(self):
        self.assertEquals(
            self.category.get_absolute_url(),
            reverse('catalog:product_category_list',
                    kwargs={'slug': self.category.slug})
        )


class ProductTestCase(TestCase):

    def setUp(self):
        self.product = mommy.make(Product, slug='produto')

    def test_get_absolute_url(self):
        self.assertEquals(
            self.product.get_absolute_url(),
            reverse('catalog:product', kwargs={'slug': 'produto'})
        )
