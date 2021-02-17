from django.urls import path

from carts.views import CartItemList, CartRetrieve, CartList

urlpatterns_carts = [
    path('', CartList.as_view(), name='CartList'),
    path('items/', CartItemList.as_view(), name='CartItemList'),
    path('items/<int:pk>/', CartRetrieve.as_view(), name='CartRetrieve'),
]
