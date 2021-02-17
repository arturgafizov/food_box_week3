from django.db import models


from users.models import User
from items.models import Item

# Create your models here.


class Cart(models.Model):
    items = models.ManyToManyField(to=Item, through='CartItem')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')

    total_cost = models.DecimalField(max_digits=13, decimal_places=2, default=True)

    @property
    def total_cost(self):
        return self.carts.price * self.carts.quantity


class CartItem(models.Model):
    item = models.ForeignKey(to=Item, on_delete=models.CASCADE, related_name='cart_items')
    cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=13, decimal_places=2)

    total_price = models.DecimalField(max_digits=13, decimal_places=2, default=True)

    @property
    def total_price(self):
        return self.price * self.quantity
