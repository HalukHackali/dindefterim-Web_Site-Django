from django.db import models
from autoslug import AutoSlugField

class KonuModel(models.Model):
    isim = models.CharField(max_length=100, blank=False, null=False)
    # SLUG KULLANMAK İÇİN : $ pipenv install django-autoslug
    slug = AutoSlugField(populate_from='isim', unique=True)

    class Meta:
        db_table = 'Konu'
        verbose_name = 'Konu'
        verbose_name_plural = 'Konular'

    # makemigrations yapabilmek için __init__.py'e ekle !

    def __str__(self):
        return self.isim