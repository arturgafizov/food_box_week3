"""food_box URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view

from items.urls import urlpatterns_items
from users.urls import urlpatterns_users
from carts.urls import urlpatterns_carts
from orders.urls import urlpatterns_orders
from reviews.urls import urlpatterns_reviews

schema_view = get_schema_view(
    openapi.Info(
        title='Stepic DRF API',
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

api_url = [
    path('carts/', include((urlpatterns_carts, 'carts'), namespace='carts')),
    path('items/', include((urlpatterns_items, 'items'), namespace='items')),
    path('users/', include((urlpatterns_users, 'users'), namespace='users')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),  # noqa
    path('orders/', include((urlpatterns_orders, 'orders'), namespace='orders')),
    path('reviews/', include((urlpatterns_reviews, 'reviews'), namespace='reviews')),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_url)),
]
