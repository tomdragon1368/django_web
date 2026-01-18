from django.db import models


class SiteConfig(models.Model):
    site_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.site_name
