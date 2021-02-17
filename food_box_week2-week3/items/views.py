from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.core import cache
from rest_framework.utils import json
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from items.models import Item
from items.models import ItemSerializer
from items.filters import ItemFilter

ITEM_CACHE_KEY = 'item_cache_{}'
ITEM_CACHE_TTL = 300


class ItemList(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = ItemFilter
    search_fields = ['price', 'title']
    ordering = ['price']
    permission_classes = [IsAuthenticatedOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        key = ITEM_CACHE_KEY.format(request.item.id)
        cached_response = cache.get(key)
        if cached_response:
            return Response(json.loads(cached_response), status=status.HTTP_200_OK)
        else:
            response = super().retrieve(request, *args, **kwargs)
            cache.set(key, json.dumps(response.data), ITEM_CACHE_TTL)
            return response

    def get_object(self):
        return self.request.item


class ItemRetrieve(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
