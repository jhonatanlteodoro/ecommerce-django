from django.db import models
from catalog.models import Product
from django.conf import settings


class CartItemManager(models.Manager):

    def add_item(self, cart_key, product):
        if self.filter(cart_key=cart_key, product=product).exists():
            created = False
            cart_item = self.get(cart_key=cart_key, product=product)
            cart_item.quantity = cart_item.quantity + 1
            cart_item.save()
        else:
            created = True
            cart_item = CartItem.objects.create(
                cart_key=cart_key, product=product, price=product.price
            )
        return cart_item, created


class CartItem(models.Model):

    cart_key = models.CharField(
        'Chave do Carrinho', max_length=40, db_index=True
    )
    product = models.ForeignKey(
        Product, verbose_name="Produto", on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField('Quantidade', default=1)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    objects = CartItemManager()

    class Meta:
        verbose_name = 'Item Carrinho'
        verbose_name_plural = 'Itens dos Carrinhos'
        unique_together = (('cart_key', 'product'),)

    def __str__(self):
        return '{} [{}]'.format(self.product, self.quantity)


class OrderManager(models.Manager):

    def create_order(self, user, cart_items):
        order = self.create(user=user)
        for cart_item in cart_items:
            order_item = OrderItem.objects.create(
                order=order, quantity=cart_item.quantity,
                product=cart_item.product, price=cart_item.price
            )
        return order


class Order(models.Model):

    STATUS_CHOICES = (
        (0, 'Aguardando Pagamento'),
        (1, 'Concluída'),
        (2, 'Cancelada'),
    )

    PAYMENT_OPTIONS_CHOICES = (
        ('deposit', 'Depósito'),
        ('pagaseguro', 'PagSeguro'),
        ('paypal', 'Paypal'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             verbose_name='Usuário')
    status = models.IntegerField('Situação', choices=STATUS_CHOICES, default=0, blank=True)
    payment_option = models.CharField('Opções de Pagamento', choices=PAYMENT_OPTIONS_CHOICES,
                                        default='deposit', max_length=20)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    objects = OrderManager()

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return 'Pedido %s' %self.pk

    def products(self):
        products_ids = self.items.values_list('product')
        return Product.objects.filter(pk__in=products_ids)

    def total(self):
        aggregate_queryset = self.items.aggregate(
            total=models.Sum(
                models.F('price') * models.F('quantity'),
                output_field = models.DecimalField()
            )
        )
        return aggregate_queryset['total']



class OrderItem(models.Model):

    order = models.ForeignKey(Order, verbose_name='Pedido', on_delete=models.CASCADE,
                              related_name='items')
    product = models.ForeignKey(
        Product, verbose_name="Produto", on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField('Quantidade', default=1)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'

    def __str__(self):
        return '[{}] {}'.format(self.order, self.product)


#signals
def post_save_cart_item(instance, **kwargs):
    if instance.quantity < 1:
        instance.delete()

models.signals.post_save.connect(
    post_save_cart_item, sender=CartItem, dispatch_uid='post_save_cart_item'
)
