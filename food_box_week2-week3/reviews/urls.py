from django.urls import path

from reviews.views import ReviewList

urlpatterns_reviews = [
    path('', ReviewList.as_view(), name='reviews-list'),
]
