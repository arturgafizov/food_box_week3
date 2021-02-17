import requests
from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response

from reviews.models import Review


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        link_review = requests.get('https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/reviews.json')
        reviews = link_review.json()

        for review in reviews:
            try:
                d = {'text': review['content'],
                     'created_at': review['created_at'],
                     'published_at': review['published_at'],
                     'status': review['status'],
                     'author_id': review['author']
                     }

                new_customer_review = Review.objects.update_or_create(defaults=d, id=review['id'])

                self.stdout.write("Review successfully created or update")
            except ValidationError:
                print("Validation Error")

        if link_review.status_code == 404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        elif link_review.status_code == 408:
            return Response(status=status.HTTP_408_REQUEST_TIMEOUT)
