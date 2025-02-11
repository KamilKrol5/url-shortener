from django.urls import path

from shortener.views import CreateShortenedURL, ResolveShortenedURL

urlpatterns = [
    path('shorten/', CreateShortenedURL.as_view(), name='shorten'),
    path('<str:short_code>/', ResolveShortenedURL.as_view(), name='resolve'),
]
