from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from shortener.models import ShortenedURL
from shortener.serializers import ShortenedURLSerializer
from shortener.utils import create_or_get_shortened_url


class CreateShortenedURL(APIView):

    def post(self, request):
        original_url = request.data.get('original_url')
        short_url = create_or_get_shortened_url(original_url)
        return Response(ShortenedURLSerializer(short_url).data, status=status.HTTP_201_CREATED)


class ResolveShortenedURL(APIView):
    def get(self, request, short_code):
        url = get_object_or_404(ShortenedURL, short_code=short_code)
        return Response({'original_url': url.original_url})
