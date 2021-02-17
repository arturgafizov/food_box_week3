from django.db import models
from django.utils import timezone

from users.models import User
# Create your models here.
from reviews.data import STATUS_CHOICES


class Review(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
