from django.db import models
from autoslug import AutoSlugField

class SinifModel(models.Model):
    isim = models.CharField(max_length=50, blank=True, null=True)
    #slug = AutoSlugField(populate_from='isim', unique=True, null=True)
    slug = models.SlugField(unique=True, null=True)

    class Meta:
        db_table = 'sinif'
        verbose_name = 'Sinif'
        verbose_name_plural = 'Siniflar'

    def __str__(self):
        return self.isim