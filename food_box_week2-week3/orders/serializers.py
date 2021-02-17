from rest_framework.serializers import ModelSerializer

from orders.models import Order
from carts.serializers import CartSerializer


class OrderSerializer(ModelSerializer):
    cart = CartSerializer()

    class Meta:
        model = Order
        fields = ('id', 'cart', 'status', 'total_cost', 'address', 'delivery_at', 'created_at')
        extra_kwargs = {
            'cart': {'read_only': True},
            'status': {'read_only': True},
            'total_cost': {'read_only': True},
            'created_at': {'read_only': True},
        }


class OrderUpdateSerializer(ModelSerializer):
    cart = CartSerializer()

    class Meta:
        model = Order
        fields = ('cart', 'status', 'address', 'delivery_at')
