from django.urls import path

# from orders.views import
from orders.views import OrderList, OrderRetrieve

urlpatterns_orders = [
    path('', OrderList.as_view(), name='order-list'),
    path('<int:pk>/', OrderRetrieve.as_view(), name='order-detail'),
]
