from rest_framework.serializers import ModelSerializer

from reviews.models import Review
from users.models import UserCurrentSerializer


class ReviewSerializer(ModelSerializer):
    author = UserCurrentSerializer()

    class Meta:
        model = Review
        fields = ('id', 'author', 'status', 'text', 'created_at', 'published_at')
