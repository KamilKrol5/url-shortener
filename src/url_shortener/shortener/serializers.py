from rest_framework import serializers

from shortener.constants import SHORTENED_LINK_PREFIX
from shortener.models import ShortenedURL


class ShortenedURLSerializer(serializers.ModelSerializer):
    shortened_url = serializers.SerializerMethodField()

    class Meta:
        model = ShortenedURL
        fields = ['id', 'original_url', 'short_code', 'shortened_url']

    @staticmethod
    def get_shortened_url(instance: ShortenedURL) -> str:
        return f"{SHORTENED_LINK_PREFIX}{instance.short_code}"
