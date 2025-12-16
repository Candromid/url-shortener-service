from django.db import models


class Link(models.Model):
    original_url = models.URLField(
        max_length=2048,
        verbose_name="Original URL"
    )
    short_code = models.CharField(
        max_length=10,
        unique=True,
        verbose_name="Short code"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created at"
    )

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"
