from django.urls import path
from .views import shorten_url, redirect_to_original

urlpatterns = [
    path('api/shorten/', shorten_url, name='shorten_url'),
    path('<str:short_code>/', redirect_to_original, name='redirect'),
]
