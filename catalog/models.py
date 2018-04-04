from django.db import models

class Category(models.Model):
    """
    Classe para modelagem de categorias simples
    """
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']


    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Classe para modelagens simples de produtos
    """
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)
    category = models.ForeignKey(Category, verbose_name='Categoria',
                                 on_delete=models.CASCADE)
    description = models.TextField('Descrição', blank=True)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']


    def __str__(self):
        return self.name
