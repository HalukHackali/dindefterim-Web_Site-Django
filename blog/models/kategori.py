from django.db import models
from autoslug import AutoSlugField

class KategoriModel(models.Model):
    isim = models.CharField(max_length=100, blank=False, null=False)
    # SLUG KULLANMAK İÇİN : $ pipenv install django-autoslug
    slug = AutoSlugField(populate_from='isim', unique=True)

    class Meta:
        db_table = 'kategori'

    # makemigrations yapabilmek için __init__.py'e ekle !