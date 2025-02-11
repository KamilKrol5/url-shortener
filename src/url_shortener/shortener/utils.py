import logging
import random
import string

from shortener.constants import SHORTEN_URL_LENGTH, MAX_GENERATE_SHORT_URL_ATTEMPTS
from shortener.models import ShortenedURL

logger = logging.getLogger(__name__)


def generate_unique_short_code(length: int = SHORTEN_URL_LENGTH) -> str:
    for _ in range(MAX_GENERATE_SHORT_URL_ATTEMPTS):
        short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        if not ShortenedURL.objects.filter(short_code=short_code).exists():
            return short_code
    raise RuntimeError(
        f"Unable to generate unique short code. Tried {MAX_GENERATE_SHORT_URL_ATTEMPTS} times.")


def create_or_get_shortened_url(original_url: str) -> ShortenedURL:
    if already_existent_url := ShortenedURL.objects.filter(original_url=original_url).first():
        return already_existent_url

    short_code = generate_unique_short_code()
    short_url = ShortenedURL.objects.create(original_url=original_url, short_code=short_code)
    return short_url


def resolve_shortened_url(short_code: str) -> ShortenedURL:
    return ShortenedURL.objects.filter(short_code=short_code).first()
