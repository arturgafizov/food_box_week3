from django.db import models

# Create your models here.
from users.models import User
from carts.models import Cart
from reviews.data import STATUS_ORDER_CHOICES


class Order(models.Model):
    created_at = models.DateTimeField()
    delivery_at = models.DateTimeField()
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    address = models.CharField(max_length=256)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=50, choices=STATUS_ORDER_CHOICES)
    total_cost = models.DecimalField(max_digits=13, decimal_places=2, default=True)

