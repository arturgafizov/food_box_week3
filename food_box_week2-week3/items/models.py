from django.db import models
from rest_framework.serializers import ModelSerializer


# Create your models here.
from django.conf import settings


class Item(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to=settings.MEDIA_ITEM_IMAGE_DIR)
    weight = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=13, decimal_places=2)


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'title', 'description', 'image', 'weight', 'price')

