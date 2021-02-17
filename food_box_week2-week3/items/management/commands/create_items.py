import requests
from django.core.management.base import BaseCommand
from urllib.request import urlretrieve
from django.core.exceptions import ValidationError

from items.models import Item
from rest_framework import status
from rest_framework.response import Response


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        link_item = requests.get('https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/foodboxes.json')
        foods = link_item.json()

        for food in foods:

            item = Item.objects.filter(id=food['id']).first()
            name_image = food['image'].split('/')[-1]
            urlretrieve(food['image'], './media/item_images/'
                        + name_image)  # через  + объединил путь и переменную

            try:
                d = {'title': food['title'],
                     'description': food['description'],
                     'image': '/media/item_images/' + food['image'].split('/')[-1],
                     'weight': food['weight_grams'],
                     'price': food['price']}

                new_item = Item.objects.update_or_create(defaults=d, id=food['id'])

                self.stdout.write("Item successfully updated or created")

            except ValidationError:
                print("Validation Error")

        if link_item.status_code == 404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        elif link_item.status_code == 408:
            return Response(status=status.HTTP_408_REQUEST_TIMEOUT)
