from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core import cache

from items.models import Item
from items.views import ITEM_CACHE_KEY


@receiver([post_save, post_delete], sender=Item)
def invalidate_item_cache(sender, instance, **kwargs):
    cache.delete(ITEM_CACHE_KEY.format(instance.id))
