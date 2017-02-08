from django.db import models
from taggit.managers import TaggableManager


class Product(models.Model):
    title = models.CharField("タイトル", unique=True, max_length=30)
    description = models.CharField("詳細", max_length=240)
    url = models.CharField("URL", max_length=240)
    category = TaggableManager()
