from django.db import models


class ShortenedURL(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.short_code
